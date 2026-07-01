---
{
  "chunk_id": "analysis_rules_09__guidelines_5bae53ec74ea3c2b",
  "source_file": "topics/analysis_rules.09.htm",
  "source_original_path": "topics/analysis_rules.09.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "When to use a Global rule"
  ],
  "heading_path": [
    "When to use a Global rule",
    "When to use a Global rule",
    "Guidelines"
  ],
  "anchor": "1247042",
  "context_ids": [],
  "index_keywords": [
    "Global",
    "described",
    "precedence"
  ],
  "index_keyword_paths": [
    "Global analysis rules > described",
    "Global analysis rules > precedence",
    "analysis rules > Global"
  ],
  "related_links": [
    "#1247054"
  ],
  "images": [],
  "content_hash": "5bae53ec74ea3c2b",
  "level": 2
}
---

# When to use a Global rule > When to use a Global rule > Guidelines

- Global analysis rules work exactly like the standard analysis rules that you apply to test case steps

- There is a small delay associated with testing the assertions of Global analysis rules, so define them only if you need them

- Typically, you define the WhenFalse actions to not raise execution messages

- Preprocessing (to replace field replacements and so on) happens in the normal way for all rules

- Global analysis rules are applied in a clearly defined order, as described in Precedence of Global Analysis rules
