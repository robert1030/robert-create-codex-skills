# Working with NTAF sessions in Velocity iTest (Obsolete and Deprecated) > To work with NTAF-enabled sessions on Velocity iTest > Advanced settings

Note The default setting is typically correct. While the NTAF standard allows for other names, changing names may confuse providers that you are trying to communicate with.

- **Domain**：XMPP domain name. Default: The NTAF server hostname. When you log onto an XMPP server, you get an ID (called a Jabber ID, JID) like username@ntafxmpp.spirent.com/unspecified “username” is the user, "ntafxmpp.spirent.com" is the domain, which is usually the same as the value of the NTAF server. However XMPP servers can be configured so that domain and server are different. (In the example, “unspecified” is the Resource).
- **Server port**：Port address of NTAF server. Default: 5222
- **Login name**：XMPP login name. Default: The value of the User credential used to log in.
- **Resource**：XMPP resource. The last part of the JID is the resource. For example, “unspecified” in username@ntafxmpp.spirent.com/unspecified Default: “unspecified”
- **Registry address**：Pubsub server address on NTAF server. Default: “pubsub.” followed by the XMPP domain.
- **Registry root node**：Pubsub root node for the NTAF registry. All NTAF provider registration information is stored under the root node. Default: ntaf.tools
- **Do not try in‑band registration if login fails**：In‑band registration means that the NTAF server will register a new account for your username if it does not yet exist. If you check the box, then your username must exist on the NTAF server for you to log in.
- **Do not reconnect if connection is lost**：Check the box to not automatically retry XMPP connections if and when the connection with the server fails.
- **Open window showing XMPP packets**：Check the box to open a window showing XMPP packets sent between iTest and the NTAF server.

![*](bullet_blue.jpg) <!-- image_ref -->

Velocity iTest is now ready to open the NTAF‑enabled session.
