---
{
  "chunk_id": "git_setting_up_git_repository_in_itest__setting_up_git_repository_in_itest_3b6ce3f2375405e8",
  "source_file": "topics/git_setting_up_Git_repository_in_iTest.htm",
  "source_original_path": "topics/git_setting_up_Git_repository_in_iTest.htm",
  "toc_path": [
    "iTest Online Help",
    "Using Git in iTest",
    "Setting up Git repository in iTest"
  ],
  "heading_path": [
    "Setting up Git repository in iTest",
    "Setting up Git repository in iTest"
  ],
  "anchor": "1463470",
  "context_ids": [
    "git_setting_up_Git_repository_in_iTest"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "git_add_your_project_folders_to%20Git.htm#1474039"
  ],
  "images": [
    "topics/images/Git_in_iTest.2.jpg",
    "topics/images/02-Git_repositories.png",
    "topics/images/02-a-Git_loca_repo.png",
    "topics/images/Git_in_iTest.5.jpg",
    "topics/images/Git_in_iTest.6.jpg",
    "topics/images/Git_in_iTest.7.jpg",
    "topics/images/Git_in_iTest.8.jpg",
    "topics/images/07-git_remote_repo_created.png"
  ],
  "content_hash": "3b6ce3f2375405e8",
  "level": 1
}
---

# Setting up Git repository in iTest > Setting up Git repository in iTest

Follow these instructions in iTest.

Step 1

Setup Local Repository

1. Click Open Perspective () at top right-hand side. Then Click Git in the Open Perspective dialog.

The Git Repositories page opens.

> **Note:** Note You may use the menu options on the top of the Git Repositories page as required.

1. 2

1. Select Create a new local Git repository the repository to add to your current view.

Create a New Git Repository dialog opens.

1. 3

1. Click Browse, navigate and choose the directory for your new local repository. For example: (example: c:\itest\builds\itest-5.4\47\git\localRepo) Click Finish.

A Local Git Repository is created at the specified location.

Setup Remote Repository (Locally)

1. Select Create a new local Git repository from the menu (at the top of the Git Repository page) to be added to your current view.

Create a New Git Repository dialog opens.

1. 2

1. Enter the remote directory path (example: c:\itest\builds\itest-5.4\47\git\remoteRepo) or navigate to the location. Click Finish.

A Remote Git Repository is created at the specified location.

Create Remote repository to push or fetch files

1. Right-Click on Remote under the localRepo and the New Remote dialog opens.

1. 2

1. Select the type of remote location you wish to create on the New Remote dialog. Enter/select the following:

| Remote name: | Default: Origin Enter the remote repository name (this name appears on the remote configuration dialogs). |
| --- | --- |
| Configure push | Select to configure the new remote location for push operation (selected by default). |
| Configure fetch | Select to configure the new remote location for fetch operation. |

It is mandatory that you configure the new remote location for either fetch or push operations. You may add configuration for the other directory at a later time.

1. 3

1. Select push and click OK and Configure push for remote ‘Origin’ dialog displays.

1. 4

1. It is mandatory to provide a valid URI. Click change and when the Destination Git Repository dialog displays, browse to the location and provide the correct destination URI and Repository path as illustrated.

1. 5

1. Click Finish and the Configure push for remote ‘Origin’ displays populated with the destination URI you specified on the Destination Git Repository dialog.

1. 6

1. Click Save and verify that the remote repository is created as required.

After setting up the Git Repository in iTest, the next step is to add your project folder to Git repository. See section Add your iTest Project Folders to Git below.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/Git_in_iTest.2.jpg) <!-- image_chunk: img_c0d3e12f1fca9006 -->

![screenshot](topics/images/02-Git_repositories.png) <!-- image_chunk: img_1c7561987d027c22 -->

![screenshot](topics/images/02-a-Git_loca_repo.png) <!-- image_chunk: img_6b909b942d2f725e -->

![screenshot](topics/images/Git_in_iTest.5.jpg) <!-- image_chunk: img_37eae0b1e49d8f80 -->

![screenshot](topics/images/Git_in_iTest.6.jpg) <!-- image_chunk: img_f68d34016a6121b1 -->

![screenshot](topics/images/Git_in_iTest.7.jpg) <!-- image_chunk: img_045dc736db03118a -->

![screenshot](topics/images/Git_in_iTest.8.jpg) <!-- image_chunk: img_cef79bb741ea5d6d -->

![screenshot](topics/images/07-git_remote_repo_created.png) <!-- image_chunk: img_84bea4b17275ba91 -->
