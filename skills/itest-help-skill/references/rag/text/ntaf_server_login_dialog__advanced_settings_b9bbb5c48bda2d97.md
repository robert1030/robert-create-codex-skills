---
{
  "chunk_id": "ntaf_server_login_dialog__advanced_settings_b9bbb5c48bda2d97",
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
    "Advanced settings"
  ],
  "anchor": "1328310",
  "context_ids": [
    "ntaf_server_login_dialog"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "ntaf_starting_command_line.htm#1334478",
    "ntaf_proxy_view.htm#1329158",
    "ntaf_preferences.htm#1328928"
  ],
  "images": [],
  "content_hash": "b9bbb5c48bda2d97",
  "level": 4
}
---

# To work with NTAF-enabled sessions on Velocity iTest > To work with NTAF-enabled sessions on Velocity iTest > Advanced settings

| Property Name | Equivalent iTestRT switch | Description |
| --- | --- | --- |
| Domain | --domain <URI> | XMPP domain name. Default: The NTAF server hostname. When you log onto an XMPP server, you get an ID (called a Jabber ID, JID) like username@ntafxmpp.spirent.com/unspecified “username” is the user, "ntafxmpp.spirent.com" is the domain, which is usually the same as the value of the NTAF server. However XMPP servers can be configured so that domain and server are different. (In the example, “unspecified” is the Resource). |
| Server port | --ntaf.port <value> | Port address of NTAF server. Default: 5222 |
| Login name | --login <name> | XMPP login name. Default: The value of the Username credential used to log in. |
| Resource | --resource <value> | XMPP resource. The last part of the JID is the resource. For example, “unspecified” in username@ntafxmpp.spirent.com/unspecified Default: “unspecified” |
| Registry address | --regAddress <value> | Pubsub server address on NTAF server. Default: “pubsub.” followed by the XMPP domain. |
| Registry root node | --regRoot <value> | Pubsub root node for the NTAF registry. All NTAF provider registration information is stored under the root node. Default: ntaf.tools Note The default setting is typically correct. While the NTAF standard allows for other names, changing names may confuse the providers that you are trying to communicate with. |
| Note | The default setting is typically correct. While the NTAF standard allows for other names, changing names may confuse the providers that you are trying to communicate with. |  |
| Do not try in‑band registration if login fails | --inband <value> | In‑band registration means that the NTAF server will register a new account for your username if it does not yet exist. If you check the box, then your username must exist on the NTAF server for you to log in. |
| Do not reconnect if connection is lost | --reconnect <value> | Check the box to not automatically retry XMPP connections if and when the connection with the server fails. |
| Open window showing XMPP packets | (none) | Check the box to open a window showing XMPP packets sent between iTest and the NTAF server. |
| Allow NTAF views to start sessions and send requests | (none) | Enable the menus in the NTAF Sessions view that start sessions and send requests. See Starting the NTAF Proxy service from the command line. |

Start the NTAF Proxy service and log it in as a client on the NTAF server

You launch the NTAF Proxy service to enable installed Spirent tools (Avalanche or Landslide) or other NTAF‑enabled tools to communicate with the NTAF server.

To support troubleshooting, the NTAF Proxy view displays information about each NTAF tool (NTAF provider) running on the local host. Details at NTAF Proxy view.



To launch the Proxy service and connect it to the NTAF server

1. On the NTAF Proxy view (Window > Show View > Other > NTAF > NTAF Proxy), click to connect to the server.

While it is not recommended, you have the option to start the NTAF Proxy using a command‑line interface. For details, see your IT admin and Starting the NTAF Proxy service from the command line.

> **Note:** Note Before using the NTAF proxy, perform these settings:

- If NTAF Proxy is not running on the same PC as iTest, on the PC that is used to run NTAF Proxy, set NTAF_PROXY_JAVA_HOME variable and this environment variable should point to JRE 32bit.

Example: NTAF_PROXY_JAVA_HOME=C:\Program Files (x86)\Java\jre1.8.0_181)

- If NTAF Proxy is running on the same host machine as iTest, install jre32bit and configure that NTAF_PROXY_JAVA_HOME variable.

> **Note:** Landslide TCL API (Replay Mode) requires 32-bit Java 8+ (1.8.0) and it is recommended to install Oracle Java JRE/JDK 1.8 32 bit from Oracle's Java Website http://www.java.com/.

1. 2

1. On the on the Login to NTAF Server dialog box, specify the following settings:

> **Tip:** Tip You can configure auto‑login and default settings for the Proxy service. See Setting preferences for NTAF sessions.
