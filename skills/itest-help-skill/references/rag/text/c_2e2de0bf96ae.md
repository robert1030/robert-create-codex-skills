# Sharing iTest Resources > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Only the options Export to directory and Publish into Network DevOps Agent are available. When Export to directory is selected, the Next button at the bottom of the Export Projects to iTars window is disabled and the Sign Assets window will not be available. When Publish into Network DevOps Agent is selected, you may sign artifacts and publish to Network DevOps Agent. See Publish into Network DevOps Agent. Publish into Velocity is disabled. Publish into Velocity

Select Publish into Velocity on the Export Projects to iTars - Select Projects window.

> **Note：** Note When Publish into Velocity is selected, the Encrypt exported iTars checkbox is not available for selection. See “Encrypt exported iTars”.

![](images/export_itar_select_publisIntoVelocity.png) <!-- image_ref -->

Click Next on the Export Projects to iTars - Select Projects window to open the Publish into Velocity window.

![](images/export_itar_publishIntoVelocity.png) <!-- image_ref -->

Note The Server URL, username, and password will be populated only if you have set up these details in iTest > Windows > Preferences > Spirent > Velocity.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

No validation: (default) When selected iTest performs security validation using the default trust store. Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store

| 欄位1 | 欄位2 |
| --- | --- |
| Server URL Username Password | These options become available when you select Publish the iTar into a Velocity Server. It is mandatory to enter correct Velocity Server URL, username, and password. An error message displays if any of the information you entered is invalid or is missing. |
| Certificate Validation | Indicates whether security validation algorithm applies to all agent/Velocity interactions using the default trust store or the custom key store. Select the required option: |
| File | Browse and select the custom key store file used for security validation. If the keystore file path is wrong, that is, no valid keystore file exists, iTest displays an error. |
| Password | Enter the password to use the selected custom key store file. |
| Algorithm | Select the security validation algorithm from the dropdown list for the custom key store. |

Click Finish and iTest uploads iTars to Velocity. See Click Finish to create iTar files.
