---
{
  "chunk_id": "itestrt_commands__velocity_integration_9106d8e1019ad294",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "Velocity integration"
  ],
  "anchor": "1269579",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "9106d8e1019ad294",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Velocity integration

To run a test case associated with a Velocity topology (using the ilo command to retrieve information about the active topology), specify the following parameters:

| ---iloLogin userName ---iloPassword password | Specify the username/password credentials to use to access the Velocity server |
| --- | --- |
| --iloServer URI /ilo | URI is the hostname or IP address of the Velocity virtual appliance. The URI is followed by “/velocity” Example --velocityServer http://velocity.acme.com/ilo |
| --reservationId reservationId | If there is more than one active reservation for the topology associated with the test case, then you must specify a value for the --reservationId option. When there is only one active reservation of the topology, then you do not need to specify a value for --reservationId |
