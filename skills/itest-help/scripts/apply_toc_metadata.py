import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_REFERENCES_DIR = SKILL_DIR / "references"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "for", "from",
    "has", "have", "how", "in", "into", "is", "it", "its", "of", "on",
    "not", "or", "that", "the", "this", "to", "with", "you", "your",
}


def clean_text(value):
    return re.sub(r"\s+", " ", (value or "").strip())


def clean_keyword(value):
    value = clean_text(value)
    value = re.sub(r"\s+on page\s+\d+$", "", value, flags=re.IGNORECASE)
    return value.strip(" \t\r\n\"'“”")


def split_href(href):
    href = (href or "").strip().replace("\\", "/")
    href = unquote(href)
    help_prefix = "help::/com.fnfr.svt.help/"
    if href.startswith(help_prefix):
        href = href[len(help_prefix):]
    while href.startswith("../"):
        href = href[3:]
    href = href.lstrip("/")

    anchor = ""
    if "#" in href:
        href, anchor = href.split("#", 1)

    if href and not href.startswith("topics/"):
        href = f"topics/{href}"
    return href, anchor


def normalize_href(href):
    source_ref, _anchor = split_href(href)
    return source_ref


def tokenize(value):
    value = (value or "").lower()
    value = re.sub(r"([a-z])([A-Z])", r"\1 \2", value)
    tokens = re.findall(r"[a-z0-9][a-z0-9_./+-]*", value)
    normalized = []
    for token in tokens:
        for part in re.split(r"[_./+-]+", token):
            if len(part) < 2 or part in STOPWORDS:
                continue
            normalized.append(part)
        if len(token) >= 2 and token not in STOPWORDS:
            normalized.append(token)
    return normalized


def unique_sorted(values):
    return sorted({value for value in values if value}, key=lambda item: item.lower())


def load_pages(pages_path):
    pages = []
    with pages_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                pages.append(json.loads(line))
    return pages


def detect_namespace(root):
    if root.tag.startswith("{"):
        return root.tag.split("}", 1)[0] + "}"
    return ""


def parse_toc(toc_xml):
    tree = ET.parse(toc_xml)
    root = tree.getroot()
    namespace = detect_namespace(root)

    root_label = clean_text(root.attrib.get("label")) or "iTest Online Help"
    entries_by_source = defaultdict(list)
    top_stats = defaultdict(lambda: {"topic_count": 0, "referenced_sources": set()})
    state = {"topic_count": 0, "order": 0}

    def walk(node, path_labels):
        for child in list(node):
            if child.tag != f"{namespace}topic":
                continue
            state["topic_count"] += 1
            label = clean_text(child.attrib.get("label"))
            child_path = path_labels + ([label] if label else [])
            top_category = child_path[1] if len(child_path) > 1 else ""
            if top_category:
                top_stats[top_category]["topic_count"] += 1

            href = normalize_href(child.attrib.get("href", ""))
            if href:
                state["order"] += 1
                breadcrumb = " > ".join(child_path)
                entry = {
                    "label": label,
                    "path": child_path,
                    "breadcrumb": breadcrumb,
                    "top_category": top_category,
                    "depth": max(len(child_path) - 1, 0),
                    "href": href,
                    "order": state["order"],
                }
                entries_by_source[href].append(entry)
                if top_category:
                    top_stats[top_category]["referenced_sources"].add(href)

            walk(child, child_path)

    walk(root, [root_label])
    top_categories = []
    for label, stats in top_stats.items():
        top_categories.append(
            {
                "label": label,
                "topic_count": stats["topic_count"],
                "referenced_source_count": len(stats["referenced_sources"]),
            }
        )
    top_categories.sort(key=lambda item: item["label"].lower())

    toc_index = {
        "version": 1,
        "root_label": root_label,
        "source": "com.fnfr.svt.help/toc.xml",
        "topic_node_count": state["topic_count"],
        "href_entry_count": sum(len(entries) for entries in entries_by_source.values()),
        "referenced_source_count": len(entries_by_source),
        "top_category_count": len(top_categories),
        "top_categories": top_categories,
        "entries_by_source_ref": dict(sorted(entries_by_source.items())),
    }
    return toc_index, entries_by_source


