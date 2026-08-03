#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XML adapter with external entities disabled and XPath locators."""

from __future__ import annotations

import re
from pathlib import Path

from adapters.base import AdapterContext
from models import DocumentIR, Location
from relationship_resolver import resolve_relationship
from utils import normalize_nfc

HEADING_TAGS = {"title", "heading", "h1", "h2", "h3", "h4", "section", "chapter"}
CODE_TAGS = {"code", "pre", "command", "example"}
LIST_TAGS = {"ul", "ol", "list", "steps"}
ITEM_TAGS = {"li", "item", "step"}
RELATIONSHIP_ATTRIBUTES = {"href", "src", "data", "target", "link", "url", "uri", "topic", "context", "file"}
VISIBLE_ATTRIBUTE_SPECS = {
    "cheatsheet": (("title", "document_title", True),),
    "compositecheatsheet": (("name", "document_title", True),),
    "taskgroup": (("name", "procedure_group", True),),
    "task": (("name", "procedure_step", True),),
    "item": (("title", "procedure_step", True),),
    "subitem": (("label", "procedure_detail", True),),
}


def _local_name(element) -> str:
    return element.tag.split("}")[-1].lower() if isinstance(element.tag, str) else ""


def _relationship_records(tree, root, context: AdapterContext) -> list[dict[str, object]]:
    """Keep XML references auditable without treating identifiers as lost files."""

    if context.collection_runtime is None or not context.collection_member_path:
        return []
    records: list[dict[str, object]] = []
    for element in root.iter():
        if not isinstance(element.tag, str):
            continue
        tag = _local_name(element)
        for attribute, raw_value in element.attrib.items():
            name = attribute.split("}")[-1].lower()
            value = str(raw_value).strip()
            if name not in RELATIONSHIP_ATTRIBUTES or not value:
                continue
            if name in {"target", "context"} and not any(token in value for token in ("/", ".", ":", "#")):
                records.append({
                    "raw_reference": value,
                    "source_member": context.collection_member_path,
                    "location": tree.getpath(element),
                    "relationship_type": f"xml_{_local_name(element)}_{name}",
                    "target_member": None,
                    "fragment": "",
                    "status": "non_file_identifier",
                    "strategy": "attribute_identifier",
                })
                continue
            semantic_hint = str(element.attrib.get("title") or element.attrib.get("label") or "").strip()
            resolution = context.collection_runtime.resolve_relationship(
                context.collection_member_path,
                value,
                semantic_hint=semantic_hint,
            )
            records.append({
                "raw_reference": resolution.raw_reference,
                "source_member": resolution.source_member,
                "location": tree.getpath(element),
                "relationship_type": f"xml_{_local_name(element)}_{name}",
                "target_member": resolution.target_member,
                "fragment": resolution.fragment,
                "status": resolution.status,
                "strategy": resolution.strategy,
                "evidence": resolution.evidence,
            })
        if tag == "param" and str(element.attrib.get("name") or "").strip().lower() == "path":
            value = str(element.attrib.get("value") or "").strip()
            if value:
                resolution = context.collection_runtime.resolve_relationship(
                    context.collection_member_path,
                    value,
                )
                records.append({
                    "raw_reference": resolution.raw_reference,
                    "source_member": resolution.source_member,
                    "location": tree.getpath(element),
                    "relationship_type": "xml_param_value",
                    "target_member": resolution.target_member,
                    "fragment": resolution.fragment,
                    "status": resolution.status,
                    "strategy": resolution.strategy,
                    "evidence": resolution.evidence,
                })
    return records


def _visible_attribute_blocks(element, tree, context, heading_path: list[str]) -> tuple[list, list[str], str | None]:
    """Emit user-visible XML attributes before descendant prose is traversed."""

    tag = _local_name(element)
    blocks = []
    updated_path = list(heading_path)
    document_title: str | None = None
    xpath = tree.getpath(element)
    for attribute, role, critical in VISIBLE_ATTRIBUTE_SPECS.get(tag, ()):
        value = normalize_nfc(str(element.attrib.get(attribute) or "")).strip()
        if not value:
            continue
        metadata = {
            "tag": tag,
            "semantic_attribute": attribute,
            "semantic_role": role,
        }
        if role == "document_title":
            updated_path = [value]
            document_title = value
            blocks.append(context.block(
                "heading", value, location=Location(xml_path=xpath), heading_path=list(updated_path),
                content_origin="native_text", required=True, critical=critical,
                metadata={**metadata, "level": 1},
            ))
        elif role == "procedure_group":
            updated_path = updated_path[:1] + [value] if updated_path else [value]
            blocks.append(context.block(
                "heading", value, location=Location(xml_path=xpath), heading_path=list(updated_path),
                content_origin="native_text", required=True, critical=critical,
                metadata={**metadata, "level": min(6, len(updated_path))},
            ))
        else:
            blocks.append(context.block(
                "paragraph", value, location=Location(xml_path=xpath), heading_path=list(updated_path),
                content_origin="native_text", required=True, critical=critical, metadata=metadata,
            ))
    return blocks, updated_path, document_title


