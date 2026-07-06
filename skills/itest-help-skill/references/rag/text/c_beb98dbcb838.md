# Using Git in iTest > Overview > 第1段

iTest integrates Eclipse EGit plugin, which allows you to use Git source control from iTest. This chapter provides instructions on using EGit from within iTest.

The instructions assumes the following:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Groups within your organization want to work on a project using EGit to develop and maintain test cases in a single location (the master branch).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Users will have their own local repository (a copy of the test cases code including all the source control relevant information).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Each user will receive changes and send changes using a remote repository at GitHub.

For details about EGit see http://wiki.eclipse.org/EGit/User_Guide.

This chapter includes the following section.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Setting up Git repository in iTest

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Add your iTest Project Folders to Git

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Adding New iTest Project Files (e.g.,Test Cases) to Git

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Restore Deleted Files

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- View and Resolve Any Merge Conflicts

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Setting preferences for Git

> **Note：** Note Set Git preferences in iTest as described in Setting preferences for Git first and then perform the rest of the tasks described in this chapter.

By default, EGit Plugin (iTest Git integration) automatically adds derived resources into .gitignore. Certain iTest files, e.g., the response map catalog (.maplib.ffrmcat), test case library catalog (testcaselib.fffmcat), etc., were being classified as derived files and were not getting pushed to Git.

To avoid runtime issues with files on Git, iTest does not classify files as derived resources to ensure that the EGit plugin would not auto-create .gitignore file for the new content created in iTest.

These iTest files are not classified as derived resources, so the Git integration will not ignore the files.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- .project

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- .formmaplib.fffmcat

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- .testcaselib.fftccat

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- .maplib.ffrmcat
