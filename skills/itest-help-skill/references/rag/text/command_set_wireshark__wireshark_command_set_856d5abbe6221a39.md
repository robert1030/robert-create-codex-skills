---
{
  "chunk_id": "command_set_wireshark__wireshark_command_set_856d5abbe6221a39",
  "source_file": "topics/command_set_wireshark.htm",
  "source_original_path": "topics/command_set_wireshark.htm",
  "toc_path": [
    "iTest Online Help",
    "Wireshark sessions",
    "Wireshark command set"
  ],
  "heading_path": [
    "Wireshark command set",
    "Wireshark command set",
    "Wireshark command set"
  ],
  "anchor": "1174249",
  "context_ids": [
    "command_set_wireshark"
  ],
  "index_keywords": [
    "Wireshark sessions",
    "command set"
  ],
  "index_keyword_paths": [
    "Wireshark sessions > command set",
    "command reference > Wireshark sessions"
  ],
  "related_links": [
    "preferences_wireshark.htm#1205584",
    "wireshark_session_example.htm#1268296"
  ],
  "images": [],
  "content_hash": "856d5abbe6221a39",
  "level": 2
}
---

# Wireshark command set > Wireshark command set > Wireshark command set

| capture load {URI|path} -offest <count> | Load captured packets from a file using the Display filter. The Display filter is specified in the session profile. Use Ctrl-C (or an asynchronous break step) to cancel. When you cancel, load stops and some, but not all packets might have been loaded. optional argument -offest <count>: Allows you to load packets from a pcap file starting from the specified offset (in packets). For example if Maximum number of load packets option in Wireshark preferences is set to 2500 (Setting preferences for Wireshark sessions) and the capture load <file> -offset 10000 command is executed, then iTest will load packets with numbers 10000-12500 (a maximum of 2500 packets). |
| --- | --- |
| capture run [-c packet_count] | Start capturing packets using the Capture filter and wait for capture to finish. When capture has finished, the packets are loaded using the Read filter. Filters are specified in the session profile. Use Ctrl-C (or an asynchronous break step) to stop capture. Default: (If packet_count is not specified) there is no capture limit |
| capture save {URI|path} | Save captured packets to specified location (pcap file). Use Ctrl-C (or an asynchronous break step) to cancel. |
| capture start [-c packet_count] | Start capturing packets in the background. Capture using the Capture filter as specified in the session profile. The capture start command returns without waiting for capture to complete. If you do not specify the number of packets to capture, capture continues until stopped. Ctrl-C (or an asynchronous break step) does not cancel capture start. Default: (If packet_count is not specified) there is no capture limit Note When you execute capture start, the packets are not loaded (and therefore cannot be viewed) until after executing a capture stop command. |
| Note | When you execute capture start, the packets are not loaded (and therefore cannot be viewed) until after executing a capture stop command. |
| capture-filter set [filter] | Set the Capture filter controlling which packets will be captured. Use Ctrl-C (or an asynchronous break step) to cancel capture-filter set. Note The <filter> argument is mandatory in the capture-filter set command. |
| Note | The <filter> argument is mandatory in the capture-filter set command. |
| capture-filter reset | Reset the Capture filter to make sure that all packets are captured. |
| capture status | Show the capture status and packet count. After capture has been started, you can detect when capture has finished by using capture status. The capture status command also shows how many packets have been captured. iTest saves responses as structured data and generates appropriate queries for the status and count. |
| capture stop | Stop any capture that is in progress and load captured packets into memory using the Display filter (the default filter is specified in the session profile). |
| capture wait | Wait for capture to finish and then load the captured packets using the display filter. Use Ctrl-C (or an asynchronous break step) to stop capture. If you want to wait for capture to complete after it has been started, use capture wait. Alternatively, use capture run to both start capture and to wait for it to complete. The capture wait and run commands return a response equivalent to capture end. |
| capture statistics | The capture statistics command display only PCAP (Packet Capture) loaded through capture load command (and not through the query load command). Also the Show decode, Show packets, Show details, and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). Note When there are only 1 or 0 packets captured, the capture statistics command cannot display the Avg packets per sec and Avg bytes per sec because the capture duration cannot be measured. |
| Note | When there are only 1 or 0 packets captured, the capture statistics command cannot display the Avg packets per sec and Avg bytes per sec because the capture duration cannot be measured. |
| exit | Exit the application |
| filter reset | Reset the Display filter to the value specified in the session profile. Use Ctrl-C (or an asynchronous break step) to cancel. |
| filter set [filter] | Update the Display filter controlling which packets will be visible. If the optional filter is not specified, then all captured packets are loaded. Use Ctrl-C (or an asynchronous break step) to cancel. |
| help [prefix] | Display command help information |
| query load {URI|path} | Initializes the specified pcap file to be used by a subsequent query command. Uses the Query filter. Use Ctrl-C (or an asynchronous break step) to cancel. When you cancel, load stops, but some packets might have been loaded. Important Show decode, Show packets, Show details, and capture statistics commands will only work after loading a PCAP through capture load command (packets loaded with the query load command are ignored). |
| query decode [-s start_ID] [-c count] query details <ID> [<format>] query interfaces query packets [-s start_ID] [-c count] | Returns information from the pcap file that was initialized by a query load command. Important You must perform a query load command before performing any other query command. If [<format>] is pdml, output is displayed in pdml format If [<format>] is not provided, the output displays in the original/legacy table output. The query command works similarly to the show command. Because the query action minimizes memory consumption, it is preferred to show when the pcap file is too big to fit in memory. See show decode, show details, show interfaces, and show packets. Note The query command must use the Query filter (see query filter set and query filter reset). |
| Note | The query command must use the Query filter (see query filter set and query filter reset). |
| show decode [-s start_ID] [-c count] | Returns a list of “decoded” packets received during this session. The decoded packets provide the same values that you see when capturing packets or loading a capture file with tshark.exe or wireshark.exe without iTest. The structure of the response table is similar to the show packets command, as illustrated in Example Wireshark session. In the response table for show decode, the Wireshark Columns setting determines the response columns. Defaults: start_id=1, count=100 Note When you execute capture start, the packets are not loaded (and therefore are not viewable by show decode) until after executing a capture stop command. Show decode and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). Important Show decode and capture statistics commands will only work after loading a PCAP through capture load command (packets loaded with the query load command are ignored). |
| Note |  |
|  | When you execute capture start, the packets are not loaded (and therefore are not viewable by show decode) until after executing a capture stop command. |
|  | Show decode and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). |
| show details <ID> [<format>] | Returns the details of selected packet in the format specified. If [<format>] is pdml, output is displayed in pdml format If [<format>] is not provided, the output displays in the original/legacy table output. iTest saves responses as structured data and generates appropriate queries. Note When you execute capture start, the packets are not loaded (and therefore are not viewable by show details) until after executing a capture stop command. Show details and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). Important Show details and capture statistics commands will only work after loading a PCAP through capture load command (packets loaded with the query load command are ignored). |
| Note |  |
|  | When you execute capture start, the packets are not loaded (and therefore are not viewable by show details) until after executing a capture stop command. |
|  | Show details and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). |
| show interfaces | Returns the network interfaces. iTest saves responses as structured data and generates appropriate queries. |
| show packets [-s start_ID] [-c count] | Lists the packets received during this session. The structure of the response table is illustrated in Example Wireshark session. iTest saves responses as structured data and generates appropriate queries. Defaults: start_id=1, count=100 Note When you execute capture start, the packets are not loaded (and therefore are not viewable by show packets) until after executing a capture stop command. Show packets and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). Important Show packets and capture statistics commands will only work after loading a PCAP through capture load command (packets loaded with the query load command are ignored). |
| Note |  |
|  | When you execute capture start, the packets are not loaded (and therefore are not viewable by show packets) until after executing a capture stop command. |
|  | Show packets and capture statistics commands will display packets loaded with the last capture command (i.e., capture start-stop/run/load). |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
