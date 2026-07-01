---
{
  "chunk_id": "mapping_tl1__about_the_tl1_response_mapping_process_db3247f155eb9944",
  "source_file": "topics/mapping_tl1.htm",
  "source_original_path": "topics/mapping_tl1.htm",
  "toc_path": [
    "iTest Online Help",
    "TL1 Sessions",
    "Mapping TL1 responses"
  ],
  "heading_path": [
    "Mapping TL1 responses",
    "Mapping TL1 responses",
    "About the TL1 response mapping process"
  ],
  "anchor": "1153850",
  "context_ids": [
    "mapping_tl1"
  ],
  "index_keywords": [
    "TL1",
    "TL1 responses",
    "mapping responses"
  ],
  "index_keyword_paths": [
    "TL1 > mapping responses",
    "mapping > TL1 responses",
    "response mapping > TL1"
  ],
  "related_links": [],
  "images": [
    "topics/images/tl1.1.jpg",
    "topics/images/tl1.2.jpg",
    "topics/images/tl1.4.jpg",
    "topics/images/tl1.5.jpg"
  ],
  "content_hash": "db3247f155eb9944",
  "level": 2
}
---

# Mapping TL1 responses > Mapping TL1 responses > About the TL1 response mapping process

TL1 is a special “in-between” case. The session is typically Telnet, Serial, or SSH, but the response does have a well defined structure — it is just not XML. For this reason, a TL1 response map does not really need any configuration other than selecting TL1 on the Response Map editor's Overview page (there is no need to use table, pattern or block).

A TL1 response map is typically unnecessary because TL1 mapping happens automatically when you set the Terminal > Style property to TL1 for Telnet, Serial, or SSH devices or session profiles.

A typical TL1 response looks like this. Notice that almost everything “interesting” is mapped (enclosed in a blue box).

Also notice that many of the queries are keyed by sblk1param1 which is typically known as the AID (COT-ACU or COT-TSI3-B in this example).

Many TL1 responses follow the format in the example where each line is really a row in a table. The TL1 mapper checks whether the first parameter of the first sub-block is unique; if so, it assumes that queries should be keyed by this value. This is not always the case. In this example, the AID is not unique, so the queries (and therefore the blue boxes) are not really what you would hope for.

There are also other cases where the response may be fully “mapped”, but there are no blue boxes around items of interest. This does not mean that mapping failed. The solution for these cases is to create a “custom query only” response map. That is, a response map whose only purpose is to add or replace the queries that were generated automatically.

> **Note:** Note When creating a “custom query only” map, it is important to launch the New Response Map wizard by clicking the Add Response Map button on the Response view. If you create a new response map and add a sample (for example of an IxiaTraffic show stats response), you may not get the entire response (you will only get the “body” and not the “structure” and “queries”).

Notice that in the example, the Structure view has all of the interesting data from the response. In addition, the value for ASSEMBLY is selected in the Structure view and the corresponding text in the Response View is also selected.

In this example, queries may need to be keyed on both AID and EQUIPTYPE. Let us say you wanted to find the CLEICODE value for a particular AID if the AID was of type PON. The XPath expression would be:

“mapped/TL1/Response/Block[SubBlock[1]/Parameter[1] = 'LET-5-1' and SubBlock[3]/EQUIPTYPE = 'CARD']//CLEICODE”

> **Tip:** Tip Use the text box at the top of the Structure view to test XPath expressions.

By turning off the automatically-generated queries and adding a single custom query, you now have full control of where the blue boxes appear and which queries are available for use in analysis rules.

You can further customize the custom query by adding an argument:

This query would also work for LET-5-2, but only the one query/argument instance (based on the Default value property) is shown.

Finally, you may add a Values query, which is another XPath expression that finds all argument values and results in more queries shown in the Queries view and more blue boxes shown in the Response view. You use a values query only to test your query. The results of the test and verification appear in the Queries view. This is done by parsing values from the values query to your actual query.

The values query for this example is:

“mapped/TL1/Response/Block[SubBlock[3]/EQUIPTYPE = 'CARD']/SubBlock[1]/Parameter[1]”

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/tl1.1.jpg) <!-- image_chunk: img_cdc79c76138c838e -->

![screenshot](topics/images/tl1.2.jpg) <!-- image_chunk: img_f2f9c76d8331b008 -->

![screenshot](topics/images/tl1.4.jpg) <!-- image_chunk: img_46904689d8704e6b -->

![screenshot](topics/images/tl1.5.jpg) <!-- image_chunk: img_0db1137f0cc2b5bc -->
