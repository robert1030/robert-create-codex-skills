# Using Git in iTest > Comparison editor appearance and behavior > Comparing two test cases > 第1段

Eclipse merge tool shows two test case editors side-by-side, which makes it easy to view and resolve merge conflicts between the source (on the right) file and the target (on the left) file.

> **Note：** Note You may use the toggle (on the right) to choose whether you would like to copy from right window to left or from left window to the right.

![](images/Git_in_iTest.01.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The test case editor windows indicate the location of the content (local or remote), at the top of each test case editor window.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- An icon shows next to the steps to indicate that the step was added, deleted, or contains differences/conflicts. Different colors also indicate the actions performed on each of the steps. For example, test step added, changed, deleted, and conflicted (merge conflicts) as set up in the preferences. See General > Appearance > Color and Fonts.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You may use the toggle (top right) to select the version (local or remote, i.e., from the right window to the left or vice versa) of the test step with conflict you wish to merge.

You may resolve conflicts for the entire step and insert steps from source to target window by clicking the corresponding buttons on the center of the compare editor.

Note:

If you wish to keep the local version, open the Git Staging view, right-click file and select Replace With/Ours.

This will remove the GIT conflict markers and keep the version from the local version in the final commit.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Selections with the two editors are synchronized, i. e., when you select a page or control in one editor, the corresponding page or control is selected in the other editor.

Scrolling with the steps tree sections are also synchronized.

You will be able to resolve conflicts for whole step (i.e.) and insert steps from one side to another by clicking corresponding buttons on the center control of compare editor

The History tab displays information about the author, last user to commit changes, and the commit date.

![](images/git_history.png) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->
