---
{
  "chunk_id": "preferences_general_signed_assets__preferences_spirent_general_signed_asset_8db57d762c6d9b75",
  "source_file": "topics/preferences_general_signed_assets.htm",
  "source_original_path": "topics/preferences_general_signed_assets.htm",
  "toc_path": [
    "iTest Online Help",
    "Configuring iTest Preferences",
    "Preferences: Spirent > General > Signed Assets"
  ],
  "heading_path": [
    "Preferences: Spirent > General > Signed Assets",
    "Preferences: Spirent > General > Signed Assets"
  ],
  "anchor": "1258612",
  "context_ids": [
    "preferences_general_signed_assets"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "8db57d762c6d9b75",
  "level": 1
}
---

# Preferences: Spirent > General > Signed Assets > Preferences: Spirent > General > Signed Assets

iTest (GUI and iTestRT) provides one built-in keystore called spirent.apt.keystore.jks which contains a certificate, a trustedCertEntry, that Spirent APT uses to sign the iTars and external script projects with the password.

You may add trusted certificates to this keystore and specify the location of the keystore file used for verification (and for signing in iTest GUI).

> **Note:** Note If keyStore is not specified, the default certificate in spirent.apt.keystore.jks will be used.

> **Note:** If custom keystore file is specified and it does not contain Spirent Certificate, the iTar files will be re-signed or Spirent self-signed certificate should be included into the custom keystore file.

Important The default value of the trusted certificate must be spirent.apt.keystore.jks

| Enable Signature verification | Select to enable the verification on signed iTars / external script projects, using the specified keystore. |
| --- | --- |
| Key Store path | Specify the location of the spirent.apt.keystore.jks file. |
| Key Store Password | Indicates the keystore file password that was set during generation of a keystore. If password is not specified, “changeit” will be used. |

> **Note:** Note Projects from iTest workspace are not considered as assets by NDO agent, so the content of these projects will be filtered out when signed assets validation is turned on. Ensure that the Enable signature verification option is not selected on Spirent > General > Signed Assets page for iTest NDO Agent.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