def _semantic_metadata(element, tree) -> list[dict[str, str]]:
    """Retain navigation and execution attributes as metadata rather than prose."""

    tag = _local_name(element)
    xpath = tree.getpath(element)
    records: list[dict[str, str]] = []
    for attribute, raw_value in element.attrib.items():
        name = attribute.split("}")[-1]
        value = normalize_nfc(str(raw_value or "")).strip()
        if not value:
            continue
        if name.lower() == "contextid":
            records.append({"kind": "context_id", "tag": tag, "attribute": name, "value": value, "xml_path": xpath})
        elif tag == "param" and name.lower() == "value":
            records.append({"kind": "parameter_value", "tag": tag, "attribute": name, "value": value, "xml_path": xpath})
        elif tag == "serialization":
            records.append({"kind": "serialization", "tag": tag, "attribute": name, "value": value, "xml_path": xpath})
    return records


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    from lxml import etree

    parser = etree.XMLParser(resolve_entities=False, no_network=True, recover=False, huge_tree=False)
    tree = etree.parse(str(path), parser)
    root = tree.getroot()
    relationships = _relationship_records(tree, root, context)
    blocks = []
    heading_path: list[str] = []
    title = path.stem
    semantic_metadata: list[dict[str, str]] = []
    for element in root.iter():
        # lxml exposes comments and processing instructions in ``root.iter()``;
        # they are not XPath-addressable content elements.
        if not isinstance(element.tag, str):
            continue
        tag = _local_name(element)
        xpath = tree.getpath(element)
        attribute_blocks, heading_path, attribute_title = _visible_attribute_blocks(element, tree, context, heading_path)
        blocks.extend(attribute_blocks)
        if attribute_title:
            title = attribute_title
        semantic_metadata.extend(_semantic_metadata(element, tree))
        text = normalize_nfc(" ".join(value.strip() for value in element.itertext() if value.strip()))
        if not text:
            continue
        child_text = any(
            normalize_nfc(" ".join(value.strip() for value in child.itertext() if value.strip())) == text
            for child in element
            if isinstance(child.tag, str)
        )
        if child_text and len(element):
            continue
        if tag in HEADING_TAGS:
            level = 1 if tag in {"title", "h1", "chapter"} else 2
            heading_path = heading_path[: level - 1] + [text]
            if level == 1:
                title = text
            blocks.append(context.block(
                "heading", text, location=Location(xml_path=xpath), heading_path=list(heading_path),
                content_origin="native_text", required=True, critical=True, metadata={"level": level, "tag": tag},
            ))
        elif tag in LIST_TAGS:
            items = []
            for child in element:
                if _local_name(child) in ITEM_TAGS:
                    value = normalize_nfc(" ".join(part.strip() for part in child.itertext() if part.strip()))
                    if value:
                        items.append(value)
            if items:
                blocks.append(context.block(
                    "list", "\n".join(f"- {item}" for item in items), location=Location(xml_path=xpath),
                    heading_path=list(heading_path), content_origin="native_text", required=True,
                    metadata={"ordered": False, "items": items, "item_count": len(items), "tag": tag},
                ))
        elif tag in CODE_TAGS:
            blocks.append(context.block(
                "code", text, location=Location(xml_path=xpath), heading_path=list(heading_path),
                content_origin="native_text", required=True, critical=True, metadata={"tag": tag},
            ))
        elif not list(element):
            critical = bool(re.search(r"date|version|id|warning|禁止|不得|must not", tag, re.IGNORECASE))
            blocks.append(context.block(
                "paragraph", text, location=Location(xml_path=xpath), heading_path=list(heading_path),
                content_origin="native_text", required=True, critical=critical, metadata={"tag": tag},
            ))
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={
            "adapter": "xml_adapter",
            "root_tag": _local_name(root),
            "xml_node_count": sum(1 for _ in root.iter()),
            "relationships": relationships,
            "semantic_metadata": semantic_metadata,
        },
    )
