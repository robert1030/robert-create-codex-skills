#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Source intake, safe archive expansion, deduplication, and provenance."""

from __future__ import annotations

import mimetypes
import re
import shutil
import zipfile
from pathlib import Path
from typing import Iterable

from collection import CollectionRuntime, build_collection_runtime
from constants import DIRECT_SOURCE_EXTENSIONS, IMAGE_EXTENSIONS, SUPPORTED_EXTENSIONS
from models import Provenance, SourceItem
from utils import sha256_file, sha256_text, slugify

MIME_BY_EXTENSION = {
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".doc": "application/msword",
    ".html": "text/html",
    ".htm": "text/html",
    ".xml": "application/xml",
    ".csv": "text/csv",
    ".md": "text/markdown",
    ".markdown": "text/markdown",
    ".mp4": "video/mp4",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".heif": "image/heif",
    ".heic": "image/heic",
    ".zip": "application/zip",
}

MAGIC_SIGNATURES: list[tuple[bytes, str]] = [
    (b"%PDF-", "application/pdf"),
    (b"PK\x03\x04", "application/zip"),
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"\xff\xd8\xff", "image/jpeg"),
]


def runtime_media_type(path: Path) -> tuple[str, str]:
    head = path.read_bytes()[:32]
    for signature, media_type in MAGIC_SIGNATURES:
        if head.startswith(signature):
            if media_type == "application/zip" and path.suffix.lower() == ".docx":
                return MIME_BY_EXTENSION[".docx"], head.hex()
            return media_type, head.hex()
    if len(head) >= 12 and head[4:8] == b"ftyp":
        brand = head[8:12]
        if brand in {b"isom", b"iso2", b"mp41", b"mp42", b"avc1"}:
            return "video/mp4", head.hex()
        if brand in {b"heic", b"heix", b"hevc", b"mif1", b"msf1"}:
            return "image/heic", head.hex()
    extension = path.suffix.lower()
    guessed = MIME_BY_EXTENSION.get(extension) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return guessed, head.hex()


def infer_requested_media_type(name: str, explicit: str | None = None) -> str:
    if explicit:
        return explicit
    lower = name.lower()
    snapshot_match = re.search(r"(\.pdf|\.docx|\.doc|\.html|\.xml)(?:\.|$)", lower)
    if snapshot_match and lower.endswith((".md", ".markdown")):
        return MIME_BY_EXTENSION[snapshot_match.group(1)]
    return MIME_BY_EXTENSION.get(Path(name).suffix.lower(), "application/octet-stream")


def _safe_extract_zip(zip_path: Path, destination: Path) -> list[Path]:
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    extracted: list[Path] = []
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            target = (destination / info.filename).resolve()
            try:
                target.relative_to(root)
            except ValueError as exc:
                raise ValueError(f"zip_path_traversal:{info.filename}") from exc
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, target.open("wb") as output:
                shutil.copyfileobj(source, output)
            extracted.append(target)
    return extracted


def _supported_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield path


def collect_sources(input_path: Path, temp_root: Path, requested_media_type: str | None = None) -> tuple[list[SourceItem], list[dict]]:
    """Expand directories and nested ZIP files, then deduplicate by SHA-256."""
    input_path = input_path.resolve()
    if not input_path.exists():
        raise FileNotFoundError(str(input_path))
    queue: list[SourceItem] = []
    if input_path.is_dir():
        for path in _supported_files(input_path):
            relative = path.relative_to(input_path).as_posix()
            queue.append(SourceItem(path=path, display_name=relative, original_upload_name=path.name))
    else:
        queue.append(SourceItem(
            path=input_path,
            display_name=input_path.name,
            original_upload_name=input_path.name,
            requested_media_type=requested_media_type,
        ))

    resolved: list[SourceItem] = []
    duplicates: list[dict] = []
    seen_hashes: dict[str, str] = {}
    archive_counter = 0
    while queue:
        item = queue.pop(0)
        extension = item.path.suffix.lower()
        if extension == ".zip":
            archive_counter += 1
            extraction_root = temp_root / f"archive-{archive_counter:04d}"
            extracted = _safe_extract_zip(item.path, extraction_root)
            for child in sorted(extracted):
                child_ext = child.suffix.lower()
                if child_ext not in SUPPORTED_EXTENSIONS:
                    continue
                relative = child.relative_to(extraction_root).as_posix()
                queue.append(SourceItem(
                    path=child,
                    display_name=f"{item.display_name}::{relative}",
                    original_upload_name=child.name,
                    derivation_chain=item.derivation_chain + [{
                        "operation": "archive_extract",
                        "source": item.display_name,
                        "member": relative,
                    }],
                ))
            continue
        if extension not in DIRECT_SOURCE_EXTENSIONS:
            continue
        digest = sha256_file(item.path)
        if digest in seen_hashes:
            duplicates.append({
                "duplicate": item.display_name,
                "canonical": seen_hashes[digest],
                "sha256": digest,
            })
            continue
        seen_hashes[digest] = item.display_name
        resolved.append(item)
    return resolved, duplicates


def _collection_member_rows(root: Path) -> list[tuple[str, Path, str, str | None]]:
    """Catalog every file before selecting content members or collapsing aliases."""

    rows: list[tuple[str, Path, str, str | None]] = []
    canonical_by_hash: dict[str, str] = {}
    for path in sorted(candidate for candidate in root.rglob("*") if candidate.is_file()):
        relative = path.relative_to(root).as_posix()
        digest = sha256_file(path)
        canonical = canonical_by_hash.get(digest)
        canonical_by_hash.setdefault(digest, relative)
        rows.append((relative, path, digest, canonical))
    return rows


