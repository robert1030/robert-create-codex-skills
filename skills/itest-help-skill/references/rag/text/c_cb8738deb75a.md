# iTest Runtime: iTestRT > iTestRT command reference > NTAF automation: Running test cases that include NTAF sessions > 第2段

| 欄位1 | 欄位2 |
| --- | --- |
| --domain URI | XMPP domain name. Default: The NTAF server hostname. When you log onto an XMPP server, you get an ID (called a Jabber ID, JID) like username@ntafxmpp.spirent.com/unspecified “username” is the user, "ntafxmpp.spirent.com" is the domain, which is usually the same as the value of the NTAF server. However XMPP servers can be configured so that domain and server are different. (In the example, “unspecified” is the Resource). file:/C:/Workspace/my_project/<folder>/<filename>.<extension> |
| --inband value | In‑band registration means that the NTAF server will register a new account for your username if it does not yet exist. false — Try in‑band registration if login fails. Your username must exist on the NTAF server for this option. true — Do not try in‑band registration Default behavior: false — try in‑band registration if login fails. |
| --login name | XMPP credential for the NTAF server. Default: The value of the Username credential used to log in. |
| --ntaf.port value | Port address of NTAF server. Default: 5222 |
| --ntaf.server URI | Specify the IP address or hostname of the NTAF server (provided by your IT administrator) file:/C:/Workspace/my_project/<folder>/<filename>.<extension> |
| --ntaf.user value --ntaf.password value | Specify the XMPP username/password credentials to use to enable iTest to access the NTAF server as a client. You can set the authentication information in the NTAF preferences page in iTest. The values are not used when an application login page asks for credentials |
| --reconnect value | false — Retry connecting if the connection with the XMPP server fails true — Do not retry Default behavior: false —retry when connection fails |
| --regAddress value | Pubsub server address on NTAF server. Default: “pubsub.” followed by the XMPP domain. |
| --regRoot value | Pubsub root node for the NTAF registry. All NTAF provider registration information is stored under the root node. Default: ntaf.tools The default setting is typically correct. While the NTAF standard allows for other names, changing names may confuse the providers that you are trying to communicate with. |
| --resource value | XMPP resource. The last part of the JID is the resource. For example, “unspecified” in username@ntafxmpp.spirent.com/unspecified Default: “unspecified” |
