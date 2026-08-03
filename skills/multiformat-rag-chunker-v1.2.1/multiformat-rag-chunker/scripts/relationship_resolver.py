#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strict and evidence-backed relationship resolution for collections."""

from __future__ import annotations

from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from posixpath import normpath
import re
from typing import Mapping
from urllib.parse import unquote, urlsplit


@dataclass(frozen=True)
class RelationshipResolution:
    """Record both a preserved raw reference and its resolution result."""

    raw_reference: str
    source_member: str
    target_member: str | None
    fragment: str
    status: str
    strategy: str
    evidence: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class _DocumentSemantics:
    """Minimal, source-derived semantic identity for one HTML member."""

    member_path: str
    title: str
    anchors: frozenset[str]


class _SemanticsParser(HTMLParser):
    """Extract only title and explicit anchors without a DOM dependency."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_title = False
        self._title_parts: list[str] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.casefold() == "title":
            self._in_title = True
        for name, value in attrs:
            if name.casefold() in {"id", "name"} and value and value.strip():
                self.anchors.add(value.strip())

    def handle_startendtag(self, _tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name.casefold() in {"id", "name"} and value and value.strip():
                self.anchors.add(value.strip())

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self._title_parts).split())


def _semantic_key(value: str) -> str:
    return " ".join(value.split()).casefold()


def _normalise(path: str) -> str:
    value = normpath(path.replace("\\", "/")).lstrip("./")
    return "" if value in {".", "/"} else value


def _candidate_paths(path: str) -> tuple[str, ...]:
    candidate = _normalise(path)
    values = [candidate]
    lowered = candidate.lower()
    if lowered.endswith(".html"):
        values.append(candidate[:-5] + ".htm")
    elif lowered.endswith(".htm"):
        values.append(candidate[:-4] + ".html")
    return tuple(dict.fromkeys(values))


def _resolve_help_path(path: str) -> str:
    value = path.lstrip("/")
    for segment in ("topics/", "popups/"):
        index = value.lower().find(segment)
        if index >= 0:
            return value[index:]
    return value


def _qualified_help_bundle(path: str) -> str | None:
    """Return an explicit Help bundle identifier when the URI names one."""

    parts = path.lstrip("/").split("/", 1)
    if len(parts) < 2:
        return None
    bundle = parts[0].strip()
    return bundle if "." in bundle else None


def resolve_relationship(
    source_member: str,
    raw_reference: str,
    available_members: set[str],
) -> RelationshipResolution:
    """Resolve local references without treating source-missing targets as loss.

    The caller is responsible for persisting an edge for every invocation,
    including ``external`` and ``source_missing_target`` outcomes.
    """

    source = _normalise(source_member)
    reference = raw_reference.strip()
    if reference.startswith("help::"):
        payload = urlsplit(reference.split("::", 1)[1])
        decoded_help_path = unquote(payload.path)
        candidate = _resolve_help_path(decoded_help_path)
        for value in _candidate_paths(candidate):
            if value in available_members:
                return RelationshipResolution(reference, source, value, payload.fragment, "resolved", "help_scheme")
        if _qualified_help_bundle(decoded_help_path):
            # A bundle-qualified Help URI names another documentation package
            # when no matching member exists locally.  It is an explicit
            # external dependency, not evidence that this source archive lost
            # a member.
            return RelationshipResolution(reference, source, None, payload.fragment, "external", "help_external_bundle")
        return RelationshipResolution(reference, source, None, payload.fragment, "source_missing_target", "help_scheme")

    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc:
        return RelationshipResolution(reference, source, None, parsed.fragment, "external", "external_uri")
    if re.fullmatch(r"[^\s@/]+@[^\s@/]+\.[^\s@/]+", reference):
        return RelationshipResolution(reference, source, None, "", "external", "bare_email")

    decoded_path = unquote(parsed.path)
    if not decoded_path and parsed.fragment:
        if source in available_members:
            return RelationshipResolution(reference, source, source, parsed.fragment, "resolved", "same_member_fragment")
        return RelationshipResolution(reference, source, None, parsed.fragment, "source_missing_target", "same_member_fragment")
    if decoded_path.startswith("/"):
        candidate = decoded_path.lstrip("/")
        strategy = "collection_root"
    else:
        candidate = str(PurePosixPath(source).parent / decoded_path)
        strategy = "relative_path"
    for value in _candidate_paths(candidate):
        if value in available_members:
            return RelationshipResolution(reference, source, value, parsed.fragment, "resolved", strategy)
    return RelationshipResolution(reference, source, None, parsed.fragment, "source_missing_target", strategy)


class CollectionRelationshipResolver:
    """Reconcile only package-internal targets backed by deterministic evidence.

    Exact relative-path resolution remains the default.  This second stage runs
    only after an explicit ``source_missing_target`` result and accepts two
    narrowly-defined proofs:

    * an identical source-member alias resolves the same raw reference; or
    * exactly one local HTML member has both the referenced fragment and a
      document title exactly matching an explicit source-side label or title.

    It never guesses from a basename, a fuzzy title, or a member in another
    package.  The raw reference remains untouched and the returned evidence is
    persisted with the relationship occurrence.
    """

    def __init__(
        self,
        available_members: set[str],
        aliases_by_member: Mapping[str, tuple[str, ...]],
        member_hashes: Mapping[str, str],
        semantic_targets: Mapping[str, tuple[_DocumentSemantics, ...]],
    ) -> None:
        self.available_members = set(available_members)
        self.aliases_by_member = dict(aliases_by_member)
        self.member_hashes = dict(member_hashes)
        self.semantic_targets = dict(semantic_targets)

    def resolve(
        self,
        source_member: str,
        raw_reference: str,
        *,
        semantic_hint: str = "",
    ) -> RelationshipResolution:
        direct = resolve_relationship(source_member, raw_reference, self.available_members)
        if direct.status != "source_missing_target":
            return direct

        for alias_member in self.aliases_by_member.get(direct.source_member, ()):
            if alias_member == direct.source_member:
                continue
            alias_resolution = resolve_relationship(alias_member, direct.raw_reference, self.available_members)
            if alias_resolution.status == "resolved" and alias_resolution.target_member:
                return RelationshipResolution(
                    direct.raw_reference,
                    direct.source_member,
                    alias_resolution.target_member,
                    direct.fragment,
                    "resolved",
                    "equivalent_source_alias",
                    {
                        "evidence_kind": "identical_source_member",
                        "alias_member": alias_member,
                        "alias_sha256": self.member_hashes.get(alias_member, ""),
                    },
                )

        hint_key = _semantic_key(semantic_hint)
        if not direct.fragment or not hint_key:
            return direct
        candidates = [
            target
            for target in self.semantic_targets.get(direct.fragment, ())
            if _semantic_key(target.title) == hint_key
        ]
        if len(candidates) != 1:
            return direct
        target = candidates[0]
        return RelationshipResolution(
            direct.raw_reference,
            direct.source_member,
            target.member_path,
            direct.fragment,
            "resolved",
            "semantic_fragment_title",
            {
                "evidence_kind": "unique_fragment_and_title",
                "semantic_hint": " ".join(semantic_hint.split()),
                "target_title": target.title,
                "target_sha256": self.member_hashes.get(target.member_path, ""),
            },
        )


def build_collection_relationship_resolver(
    member_paths: Mapping[str, Path],
    member_hashes: Mapping[str, str],
) -> CollectionRelationshipResolver:
    """Build a resolver index from members already present in one collection."""

    normalized_paths = {_normalise(path): value for path, value in member_paths.items()}
    normalized_hashes = {_normalise(path): value for path, value in member_hashes.items()}
    paths_by_hash: dict[str, list[str]] = {}
    for member_path, digest in normalized_hashes.items():
        paths_by_hash.setdefault(digest, []).append(member_path)
    aliases_by_member = {
        member_path: tuple(sorted(paths_by_hash[digest]))
        for member_path, digest in normalized_hashes.items()
        if len(paths_by_hash[digest]) > 1
    }

    semantic_targets: dict[str, list[_DocumentSemantics]] = {}
    for member_path, path in normalized_paths.items():
        if path.suffix.casefold() not in {".htm", ".html"}:
            continue
        try:
            parser = _SemanticsParser()
            parser.feed(path.read_text(encoding="utf-8", errors="replace"))
            parser.close()
        except OSError:
            continue
        if not parser.title or not parser.anchors:
            continue
        target = _DocumentSemantics(member_path, parser.title, frozenset(parser.anchors))
        for anchor in target.anchors:
            semantic_targets.setdefault(anchor, []).append(target)

    return CollectionRelationshipResolver(
        set(normalized_paths),
        {member: tuple(values) for member, values in aliases_by_member.items()},
        normalized_hashes,
        {fragment: tuple(values) for fragment, values in semantic_targets.items()},
    )
