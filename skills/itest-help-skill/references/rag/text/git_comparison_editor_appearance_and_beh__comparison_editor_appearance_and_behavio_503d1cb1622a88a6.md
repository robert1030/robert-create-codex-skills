---
{
  "chunk_id": "git_comparison_editor_appearance_and_beh__comparison_editor_appearance_and_behavio_503d1cb1622a88a6",
  "source_file": "topics/git_comparison_editor_appearance_and_behavior.htm",
  "source_original_path": "topics/git_comparison_editor_appearance_and_behavior.htm",
  "toc_path": [
    "iTest Online Help",
    "Using Git in iTest",
    "Comparison editor appearance and behavior"
  ],
  "heading_path": [
    "Comparison editor appearance and behavior",
    "Comparison editor appearance and behavior"
  ],
  "anchor": "1486499",
  "context_ids": [
    "git_comparison_editor_appearance_and_behavior"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "503d1cb1622a88a6",
  "level": 1
}
---

# Comparison editor appearance and behavior > Comparison editor appearance and behavior

iTest merge conflicts algorithm compares as follows.

| Compares two test cases | Two-way merge comparison applies current test case revision with previous revision Target: Test case revision Source: Test case revision which you would like to compare with the target |  | Target: Test case revision |  | Source: Test case revision which you would like to compare with the target |
| --- | --- | --- | --- | --- | --- |
|  | Target: Test case revision |  |  |  |  |
|  | Source: Test case revision which you would like to compare with the target |  |  |  |  |
| compares test cases Three-way | Three-way comparison applies in the following merge situations: Target: Test case revision Source: Test case revision which you wish to merge into target Ancestor: Base test case version for target and source revisions. When comparing target, source, and ancestor, merge conflicts may appear. Comparison algorithm considers two (or three) versions of the test case object and display the set of differences as a result. |  | Target: Test case revision |  | Source: Test case revision which you wish to merge into target |
|  | Target: Test case revision |  |  |  |  |
|  | Source: Test case revision which you wish to merge into target |  |  |  |  |
|  | Ancestor: Base test case version for target and source revisions. |  |  |  |  |
