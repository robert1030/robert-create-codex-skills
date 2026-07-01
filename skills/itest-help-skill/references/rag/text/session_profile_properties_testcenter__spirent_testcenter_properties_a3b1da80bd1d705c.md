---
{
  "chunk_id": "session_profile_properties_testcenter__spirent_testcenter_properties_a3b1da80bd1d705c",
  "source_file": "topics/session_profile_properties_testcenter.htm",
  "source_original_path": "topics/session_profile_properties_testcenter.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session profiles",
    "Session profile property settings for Spirent TestCenter sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter sessions",
    "Session profile property settings for Spirent TestCenter sessions",
    "Spirent TestCenter properties"
  ],
  "anchor": "1317028",
  "context_ids": [
    "session_profile_properties_testcenter"
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
    "tgen_cmds_testcenter.htm#1332853"
  ],
  "images": [],
  "content_hash": "a3b1da80bd1d705c",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter sessions > Session profile property settings for Spirent TestCenter sessions > Spirent TestCenter properties

| Chassis IP | Specify the IPv4 address or DNS hostname of the device. Note If you do not specify a Chassis IP value, then you can use //chassis/slot/port notation in the Ports property to refer to ports on multiple chassis. | Note | If you do not specify a Chassis IP value, then you can use //chassis/slot/port notation in the Ports property to refer to ports on multiple chassis. |
| --- | --- | --- | --- |
| Note | If you do not specify a Chassis IP value, then you can use //chassis/slot/port notation in the Ports property to refer to ports on multiple chassis. |  |  |
| Ports | Specify a single port or list of ports for the session. See To specify a list of port locations. If no Configuration file is specified, then, when the session starts, one port is created for each location in the list. The ports are then connected to and reserved. Note iTest assigns ports in the listed order. For example, "1:9,1:8" assigns Port 9 first and "1:8,1:9" assigns port 8 first. If you are loading a configuration file and port order is important, you must specify ports in the same order as in the configuration file. Note In addition to supporting 10G, 40G, and 100G traffic and port settings, iTest supports you to view and configure 10G, 40G, 100G port settings in TestCenter.console. iTest also supports viewing and displaying of IEEE802.11 port type. | Note | iTest assigns ports in the listed order. For example, "1:9,1:8" assigns Port 9 first and "1:8,1:9" assigns port 8 first. If you are loading a configuration file and port order is important, you must specify ports in the same order as in the configuration file. |
| Note | iTest assigns ports in the listed order. For example, "1:9,1:8" assigns Port 9 first and "1:8,1:9" assigns port 8 first. If you are loading a configuration file and port order is important, you must specify ports in the same order as in the configuration file. |  |  |
| Note | In addition to supporting 10G, 40G, and 100G traffic and port settings, iTest supports you to view and configure 10G, 40G, 100G port settings in TestCenter.console. iTest also supports viewing and displaying of IEEE802.11 port type. |  |  |
| Configuration file | Optional: Specify the configuration file (either XML or tcc format file) to use to configure the device when the session starts. The path is limited to 256 characters. You can generate a configuration file using the TestCenter configuration save command. When the session starts: If no port locations are specified by the Ports property, ports in the configuration file with valid locations are connected to and reserved. Offline or inactive ports (Active attribute false) are ignored. If the Ports property specifies the same number of port locations as in the configuration file, the ports in the file are mapped to the listed locations in order. If the Ports property specifies fewer port locations than the file, then as many ports as possible are mapped to the listed locations. The mapping begins with the first port in the file and continues until the list is exhausted. All mapped ports are activated and then connected to and reserved. Any ports remaining in the file that have valid addresses and are active are also connected to and reserved. If the Ports property specifies more port locations than the file, then all ports in the file are mapped to listed locations. Mapping begins with the first listed location and continues until all ports in the file are exhausted. All mapped ports are activated. Any locations remaining in the list specified for the Ports property are used to create ports. All ports are connected to and reserved. |  | If no port locations are specified by the Ports property, ports in the configuration file with valid locations are connected to and reserved. Offline or inactive ports (Active attribute false) are ignored. |
|  | If no port locations are specified by the Ports property, ports in the configuration file with valid locations are connected to and reserved. Offline or inactive ports (Active attribute false) are ignored. |  |  |
|  | If the Ports property specifies the same number of port locations as in the configuration file, the ports in the file are mapped to the listed locations in order. |  |  |
|  | If the Ports property specifies fewer port locations than the file, then as many ports as possible are mapped to the listed locations. The mapping begins with the first port in the file and continues until the list is exhausted. All mapped ports are activated and then connected to and reserved. Any ports remaining in the file that have valid addresses and are active are also connected to and reserved. |  |  |
|  | If the Ports property specifies more port locations than the file, then all ports in the file are mapped to listed locations. Mapping begins with the first listed location and continues until all ports in the file are exhausted. All mapped ports are activated. Any locations remaining in the list specified for the Ports property are used to create ports. All ports are connected to and reserved. |  |  |
| Force taking port ownership | Upon connecting, take ownership so no other user can submit commands. |  |  |
