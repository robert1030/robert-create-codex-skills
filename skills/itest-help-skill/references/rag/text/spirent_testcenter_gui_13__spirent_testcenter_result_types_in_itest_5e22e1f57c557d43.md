---
{
  "chunk_id": "spirent_testcenter_gui_13__spirent_testcenter_result_types_in_itest_5e22e1f57c557d43",
  "source_file": "topics/spirent_testcenter_gui.13.htm",
  "source_original_path": "topics/spirent_testcenter_gui.13.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "CLI integration commands"
  ],
  "heading_path": [
    "CLI integration commands",
    "CLI integration commands",
    "Spirent TestCenter result types in iTest"
  ],
  "anchor": "1504792",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tgen_cmds_testcenter.htm#1371413"
  ],
  "images": [],
  "content_hash": "5e22e1f57c557d43",
  "level": 2
}
---

# CLI integration commands > CLI integration commands > Spirent TestCenter result types in iTest

This table correlates TestCenter data items with the responses to TestCenter commands in iTest.

iTest saves all responses to commands as structured data. In addition, iTest auto-generates appropriate queries, so you can easily work with or apply analysis rules to the values of interest in the response

| UI grouping/location | iTest result type |
| --- | --- |
| Port Traffic | Basic Traffic Results |
| Diffserv Results | DiffServResults |
| Port Average Latency Results | PortAvgLatencyResults |
| Overflow Results | OverflowResults |
| Port Pair Results | Tx/RxPortPairResults |
| CPU Port Results | Tx/RxCpuPortResults |
| Stream Results | Traffic Group Results |
| Filtered Stream Results | FilteredStreamResults |
| Detailed Stream Results | TxStreamResults, RxStreamSummaryResults |
| Stream Block Results | Tx/RxStreamBlockResults |
| Port Protocols | SONET Interface Results |
| POS Interface Results | PppProtocolResults |
| ARPND Results | ArpNdResults |
| LACP Results | LacpPortResults |
| L2TP Results Not supported in iTest 3.1 | L2tpPortResults |
| PPPoX Results | PPPoEPortResults |
| DHCP Results | Dhcpv4PortResults |
| DHCPv6 Results | Dhcpv6PortResults |
| IGMP Results | IgmpPortResults |
| MLD Results | MldPortResults |
| EOAM Results | EoamPortResults |
| Router Protocols | BGP Results |
| OSPFv2 Results | Ospfv2Results |
| OSPFv3 Results | Ospfv3Results |
| ISIS Results | IsisRouterResults |
| RIP Results | RipRouterResults |
| LDP Results | LdpRouterResults |
| RSVP Results | RsvpRouterResults |
| PIM Results | PimRouterResults |
| IGMP Querier Results | IgmpRouterResults |
| MLD Querier Results | MldRouterResults |
| STP Results | BridgePortResults |
| MSTI Results | BridgePortResults |
| LDP-RSVP LSP Results | LDP LSP Results |
| RSVP LSP Results | RsvpLspResults |
| EOAM Results | Port Results Not supported in iTest 3.1 |
| MEG Results Not supported in iTest 3.1 | EoamMegResults |
| CC Results Not supported in iTest 3.1 | EoamContChkLocalResults |
| LB Results Not supported in iTest 3.1 | EoamLoopbackResults |
| LT Results Not supported in iTest 3.1 | EoamLinkTraceResults |
| Host Protocols | DHCP Results |
| PPPoX Results | PPP/PPPoeClientBlockResults, PPP/PPPoeServerBlockResults Not supported in iTest 3.1 |
| DHCPv6PD Results | Dhcpv6BlockResults |
| L2TP Results | L2TPv2BlockResults Not supported in iTest 3.1 |
| IGMP Results | IgmpHostResults |
| MLD Results | MldHostResults |
| IGMP-MLD Group Results | IGMP Host-Group Results |
| MLD Host-Group Results | MldGroupMembershipResults |
| SIP Results Not supported in iTest 3.1 | SipUaBlockResults |
| IPTV | Test Results |
| Port Results | IptvPortResults |
| STB Block Results | IptvStbBlockResults |
| Viewing Profile Results | IptvViewingProfileResults |
| Channel Results | IptvChannelResults |

Capture actions and analyze data

The following sections provide overviews for common testing situations. You perform all actions (except getting data) the same way as in TestCenter.

Descriptions for the actions appear in Spirent TestCenter Command reference.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
