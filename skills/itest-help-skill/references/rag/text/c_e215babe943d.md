# About the iTest Window > Specifying a default project for iTest > To specify the default project

The default project has a iTest Project Nature of iTest Default Project.

![*](bullet_blue.jpg) <!-- image_ref -->

1. In the Project Explorer, select the project.

1. 2 On the Project menu, select Properties.

1. 3 In the Properties for [projectName] dialog box, on the iTest Project Natures list, check the iTest Default Project check box.

![](images/project_natures.png) <!-- image_ref -->

The Project Natures are added by virtue of the Eclipse plugins installed on your system. The Project Natures allows you to tag a project as a specific type of project (e.g., iTest project) and indicate that a certain tool is used to operate on that project. Select the following options to specify the Project Natures:

Note It is recommended to use this only in conjunction with Spirent Support ( https://support.spirent.com/SpirentCSC/).

| 欄位1 | 欄位2 |
| --- | --- |
| iTest Default Project | Allows the framework to treat the files as required by iTest. |
| iTest Documentation Builder | Verifies files, checks for missing dependencies and other warnings that might exist. |
| iTest Response Map Library | Indicates that this project is a container of response maps that can be organized within a Response Map Library. |
| iTest Resource | Indicates a project that contains resources necessary for iTest to function. This includes templates for Test Report formats. |
| org,eclipse.core.resources.neture | This Eclipse resources plug-in provides services for accessing the projects, folders, and files with which you are working. For use iTest internal use. |
| Security Nature | For iTest internal use only. Security Nature is added by default to all new projects. Selected: iTest will automatically verify signatures of the test cases (.iTar files ) and test report archives (*.fftz files) located in that project, creates problem markers and displays indicators accordingly. Not Selected: iTest will not automatically verify signatures of the .iTar and ..fftz files. |
| Web Properties | For iTest internal use (this is an Eclipse artefact). |

> **Note：** Note You cannot directly add options to the Project Natures. However, it is possible for you to install additional Plugins, which may add relevant Natures to the list of Project Natures. For example, if you add Python development plugins, relevant Natures may be added to the list of Project Natures.
