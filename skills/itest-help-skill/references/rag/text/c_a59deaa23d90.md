# Using Git in iTest > Adding New iTest Project Files (e.g.,Test Cases) to Git

This section provides instructs on adding new project files to Git. The examples illustrates adding a test case to Git.

Step 1

Adding a Test Case to Git

![*](bullet_blue.jpg) <!-- image_ref -->

1. Create a a new test case (See , “” on page 133) and save. The new test case appears in the Unstaged Changes section of the Git Staging page on the right. See illustration below.

1. 2 Right-click the test cases folder in Project Explorer view and then click Team > Add to Index.

![](images/21-Add_test_cases_folder_to_Git.png) <!-- image_ref -->

1. 3 The Test case is staged when you click Team > Add to Index.

1. 4 Add a commit message and click Commit. Verify the commit in local repository as illustrated.

![](images/23-new-commit-in-local-repo.png) <!-- image_ref -->

Verify in the remote repository to confirm that the new change has not yet been pushed.

![](images/24-Verify_master_history_no_commit.png) <!-- image_ref -->

1. 5 Right-click the local commit and then click Push Branch. Make sure that the project is pushed to the required repository. (Refer to the description and illustration in Step 4 page 2272).
