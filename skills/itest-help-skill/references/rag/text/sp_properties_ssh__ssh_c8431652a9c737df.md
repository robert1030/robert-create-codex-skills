---
{
  "chunk_id": "sp_properties_ssh__ssh_c8431652a9c737df",
  "source_file": "topics/sp_properties_ssh.htm",
  "source_original_path": "topics/sp_properties_ssh.htm",
  "toc_path": [
    "iTest Online Help",
    "SSH Sessions",
    "Session profile property settings for SSH sessions"
  ],
  "heading_path": [
    "Session profile property settings for SSH sessions",
    "Session profile property settings for SSH sessions",
    "SSH"
  ],
  "anchor": "1255911",
  "context_ids": [
    "sp_properties_ssh"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions",
    "configuring",
    "session profile property settings for"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions > configuring",
    "SSH sessions > session profile property settings for",
    "configuring > SSH sessions",
    "session profile property settings > SSH sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "c8431652a9c737df",
  "level": 2
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > SSH

| IP address | Required. Specify the IP address or hostname for the session with the remote host. To use IPv6 with a session, use the following syntax: Without substitution: [<IPv6>] With substitution: ['\[']::<IPv6>['\]'] Python: eval IPv6="http://[::1]:8080/dashboard/" TCL: eval set IPv6 "http://\[::1\]:8080/dashboard/" |  | Without substitution: [<IPv6>] |  | With substitution: ['\[']::<IPv6>['\]'] |
| --- | --- | --- | --- | --- | --- |
|  | Without substitution: [<IPv6>] |  |  |  |  |
|  | With substitution: ['\[']::<IPv6>['\]'] |  |  |  |  |
| Port | Required. Specify the port for the session (number between 1 and 65535). Default: 22 |  |  |  |  |
| User and Password | Required. Specify the user name and password used to connect to the remote host. |  |  |  |  |
| SSH version | Required. Specify the SSH version. You must further specify authentication settings on the SSH authentication property pages. Default: Auto Auto: When iTest connects to the SSH server, they negotiate to determine the SSH version that they both support SSHv1: SSH Version 1 (not recommended) SSHv2: SSH Version 2 |  |  |  |  |
