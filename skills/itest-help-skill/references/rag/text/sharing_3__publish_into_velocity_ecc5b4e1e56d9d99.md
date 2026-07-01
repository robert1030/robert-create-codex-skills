---
{
  "chunk_id": "sharing_3__publish_into_velocity_ecc5b4e1e56d9d99",
  "source_file": "topics/sharing.3.htm",
  "source_original_path": "topics/sharing.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity"
  ],
  "heading_path": [
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity",
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity",
    "Publish into Velocity"
  ],
  "anchor": "1121122",
  "context_ids": [],
  "index_keywords": [
    "export projects to Itars",
    "signing artifact"
  ],
  "index_keyword_paths": [
    "export projects to Itars > signing artifact",
    "signing artifacts > export projects to Itars"
  ],
  "related_links": [
    "#1251004",
    "#1253926"
  ],
  "images": [
    "topics/images/export_itar_select_publisIntoVelocity.png",
    "topics/images/export_itar_publishIntoVelocity.png"
  ],
  "content_hash": "ecc5b4e1e56d9d99",
  "level": 4
}
---

# Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Publish into Velocity

Select Publish into Velocity on the Export Projects to iTars - Select Projects window.

> **Note:** Note When Publish into Velocity is selected, the Encrypt exported iTars checkbox is not available for selection. See “Encrypt exported iTars”.

Click Next on the Export Projects to iTars - Select Projects window to open the Publish into Velocity window.

| Server URL Username Password | These options become available when you select Publish the iTar into a Velocity Server. It is mandatory to enter correct Velocity Server URL, username, and password. An error message displays if any of the information you entered is invalid or is missing. Note The Server URL, username, and password will be populated only if you have set up these details in iTest > Windows > Preferences > Spirent > Velocity. | Note | The Server URL, username, and password will be populated only if you have set up these details in iTest > Windows > Preferences > Spirent > Velocity. |
| --- | --- | --- | --- |
| Note | The Server URL, username, and password will be populated only if you have set up these details in iTest > Windows > Preferences > Spirent > Velocity. |  |  |
| Certificate Validation | Indicates whether security validation algorithm applies to all agent/Velocity interactions using the default trust store or the custom key store. Select the required option: No validation: (default) When selected iTest performs security validation using the default trust store. Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store |  | No validation: (default) When selected iTest performs security validation using the default trust store. |
|  | No validation: (default) When selected iTest performs security validation using the default trust store. |  |  |
|  | Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store |  |  |
| File | Browse and select the custom key store file used for security validation. If the keystore file path is wrong, that is, no valid keystore file exists, iTest displays an error. |  |  |
| Password | Enter the password to use the selected custom key store file. |  |  |
| Algorithm | Select the security validation algorithm from the dropdown list for the custom key store. |  |  |

Click Finish and iTest uploads iTars to Velocity. See Click Finish to create iTar files.

![screenshot](topics/images/export_itar_select_publisIntoVelocity.png) <!-- image_chunk: img_8cf16c029c358147 -->

![screenshot](topics/images/export_itar_publishIntoVelocity.png) <!-- image_chunk: img_8d059e036f8547c9 -->
