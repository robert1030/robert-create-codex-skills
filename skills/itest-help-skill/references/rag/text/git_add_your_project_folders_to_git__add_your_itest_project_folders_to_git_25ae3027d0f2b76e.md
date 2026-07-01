---
{
  "chunk_id": "git_add_your_project_folders_to_git__add_your_itest_project_folders_to_git_25ae3027d0f2b76e",
  "source_file": "topics/git_add_your_project_folders_to Git.htm",
  "source_original_path": "topics/git_add_your_project_folders_to Git.htm",
  "toc_path": null,
  "heading_path": [
    "Add your iTest Project Folders to Git",
    "Add your iTest Project Folders to Git"
  ],
  "anchor": "1474039",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "git_overview_view_and_solve_any_merge_conflicts.htm#1486276"
  ],
  "images": [
    "topics/images/08-Add_project_to_git_local.png",
    "topics/images/Git_in_iTest.02.jpg",
    "topics/images/10-Project_added_toGit_itest_Explorer.png",
    "topics/images/Git_in_iTest.04.jpg",
    "topics/images/Git_in_iTest.05.jpg",
    "topics/images/Git_in_iTest.06.jpg",
    "topics/images/14-Project_staged.png",
    "topics/images/16_view_commit_history.png",
    "topics/images/17-View_commit_history.png",
    "topics/images/git_merge_rightClick_menu.png",
    "topics/images/Git_in_iTest.11.jpg",
    "topics/images/Git_in_iTest.12.jpg",
    "topics/images/20-Pushed_proked_in_Git_remote_repo.png"
  ],
  "content_hash": "25ae3027d0f2b76e",
  "level": 1
}
---

# Add your iTest Project Folders to Git > Add your iTest Project Folders to Git

This section provides instruction to add your iTest project folders to Git. This involves adding the project to the local repository and then uploading (push) to the remote repository.

Step 1

Add your project folder to Git (local repository)

1. Go to iTest Development Perspective (select from the icons at the top right-hand side of iTest window).

1. 2

1. From the Project Explorer, select project to be added to Git. Right-click select Team > Share Project.

1. 3

1. Select Git when the Share Project dialog opens. The Configure Git Repository dialog opens populated with the project folder you selected.

Select the appropriate Repository from the list and Path within the repository (if required)

1. 4

1. Click Finish. The selected project is added to Git and the Project Explorer tree view displays as follows.

Add your project folder to Git (remote repository)

After your project is in the Git local repository follow these steps to push it to the remote repository.

1. Select project added to Git. Right-click select Team > Commit.

1. 2

1. The Git Staging tab displays with local project ready to be staged, committed, and pushed to the remote repository.

1. 3

1. Expand the Git Staging tab, select and right-click the files in the Unstaged Changes section of the Git Staging page.

The project/files are staged as illustrated below. Add a commit message for clarify and verification purposes. Click Commit. .

After you click Commit, go to the Git Repositories page and notice that the project/files are ready to be added/pushed to the remote repository as illustrated below. You may view the commit history to verify the commit...

1. 4

1. Right-click the local commit and then click Push Branch. Make sure that the project is pushed to the required repository.

If there are merge conflicts, see View and Resolve Any Merge Conflicts to resolve merge conflicts.

If there are no conflicts, click Finish and a confirmation dialog displays as illustrated..

Go to the Git Repository page a verify as illustrated..

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/08-Add_project_to_git_local.png) <!-- image_chunk: img_0cb75cd3f11b70ec -->

![screenshot](topics/images/Git_in_iTest.02.jpg) <!-- image_chunk: img_d46851499d0c9492 -->

![screenshot](topics/images/10-Project_added_toGit_itest_Explorer.png) <!-- image_chunk: img_e8a73b058fbec1a6 -->

![screenshot](topics/images/Git_in_iTest.04.jpg) <!-- image_chunk: img_2254c47a9564d362 -->

![screenshot](topics/images/Git_in_iTest.05.jpg) <!-- image_chunk: img_cb82622accaf6b4c -->

![screenshot](topics/images/Git_in_iTest.06.jpg) <!-- image_chunk: img_77ce0af2d5d6e7de -->

![screenshot](topics/images/14-Project_staged.png) <!-- image_chunk: img_c639932e84ae751e -->

![screenshot](topics/images/16_view_commit_history.png) <!-- image_chunk: img_b2ad5d02c59abb64 -->

![screenshot](topics/images/17-View_commit_history.png) <!-- image_chunk: img_a396952ce7ea8f48 -->

![screenshot](topics/images/git_merge_rightClick_menu.png) <!-- image_chunk: img_90319f5180ba6dff -->

![screenshot](topics/images/Git_in_iTest.11.jpg) <!-- image_chunk: img_48caaa87e6eb2753 -->

![screenshot](topics/images/Git_in_iTest.12.jpg) <!-- image_chunk: img_877a074467fe0ad2 -->

![screenshot](topics/images/20-Pushed_proked_in_Git_remote_repo.png) <!-- image_chunk: img_b23690f8f8d2cd8a -->
