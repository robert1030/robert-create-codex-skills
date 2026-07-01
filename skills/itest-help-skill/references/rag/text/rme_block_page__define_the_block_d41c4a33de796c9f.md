---
{
  "chunk_id": "rme_block_page__define_the_block_d41c4a33de796c9f",
  "source_file": "topics/rme_block_page.htm",
  "source_original_path": "topics/rme_block_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor Block page: Creating a block map"
  ],
  "heading_path": [
    "Response Map editor Block page: Creating a block map",
    "Response Map editor Block page: Creating a block map",
    "Define the block"
  ],
  "anchor": "1107058",
  "context_ids": [
    "rme_block_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_11.1.jpg",
    "topics/images/response_mapping_9.2.jpg"
  ],
  "content_hash": "d41c4a33de796c9f",
  "level": 2
}
---

# Response Map editor Block page: Creating a block map > Response Map editor Block page: Creating a block map > Define the block

First, we define the block that will map (return the required data from) any Vlan block of data in a response.

1. 1

1. In the Block Map editor, click Add Block to add a new block to the root node of the response map.

1. 2

1. In the Name box, type a name that represents the purpose of the block. For example, you might name the block vlan because it represents a block of data in the response that lists the configuration of a particular VLAN interface.

1. 3

1. In the Response view, select and copy one representative block of text. If the blocks are separated by blank lines, then include the blank line that appears after the text. In our example, we copy the following text:

Vlan1 is up, line protocol is down

Hardware is EtherSVI, address is 0012.d90e.eb40 (bia 0012.d90e.eb40)

MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,

reliability 255/255, txload 1/255, rxload 1/255

Encapsulation ARPA, loopback not set

ARP type: ARPA, ARP Timeout 04:00:00

1. 4

1. Paste the text into the Block contents box. iTest applies its built-in parsers (Word, Number, MAC Address, Timestamp, and so on) to color green the text that seems to be variable and to color black the text that seems to be static (words and punctuation). Each item of text in the response is now a token.

1. 5

1. Now we specify which tokens to ignore and which tokens to extract from any response, as follows:

- Tokens that should have names: Naming a token makes the value of the field available to be extracted from any response. (Analysis rules associated with test case steps return the value and then make the appropriate comparisons.) In our example, we’ll name the circled tokens.

- Tokens that will change from test to test, but that are also irrelevant to test case results: For example, the 04:00:00 token in the last line was correctly identified by the Time parser as a value that might change from test to test (depending on device configuration). However, the value of the ARP Timeout token is not important for the kinds of tests that you will run. You will specify that such tokens can take on any contents.

- Tokens that were incorrectly identified by iTest as not expected to change from test to test: For example, the ARP type value in the last line is ARPA — iTest identified ARPA as a static word, but, in tests, this field can take on different values. You will need to specify that you would like to return and work with the value of this token in test cases.

![screenshot](topics/images/response_mapping_11.1.jpg) <!-- image_chunk: img_15b40afa38388049 -->

![screenshot](topics/images/response_mapping_9.2.jpg) <!-- image_chunk: img_6e8939a503ba2f0a -->
