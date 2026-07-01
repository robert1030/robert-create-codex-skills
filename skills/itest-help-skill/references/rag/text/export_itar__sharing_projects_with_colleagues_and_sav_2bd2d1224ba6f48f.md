---
{
  "chunk_id": "export_itar__sharing_projects_with_colleagues_and_sav_2bd2d1224ba6f48f",
  "source_file": "topics/export_itar.htm",
  "source_original_path": "topics/export_itar.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Sharing projects with colleagues and saving them for use in automated testing"
  ],
  "heading_path": [
    "Sharing projects with colleagues and saving them for use in automated testing",
    "Sharing projects with colleagues and saving them for use in automated testing"
  ],
  "anchor": "1211343",
  "context_ids": [
    "export_itar"
  ],
  "index_keywords": [
    "exporting and importing",
    "iTest files",
    "itar files",
    "projects",
    "saving to regression system",
    "sharing with coworkers"
  ],
  "index_keyword_paths": [
    "exporting > iTest files",
    "exporting > projects",
    "iTest files > exporting and importing",
    "iTest files > saving to regression system",
    "iTest files > sharing with coworkers",
    "importing > iTest files",
    "importing > projects",
    "itar files",
    "projects > exporting and importing",
    "projects > saving to regression system",
    "projects > sharing with coworkers"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "2bd2d1224ba6f48f",
  "level": 1
}
---

# Sharing projects with colleagues and saving them for use in automated testing > Sharing projects with colleagues and saving them for use in automated testing

This topic describes sharing iTest files, for example:

- Sharing a test case with a coworker that uses iTest (and easily including all supporting files in the package) so that they can run the test case under identical conditions.

- While every test case developer uses the “official” set of response maps, there is no need for each developer to have a copy of the files in their workspace. Instead, share the files by storing them in a central file.

- Saving the full set of test cases for a particular release and all supporting files to the regression system (under source control) to support headless execution by iTestRT. The tests do not have to be in a iTest workspace for iTestRT to run them.

iTest files are interdependent; test cases depend on topologies or testbeds, topologies and testbeds depend on session profiles, session profiles depend on reference session profiles, and so on. One file might depend on a file in another folder in its project or on a file in a different project altogether. This means that, to ensure that all dependencies are met when sharing a particular file, you will actually export one or more projects to the file system.