def parse_help_index(index_xml, page_refs):
    tree = ET.parse(index_xml)
    root = tree.getroot()
    namespace = detect_namespace(root)
    entries_by_source = defaultdict(list)
    missing_source_refs = []
    keyword_paths = set()
    top_keyword_counts = Counter()
    seen_entries = set()
    state = {"topic_ref_count": 0, "order": 0}

    def walk(entry_node, parent_path):
        raw_keyword = clean_text(entry_node.attrib.get("keyword"))
        keyword = clean_keyword(raw_keyword)
        keyword_path = parent_path + ([keyword] if keyword else [])

        topics = [child for child in list(entry_node) if child.tag == f"{namespace}topic"]
        for topic in topics:
            href = topic.attrib.get("href", "")
            source_ref, anchor = split_href(href)
            if not source_ref:
                continue

            state["topic_ref_count"] += 1
            breadcrumb = " > ".join(keyword_path)
            if breadcrumb:
                keyword_paths.add(breadcrumb)
            if keyword_path:
                top_keyword_counts[keyword_path[0]] += 1

            state["order"] += 1
            entry = {
                "keyword": keyword_path[-1] if keyword_path else "",
                "keyword_path": keyword_path,
                "index_path": breadcrumb,
                "top_keyword": keyword_path[0] if keyword_path else "",
                "source_ref": source_ref,
                "anchor": anchor,
                "order": state["order"],
            }
            key = (source_ref, anchor, breadcrumb)
            if source_ref in page_refs:
                if key not in seen_entries:
                    entries_by_source[source_ref].append(entry)
                    seen_entries.add(key)
            else:
                missing_source_refs.append(entry)

        for child in list(entry_node):
            if child.tag == f"{namespace}entry":
                walk(child, keyword_path)

    for child in list(root):
        if child.tag == f"{namespace}entry":
            walk(child, [])

    top_keywords = [
        {"keyword": keyword, "topic_ref_count": count}
        for keyword, count in sorted(top_keyword_counts.items(), key=lambda item: (-item[1], item[0].lower()))
    ]
    help_index = {
        "version": 1,
        "source": "com.fnfr.svt.help/index.xml",
        "topic_ref_count": state["topic_ref_count"],
        "entry_count": sum(len(entries) for entries in entries_by_source.values()),
        "referenced_source_count": len(entries_by_source),
        "keyword_path_count": len(keyword_paths),
        "missing_source_ref_count": len(missing_source_refs),
        "missing_source_refs": missing_source_refs,
        "top_keywords": top_keywords,
        "entries_by_source_ref": dict(sorted(entries_by_source.items())),
    }
    return help_index, entries_by_source


def parse_contexts(contexts_xml, page_refs):
    tree = ET.parse(contexts_xml)
    root = tree.getroot()
    namespace = detect_namespace(root)
    entries_by_source = defaultdict(list)
    contexts_without_topics = []
    missing_source_refs = []
    seen_entries = set()
    state = {
        "context_count": 0,
        "contexts_with_topics": 0,
        "topic_ref_count": 0,
        "order": 0,
    }

    for context in root.findall(f"{namespace}context"):
        state["context_count"] += 1
        context_id = clean_text(context.attrib.get("id"))
        description_node = context.find(f"{namespace}description")
        description = clean_text(description_node.text if description_node is not None else "")
        topics = context.findall(f"{namespace}topic")

        if not topics:
            contexts_without_topics.append(
                {
                    "context_id": context_id,
                    "description": description,
                }
            )
            continue

        state["contexts_with_topics"] += 1
        for topic in topics:
            href = topic.attrib.get("href", "")
            source_ref, anchor = split_href(href)
            if not source_ref:
                continue
            state["topic_ref_count"] += 1
            state["order"] += 1
            entry = {
                "context_id": context_id,
                "description": description,
                "label": clean_text(topic.attrib.get("label")),
                "source_ref": source_ref,
                "anchor": anchor,
                "order": state["order"],
            }
            key = (context_id, source_ref, anchor, entry["label"])
            if source_ref in page_refs:
                if key not in seen_entries:
                    entries_by_source[source_ref].append(entry)
                    seen_entries.add(key)
            else:
                missing_source_refs.append(entry)

    contexts_index = {
        "version": 1,
        "source": "com.fnfr.svt.help/contexts.xml",
        "context_count": state["context_count"],
        "contexts_with_topics": state["contexts_with_topics"],
        "contexts_without_topic_count": len(contexts_without_topics),
        "contexts_without_topics": contexts_without_topics,
        "topic_ref_count": state["topic_ref_count"],
        "entry_count": sum(len(entries) for entries in entries_by_source.values()),
        "referenced_source_count": len(entries_by_source),
        "missing_source_ref_count": len(missing_source_refs),
        "missing_source_refs": missing_source_refs,
        "entries_by_source_ref": dict(sorted(entries_by_source.items())),
    }
    return contexts_index, entries_by_source


