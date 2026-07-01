---
{
  "chunk_id": "procedures_overview__local_procedures_foreign_procedures_and__c4fc6e1733de0273",
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
    "Local procedures, foreign procedures, and procedure libraries"
  ],
  "anchor": "1278577",
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
  "related_links": [
    "procedure_library_creating.htm#1291658"
  ],
  "images": [],
  "content_hash": "c4fc6e1733de0273",
  "level": 2
}
---

# Overview: Procedures in test cases > Overview: Procedures in test cases > Local procedures, foreign procedures, and procedure libraries

A local procedure is a procedure that is defined in the same test case from which it is called — defined in test case A and called from test case A.

A foreign procedure is a procedure that is defined in a different test case than the one from which it is called — defined in test case A and called from test case B.

There are two important uses for foreign procedures:

- You might want to build up a library of procedures that can be used by any test case. For this purpose, you can create a test case (named, for example, myProcedureLibrary) with a blank main procedure and multiple defined procedures. See Creating a procedure library.

- Your test case might call procedures in a variety of other test cases or from a test case that acts as a procedure library. (This differs from executing the main procedure of a referenced test case using the run action).
