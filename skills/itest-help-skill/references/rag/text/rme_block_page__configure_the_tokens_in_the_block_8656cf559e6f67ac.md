---
{
  "chunk_id": "rme_block_page__configure_the_tokens_in_the_block_8656cf559e6f67ac",
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
    "Configure the tokens in the block"
  ],
  "anchor": "1107079",
  "context_ids": [
    "rme_block_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "rme_block_properties.htm#1107149"
  ],
  "images": [
    "topics/images/response_mapping_6.3.jpg",
    "topics/images/response_mapping_5.4.jpg",
    "topics/images/response_mapping_4.5.jpg",
    "topics/images/response_mapping_3.6.jpg",
    "topics/images/response_mapping_3.7.jpg",
    "topics/images/response_mapping_3.8.jpg"
  ],
  "content_hash": "8656cf559e6f67ac",
  "level": 2
}
---

# Response Map editor Block page: Creating a block map > Response Map editor Block page: Creating a block map > Configure the tokens in the block

The first token that we’ll configure is the number that identifies the VLAN whose data is being displayed. We’ll name the token vlan_number.

1. Right-click the green 1 and select Set token > Name.

In the Token Name dialog box, type the name of the token and click OK.

Notice the following changes:

- The green 1 in both the Response view and the Block contents box is now enclosed in a blue box to indicate that it represents a token query that can return the value in this field from any response.

- The Queries view now displays one match with the vlan_number token query in line 0, column 4 of the sample response text. The value of the matching text is “1”.

- The Structure view now displays a match in the sample response text with the vlan_number token query and the value is “1”.

- The Issues view displays a mapping issue, but we can safely ignore issues while we’re putting the first configuration settings into place. More on this later.

1. 2

1. Now let us configure the token that holds the MAC address of the device. Based on the format of the text (0012.d90e.eb40), iTest has identified it as a MAC address. Your task is to name the token so that, in any test case step that submits the show interfaces command, iTest can return the MAC address for further analysis or processing. This time, we’ll use a shortcut and double-click the green text to open the Token Name dialog box. Type the name of the token (let us use device_mac_address). Click OK.

Again, iTest updates the views to reflect the new token query.

1. 3

1. The value that you see for reliability is 255/255. Notice that the two numbers are green to indicate that the parsers identified them as numbers (and therefore, likely to change from test to test). The slash character /, however, is black, indicating that it is a punctuation token and therefore unlikely to change its value from test to test. So it seems that our task is to configure two tokens. Let us call them the reliability_score and the reliability_basis.

> **Note:** Note Alternatively, you could select the full 255/255 text and name the token mask. Then, in the Advanced Matching Constraints section, check Match only on one of the following values and specify the value 255/255.

1. 4

1. iTest incorrectly identified ARPA in the last line as a static word. Now, let us configure it as the arp_type token because this field will take on different values that we want test case steps to return and analyze. Right-click the text and select Set token > Advanced token properties. The Token properties page opens. The name of the token appears in the Name box, and the token is correctly configured as Variable (the field can take other values that the ARPA text in the response sample). Now, in the Advanced Matching Constraints section, check Match only on one of the following values and then type each value that you expect in responses, as in this example:

1. 5

1. At this point, we have configured all of the named tokens in the response. The next step is to define the properties of the blocks in the response, as discussed in Response Map editor: Block Map properties.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/response_mapping_6.3.jpg) <!-- image_chunk: img_9664e08175f834b8 -->

![screenshot](topics/images/response_mapping_5.4.jpg) <!-- image_chunk: img_9b6721e86a1ed11c -->

![screenshot](topics/images/response_mapping_4.5.jpg) <!-- image_chunk: img_bac725e07d6fb51c -->

![screenshot](topics/images/response_mapping_3.6.jpg) <!-- image_chunk: img_32bb833c6e121429 -->

![screenshot](topics/images/response_mapping_3.7.jpg) <!-- image_chunk: img_0b5ace387a53d82d -->

![screenshot](topics/images/response_mapping_3.8.jpg) <!-- image_chunk: img_29492180f0462fde -->