def apply_toc_to_pages(pages, entries_by_source):
    for page in pages:
        entries = entries_by_source.get(page.get("source_ref", ""), [])
        toc_paths = []
        toc_top_categories = []
        toc_labels = []
        for entry in entries:
            toc_paths.append(entry["breadcrumb"])
            if entry["top_category"] and entry["top_category"] not in toc_top_categories:
                toc_top_categories.append(entry["top_category"])
            for label in entry["path"]:
                if label and label not in toc_labels:
                    toc_labels.append(label)

        page["toc_entries"] = entries
        page["toc_paths"] = toc_paths
        page["toc_top_categories"] = toc_top_categories
        page["toc_labels"] = toc_labels
        page["toc_primary_path"] = toc_paths[0] if toc_paths else ""
        page["toc_primary_top_category"] = toc_top_categories[0] if toc_top_categories else ""
        page["toc_order"] = entries[0]["order"] if entries else None
    return pages


def apply_help_index_to_pages(pages, entries_by_source):
    for page in pages:
        entries = entries_by_source.get(page.get("source_ref", ""), [])
        page["index_entries"] = entries
        page["index_paths"] = unique_sorted(entry.get("index_path", "") for entry in entries)
        terms = []
        for entry in entries:
            terms.extend(entry.get("keyword_path", []))
        page["index_terms"] = unique_sorted(terms)
    return pages


def apply_contexts_to_pages(pages, entries_by_source):
    for page in pages:
        entries = entries_by_source.get(page.get("source_ref", ""), [])
        page["context_entries"] = entries
        page["context_ids"] = unique_sorted(entry.get("context_id", "") for entry in entries)
        page["context_labels"] = unique_sorted(entry.get("label", "") for entry in entries)
    return pages


def build_index(pages):
    documents = []
    terms = defaultdict(list)

    for doc_id, page in enumerate(pages):
        heading_text = " ".join(item.get("text", "") for item in page.get("headings", []))
        toc_text = " ".join(
            page.get("toc_paths", [])
            + page.get("toc_top_categories", [])
            + page.get("toc_labels", [])
        )
        index_metadata_text = " ".join(page.get("index_terms", []) + page.get("index_paths", []))
        context_metadata_text = " ".join(page.get("context_ids", []) + page.get("context_labels", []))
        fields = {
            "file": page.get("file_name", ""),
            "title": page.get("title", ""),
            "h1": page.get("h1", ""),
            "heading": heading_text,
            "toc": toc_text,
            "index_metadata": index_metadata_text,
            "context_metadata": context_metadata_text,
            "text": page.get("text", ""),
        }
        counters = {name: Counter(tokenize(text)) for name, text in fields.items()}
        all_terms = set()
        for counter in counters.values():
            all_terms.update(counter.keys())

        for term in sorted(all_terms):
            score = (
                counters["file"][term] * 6
                + counters["title"][term] * 10
                + counters["h1"][term] * 8
                + counters["heading"][term] * 4
                + counters["toc"][term] * 5
                + counters["index_metadata"][term] * 2
                + counters["context_metadata"][term] * 2
                + min(counters["text"][term], 20)
            )
            if score:
                terms[term].append([doc_id, score])

        documents.append(
            {
                "id": doc_id,
                "file_name": page.get("file_name", ""),
                "relative_path": page.get("relative_path", ""),
                "source_ref": page.get("source_ref", ""),
                "title": page.get("title", ""),
                "h1": page.get("h1", ""),
                "doc_set": page.get("doc_set", ""),
                "probable_category": page.get("probable_category", ""),
                "toc_primary_path": page.get("toc_primary_path", ""),
                "toc_primary_top_category": page.get("toc_primary_top_category", ""),
                "toc_path_count": len(page.get("toc_paths", [])),
                "index_term_count": len(page.get("index_terms", [])),
                "index_path_count": len(page.get("index_paths", [])),
                "context_id_count": len(page.get("context_ids", [])),
                "context_label_count": len(page.get("context_labels", [])),
                "text_length": page.get("text_length", 0),
                "heading_count": len(page.get("headings", [])),
            }
        )

    compact_terms = {
        term: sorted(postings, key=lambda item: item[1], reverse=True)
        for term, postings in sorted(terms.items())
    }
    return {
        "version": 3,
        "source": "packaged references/help_pages.jsonl",
        "document_count": len(documents),
        "term_count": len(compact_terms),
        "documents": documents,
        "terms": compact_terms,
    }


