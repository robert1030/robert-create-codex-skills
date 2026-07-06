# Working with NTAF sessions in Velocity iTest (Obsolete and Deprecated) > To work with NTAF-enabled sessions on Velocity iTest > Advanced settings > 第1段

Note The default setting is typically correct. While the NTAF standard allows for other names, changing names may confuse the providers that you are trying to communicate with.

| 欄位1 | 欄位2 | 欄位3 |
| --- | --- | --- |
| Property Name | Equivalent iTestRT switch | Description |
| Domain | --domain <URI> | XMPP domain name. Default: The NTAF server hostname. When you log onto an XMPP server, you get an ID (called a Jabber ID, JID) like username@ntafxmpp.spirent.com/unspecified “username” is the user, "ntafxmpp.spirent.com" is the domain, which is usually the same as the value of the NTAF server. However XMPP servers can be configured so that domain and server are different. (In the example, “unspecified” is the Resource). |
| Server port | --ntaf.port <value> | Port address of NTAF server. Default: 5222 |
| Login name | --login <name> | XMPP login name. Default: The value of the Username credential used to log in. |
| Resource | --resource <value> | XMPP resource. The last part of the JID is the resource. For example, “unspecified” in username@ntafxmpp.spirent.com/unspecified Default: “unspecified” |
| Registry address | --regAddress <value> | Pubsub server address on NTAF server. Default: “pubsub.” followed by the XMPP domain. |
| Registry root node | --regRoot <value> | Pubsub root node for the NTAF registry. All NTAF provider registration information is stored under the root node. Default: ntaf.tools |
| Do not try in‑band registration if login fails | --inband <value> | In‑band registration means that the NTAF server will register a new account for your username if it does not yet exist. If you check the box, then your username must exist on the NTAF server for you to log in. |
| Do not reconnect if connection is lost | --reconnect <value> | Check the box to not automatically retry XMPP connections if and when the connection with the server fails. |
| Open window showing XMPP packets | (none) | Check the box to open a window showing XMPP packets sent between iTest and the NTAF server. |
| Allow NTAF views to start sessions and send requests | (none) | Enable the menus in the NTAF Sessions view that start sessions and send requests. See Starting the NTAF Proxy service from the command line. |

![*](bullet_blue.jpg) <!-- image_ref -->

Start the NTAF Proxy service and log it in as a client on the NTAF server
