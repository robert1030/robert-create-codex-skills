#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independently audit source semantics that adapters must not silently drop."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping

from utils import normalize_nfc


XML_VISIBLE_ATTRIBUTES: dict[str, tuple[tuple[str, str, bool], ...]] = {
    "cheatsheet": (("title", "document_title", True),),
    "compositecheatsheet": (("name", "document_title", True),),
    "taskgroup": (("name", "procedure_group", True),),
    "task": (("name", "procedure_step", True),),
    "item": (("title", "procedure_step", True),),
    "subitem": (("label", "procedure_detail", True),),
}


def _compact(value: object) -> str:
    return re.sub(r"\s+", " ", normalize_nfc(str(value or ""))).strip()


def _xml_expectations(path: Path) -> list[dict[str, Any]]:
    from lxml import etree

    parser = etree.XMLParser(resolve_entities=False, no_network=True, recover=False, huge_tree=False)
    tree = etree.parse(str(path), parser)
    expected: list[dict[str, Any]] = []
    for element in tree.getroot().iter():
        if not isinstance(element.tag, str):
            continue
        tag = element.tag.split("}")[-1].lower()
        for attribute, role, critical in XML_VISIBLE_ATTRIBUTES.get(tag, ()):
            value = _compact(element.attrib.get(attribute))
            if value:
                expected.append({
                    "kind": "xml_visible_attribute",
                    "role": role,
                    "critical": critical,
                    "value": value,
                    "location": tree.getpath(element),
                    "attribute": attribute,
                })
    return expected


def _html_expectations(path: Path) -> list[dict[str, Any]]:
    from bs4 import BeautifulSoup
    from bs4.element import NavigableString, Tag

    raw_html = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw_html, "html.parser")
    raw_lists = list(re.finditer(
        r"<(?P<tag>ul|ol)\b[^>]*>(?P<body>.*?)(?:</(?P=tag)\s*>|(?=</body\b)|\Z)",
        raw_html,
        flags=re.IGNORECASE | re.DOTALL,
    ))
    expected: list[dict[str, Any]] = []
    for list_index, container in enumerate(soup.find_all(["ul", "ol"]), start=1):
        raw_body = ""
        if list_index <= len(raw_lists):
            candidate = raw_lists[list_index - 1]
            if candidate.group("tag").casefold() == container.name.casefold():
                raw_body = candidate.group("body")
        raw_paragraphs = [
            _compact(BeautifulSoup(fragment, "html.parser").get_text(" ", strip=True))
            for fragment in re.findall(
                r"<p\b[^>]*>(.*?)(?=</p\s*>|<p\b|</(?:ul|ol)\b|$)",
                raw_body,
                flags=re.IGNORECASE | re.DOTALL,
            )
        ]
        raw_paragraphs = [value for value in raw_paragraphs if value]
        if raw_paragraphs:
            # Broken Help HTML often omits closing </p> tags. BeautifulSoup
            # merges those paragraphs, whereas the adapter's HTML recovery
            # retains one list item per source paragraph. Audit the original
            # paragraph boundaries so the checker measures semantics, not the
            # recovery quirks of its own parser.
            for paragraph_index, value in enumerate(raw_paragraphs, start=1):
                expected.append({
                    "kind": "html_nonstandard_list_content",
                    "role": "list_direct_child",
                    "critical": False,
                    "value": value,
                    "location": f"{container.name}[{list_index}]/raw-p[{paragraph_index}]",
                })
        for child_index, child in enumerate(container.contents, start=1):
            if isinstance(child, NavigableString):
                value = _compact(child)
            elif isinstance(child, Tag):
                if child.name in {"li", "script", "style", "noscript", "template", "br"}:
                    continue
                if raw_paragraphs and child.name == "p":
                    continue
                value = _compact(child.get_text(" ", strip=True))
            else:
                continue
            if value:
                expected.append({
                    "kind": "html_nonstandard_list_content",
                    "role": "list_direct_child",
                    "critical": False,
                    "value": value,
                    "location": f"{container.name}[{list_index}]/direct-child[{child_index}]",
                })
    for table_index, table in enumerate(soup.find_all("table"), start=1):
        caption = table.find("caption", recursive=False)
        value = _compact(caption.get_text(" ", strip=True)) if caption else ""
        if value:
            expected.append({
                "kind": "table_caption",
                "role": "table_caption",
                "critical": False,
                "value": value,
                "location": f"table[{table_index}]/caption[1]",
            })
    return expected


def source_semantic_expectations(path: Path) -> list[dict[str, Any]]:
    """Extract only the raw-source semantic units covered by this hardening release."""

    extension = path.suffix.lower()
    if extension == ".xml":
        return _xml_expectations(path)
    if extension in {".html", ".htm"}:
        return _html_expectations(path)
    return []


def observed_semantic_units(
    blocks: Iterable[object],
    normalized_markdown: str = "",
) -> list[str]:
    """Collect independently matchable units from Document IR plus rendered Markdown."""

    units: list[str] = []
    for block in blocks:
        if isinstance(block, Mapping):
            text = block.get("text", "")
            metadata = block.get("metadata", {})
        else:
            text = getattr(block, "text", "")
            metadata = getattr(block, "metadata", {})
        value = _compact(text)
        if value:
            units.append(value)
        if not isinstance(metadata, Mapping):
            continue
        items = metadata.get("items")
        if isinstance(items, list):
            units.extend(value for item in items if (value := _compact(item)))
        caption = _compact(metadata.get("caption"))
        if caption:
            units.append(caption)
    rendered = _compact(normalized_markdown)
    # IR units are the primary evidence. The complete rendered document is a
    # fallback only for callers with no IR; otherwise one large Markdown value
    # could accidentally satisfy more than one repeated source value.
    if rendered and not units:
        units.append(rendered)
    return units


def _matches(expected: str, observed: str) -> bool:
    return expected.casefold() in observed.casefold()


def audit_source_semantics(path: Path, observed_units: Iterable[str]) -> dict[str, Any]:
    """Compare raw semantic units against rendered or IR evidence without trusting adapters."""

    expected = source_semantic_expectations(path)
    if not expected:
        return {
            "status": "not_applicable",
            "expected_total": 0,
            "verified_total": 0,
            "critical_expected_total": 0,
            "critical_verified_total": 0,
            "coverage_ratio": None,
            "critical_coverage_ratio": None,
            "by_kind": {},
            "missing": [],
        }
    available = [_compact(value) for value in observed_units if _compact(value)]
    matched: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    for item in expected:
        index = next((index for index, value in enumerate(available) if _matches(str(item["value"]), value)), None)
        if index is None:
            missing.append(item)
        else:
            matched.append(item)
            available.pop(index)
    expected_by_kind = Counter(str(item["kind"]) for item in expected)
    verified_by_kind = Counter(str(item["kind"]) for item in matched)
    critical_expected = sum(bool(item["critical"]) for item in expected)
    critical_verified = sum(bool(item["critical"]) for item in matched)
    return {
        "status": "passed" if not missing else "failed",
        "expected_total": len(expected),
        "verified_total": len(matched),
        "critical_expected_total": critical_expected,
        "critical_verified_total": critical_verified,
        "coverage_ratio": round(len(matched) / len(expected), 6),
        "critical_coverage_ratio": round(critical_verified / critical_expected, 6) if critical_expected else None,
        "by_kind": {
            kind: {"expected": count, "verified": verified_by_kind.get(kind, 0)}
            for kind, count in sorted(expected_by_kind.items())
        },
        "missing": missing,
    }
