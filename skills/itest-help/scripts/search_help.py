import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = SKILL_DIR / "references"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "for", "from",
    "has", "have", "how", "in", "into", "is", "it", "its", "of", "on",
    "not", "or", "that", "the", "this", "to", "with", "you", "your",
}


def tokenize(value):
    value = (value or "").lower()
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


def load_pages(data_dir):
    pages = []
    with (data_dir / "help_pages.jsonl").open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                pages.append(json.loads(line))
    return pages


def load_index(data_dir):
    return json.loads((data_dir / "search_index.json").read_text(encoding="utf-8"))


def is_specific_token(token):
    return "_" in token or any(char.isdigit() for char in token) or len(token) >= 12


def guardrail_boost(page, query_terms):
    terms = set(query_terms)
    source_ref = page.get("source_ref", page.get("relative_path", page["file_name"]))
    boost = 0

    if {"itest_value", "itest_index"} & terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_processor_properties.htm",
            "topics/commands_built_in_local_variables.htm",
            "topics/arw_assertion_page.htm",
            "topics/arw_message_page.htm",
        }:
            boost += 220

    if {"thread", "safe"} <= terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_processor_properties.htm",
            "topics/commands_built_in_local_variables.htm",
        }:
            boost += 120

    if "secret" in terms and ({"wizard", "rule", "rules"} & terms or {"mask", "masked"} & terms):
        if source_ref in {
            "topics/arw_rule_type_selection_page.htm",
            "topics/arw_extractor_selection_page.htm",
            "topics/param_parameters_type_secret.htm",
            "topics/arules_processor_properties.htm",
        }:
            boost += 180

    if "query" in terms and ({"right", "click", "right-click"} & terms) and {"analysis", "rule", "rules"} & terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_global_working_with.htm",
        }:
            boost += 180

    if "clock" in terms and (
        {"scan", "format", "time", "date", "conversion", "2038", "2041", "2049"} & terms
    ):
        if source_ref == "topics/command_syntax.htm":
            boost += 300
        if source_ref == "topics/popups/clock.html":
            boost += 520
        if "tcl" in terms and source_ref == "topics/command_tcl.htm":
            boost += 180

    return boost


def compact_snippet(text, query, tokens, width=240):
    lowered = text.lower()
    needle = query.lower().strip()
    pos = lowered.find(needle) if needle else -1
    if pos < 0:
        for token in tokens:
            pos = lowered.find(token)
            if pos >= 0:
                break
    if pos < 0:
        pos = 0

    start = max(0, pos - 80)
    end = min(len(text), start + width)
    start = max(0, end - width)
    snippet = re.sub(r"\s+", " ", text[start:end]).strip()
    if start > 0:
        snippet = "... " + snippet
    if end < len(text):
        snippet += " ..."
    return snippet


def search(query, data_dir, top):
    index = load_index(data_dir)
    pages = load_pages(data_dir)
    tokens = tokenize(query)
    query_terms = sorted(set(tokens))
    unmatched_terms = [token for token in query_terms if token not in index["terms"]]
    scores = defaultdict(int)
    matched_terms = defaultdict(list)

    for token in tokens:
        for doc_id, score in index["terms"].get(token, []):
            scores[doc_id] += score
            if is_specific_token(token):
                scores[doc_id] += 120
            matched_terms[doc_id].append(token)

    phrase = query.lower().strip()
    for doc_id in list(scores.keys()):
        page = pages[doc_id]
        scores[doc_id] += guardrail_boost(page, query_terms)
        haystack = "\n".join(
            [
                page.get("title", ""),
                page.get("h1", ""),
                " ".join(item["text"] for item in page.get("headings", [])),
                " ".join(page.get("toc_paths", [])),
                " ".join(page.get("toc_top_categories", [])),
                page.get("text", ""),
            ]
        ).lower()
        if phrase and phrase in haystack:
            scores[doc_id] += 50

    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:top]
    results = []
    for doc_id, score in ranked:
        page = pages[doc_id]
        results.append(
            {
                "score": score,
                "file_name": page["file_name"],
                "relative_path": page.get("relative_path", page["file_name"]),
                "title": page["title"],
                "h1": page["h1"],
                "doc_set": page["doc_set"],
                "probable_category": page["probable_category"],
                "toc_primary_path": page.get("toc_primary_path", ""),
                "toc_top_categories": page.get("toc_top_categories", []),
                "toc_paths": page.get("toc_paths", []),
                "matched_terms": sorted(set(matched_terms[doc_id])),
                "unmatched_terms": unmatched_terms,
                "snippet": compact_snippet(page.get("text", ""), query, tokens),
                "source_ref": page.get("source_ref", page["file_name"]),
            }
        )
    return {
        "query": query,
        "query_terms": query_terms,
        "unmatched_terms": unmatched_terms,
        "results": results,
    }


def show_file(file_name, data_dir, text_only):
    pages = load_pages(data_dir)
    needle = file_name.replace("\\", "/").lower()
    matches = []
    for page in pages:
        candidates = {
            page["file_name"].lower(),
            page.get("relative_path", page["file_name"]).lower(),
            page.get("source_ref", page["file_name"]).lower(),
        }
        source_ref = page.get("source_ref", "")
        if source_ref.lower().startswith("topics/"):
            candidates.add(source_ref[7:].lower())
        if needle in candidates:
            matches.append(page)

    if len(matches) == 1:
        page = matches[0]
        if text_only:
            print(page["text"])
        else:
            print(json.dumps(page, ensure_ascii=False, indent=2))
        return 0
    if len(matches) > 1:
        print(f"Multiple help pages match: {file_name}")
        for page in matches:
            print(page.get("source_ref", page.get("relative_path", page["file_name"])))
        print("Use --show-file with the relative path or source_ref.")
        return 1
    print(f"No help page found for file: {file_name}")
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--show-file")
    parser.add_argument("--text", action="store_true")
    args = parser.parse_args()

    if args.show_file:
        raise SystemExit(show_file(args.show_file, args.data_dir, args.text))
    if not args.query:
        parser.error("query is required unless --show-file is used")

    response = search(args.query, args.data_dir, args.top)
    if args.json:
        print(json.dumps(response, ensure_ascii=False, indent=2))
        return

    if response["unmatched_terms"]:
        print(f"unmatched terms: {', '.join(response['unmatched_terms'])}")
    if not response["results"]:
        print("No matching help pages found.")
        return

    for rank, result in enumerate(response["results"], start=1):
        print(f"{rank}. [{result['score']}] {result['source_ref']}")
        print(f"   title: {result['title']}")
        if result.get("toc_primary_path"):
            print(f"   toc: {result['toc_primary_path']}")
        print(f"   category: {result['probable_category']} / {result['doc_set']}")
        print(f"   snippet: {result['snippet']}")


if __name__ == "__main__":
    main()
