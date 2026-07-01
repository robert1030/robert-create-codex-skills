---
{
  "chunk_id": "properties_topo_editor_session_tab__session_tab_toolbar_e573904ad67f824f",
  "source_file": "topics/properties_topo_editor_session_tab.htm",
  "source_original_path": "topics/properties_topo_editor_session_tab.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "General Local Topology Operations",
    "Topology editor: Properties view, Session tab"
  ],
  "heading_path": [
    "Topology editor: Properties view, Session tab",
    "Topology editor: Properties view, Session tab",
    "Session tab toolbar"
  ],
  "anchor": "1276900",
  "context_ids": [
    "properties_topo_editor_session_tab"
  ],
  "index_keywords": [
    "Session tab",
    "sessions with topology devices",
    "starting from topology",
    "starting sessions"
  ],
  "index_keyword_paths": [
    "Properties page > Session tab",
    "Topology Properties page > Session tab",
    "Topology editor > Session tab",
    "sessions > starting from topology",
    "starting > sessions with topology devices",
    "topologies > starting sessions"
  ],
  "related_links": [
    "topo_add_session_profile_wizard.htm#1396646"
  ],
  "images": [
    "topics/images/topologies_6.1.jpg",
    "topics/images/topologies_3.5.jpg"
  ],
  "content_hash": "e573904ad67f824f",
  "level": 3
}
---

# Topology editor: Properties view, Session tab > Topology editor: Properties view, Session tab > Session tab toolbar

|  | Add a new session profile for the selected topology element. The Add Session Profile page takes you through the process. See Add, edit, or remove a session configuration for a iTest topology device. |
| --- | --- |
|  | Delete the selected session profile definition. (Use Ctrl-click or Shift-click to select multiple session profiles.) |
|  | Start the selected session in a new window. (Use Ctrl-click or Shift-click to select multiple session profiles.) |
|  | Open the Edit Session Profile page to view or edit property settings for the session profile. (Use Ctrl-click or Shift-click to select multiple session profiles.) |
|  | Common editing tools. Cut, Copy, Paste the selected device sessions within the current topology or to another topology. (Use Ctrl-click or Shift-click to select multiple session profiles.) |

> **Note:** Note When you use the Topology editor to define a session profile for a device, you cannot specify a value for the session profile Session name property.

| Name | Type the name for this particular set of session configuration settings. The name is used as the default session name when you create a test case from captured steps or add an open step to a test case. The name appears in the Session column for each step in the session |
| --- | --- |
| Type | The session type; Telnet, SSH, Web, SNMP, Spirent TestCenter, Serial, and so on. |
| Base session | The session profile that this device session inherits its property settings from |
| IP Address | The IP address or hostname for the device |
| Port | the port used to communicate with the device or software |
| User ID | Some session types require user authentication to start a session If required, you specified the User ID while configuring the device session profile. |
| Password | Some session types require user authentication to start a session If required, you specified the Password while configuring the device session profile. The text is masked here and in all locations in which it is used |
| URL | Web-based session types offer the option to specify the URL to use when starting a session You specify the URL while configuring the device session profile. The text is masked here and in all locations in which it is used. To use a literal IPv6 address in a URL: Disable field replacement (substitution) for the property. As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html |
|  | Disable field replacement (substitution) for the property. |
|  | As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/topologies_6.1.jpg) <!-- image_chunk: img_79030e45a9ca579f -->

![unknown](topics/images/topologies_3.5.jpg) <!-- image_chunk: img_3a633f151dd4104d -->