def _collection_identifier(display_name: str, rows: list[tuple[str, Path, str, str | None]]) -> str:
    material = "\n".join(f"{relative}\t{digest}" for relative, _path, digest, _canonical in rows)
    return slugify(f"{display_name}-{sha256_text(material)[:16]}")


def _collection_sources_from_root(
    root: Path,
    display_name: str,
    display_prefix: str,
    derivation_chain: list[dict],
    *,
    requested_media_type: str | None = None,
) -> tuple[CollectionRuntime, list[SourceItem], list[dict]]:
    rows = _collection_member_rows(root)
    runtime = build_collection_runtime(
        _collection_identifier(display_name, rows),
        display_name,
        root,
        rows,
        content_extensions=DIRECT_SOURCE_EXTENSIONS,
        image_extensions=IMAGE_EXTENSIONS,
    )
    sources: list[SourceItem] = []
    aliases: list[dict] = []
    for relative, path, digest, canonical in rows:
        if runtime.member_categories.get(relative) != "content":
            continue
        display = f"{display_prefix}::{relative}" if display_prefix else relative
        if canonical is not None:
            aliases.append({
                "duplicate": display,
                "canonical": f"{display_prefix}::{canonical}" if display_prefix else canonical,
                "sha256": digest,
                "collection_id": runtime.collection_id,
            })
        sources.append(SourceItem(
            path=path,
            display_name=display,
            original_upload_name=path.name,
            requested_media_type=requested_media_type,
            derivation_chain=list(derivation_chain),
            collection_id=runtime.collection_id,
            collection_member_path=relative,
            collection_virtual_base_path=str(Path(relative).parent).replace("\\", "/"),
            canonical_member_path=canonical,
        ))
    return runtime, sources, aliases


def collect_collection_sources(
    input_path: Path,
    temp_root: Path,
    requested_media_type: str | None = None,
) -> tuple[list[SourceItem], list[dict], list[CollectionRuntime]]:
    """Collect ZIP, nested ZIP, or directory members without erasing aliases.

    This is intentionally separate from ``collect_sources`` so the frozen
    single-source and legacy deduplication behaviour remains unchanged.
    """

    input_path = input_path.resolve()
    if not input_path.exists():
        raise FileNotFoundError(str(input_path))
    if not input_path.is_dir() and input_path.suffix.lower() != ".zip":
        sources, duplicates = collect_sources(input_path, temp_root, requested_media_type)
        return sources, duplicates, []

    runtimes: list[CollectionRuntime] = []
    sources: list[SourceItem] = []
    aliases: list[dict] = []
    archive_counter = 0

    def walk(root: Path, display_name: str, display_prefix: str, chain: list[dict]) -> None:
        nonlocal archive_counter
        runtime, direct_sources, direct_aliases = _collection_sources_from_root(
            root,
            display_name,
            display_prefix,
            chain,
            requested_media_type=requested_media_type if not chain else None,
        )
        runtimes.append(runtime)
        sources.extend(direct_sources)
        aliases.extend(direct_aliases)
        for relative, path, _digest, _canonical in _collection_member_rows(root):
            if path.suffix.lower() != ".zip":
                continue
            archive_counter += 1
            child_root = temp_root / f"archive-{archive_counter:04d}"
            _safe_extract_zip(path, child_root)
            child_prefix = f"{display_prefix}::{relative}" if display_prefix else relative
            walk(
                child_root,
                child_prefix,
                child_prefix,
                chain + [{
                    "operation": "archive_extract",
                    "source": display_name,
                    "member": relative,
                }],
            )

    if input_path.is_dir():
        walk(input_path, input_path.name, "", [])
    else:
        archive_counter += 1
        root = temp_root / f"archive-{archive_counter:04d}"
        _safe_extract_zip(input_path, root)
        walk(root, input_path.name, input_path.name, [])
    return sources, aliases, runtimes


def build_provenance(item: SourceItem, adapter_name: str) -> Provenance:
    runtime_type, magic = runtime_media_type(item.path)
    requested = infer_requested_media_type(item.display_name, item.requested_media_type)
    derived_snapshot = requested != runtime_type and runtime_type in {"text/markdown", "text/plain"}
    original_binary_processed = not derived_snapshot and runtime_type != "application/octet-stream"
    fidelity = "derived_snapshot" if derived_snapshot else "original_binary"
    source_sha256 = sha256_file(item.path)
    if item.collection_id:
        # ``slugify`` deliberately truncates labels for readable output paths.
        # Keep path and binary fingerprints outside that truncated prefix so
        # similarly named collection members can never overwrite each other.
        source_id = f"{slugify(item.display_name)[:68]}-{sha256_text(item.display_name)[:12]}-{source_sha256[:12]}"
    else:
        source_id = slugify(f"{item.display_name}-{source_sha256[:12]}")
    return Provenance(
        source_id=source_id,
        user_specified_name=item.display_name,
        original_upload_name=item.original_upload_name,
        runtime_path=str(item.path.resolve()),
        extension=item.path.suffix.lower(),
        requested_media_type=requested,
        runtime_media_type=runtime_type,
        magic_bytes=magic,
        sha256=source_sha256,
        actual_adapter=adapter_name,
        original_binary_processed=original_binary_processed,
        derived_snapshot=derived_snapshot,
        input_fidelity=fidelity,
        derivation_chain=list(item.derivation_chain),
    )
