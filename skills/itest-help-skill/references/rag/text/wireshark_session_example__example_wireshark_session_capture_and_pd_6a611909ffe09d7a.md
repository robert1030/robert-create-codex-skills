---
{
  "chunk_id": "wireshark_session_example__example_wireshark_session_capture_and_pd_6a611909ffe09d7a",
  "source_file": "topics/wireshark_session_example.htm",
  "source_original_path": "topics/wireshark_session_example.htm",
  "toc_path": [
    "iTest Online Help",
    "Wireshark sessions",
    "Session profile property settings for Wireshark sessions"
  ],
  "heading_path": [
    "Session profile property settings for Wireshark sessions",
    "Session profile property settings for Wireshark sessions",
    "Example Wireshark session",
    "Example: Wireshark session capture and PDML output"
  ],
  "anchor": "1276998",
  "context_ids": [
    "sp_properties_wireshark",
    "wireshark_session_example"
  ],
  "index_keywords": [
    "Wireshark session",
    "Wireshark sessions",
    "defining",
    "example"
  ],
  "index_keyword_paths": [
    "Wireshark sessions > defining",
    "Wireshark sessions > example",
    "defining > Wireshark sessions",
    "examples > Wireshark session"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "6a611909ffe09d7a",
  "level": 3
}
---

# Session profile property settings for Wireshark sessions > Session profile property settings for Wireshark sessions > Example Wireshark session > Example: Wireshark session capture and PDML output

1. Capture two network packets in Wireshark session

capture run -c 2

1. 2

1. Wireshark session output:

Wireshark>capture run -c 2

Capture started on the default interface using C:\Program Files\Wireshark\tshark.exe...

2

Capture finished, 2 packets captured

Loading ... done

Total of 2 packets loaded

1. 3

1. Use the show details command to display the first packet in pdml format

show details 1 pdml

Wireshark session output:

Wireshark>show details 1 pdml

<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<?xml-stylesheet type="text/xsl" href="pdml2html.xsl"?>

<!-- You can find pdml2html.xsl in C:\Program Files\Wireshark or at https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=pdml2html.xsl. -->

<pdml capture_file="C:\Users\Acme\AppData\Local\Temp\itestwireshark4053926233962652687.pcap" creator="wireshark/2.6.8" time="Fri May 17 18:13:35 2019" version="0">

<packet>

<proto name="geninfo" pos="0" showname="General information" size="82">

<field name="num" pos="0" show="1" showname="Number" size="82" value="1"/>

<field name="len" pos="0" show="82" showname="Frame Length" size="82" value="52"/>

<field name="caplen" pos="0" show="82" showname="Captured Length" size="82" value="52"/>

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
