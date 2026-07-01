---
{
  "chunk_id": "tgen_cmds_ixiatraffic__command_syntax_conventions_163d4f8b94bc3de3",
  "source_file": "topics/tgen_cmds_ixiatraffic.htm",
  "source_original_path": "topics/tgen_cmds_ixiatraffic.htm",
  "toc_path": [
    "iTest Online Help",
    "Syslog Sessions",
    "Syslog command set"
  ],
  "heading_path": [
    "Syslog command set",
    "Syslog command set",
    "Command reference",
    "Command syntax conventions"
  ],
  "anchor": "1185109",
  "context_ids": [
    "tgen_cmds_ixiatraffic"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1184509"
  ],
  "images": [],
  "content_hash": "163d4f8b94bc3de3",
  "level": 3
}
---

# Syslog command set > Syslog command set > Command reference > Command syntax conventions

| Convention | Description |
| --- | --- |
| boldface | Indicates commands and keywords that are entered literally as shown. |
| italics | Indicates arguments for which you supply values; in contexts that do not allow italics, arguments are enclosed in angle brackets (< >). |
| [x] | Keywords or arguments that appear within square brackets are optional. |
| {x | y | z} | A choice of required keywords (represented by x, y, and z) appears in braces separated by vertical bars. You must select one. |
| [x {y | z}] | Braces and vertical bars within square brackets indicate a required choice within an optional element. You do not need to select one. If you do, you have some required choices. |

You can use the following commands when defining steps in a test case:

| clear | Clear |
| --- | --- |
| exit | Exit, and then close the Syslog session |
| help [prefix] | Display all command syntax and descriptions Specify the prefix option to display the prefix for the message |
| show details messageID | For the ports specified as described in Specifying the ports to listen to: Display details about the message |
| show messages [all] | For the ports specified as described in Specifying the ports to listen to: Display a summary of messages received. Use the all option to display a list of all messages received. |
| wait [-timeout|-t seconds] [-host|-h host] [-facility|-f facility] [-severity|-s severity] [-tag|-g tag] | Specify the timeout |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
