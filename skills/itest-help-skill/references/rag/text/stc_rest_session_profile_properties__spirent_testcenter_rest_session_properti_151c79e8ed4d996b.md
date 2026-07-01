---
{
  "chunk_id": "stc_rest_session_profile_properties__spirent_testcenter_rest_session_properti_151c79e8ed4d996b",
  "source_file": "topics/stc_rest_session_profile_properties.htm",
  "source_original_path": "topics/stc_rest_session_profile_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session profiles",
    "Session profile property settings for Spirent TestCenter REST sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter REST sessions",
    "Session profile property settings for Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session properties"
  ],
  "anchor": "1317028",
  "context_ids": [
    "stc_rest_session_profile_properties"
  ],
  "index_keywords": [
    "Spirent TestCenter GUI sessions",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Spirent TestCenter GUI > session profile property settings",
    "session profile property settings > Spirent TestCenter GUI sessions"
  ],
  "related_links": [
    "#1317009",
    "tgen_cmds_testcenter.htm#1332853"
  ],
  "images": [
    "topics/images/stc_rest_itestSession.png"
  ],
  "content_hash": "151c79e8ed4d996b",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter REST sessions > Session profile property settings for Spirent TestCenter REST sessions > Spirent TestCenter REST session properties

| STC URL | (Mandatory): Enter the correct STC Lab server URL (e.g: http://192.168.51.64/stcapi/) or the stcweb app URL. (http://localhost:8888/stcapi). |
| --- | --- |
| Create or Replace session on connect | When checked: Creates a new session on STC lab server and replaces an existing session, if any. A message displays if the session already exists. when unchecked: Use the currently running LabServer session for the iTest STC REST session If no session is currently running, an error message displays. Note Works in conjunction with the Terminate session on disconnect setting. |
|  | When checked: Creates a new session on STC lab server and replaces an existing session, if any. |
|  | when unchecked: Use the currently running LabServer session for the iTest STC REST session |
| Note | Works in conjunction with the Terminate session on |
| Terminate session on disconnect | If checked, then end the LabServer session when iTest disconnects from LabServer. If unchecked, then do not end the LabServer session. Works in conjunction with the Create new session on connect setting. |
| Session name | Session name must be unique as it is used to create session name in the STC Lab server. Note If the Session name and Owner ID are not unique, that is, if the session name already exists, the session will fail when iTest tries to create a session. The iTest STC REST session profile maps the Owner ID and Session name to the STC Lab Manager to create a new Test Session as follows. Owner ID is mapped to the User Name in STC Lab Manager Session name is mapped to the Test Map in STC Lab Manager |
|  | Owner ID is mapped to the User Name in STC Lab Manager |
|  | Session name is mapped to the Test Map in STC Lab Manager |
| Owner ID | Owner ID must be unique and is associated with the User Name in STC Lab server. See also the “Note” above. |
| Chassis IP | Specify the IPv4 address or DNS hostname of the device. Note If you do not specify a Chassis IP value, then you can use //chassis/slot/port notation in the Ports property to refer to ports on multiple chassis. |
| Note | If you do not specify a Chassis IP value, then you can use //chassis/slot/port notation in the Ports property to refer to ports on multiple chassis. |
| Ports | Specify a single port or list of ports for the session. See To specify a list of port locations. If no Configuration file is specified, then, when the session starts, one port is created for each location in the list. The ports are then connected to and reserved. Note iTest assigns ports in the listed order. For example, "1:9,1:8" assigns Port 9 first and "1:8,1:9" assigns port 8 first. If you are loading a configuration file and port order is important, you must specify ports in the same order as in the configuration file. Note In addition to supporting 10G, 40G, and 100G traffic and port settings, iTest supports you to view and configure 10G, 40G, 100G port settings in TestCenter.console. iTest also supports viewing and displaying of IEEE802.11 port type. |
| Note | iTest assigns ports in the listed order. For example, "1:9,1:8" assigns Port 9 first and "1:8,1:9" assigns port 8 first. If you are loading a configuration file and port order is important, you must specify ports in the same order as in the configuration file. |
| Note | In addition to supporting 10G, 40G, and 100G traffic and port settings, iTest supports you to view and configure 10G, 40G, 100G port settings in TestCenter.console. iTest also supports viewing and displaying of IEEE802.11 port type. |
| Configuration file | Optional: Specify the configuration file (either XML or tcc format file) to use to configure the device when the session starts. The path is limited to 256 characters. You can generate a configuration file using the TestCenter configuration save command. When the session starts: If no port locations are specified by the Ports property, ports in the configuration file with valid locations are connected to and reserved. Offline or inactive ports (Active attribute false) are ignored. If the Ports property specifies the same number of port locations as in the configuration file, the ports in the file are mapped to the listed locations in order. If the Ports property specifies fewer port locations than the file, then as many ports as possible are mapped to the listed locations. The mapping begins with the first port in the file and continues until the list is exhausted. All mapped ports are activated and then connected to and reserved. Any ports remaining in the file that have valid addresses and are active are also connected to and reserved. If the Ports property specifies more port locations than the file, then all ports in the file are mapped to listed locations. Mapping begins with the first listed location and continues until all ports in the file are exhausted. All mapped ports are activated. Any locations remaining in the list specified for the Ports property are used to create ports. All ports are connected to and reserved. |
|  | If no port locations are specified by the Ports property, ports in the configuration file with valid locations are connected to and reserved. Offline or inactive ports (Active attribute false) are ignored. |
|  | If the Ports property specifies the same number of port locations as in the configuration file, the ports in the file are mapped to the listed locations in order. |
|  | If the Ports property specifies fewer port locations than the file, then as many ports as possible are mapped to the listed locations. The mapping begins with the first port in the file and continues until the list is exhausted. All mapped ports are activated and then connected to and reserved. Any ports remaining in the file that have valid addresses and are active are also connected to and reserved. |
|  | If the Ports property specifies more port locations than the file, then all ports in the file are mapped to listed locations. Mapping begins with the first listed location and continues until all ports in the file are exhausted. All mapped ports are activated. Any locations remaining in the list specified for the Ports property are used to create ports. All ports are connected to and reserved. |
| Command Set | (Mandatory) Select the STC command set to be used from the list. The selected version of iTest STC session commands will be loaded when the session starts or a testcase runs. |
| Force taking port ownership | Upon connecting, take ownership so no other user can submit commands. |
| Connect to port when session starts | When selected, the session connects to the port automatically when the session starts. |
| Subscribe to results from configuration file | When selected, you receive a notification of the results of running the configuration file. See Configuration file above. |
| Verify port status before reserve | If selected, iTest will check port status before reserving the ports. If the ports are unavailable, an error displays. |

![screenshot](topics/images/stc_rest_itestSession.png) <!-- image_chunk: img_69810fcc5801bd1e -->