def write_jsonl(path, pages):
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for page in pages:
            handle.write(json.dumps(page, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def resolve_optional_xml(explicit_path, toc_xml, file_name):
    if explicit_path:
        return explicit_path
    candidate = toc_xml.parent / file_name
    return candidate if candidate.exists() else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--toc-xml", type=Path, required=True)
    parser.add_argument("--index-xml", type=Path)
    parser.add_argument("--contexts-xml", type=Path)
    parser.add_argument("--references-dir", type=Path, default=DEFAULT_REFERENCES_DIR)
    args = parser.parse_args()

    pages_path = args.references_dir / "help_pages.jsonl"
    index_path = args.references_dir / "search_index.json"
    summary_path = args.references_dir / "search_index_summary.json"
    toc_index_path = args.references_dir / "toc_index.json"
    help_index_path = args.references_dir / "help_index.json"
    contexts_index_path = args.references_dir / "contexts_index.json"

    pages = load_pages(pages_path)
    page_refs = {page.get("source_ref", "") for page in pages}

    toc_index, toc_entries_by_source = parse_toc(args.toc_xml)
    pages = apply_toc_to_pages(pages, toc_entries_by_source)

    source_index_xml = resolve_optional_xml(args.index_xml, args.toc_xml, "index.xml")
    if source_index_xml:
        help_index, index_entries_by_source = parse_help_index(source_index_xml, page_refs)
    else:
        help_index, index_entries_by_source = (
            {
                "version": 1,
                "source": "com.fnfr.svt.help/index.xml",
                "topic_ref_count": 0,
                "entry_count": 0,
                "referenced_source_count": 0,
                "keyword_path_count": 0,
                "missing_source_ref_count": 0,
                "missing_source_refs": [],
                "top_keywords": [],
                "entries_by_source_ref": {},
            },
            {},
        )
    pages = apply_help_index_to_pages(pages, index_entries_by_source)

    source_contexts_xml = resolve_optional_xml(args.contexts_xml, args.toc_xml, "contexts.xml")
    if source_contexts_xml:
        contexts_index, context_entries_by_source = parse_contexts(source_contexts_xml, page_refs)
    else:
        contexts_index, context_entries_by_source = (
            {
                "version": 1,
                "source": "com.fnfr.svt.help/contexts.xml",
                "context_count": 0,
                "contexts_with_topics": 0,
                "contexts_without_topic_count": 0,
                "contexts_without_topics": [],
                "topic_ref_count": 0,
                "entry_count": 0,
                "referenced_source_count": 0,
                "missing_source_ref_count": 0,
                "missing_source_refs": [],
                "entries_by_source_ref": {},
            },
            {},
        )
    pages = apply_contexts_to_pages(pages, context_entries_by_source)

    index = build_index(pages)
    summary = {
        "document_count": len(pages),
        "documents_with_contexts": sum(1 for page in pages if page.get("context_ids")),
        "documents_with_index": sum(1 for page in pages if page.get("index_terms")),
        "documents_with_toc": sum(1 for page in pages if page.get("toc_paths")),
        "documents_without_contexts": sum(1 for page in pages if not page.get("context_ids")),
        "documents_without_index": sum(1 for page in pages if not page.get("index_terms")),
        "documents_without_toc": sum(1 for page in pages if not page.get("toc_paths")),
        "contexts_count": contexts_index["context_count"],
        "contexts_index_path": "references/contexts_index.json",
        "contexts_missing_source_ref_count": contexts_index["missing_source_ref_count"],
        "contexts_referenced_source_count": contexts_index["referenced_source_count"],
        "contexts_topic_ref_count": contexts_index["topic_ref_count"],
        "contexts_without_topic_count": contexts_index["contexts_without_topic_count"],
        "help_index_entry_count": help_index["entry_count"],
        "help_index_keyword_path_count": help_index["keyword_path_count"],
        "help_index_missing_source_ref_count": help_index["missing_source_ref_count"],
        "help_index_path": "references/help_index.json",
        "help_index_referenced_source_count": help_index["referenced_source_count"],
        "help_index_topic_ref_count": help_index["topic_ref_count"],
        "index_path": "references/search_index.json",
        "pages_path": "references/help_pages.jsonl",
        "source": "packaged references/help_pages.jsonl",
        "term_count": index["term_count"],
        "toc_href_entry_count": toc_index["href_entry_count"],
        "toc_path": "references/toc_index.json",
        "toc_referenced_source_count": toc_index["referenced_source_count"],
        "toc_root_label": toc_index["root_label"],
        "toc_top_category_count": toc_index["top_category_count"],
        "toc_topic_node_count": toc_index["topic_node_count"],
    }

    write_jsonl(pages_path, pages)
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    toc_index_path.write_text(
        json.dumps(toc_index, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    help_index_path.write_text(
        json.dumps(help_index, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    contexts_index_path.write_text(
        json.dumps(contexts_index, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
