# Sharing iTest Resources > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Export to Directory

In the Export to directory field, specify the folder or browse to the folder to export the iTar files.

![](images/exppot_itar_publishIntoDirectory.png) <!-- image_ref -->

For example, this can be a location in your regression system under source control. (For instructions on accessing files that are stored in iTar files, see Accessing iTest files that are held in iTar files.)

You have the following options:

![*](bullet_blue.jpg) <!-- image_ref -->

- Save all iTar files to a central location (typically under source control). Any reference to a file using a project:// URI in an instance of iTest or iTestRT will look in this location to find files that are included in an iTar file.

![*](bullet_blue.jpg) <!-- image_ref -->

- While browsing to the folder, create a subfolder directly under a shared workspace root directory and name the subdirectory iTar. Any instance of iTest will, by default, look in this location to find files that are included in an iTar file.

![*](bullet_blue.jpg) <!-- image_ref -->

- Select Encrypt exported iTars, if required. See Encrypt exported iTars.

![*](bullet_blue.jpg) <!-- image_ref -->

- When Export to directory and Encrypt exported iTars are selected, the Next option does not display.

Click Finish. See Click Finish to create iTar files.

![*](bullet_blue.jpg) <!-- image_ref -->

- When Export to directory is selected and Encrypt exported iTars is not selected, click Next option is available. Click Next to display the Signing Artifacts page. Go to Signing Artifacts to sign the artifacts and then create iTars.
