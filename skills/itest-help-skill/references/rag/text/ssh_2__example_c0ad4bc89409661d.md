---
{
  "chunk_id": "ssh_2__example_c0ad4bc89409661d",
  "source_file": "topics/ssh.2.htm",
  "source_original_path": "topics/ssh.2.htm",
  "toc_path": [
    "iTest Online Help",
    "SSH Sessions",
    "Using SSH Local Port Forwarding to connect iTest from your desktop through a firewall to your lab devices"
  ],
  "heading_path": [
    "Using SSH Local Port Forwarding to connect iTest from your desktop through a firewall to your lab devices",
    "Using SSH Local Port Forwarding to connect iTest from your desktop through a firewall to your lab devices",
    "Example"
  ],
  "anchor": "1230772",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/ssh.1.jpg",
    "topics/images/ssh.2.jpg",
    "topics/images/ssh.3.jpg"
  ],
  "content_hash": "c0ad4bc89409661d",
  "level": 2
}
---

# Using SSH Local Port Forwarding to connect iTest from your desktop through a firewall to your lab devices > Using SSH Local Port Forwarding to connect iTest from your desktop through a firewall to your lab devices > Example

Here is a typical situation: You want to use iTest from your desktop, but the lab is firewalled. In this example, we will set up a iTest session with a device in the lab (10.155.2.4) that uses both a Telnet interface and a Web interface. The table lists the ports that we have decided to use and will configure on the session profiles for both the SSH server and the Web device.

Step 1

Configure a session profile for the SSH server

1. Create a session profile for the SSH server. On the SSH properties page, specify the IP address of the SSH server (iTest can automatically assign an available port on the local host).

1. 2

1. On the More > Local port forwarding properties page, configure the SSH session with a port forwarding list:

Check the box to Enable local port forwarding.

Define a port for each device beyond the firewall that you will connect to. For each port forwarding pair, provide host and port information in the following format (one pair per line):

[localIPaddress:]localPort:remoteIPaddress_or_hostName:remotePort

Notice that localIPaddress: is optional.

Field substitutions are supported in any part of the text.

In our example, for the router at 10.155.2.4, we specify that traffic on port 2028 (from the SSH server that is communicating with iTest) should be forwarded to port 80 (typically HTTP traffic) on the router. We also specify that traffic on port 2027 should be forwarded to port 22 (Telnet)

Configure a session profile for each device behind the firewall

1. In our example, we create a session profile for the router with the Web interface.

1. 2

1. We specify the Base URL as the device’s IP address and the port number that it uses for Web traffic with the SSH server.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/ssh.1.jpg) <!-- image_chunk: img_b3d4bbae09ffda86 -->

![screenshot](topics/images/ssh.2.jpg) <!-- image_chunk: img_01a4c6d026603d07 -->

![screenshot](topics/images/ssh.3.jpg) <!-- image_chunk: img_e9b85990296a8c20 -->
