---
{
  "chunk_id": "procedures_overview__overview_procedures_in_test_cases_587c226e5a8f08e6",
  "source_file": "topics/procedures_overview.htm",
  "source_original_path": "topics/procedures_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Overview: Procedures in test cases"
  ],
  "heading_path": [
    "Overview: Procedures in test cases",
    "Overview: Procedures in test cases"
  ],
  "anchor": "1382984",
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
  "content_hash": "587c226e5a8f08e6",
  "level": 1
}
---

# Overview: Procedures in test cases > Overview: Procedures in test cases

A procedure is a set of steps that performs an identifiable operation like initializing a device or starting and stopping traffic on a particular port. You call the procedure from a test case to perform its operation. For example, the setupRouter procedure might include:

- Steps that reset the routing table and port assignments

- Parameters with settings that specify the firmware on the device (the parameter values will be used to adjust the syntax of the steps because, for example, the syntax changed in the latest firmware revision)

- A return string of either “success” or “fail” to tell the test case (which called the procedure) whether the router was successfully set up and therefore how to proceed

- A return or write step in the procedure to return a value to the caller. The returned value becomes the response to the call step in the caller. Now you can extract the data using a response map, or simply store the data in a variable and use it in the calling procedure.

Procedures are powerful because, when you update a procedure, then every test case that calls the procedure is updated as well. Procedures make test steps reusable.

Test cases are made up of one or more named procedures (by default, each test case has one procedure named main). You have the option to create any number of procedures within a test case. Any step in a test case can call a procedure that is defined in the current test case or in other test cases. In addition, you can create a special test case to act as a procedure library — other test cases can call any of the procedures in the library.

> **Tip:** Tip You can associate a response map with a procedure so that whatever is returned by the procedure will automatically have “blue boxes” — structured queries available on the corresponding call step.
