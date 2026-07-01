---
{
  "chunk_id": "wireshark_session_example__example_wireshark_session_d2b5350328974bf4",
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
    "Example Wireshark session"
  ],
  "anchor": "1268296",
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
  "content_hash": "d2b5350328974bf4",
  "level": 2
}
---

# Session profile property settings for Wireshark sessions > Session profile property settings for Wireshark sessions > Example Wireshark session

Start capture, then wait a short while before stopping capture. Capture uses the ‘capture filter’ and other advanced capture properties. When capture is stopped, “Loading...” appears while the temporary capture file is loaded into memory and “done” is appended after.

Wireshark>capture start

Capture started...

Capturing on Broadcom NetXtreme Gigabit Ethernet Driver (Microsoft's Packet Scheduler)

Wireshark>capture stop

Capture finished, 277 packets captured

Loading ... done

Total of 277 packets loaded

Wireshark>

// Show the first 10 packets, gives an overview of the main fields (without the packet details)

// Terminal uses a fixed width of 1000 characters, but this content is wrapped to fit on your screen. Here’s the actual content:

Wireshark>show packets -c 10

ID | Time | Source | Destination | Protocol | info

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1 | 0.000 | 10.155.0.59 | 10.155.0.145 | tcp | Transmission Control Protocol, Src Port: 1061 (1061), Dst Port: 3389 (3389), Seq: 0, Ack: 0, Len: 0

2 | 0.110 | 00:10:db:53:a8:51 | ff:ff:ff:ff:ff:ff | arp | Address Resolution Protocol (request)

3 | 0.111 | 00:10:db:53:a8:51 | ff:ff:ff:ff:ff:ff | arp | Address Resolution Protocol (request)

4 | 0.203 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 0, Ack: 0, Len: 32

5 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 32, Ack: 0, Len: 894

6 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 926, Ack: 0, Len: 512

7 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 1438, Ack: 0, Len: 247

8 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 1685, Ack: 0, Len: 192

9 | 0.494 | 10.155.0.59 | 10.155.0.145 | tcp | Transmission Control Protocol, Src Port: 1061 (1061), Dst Port: 3389 (3389), Seq: 0, Ack: 926, Len: 0

10 | 0.497 | 10.155.0.59 | 10.155.0.145 | tcp | Transmission Control Protocol, Src Port: 1061 (1061), Dst Port: 3389 (3389), Seq: 0, Ack: 1685, Len: 0

Wireshark>

// Now use capture run to capture 4 packets and wait for capture to finish (in this case 4 packets are captured but only 2 packets are loaded because of the read filter. Use filter set to clear the read filter and show all captured packets)

// The value 4 (in bold) changes from 0 to 4 while the packets are captured.

Wireshark>capture run -c 4

Capture started...

Capturing on Broadcom NetXtreme Gigabit Ethernet Driver (Microsoft's Packet Scheduler)

4

Capture finished, 4 packets captured

Loading ... done

Total of 2 packets loaded

Wireshark>filter set

Updating filter ... done

Total of 4 packets reloaded

Wireshark>

// Now start capture, optionally execute some other steps (which might generate some packets) and then wait for capture to complete.

Wireshark>capture start -c 200

Capture started...

Capturing on Broadcom NetXtreme Gigabit Ethernet Driver (Microsoft's Packet Scheduler)

Wireshark>

Wireshark>

Wireshark>capture wait

200

Capture finished, 200 packets captured

Loading ... done

Total of 200 packets loaded

Wireshark>
