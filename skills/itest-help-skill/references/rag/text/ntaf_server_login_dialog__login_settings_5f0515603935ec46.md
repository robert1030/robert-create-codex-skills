---
{
  "chunk_id": "ntaf_server_login_dialog__login_settings_5f0515603935ec46",
  "source_file": "topics/ntaf_server_login_dialog.htm",
  "source_original_path": "topics/ntaf_server_login_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Working with NTAF sessions in Velocity iTest (Obsolete and Deprecated)",
    "To work with NTAF-enabled sessions on Velocity iTest"
  ],
  "heading_path": [
    "To work with NTAF-enabled sessions on Velocity iTest",
    "To work with NTAF-enabled sessions on Velocity iTest",
    "Login settings"
  ],
  "anchor": "1319070",
  "context_ids": [
    "ntaf_server_login_dialog"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "5f0515603935ec46",
  "level": 4
}
---

# To work with NTAF-enabled sessions on Velocity iTest > To work with NTAF-enabled sessions on Velocity iTest > Login settings

| Property Name | Equivalent iTestRT switch | Description |
| --- | --- | --- |
| NTAF server | --ntaf.server <URI> | Specify the IP address or hostname of the NTAF server (provided by your IT administrator). |
| Username / Password | --ntaf.user <value> --ntaf.password <value> | Specify the XMPP credentials to use to enable iTest to access the NTAF server as a client. IMPORTANT The credentials represent iTest as a client on the NTAF server. Remember that the Proxy service is a different client on the NTAF server and therefore has a different username. Note You can set the authentication information in the NTAF preferences page in iTest. The values are not used when an application login page asks for credentials |
| IMPORTANT |  |  |
| Note | You can set the authentication information in the NTAF preferences page in iTest. The values are not used when an application login page asks for credentials |  |
| Automatically sign me in Prompt for login every time Do not auto-login | (none) | Specify what should happen when you open a session with the NTAF server: Apply the specified credentials or open this dialog box and request credentials. |
| Remember login settings | (none) | Check the box to use the specified credentials by default when logging in. |
