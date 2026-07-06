# Sharing iTest Resources > Sharing projects with colleagues and saving them for use in automated testing

This topic describes sharing iTest files, for example:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Sharing a test case with a coworker that uses iTest (and easily including all supporting files in the package) so that they can run the test case under identical conditions.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- While every test case developer uses the “official” set of response maps, there is no need for each developer to have a copy of the files in their workspace. Instead, share the files by storing them in a central file.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Saving the full set of test cases for a particular release and all supporting files to the regression system (under source control) to support headless execution by iTestRT. The tests do not have to be in a iTest workspace for iTestRT to run them.

iTest files are interdependent; test cases depend on topologies or testbeds, topologies and testbeds depend on session profiles, session profiles depend on reference session profiles, and so on. One file might depend on a file in another folder in its project or on a file in a different project altogether. This means that, to ensure that all dependencies are met when sharing a particular file, you will actually export one or more projects to the file system.
