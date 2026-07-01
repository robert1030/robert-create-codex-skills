---
{
  "chunk_id": "sharing_3__publish_into_network_devops_agent_02060767fcabc90e",
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
    "Publish into Network DevOps Agent"
  ],
  "anchor": "1244307",
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
    "#1253890"
  ],
  "images": [
    "topics/images/export_itar_select_publisIntoNDO.png",
    "topics/images/export_itar_publishIntoNDO.png"
  ],
  "content_hash": "02060767fcabc90e",
  "level": 4
}
---

# Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Publish into Network DevOps Agent

Select project(s), option Publish into Network DevOps Agent and Encrypt exported iTars, if required. See Encrypt exported iTars.

Click Next and the page opens the Publish into Network DevOps Agent window as shown below.

| Server URL Username Password | These options become available when you select Publish the iTar into Network DevOps Agent. It is mandatory to enter correct Network DevOps Agent Server URL, username, and password. An error message displays if any of the information you entered is invalid or is missing. Note The Server URL, username, and password will be saved and populated for subsequent exports into Network DevOps Agent server. | Note | The Server URL, username, and password will be saved and populated for subsequent exports into Network DevOps Agent server. |
| --- | --- | --- | --- |
| Note | The Server URL, username, and password will be saved and populated for subsequent exports into Network DevOps Agent server. |  |  |
| Test Connection | Click the Test Connection button to validate connection to the Server URL you entered. iTest automatically verifies connection to the URL when you click the Next or Finish buttons. An error displays if the connection fails. Note As the Server URL, username, and password are saved, iTest verifies the URL connection for subsequent exports into Network DevOps Agent server. | Note | As the Server URL, username, and password are saved, iTest verifies the URL connection for subsequent exports into Network DevOps Agent server. |
| Note | As the Server URL, username, and password are saved, iTest verifies the URL connection for subsequent exports into Network DevOps Agent server. |  |  |
| Replace iTars | Indicates whether the iTars being uploaded should replace existing iTars. Selected by default. Selected: When selected, the existing iTars are replaced by the uploaded files. Not Selected: When not selected iTest displays the Overwrite dialog asking you to confirm whether you wish to overwrite the displayed iTar files (Yes, Yes to All, No, No to All). Informative messages display for these circumstances: iTars are skipped: The iTars exists on the Network DevOps Agent and is up to date (modification date/ETag is current). No disk Space: The iTars could not be downloaded due to inadequate disk space on the Network DevOps Agent. iTars rejected: the agent has been configured to run only digitally signed archives, and this archive does not contain a trusted, non-expired digital signature |  | iTars are skipped: The iTars exists on the Network DevOps Agent and is up to date (modification date/ETag is current). |
|  | iTars are skipped: The iTars exists on the Network DevOps Agent and is up to date (modification date/ETag is current). |  |  |
|  | No disk Space: The iTars could not be downloaded due to inadequate disk space on the Network DevOps Agent. |  |  |
|  | iTars rejected: the agent has been configured to run only digitally signed archives, and this archive does not contain a trusted, non-expired digital signature |  |  |
| Certificate Validation | Indicates whether security validation algorithm applies to all agent/Velocity interactions using the default trust store or the custom key store. Select the required option: No validation: (default) When selected iTest performs security validation using the default trust store. Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store Note HTTPS certificates are mandated to have SAN field that indicates to which internet addresses the certificate applies. Add -ext argument to keytool command line Example: keytool -genkey -alias serverkey -storetype jks -keyalg RSA -keysize 2048 -keystore myapprestws.keystore -validity 730 -storepass "MYAPPS Private Keys" -dname "CN=ndo.spirent.com, OU=BANK, O=clientws, L=City, ST=State, C=Country" -keypass "MYAPPS Private Keys" -ext SAN=ip:10.141.0.182 |  | No validation: (default) When selected iTest performs security validation using the default trust store. |
|  | No validation: (default) When selected iTest performs security validation using the default trust store. |  |  |
|  | Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store |  |  |
| Note |  |  |  |
| File | Browse and select the custom key store file used for security validation. If the keystore file path is wrong, that is, no valid keystore file exists, iTest displays an error. |  |  |
| Password | Enter the password to use the selected custom key store file. |  |  |
| Algorithm | Select the security validation algorithm from the dropdown list for the custom key store. |  |  |

1. 5

1. Click Next and the Signing Artifacts page opens. See Signing Artifacts.

![screenshot](topics/images/export_itar_select_publisIntoNDO.png) <!-- image_chunk: img_819e0f851992b220 -->

![screenshot](topics/images/export_itar_publishIntoNDO.png) <!-- image_chunk: img_6ae0bb758d04cec0 -->
