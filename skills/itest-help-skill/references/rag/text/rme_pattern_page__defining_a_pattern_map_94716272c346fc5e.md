---
{
  "chunk_id": "rme_pattern_page__defining_a_pattern_map_94716272c346fc5e",
  "source_file": "topics/rme_pattern_page.htm",
  "source_original_path": "topics/rme_pattern_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Pattern page"
  ],
  "heading_path": [
    "Response Map editor: Pattern page",
    "Response Map editor: Pattern page",
    "Defining a Pattern map"
  ],
  "anchor": "1123279",
  "context_ids": [
    "rme_pattern_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_5.2.jpg",
    "topics/images/response_mapping_3.3.jpg"
  ],
  "content_hash": "94716272c346fc5e",
  "level": 2
}
---

# Response Map editor: Pattern page > Response Map editor: Pattern page > Defining a Pattern map

1. Click Add to add a new pattern match definition.

1. 2

1. In the Name box, type a name that represents the values that the pattern will extract. For example, you might name a pattern image_and_database because you can extract both the image text-base and the database from the line (see the example in Step 4).

1. 3

1. In the Response view, select a fragment of the response that contains only enough text to define the context for the information that you want to extract. Sometimes, to ensure that the text is the unique way to find the value, you will need to include text from the line before or after, or even several lines. There are two options for providing the pattern that includes the matches:

1. 4

1. In the sidebar, click Add Pattern. iTest pastes the selected lines into the Identifying Text box.

Alternatively, Copy the text and paste the text into the Identifying Text box.

iTest immediately attempts to identify values that you want to extract. iTest draws a blue box around each group of interest (numbers, timestamps, IP addresses, and other types of response value that you might typically want to analyze). If you modify the text, iTest immediately updates the groups.(To disable auto-update, uncheck Automatically update definitions to maintain consistency with the text in the Identifying Text box.)

At this point, you have identified one or more tokens (in blue boxes) and queries that extract the token values. The groups of text between the tokens are anchors. Anchors function to locate the tokens whose values you want to extract. By default, iTest creates default names for tokens by using the anchor text. In the example, iTest names the 0x00003000 token Image_text_base and the 0x00C7FC04 token data_base. Depending on the order of the text, iTest might use the text that occurs after a token to form its “best guess” name.

1. 5

1. If iTest does not specify a token correctly or misses a value that you want to extract, then select the actual value that you want to extract and click Make Token. Other controls:

| Clear Tokens | If iTest has identified a token that you are not interested in: Click anywhere in the token text. Click Clear Tokens to change the text into an anchor group. |
| --- | --- |
| Reset | Click Reset to revert the Token definitions to the initial settings suggested by iTest. Reset is useful when you have made changes to token definitions that you do not want to save, |

1. 6

1. Optional. Check Generate an error if no matches are found to specify that an error should be generated when the token does not appear in the response. Errors appear in the Execution view, in the Step Issues view, and in test reports.

1. 7

1. In the Identifying Text box, select a named token. In the Match with box, iTest suggests a regular expression that matches the selection and could extract the value. The associated actual regular expression appears in the Regular Expression box. From the Match with box, select the regular expression that best matches the field. In our example, we realize that the values will always be hex numbers, so we can safely select HexNumber.

1. 8

1. You can modify the regex in the Expression box as needed.

![screenshot](topics/images/response_mapping_5.2.jpg) <!-- image_chunk: img_957dab548521e7b9 -->

![screenshot](topics/images/response_mapping_3.3.jpg) <!-- image_chunk: img_31c647abbd326d35 -->
