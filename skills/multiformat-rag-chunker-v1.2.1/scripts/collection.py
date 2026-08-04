#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Collection planning primitives for v1.2.0-dev-r1.

This module is deliberately not imported by the v1.1.2 processing path.  It
defines the stable planning boundary that a later development revision can
wire into intake without changing existing single-source behaviour first.
"""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping

from relationship_resolver import CollectionRelationshipResolver, build_collection_relationship_resolver, resolve_relationship
from utils import sha256_text


GENERIC_COLLECTION = "generic_collection"
LINKED_MARKUP_COLLECTION = "linked_markup_collection"
ECLIPSE_HELP_COLLECTION = "eclipse_help_collection"


@dataclass(frozen=True)
class CollectionProfile:
    """Describe a selected collection strategy without parsing source content."""

    name: str
    reason: str
    requires_control_documents: bool


@dataclass(frozen=True)
class CollectionMember:
    """Keep a member identity even when its binary blob has a duplicate alias."""

    relative_path: str
    sha256: str
    virtual_base_path: str
    canonical_member: str | None = None


@dataclass(frozen=True)
class CollectionInventory:
    """Capture collection membership before any Adapter can discard context."""

    collection_id: str
    members: tuple[CollectionMember, ...]
    profile: CollectionProfile

    @property
    def alias_count(self) -> int:
        return sum(member.canonical_member is not None for member in self.members)


@dataclass(frozen=True)
class CollectionRuntime:
    """Keep runtime paths separate from the serialisable collection inventory."""

    collection_id: str
    display_name: str
    root_path: Path
    inventory: CollectionInventory
    member_paths: Mapping[str, Path]
    member_categories: Mapping[str, str]
    toc_paths: Mapping[str, tuple[str, ...]]
    toc_order: Mapping[str, int]
    toc_occurrences: tuple[dict[str, object], ...]
    control_relationships: tuple[dict[str, object], ...]
    relationship_resolver: CollectionRelationshipResolver

    @property
    def available_members(self) -> set[str]:
        return set(self.member_paths)

    def path_for(self, member_path: str) -> Path | None:
        return self.member_paths.get(_normalise_member_path(member_path))

    def resolve_relationship(
        self,
        source_member: str,
        raw_reference: str,
        *,
        semantic_hint: str = "",
    ):
        """Resolve one edge with strict matching before internal reconciliation."""

        return self.relationship_resolver.resolve(
            source_member,
            raw_reference,
            semantic_hint=semantic_hint,
        )

    def context_for(self, member_path: str) -> dict[str, object]:
        normalized = _normalise_member_path(member_path)
        return {
            "collection_id": self.collection_id,
            "profile": self.inventory.profile.name,
            "profile_reason": self.inventory.profile.reason,
            "member_path": normalized,
            "virtual_base_path": str(PurePosixPath(normalized).parent),
            "member_category": self.member_categories.get(normalized, "resource"),
            "toc_heading_path": list(self.toc_paths.get(normalized, ())),
            "toc_order": self.toc_order.get(normalized),
        }


def _normalise_member_path(value: str) -> str:
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"invalid_collection_member_path:{value}")
    return path.as_posix().lstrip("./")


def select_collection_profile(
    member_paths: Iterable[str],
    *,
    markers: Mapping[str, bool] | None = None,
) -> CollectionProfile:
    """Choose the least-specific verified profile for a collection.

    A path named ``toc.xml`` is not enough to infer an Eclipse Help package.
    The caller must separately prove the parser-specific marker, for example an
    Eclipse namespace or processing instruction, before the specialised profile
    can be selected.
    """

    paths = {_normalise_member_path(value).lower() for value in member_paths}
    has_html = any(path.endswith((".html", ".htm")) for path in paths)
    has_xml = any(path.endswith(".xml") for path in paths)
    signals = {key: bool(value) for key, value in (markers or {}).items()}
    required_controls = {"toc.xml", "contexts.xml", "index.xml"}
    if required_controls.issubset(paths) and signals.get("eclipse_help_signature", False):
        return CollectionProfile(
            ECLIPSE_HELP_COLLECTION,
            "verified_eclipse_help_controls_and_signature",
            True,
        )
    if has_html or has_xml:
        return CollectionProfile(
            LINKED_MARKUP_COLLECTION,
            "multiple_html_or_xml_members_without_profile_assumption",
            False,
        )
    return CollectionProfile(
        GENERIC_COLLECTION,
        "multiple_members_without_markup_profile",
        False,
    )


def build_collection_inventory(
    collection_id: str,
    members: Iterable[CollectionMember],
    *,
    markers: Mapping[str, bool] | None = None,
) -> CollectionInventory:
    """Validate member paths and select a profile without collapsing aliases."""

    normalized = tuple(
        CollectionMember(
            relative_path=_normalise_member_path(member.relative_path),
            sha256=member.sha256,
            virtual_base_path=_normalise_member_path(member.virtual_base_path),
            canonical_member=(
                _normalise_member_path(member.canonical_member)
                if member.canonical_member is not None
                else None
            ),
        )
        for member in members
    )
    if not normalized:
        raise ValueError("collection_requires_members")
    profile = select_collection_profile(
        (member.relative_path for member in normalized),
        markers=markers,
    )
    return CollectionInventory(collection_id=collection_id, members=normalized, profile=profile)


def _eclipse_help_signature(root_path: Path) -> bool:
    """Require an actual Eclipse Help marker, never only familiar filenames."""

    toc = root_path / "toc.xml"
    if not toc.is_file():
        return False
    try:
        sample = toc.read_bytes()[:262144].decode("utf-8", errors="replace").lower()
    except OSError:
        return False
    return "org.eclipse.help.toc" in sample or "eclipse-toc-schema" in sample


def _eclipse_toc_semantics(runtime: CollectionRuntime) -> tuple[dict[str, tuple[str, ...]], dict[str, int], tuple[dict[str, object], ...]]:
    """Parse only a verified Eclipse TOC and preserve preorder plus sibling order."""

    toc = runtime.path_for("toc.xml")
    if toc is None:
        return {}, {}, ()
    try:
        from xml.etree import ElementTree

        root = ElementTree.parse(toc).getroot()
    except Exception:
        return {}, {}, ()

    def local_name(value: str) -> str:
        return value.split("}")[-1].lower()

    paths: dict[str, tuple[str, ...]] = {}
    order: dict[str, int] = {}
    occurrences: list[dict[str, object]] = []
    preorder = 0

    def walk(element, parent_path: tuple[str, ...], depth: int, sibling_index: int) -> None:
        nonlocal preorder
        if local_name(str(element.tag)) != "topic":
            for child_index, child in enumerate(list(element), start=1):
                walk(child, parent_path, depth, child_index)
            return
        label = str(element.attrib.get("label") or "").strip()
        current_path = parent_path + ((label,) if label else ())
        href = str(element.attrib.get("href") or "").strip()
        if href:
            preorder += 1
            resolved = runtime.resolve_relationship("toc.xml", href, semantic_hint=label)
            occurrence = {
                "source_member": "toc.xml",
                "raw_reference": href,
                "target_member": resolved.target_member,
                "fragment": resolved.fragment,
                "status": resolved.status,
                "strategy": resolved.strategy,
                "evidence": resolved.evidence,
                "preorder": preorder,
                "sibling_index": sibling_index,
                "depth": depth,
                "heading_path": list(current_path),
            }
            occurrences.append(occurrence)
            if resolved.status == "resolved" and resolved.target_member:
                paths.setdefault(resolved.target_member, current_path)
                order.setdefault(resolved.target_member, preorder)
        for child_index, child in enumerate(list(element), start=1):
            walk(child, current_path, depth + 1, child_index)

    walk(root, (), 0, 1)
    return paths, order, tuple(occurrences)


def _control_relationship_records(runtime: CollectionRuntime) -> tuple[dict[str, object], ...]:
    """Keep profile control-file references even though controls are not chunked."""

    try:
        from xml.etree import ElementTree
    except ImportError:
        return ()
    records: list[dict[str, object]] = []
    relationship_attributes = {"href", "src", "data", "target", "link", "url", "uri", "topic", "context", "file"}
    for member_path, category in runtime.member_categories.items():
        if category != "control" or not member_path.lower().endswith(".xml"):
            continue
        path = runtime.path_for(member_path)
        if path is None:
            continue
        try:
            root = ElementTree.parse(path).getroot()
        except Exception:
            continue
        for element in root.iter():
            tag = str(element.tag).split("}")[-1].lower()
            for attribute, raw_value in element.attrib.items():
                name = str(attribute).split("}")[-1].lower()
                value = str(raw_value).strip()
                if name not in relationship_attributes or not value:
                    continue
                if name in {"target", "context"} and not any(token in value for token in ("/", ".", ":", "#")):
                    records.append({
                        "raw_reference": value,
                        "source_member": member_path,
                        "location": f"xml:{tag}",
                        "relationship_type": f"xml_{tag}_{name}",
                        "target_member": None,
                        "fragment": "",
                        "status": "non_file_identifier",
                        "strategy": "attribute_identifier",
                    })
                    continue
                semantic_hint = str(element.attrib.get("title") or element.attrib.get("label") or "").strip()
                resolution = runtime.resolve_relationship(member_path, value, semantic_hint=semantic_hint)
                records.append({
                    "raw_reference": resolution.raw_reference,
                    "source_member": resolution.source_member,
                    "location": f"xml:{tag}",
                    "relationship_type": f"xml_{tag}_{name}",
                    "target_member": resolution.target_member,
                    "fragment": resolution.fragment,
                    "status": resolution.status,
                    "strategy": resolution.strategy,
                    "evidence": resolution.evidence,
                })
    return tuple(records)


def _referenced_members(member_paths: Mapping[str, Path]) -> set[str]:
    """Classify referenced binaries as collection resources without site assumptions."""

    available = set(member_paths)
    referenced: set[str] = set()

    class AttributeCollector(HTMLParser):
        def __init__(self, source_member: str) -> None:
            super().__init__(convert_charrefs=False)
            self.source_member = source_member

        def handle_starttag(self, _tag: str, attrs: list[tuple[str, str | None]]) -> None:
            for name, value in attrs:
                if name.lower() not in {"href", "src", "data"} or not value:
                    continue
                resolution = resolve_relationship(self.source_member, value, available)
                if resolution.status == "resolved" and resolution.target_member:
                    referenced.add(resolution.target_member)

    xml_attributes = {"href", "src", "data", "target", "link", "url", "uri", "topic", "context", "file"}
    for member_path, path in member_paths.items():
        extension = path.suffix.lower()
        try:
            if extension in {".html", ".htm"}:
                parser = AttributeCollector(member_path)
                parser.feed(path.read_text(encoding="utf-8", errors="replace"))
                parser.close()
            elif extension == ".xml":
                from xml.etree import ElementTree

                root = ElementTree.parse(path).getroot()
                for element in root.iter():
                    for attribute, value in element.attrib.items():
                        name = str(attribute).split("}")[-1].lower()
                        if name not in xml_attributes or not str(value).strip():
                            continue
                        resolution = resolve_relationship(member_path, str(value), available)
                        if resolution.status == "resolved" and resolution.target_member:
                            referenced.add(resolution.target_member)
        except Exception:
            # A malformed document cannot safely demote a binary to resource.
            continue
    return referenced


def _xml_is_semantic_content(path: Path) -> bool:
    """Conservatively distinguish authored XML from collection support data.

    This is intentionally a structural check, never a path or product-name
    allowlist.  Malformed XML remains content so an Adapter failure is visible
    instead of silently excluding a potentially authored document.
    """

    try:
        from xml.etree import ElementTree

        root = ElementTree.parse(path).getroot()
    except Exception:
        return True

    def local_name(value: object) -> str:
        return str(value).split("}")[-1].lower()

    root_name = local_name(root.tag)
    namespace = str(root.tag).split("}", 1)[0].lstrip("{").lower()
    textual_nodes: list[tuple[str, str]] = []
    for element in root.iter():
        if not isinstance(element.tag, str):
            continue
        name = local_name(element.tag)
        for value in (element.text, element.tail):
            compact = " ".join((value or "").split())
            if compact and any(character.isalnum() for character in compact):
                textual_nodes.append((name, compact))

    if not textual_nodes:
        return False

    narrative_tags = {
        "article", "body", "chapter", "cheatsheet", "concept", "description",
        "document", "guide", "help", "intro", "item", "page", "para",
        "paragraph", "procedure", "reference", "section", "step", "task",
        "title", "topic", "tutorial",
    }
    has_narrative_structure = any(name in narrative_tags for name, _value in textual_nodes)

    # Generated diagnostics identify themselves through their XML vocabulary,
    # rather than their location.  They are collection evidence/resources, not
    # end-user knowledge documents.  A plain ``<report>`` with narrative
    # content is deliberately not demoted without this namespace signal.
    if root_name == "report" and "report" in namespace:
        return False

    # Publisher support registries can contain words such as MIME values or
    # stop-word lists, but do not represent an authored knowledge document.
    # The decision is based on generic XML vocabulary plus the absence of any
    # narrative structure, never on a package path or publisher name.
    support_vocabulary = (
        "catalog", "config", "locale", "manifest", "mapentry", "mime",
        "plugin", "schema", "settings", "style", "stylesheet", "xslt",
    )
    vocabulary = f"{root_name} {namespace}"
    if not has_narrative_structure and any(token in vocabulary for token in support_vocabulary):
        return False

    return True


def build_collection_runtime(
    collection_id: str,
    display_name: str,
    root_path: Path,
    members: Iterable[tuple[str, Path, str, str | None]],
    *,
    content_extensions: set[str],
    image_extensions: set[str],
) -> CollectionRuntime:
    """Build generic inventory first, then add verified profile semantics only."""

    materialized = tuple(members)
    markers = {"eclipse_help_signature": _eclipse_help_signature(root_path)}
    inventory = build_collection_inventory(
        collection_id,
        (
            CollectionMember(
                relative_path=relative_path,
                sha256=sha256,
                virtual_base_path=str(PurePosixPath(_normalise_member_path(relative_path)).parent),
                canonical_member=canonical_member,
            )
            for relative_path, _path, sha256, canonical_member in materialized
        ),
        markers=markers,
    )
    paths = {
        _normalise_member_path(relative_path): path
        for relative_path, path, _sha256, _canonical_member in materialized
    }
    member_hashes = {
        _normalise_member_path(relative_path): sha256
        for relative_path, _path, sha256, _canonical_member in materialized
    }
    resolver = build_collection_relationship_resolver(paths, member_hashes)
    referenced_members = _referenced_members(paths)
    controls = {"toc.xml", "contexts.xml", "index.xml"}
    categories: dict[str, str] = {}
    for member in inventory.members:
        extension = PurePosixPath(member.relative_path).suffix.lower()
        if inventory.profile.name == ECLIPSE_HELP_COLLECTION and member.relative_path.lower() in controls:
            categories[member.relative_path] = "control"
        elif extension in image_extensions and inventory.profile.name == ECLIPSE_HELP_COLLECTION:
            # A verified Eclipse Help package owns visual binaries as package
            # resources, including CSS- and runtime-referenced assets that do
            # not appear in a plain HTML ``src`` attribute.  Generic
            # collections retain the established direct-image behaviour.
            categories[member.relative_path] = "resource"
        elif (
            extension == ".xml"
            and inventory.profile.name in {LINKED_MARKUP_COLLECTION, ECLIPSE_HELP_COLLECTION}
            and not _xml_is_semantic_content(paths[member.relative_path])
        ):
            # XML configuration, schema, index, and generated diagnostics are
            # catalogued as resources.  Authored XML remains content based on
            # structure and text, not package-specific names or paths.
            categories[member.relative_path] = "resource"
        elif extension in content_extensions:
            categories[member.relative_path] = "content"
        else:
            categories[member.relative_path] = "resource"
    provisional = CollectionRuntime(
        collection_id=collection_id,
        display_name=display_name,
        root_path=root_path,
        inventory=inventory,
        member_paths=paths,
        member_categories=categories,
        toc_paths={},
        toc_order={},
        toc_occurrences=(),
        control_relationships=(),
        relationship_resolver=resolver,
    )
    if inventory.profile.name != ECLIPSE_HELP_COLLECTION:
        return provisional
    toc_paths, toc_order, toc_occurrences = _eclipse_toc_semantics(provisional)
    return CollectionRuntime(
        collection_id=collection_id,
        display_name=display_name,
        root_path=root_path,
        inventory=inventory,
        member_paths=paths,
        member_categories=categories,
        toc_paths=toc_paths,
        toc_order=toc_order,
        toc_occurrences=toc_occurrences,
        control_relationships=_control_relationship_records(provisional),
        relationship_resolver=resolver,
    )


def _merge_heading_paths(prefix: tuple[str, ...], value: list[str]) -> list[str]:
    """Add verified collection context without duplicating a document H1."""

    merged = list(prefix)
    suffix = list(value)
    if merged and suffix and merged[-1].casefold() == suffix[0].casefold():
        suffix = suffix[1:]
    return merged + suffix


def attach_collection_context(document, runtime: CollectionRuntime, member_path: str, canonical_member: str | None) -> None:
    """Annotate one Document IR after parsing, before normalisation and chunking."""

    normalized = _normalise_member_path(member_path)
    context = runtime.context_for(normalized)
    context["canonical_member"] = canonical_member
    document.metadata["collection"] = context
    document.metadata.setdefault("relationships", [])
    prefix = tuple(str(value) for value in context.get("toc_heading_path", []) if value)
    for index, block in enumerate(document.blocks, start=1):
        block.metadata.setdefault("source_order", index)
        block.metadata["collection_occurrence"] = {
            "source_member": normalized,
            "occurrence_index": index,
            "source_order": block.metadata["source_order"],
            "raw_text_sha256": sha256_text(block.raw_text if block.raw_text is not None else block.text),
        }
        if prefix:
            block.metadata["collection_heading_path"] = list(prefix)
            block.heading_path = _merge_heading_paths(prefix, block.heading_path)
    document.metadata["collection_semantic_occurrence_total"] = len(document.blocks)
    document.metadata["collection_semantic_occurrence_accounted"] = len(document.blocks)
