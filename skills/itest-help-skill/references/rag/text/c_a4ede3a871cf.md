# Parameters > Parameter Files: Centralizing parameter definitions > Saving parameter definitions as a parameter file

While working on the Parameters page in the Test Case editor or Session Profile editor, you can save the current set of parameter definitions as a parameter file:

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/parameters_5.1.jpg) <!-- image_ref -->

1. Click .

1. 2 Specify the following settings for the new parameter file. iTest saves the parameter definitions and references to the included parameter files into the new parameter file.

- **Destination Folder**：Specify where to save the file. Workspace folder: Save the file in a folder in the current workspace. iTest users that use the workspace will see the folder (and the new test report file) in the Project Explorer. The default folder is parameter_files, but you can specify any folder in the workspace or specify a new folder. If you specify a new folder, iTest creates it and then adds the file to it. File system folder: Save the file in the specified folder (typically, outside of the current workspace). If the file is saved outside of the workspace, iTest users that use the current workspace will not see the folder (or the new test report file) in the Project Explorer. Instead, use the operating system's methods for accessing files.
- **File name**：iTest provides a unique, numbered name for the file (parameters<n>.ffpt, where n is a number). You can modify the name as needed.
- **Open file in the Parameter editor after saving**：Check the box to display the file in the Parameter editor once it has been saved.
