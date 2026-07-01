---
{
  "chunk_id": "sharing_3__signing_artifacts_2aba1bc77410f9f8",
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
    "Signing Artifacts"
  ],
  "anchor": "1253890",
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
    "preferences_general_signed_assets.htm#1258612",
    "preferences_itest.htm#",
    "#1253926"
  ],
  "images": [
    "topics/images/export_itar_signing_artifacts.png"
  ],
  "content_hash": "2aba1bc77410f9f8",
  "level": 4
}
---

# Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Signing Artifacts

> **Note:** Note The Signing Artifacts dialog does not display under these circumstances:

- When uploading iTars to Velocity. Velocity server is responsible to inform the Agent how it should treat signatures (whether it should reject unsigned iTars).

- When Encrypt exported iTar option is selected.

Sign test assets (iTars) and test reports by selecting the Sign exported files option.

Before using the default keystore file (spirent.apt.keystore.jks) for signing the exported artifacts, ensure that you perform these tasks.

1. Add a private key to the default keystore.

1. 2

1. Enable Signature Verification on iTest Preferences: Spirent > General > Signed Assets (“Configuring iTest Preferences”).

| Sign exported files | Indicates whether the exported iTars should be signed. Selected: iTars are signed with the Key ID specified below. Not Selected: iTars are not signed and the options below the checkbox is disabled. |  | Selected: iTars are signed with the Key ID specified below. |  | Not Selected: iTars are not signed and the options below the checkbox is disabled. |
| --- | --- | --- | --- | --- | --- |
|  | Selected: iTars are signed with the Key ID specified below. |  |  |  |  |
|  | Not Selected: iTars are not signed and the options below the checkbox is disabled. |  |  |  |  |
| Key Store Path | Indicates the location of the Keystore file (default keystore is spirent.apt.keystore.jks) |  |  |  |  |
| Key ID (Alias) | Mandatory. Alias of the key from the keystore that is used for signing (default: spirent). |  |  |  |  |
| Timestamping Authority | Optional. The URL of the Time Stamp Authority service. |  |  |  |  |
| Key Store Password | Default. The password that is required to access the keystore (default spirent.apt.keystore.jks password is changeit) |  |  |  |  |
| Key Password | Optional. Enter the private key password. |  |  |  |  |

> **Note:** Note iTest uses jarsigner for signing artifacts, so more proper description of these options can be found in https://docs.oracle.com/javase/7/docs/technotes/tools/windows/jarsigner.html.

1. 3

1. Click Finish to create iTars. See “Click Finish to create iTar files” below.

![screenshot](topics/images/export_itar_signing_artifacts.png) <!-- image_chunk: img_aaf10165b1602e64 -->
