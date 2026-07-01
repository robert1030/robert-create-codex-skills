---
{
  "chunk_id": "git_in_itest_overview__overview_a5911f5ea69c7d5e",
  "source_file": "topics/git_in_itest_overview.htm",
  "source_original_path": "topics/git_in_itest_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Using Git in iTest",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview"
  ],
  "anchor": "1462986",
  "context_ids": [
    "git_in_itest_overview"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "git_setting_up_Git_repository_in_iTest.htm#1463470",
    "git_add_your_project_folders_to%20Git.htm#1474039",
    "git_adding_new_iTest_project_files_to_Git.htm#1469870",
    "git_restore_deleted_files.htm#1472153",
    "git_overview_view_and_solve_any_merge_conflicts.htm#1486276",
    "git_preferences.htm#1466547",
    "git_preferences_declassify.htm#1478997"
  ],
  "images": [],
  "content_hash": "a5911f5ea69c7d5e",
  "level": 1
}
---

# Overview > Overview

iTest integrates Eclipse EGit plugin, which allows you to use Git source control from iTest. This chapter provides instructions on using EGit from within iTest.

The instructions assumes the following:

- Groups within your organization want to work on a project using EGit to develop and maintain test cases in a single location (the master branch).

- Users will have their own local repository (a copy of the test cases code including all the source control relevant information).

- Each user will receive changes and send changes using a remote repository at GitHub.

For details about EGit see http://wiki.eclipse.org/EGit/User_Guide.

This chapter includes the following section.

- Setting up Git repository in iTest

- Add your iTest Project Folders to Git

- Adding New iTest Project Files (e.g.,Test Cases) to Git

- Restore Deleted Files

- View and Resolve Any Merge Conflicts

- Setting preferences for Git

> **Note:** Note Set Git preferences in iTest as described in Setting preferences for Git first and then perform the rest of the tasks described in this chapter.

By default, EGit Plugin (iTest Git integration) automatically adds derived resources into .gitignore. Certain iTest files, e.g., the response map catalog (.maplib.ffrmcat), test case library catalog (testcaselib.fffmcat), etc., were being classified as derived files and were not getting pushed to Git.

To avoid runtime issues with files on Git, iTest does not classify files as derived resources to ensure that the EGit plugin would not auto-create .gitignore file for the new content created in iTest.

These iTest files are not classified as derived resources, so the Git integration will not ignore the files.

- .project

- .formmaplib.fffmcat

- .testcaselib.fftccat

- .maplib.ffrmcat

> **Note:** Note See set preferences in iTest as described in Setting preferences to Declassify iTest Files as Derived Resources to see the files declassified as derived resources by iTest.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
