---
{
  "chunk_id": "procedures_overview__why_create_procedures_ed5dbbeb9718ce21",
  "source_file": "topics/procedures_overview.htm",
  "source_original_path": "topics/procedures_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Overview: Procedures in test cases"
  ],
  "heading_path": [
    "Overview: Procedures in test cases",
    "Overview: Procedures in test cases",
    "Why create procedures?"
  ],
  "anchor": "1278569",
  "context_ids": [
    "procedures_overview"
  ],
  "index_keywords": [
    "building",
    "default entry point",
    "defined",
    "external",
    "foreign",
    "internal",
    "local",
    "main",
    "main procedure",
    "overview",
    "procedure libraries",
    "test cases"
  ],
  "index_keyword_paths": [
    "entry points > test cases",
    "external procedures > defined",
    "foreign procedures > defined",
    "internal procedures > defined",
    "library of procedures > building",
    "local procedures > defined",
    "main procedure",
    "main procedure > defined",
    "procedure libraries",
    "procedures > default entry point",
    "procedures > defined",
    "procedures > external",
    "procedures > foreign",
    "procedures > internal",
    "procedures > local",
    "procedures > main",
    "procedures > overview"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "ed5dbbeb9718ce21",
  "level": 2
}
---

# Overview: Procedures in test cases > Overview: Procedures in test cases > Why create procedures?

The most common use for procedures is for tasks that you want to execute often, for example, resetting ports, initializing a device (before starting a test or to “clean up” after execution), setting up a particular configuration in preparation for checking a particular value, and so on. In any test case, rather than copy/pasting all the steps that perform the operation, you add a single call step that executes the procedure.

The benefits? The test case is more modular and therefore more easily …

- Understood: Test case developers can read the procedure name (for example, setupRouter) and understand what's happening without having to see all the details.

- Debugged: Because the functionality in the procedure is isolated, once you know that the procedure is working as expected, you can ignore the procedure and focus on other problem areas.

- Ported: When a set of tests has to cover a new revision, just update the procedure as needed and every test case is that much further along.

- Maintained: When you update a procedure, all test cases that use the procedure are automatically updated too.
