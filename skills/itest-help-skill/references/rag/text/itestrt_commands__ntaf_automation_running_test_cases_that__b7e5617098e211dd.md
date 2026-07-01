---
{
  "chunk_id": "itestrt_commands__ntaf_automation_running_test_cases_that__b7e5617098e211dd",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "NTAF automation: Running test cases that include NTAF sessions"
  ],
  "anchor": "1258315",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b7e5617098e211dd",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > NTAF automation: Running test cases that include NTAF sessions

To execute an NTAF test case using iTestRT, first start the Spirent NTAF proxy, and then connect to the NTAF server using the NTAF options. For example:

iTestRt --itar file:/c:/iTestRt --test project://my_project/TestCases/NtafAvTest42.fftc --ntaf.server crt-fm5q1 --login itestrt --ntaf.password mypassword

| --domain URI | XMPP domain name. Default: The NTAF server hostname. When you log onto an XMPP server, you get an ID (called a Jabber ID, JID) like username@ntafxmpp.spirent.com/unspecified “username” is the user, "ntafxmpp.spirent.com" is the domain, which is usually the same as the value of the NTAF server. However XMPP servers can be configured so that domain and server are different. (In the example, “unspecified” is the Resource). Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> Note | Note | Use a single slash character after “file:” in the URI. For example: | Note |  |
| --- | --- | --- | --- | --- | --- |
| Note | Use a single slash character after “file:” in the URI. For example: |  |  |  |  |
| Note |  |  |  |  |  |
| --inband value | In‑band registration means that the NTAF server will register a new account for your username if it does not yet exist. Note The logic of the following values seems reversed, but the following descriptions are correct: false — Try in‑band registration if login fails. Your username must exist on the NTAF server for this option. true — Do not try in‑band registration Default behavior: false — try in‑band registration if login fails. | Note | The logic of the following values seems reversed, but the following descriptions are correct: |  |  |
| Note | The logic of the following values seems reversed, but the following descriptions are correct: |  |  |  |  |
| --login name | XMPP credential for the NTAF server. Default: The value of the Username credential used to log in. |  |  |  |  |
| --ntaf.port value | Port address of NTAF server. Default: 5222 |  |  |  |  |
| --ntaf.server URI | Specify the IP address or hostname of the NTAF server (provided by your IT administrator) Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> | Note | Use a single slash character after “file:” in the URI. For example: |  |  |
| Note | Use a single slash character after “file:” in the URI. For example: |  |  |  |  |
| --ntaf.user value --ntaf.password value | Specify the XMPP username/password credentials to use to enable iTest to access the NTAF server as a client. Note The credentials represent iTest as a client on the NTAF server. Remember that the Proxy service is a different client on the NTAF server and therefore has a different username. You can set the authentication information in the NTAF preferences page in iTest. The values are not used when an application login page asks for credentials | Note | The credentials represent iTest as a client on the NTAF server. Remember that the Proxy service is a different client on the NTAF server and therefore has a different username. |  |  |
| Note | The credentials represent iTest as a client on the NTAF server. Remember that the Proxy service is a different client on the NTAF server and therefore has a different username. |  |  |  |  |
| --reconnect value | Note The logic of the following values seems reversed, but the following descriptions are correct: false — Retry connecting if the connection with the XMPP server fails true — Do not retry Default behavior: false —retry when connection fails | Note | The logic of the following values seems reversed, but the following descriptions are correct: |  |  |
| Note | The logic of the following values seems reversed, but the following descriptions are correct: |  |  |  |  |
| --regAddress value | Pubsub server address on NTAF server. Default: “pubsub.” followed by the XMPP domain. |  |  |  |  |
| --regRoot value | Pubsub root node for the NTAF registry. All NTAF provider registration information is stored under the root node. Default: ntaf.tools The default setting is typically correct. While the NTAF standard allows for other names, changing names may confuse the providers that you are trying to communicate with. |  |  |  |  |
| --resource value | XMPP resource. The last part of the JID is the resource. For example, “unspecified” in username@ntafxmpp.spirent.com/unspecified Default: “unspecified” |  |  |  |  |
