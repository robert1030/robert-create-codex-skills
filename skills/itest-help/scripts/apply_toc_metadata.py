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


def normalize_href(href):
    href = (href or "").strip().replace("\\", "/")
    href = href.split("#", 1)[0]
    href = unquote(href)
    help_prefix = "help::/com.fnfr.svt.help/"
    if href.startswith(help_prefix):
        href = href[len(help_prefix):]
    href = href.lstrip("/")
    if href and not href.startswith("topics/"):
        href = f"topics/{href}"
    return href


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


def load_pages(pages_path):
    pages = []
    with pages_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                pages.append(json.loads(line))
    return pages


def parse_toc(toc_xml):
    tree = ET.parse(toc_xml)
    root = tree.getroot()
    namespace = ""
    if root.tag.startswith("{"):
        namespace = root.tag.split("}", 1)[0] + "}"

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
        fields = {
            "file": page.get("file_name", ""),
            "title": page.get("title", ""),
            "h1": page.get("h1", ""),
            "heading": heading_text,
            "toc": toc_text,
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
                "text_length": page.get("text_length", 0),
                "heading_count": len(page.get("headings", [])),
            }
        )

    compact_terms = {
        term: sorted(postings, key=lambda item: item[1], reverse=True)
        for term, postings in sorted(terms.items())
    }
    return {
        "version": 2,
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--toc-xml", type=Path, required=True)
    parser.add_argument("--references-dir", type=Path, default=DEFAULT_REFERENCES_DIR)
    args = parser.parse_args()

    pages_path = args.references_dir / "help_pages.jsonl"
    index_path = args.references_dir / "search_index.json"
    summary_path = args.references_dir / "search_index_summary.json"
    toc_index_path = args.references_dir / "toc_index.json"

    toc_index, entries_by_source = parse_toc(args.toc_xml)
    pages = apply_toc_to_pages(load_pages(pages_path), entries_by_source)
    index = build_index(pages)
    summary = {
        "document_count": len(pages),
        "documents_with_toc": sum(1 for page in pages if page.get("toc_paths")),
        "documents_without_toc": sum(1 for page in pages if not page.get("toc_paths")),
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
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
