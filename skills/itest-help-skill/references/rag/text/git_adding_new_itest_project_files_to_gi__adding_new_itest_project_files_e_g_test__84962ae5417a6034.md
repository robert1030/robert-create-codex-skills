---
{
  "chunk_id": "git_adding_new_itest_project_files_to_gi__adding_new_itest_project_files_e_g_test__84962ae5417a6034",
  "source_file": "topics/git_adding_new_iTest_project_files_to_Git.htm",
  "source_original_path": "topics/git_adding_new_iTest_project_files_to_Git.htm",
  "toc_path": [
    "iTest Online Help",
    "Using Git in iTest",
    "Adding New iTest Project Files (e.g.,Test Cases) to Git"
  ],
  "heading_path": [
    "Adding New iTest Project Files (e.g.,Test Cases) to Git",
    "Adding New iTest Project Files (e.g.,Test Cases) to Git"
  ],
  "anchor": "1469870",
  "context_ids": [
    "git_adding_new_iTest_project_files_to_Git"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "test_cases_creating_by_capture.htm#",
    "git_add_your_project_folders_to%20Git.htm#1488634"
  ],
  "images": [
    "topics/images/21-Add_test_cases_folder_to_Git.png",
    "topics/images/23-new-commit-in-local-repo.png",
    "topics/images/24-Verify_master_history_no_commit.png"
  ],
  "content_hash": "84962ae5417a6034",
  "level": 1
}
---

# Adding New iTest Project Files (e.g.,Test Cases) to Git > Adding New iTest Project Files (e.g.,Test Cases) to Git

This section provides instructs on adding new project files to Git. The examples illustrates adding a test case to Git.

Step 1

Adding a Test Case to Git

1. Create a a new test case (See , “” on page 133) and save. The new test case appears in the Unstaged Changes section of the Git Staging page on the right. See illustration below.

1. 2

1. Right-click the test cases folder in Project Explorer view and then click Team > Add to Index.

1. 3

1. The Test case is staged when you click Team > Add to Index.

1. 4

1. Add a commit message and click Commit. Verify the commit in local repository as illustrated.

Verify in the remote repository to confirm that the new change has not yet been pushed.

1. 5

1. Right-click the local commit and then click Push Branch. Make sure that the project is pushed to the required repository. (Refer to the description and illustration in Step 4 page 2272).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/21-Add_test_cases_folder_to_Git.png) <!-- image_chunk: img_6956d2f3ab86de70 -->

![screenshot](topics/images/23-new-commit-in-local-repo.png) <!-- image_chunk: img_420c540737c51f1f -->

![screenshot](topics/images/24-Verify_master_history_no_commit.png) <!-- image_chunk: img_d9cf85df65d35d94 -->
