#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate declarative collection supplements before runtime integration.

The r3 helper validates provenance and one-to-one relationship assignments.
It intentionally does not read files, alter a Package IR, or change a
collection status.  A later runtime integration must verify supplied bytes and
re-run the normal collection validators.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
import re
from typing import Any, Mapping, Sequence
from urllib.parse import unquote, urlsplit


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_CATEGORIES = frozenset({"content", "resource"})


@dataclass(frozen=True)
class MissingRelationship:
    """Identify one original missing occurrence without collapsing duplicates."""

    source_member: str
    raw_reference: str
    relationship_type: str
    fragment: str
    location: str

    @property
    def key(self) -> tuple[str, str, str, str, str]:
        return (
            self.source_member,
            self.raw_reference,
            self.relationship_type,
            self.fragment,
            self.location,
        )


@dataclass(frozen=True)
class SupplementValidation:
    """Return validation evidence without pretending unresolved edges are fixed."""

    passed: bool
    violations: tuple[str, ...]
    resolved_relationships: tuple[MissingRelationship, ...]
    unresolved_relationships: tuple[MissingRelationship, ...]

    @property
    def fully_resolves_known_missing(self) -> bool:
        return self.passed and not self.unresolved_relationships


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and bool(_SHA256.fullmatch(value))


def _normalise_path(value: str) -> str:
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute():
        raise ValueError("absolute_path")
    parts: list[str] = []
    for part in path.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if not parts:
                raise ValueError("path_escape")
            parts.pop()
            continue
        parts.append(part)
    if not parts:
        raise ValueError("empty_path")
    return "/".join(parts)


def expected_target_member(edge: MissingRelationship) -> str:
    """Derive the required local target from one original missing edge."""

    parsed = urlsplit(edge.raw_reference)
    if parsed.scheme or parsed.netloc:
        raise ValueError("non_local_reference")
    raw_path = unquote(parsed.path)
    if not raw_path:
        raise ValueError("fragment_only_reference")
    if raw_path.startswith("/"):
        return _normalise_path(raw_path.lstrip("/"))
    return _normalise_path(str(PurePosixPath(edge.source_member).parent / raw_path))


def _edge_from_mapping(value: object) -> MissingRelationship:
    if not isinstance(value, Mapping):
        raise ValueError("edge_not_object")
    fields = ("source_member", "raw_reference", "relationship_type", "fragment", "location")
    if any(not isinstance(value.get(field), str) or not str(value.get(field)).strip() for field in fields):
        raise ValueError("edge_required_field_missing")
    return MissingRelationship(*(str(value[field]) for field in fields))


def validate_supplement_manifest(
    manifest: Mapping[str, Any],
    *,
    base_collection_sha256: str,
    missing_relationships: Sequence[MissingRelationship],
) -> SupplementValidation:
    """Validate a supplement's declared coverage against original missing edges.

    A manifest may deliberately cover only a subset.  The returned unresolved
    relationships remain evidence that the final collection must stay partial.
    """

    violations: list[str] = []
    resolved: list[MissingRelationship] = []
    expected = {edge.key: edge for edge in missing_relationships}
    assigned: set[tuple[str, str, str, str, str]] = set()

    if manifest.get("schema_version") != "1.0":
        violations.append("unsupported_schema_version")
    base = manifest.get("base")
    if not isinstance(base, Mapping) or base.get("collection_sha256") != base_collection_sha256:
        violations.append("base_collection_sha256_mismatch")
    members = manifest.get("members")
    if not isinstance(members, list) or not members:
        violations.append("members_missing")
        members = []

    target_members: set[str] = set()
    for index, member in enumerate(members):
        prefix = f"member_{index}"
        if not isinstance(member, Mapping):
            violations.append(f"{prefix}:not_object")
            continue
        try:
            target_member = _normalise_path(str(member.get("target_member") or ""))
        except ValueError as exc:
            violations.append(f"{prefix}:invalid_target_member:{exc}")
            continue
        if target_member in target_members:
            violations.append(f"{prefix}:duplicate_target_member")
        target_members.add(target_member)
        if member.get("category") not in _CATEGORIES:
            violations.append(f"{prefix}:invalid_category")
        if not _is_sha256(member.get("content_sha256")):
            violations.append(f"{prefix}:invalid_content_sha256")
        origin = member.get("origin")
        if not isinstance(origin, Mapping) or not isinstance(origin.get("kind"), str) or not origin.get("kind"):
            violations.append(f"{prefix}:origin_missing")
        elif not _is_sha256(origin.get("artifact_sha256")):
            violations.append(f"{prefix}:origin_artifact_sha256_invalid")
        edges = member.get("resolves")
        if not isinstance(edges, list) or not edges:
            violations.append(f"{prefix}:resolves_missing")
            continue
        for edge_value in edges:
            try:
                edge = _edge_from_mapping(edge_value)
            except ValueError as exc:
                violations.append(f"{prefix}:invalid_edge:{exc}")
                continue
            if edge.key not in expected:
                violations.append(f"{prefix}:edge_not_originally_missing")
                continue
            if edge.key in assigned:
                violations.append(f"{prefix}:edge_assigned_more_than_once")
                continue
            try:
                expected_target = expected_target_member(edge)
            except ValueError as exc:
                violations.append(f"{prefix}:edge_has_invalid_local_target:{exc}")
                continue
            if target_member != expected_target:
                violations.append(f"{prefix}:target_member_mismatch")
                continue
            assigned.add(edge.key)
            resolved.append(edge)

    unresolved = tuple(edge for edge in missing_relationships if edge.key not in assigned)
    return SupplementValidation(
        passed=not violations,
        violations=tuple(violations),
        resolved_relationships=tuple(resolved),
        unresolved_relationships=unresolved,
    )
