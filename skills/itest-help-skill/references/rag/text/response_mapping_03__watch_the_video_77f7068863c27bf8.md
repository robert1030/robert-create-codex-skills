---
{
  "chunk_id": "response_mapping_03__watch_the_video_77f7068863c27bf8",
  "source_file": "topics/response_mapping.03.htm",
  "source_original_path": "topics/response_mapping.03.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Overview: Creating a response map"
  ],
  "heading_path": [
    "Overview: Creating a response map",
    "Overview: Creating a response map",
    "Watch the video"
  ],
  "anchor": "1155455",
  "context_ids": [],
  "index_keywords": [
    "automatic",
    "automatic response mapping",
    "limitations"
  ],
  "index_keyword_paths": [
    "automatic response mapping",
    "automatic response mapping > limitations",
    "response mapping > automatic"
  ],
  "related_links": [
    "tl1.1.htm#"
  ],
  "images": [],
  "content_hash": "77f7068863c27bf8",
  "level": 2
}
---

# Overview: Creating a response map > Overview: Creating a response map > Watch the video

Watch a short video to learn nearly everything you need to know to get started on the Spirent Knowledge Base



Step 1A: Get a sample response

A response map normally contains one or more samples of the responses that it is intended to map. Before you create a response map, find a good sample response to use while creating the map. The most common way to get a sample is to start with a test case containing a step that produces the type of response that you want to map. Select the step in the Test Case editor and the Response view displays the most recent response received while executing that step. You can also populate the Response view when you select a step in a Test Report or in the Capture view.



Step 1B: Optional: Filter the response if needed

The Response Filtering feature enables you to remove unwanted text from a response after a step has completed and before iTest applies analysis rules. The resulting portion of the response is cleaner to read, to understand, and to map. This feature is useful in the following situations:

- The response contains a lot of text, but it would be easier to analyze and display a portion of the response and to ignore the rest.

- The device produces logging messages that are mixed into the output (common for TL1). The messages appear as separate lines. You might want to analyze the messages in a different step, but you need to filter out the messages so that you can define a response map for the base response. (More information on working with TL1 responses appears in “TL1 Sessions”.)

- The device produces XML output, but the output includes non-XML headers and footers that mess up the XML (or HTML) mapping. Filtering can remove the headers and footers before you apply the queries.



Step 2: Choose a location for the response map

Before you actually create a response map, you should first think about where the map belongs in your workspace. In most cases, you will want to store the response map in a response map library that contains all maps for a particular device type. In special cases, you might want to create your own response map library that contains your own maps, but also inherits maps from another shared response map library. In other cases, you may want to store the response map along with the test case – in those cases where the response map is only useful in that one special case.



Step 3: Create the map

A response map is a file. The easiest (and recommended) way to create a new response map is to start from the Response view when it contains a good sample of the response. Click New Response Map to start the Response Map wizard. The wizard will populate the map based on information you provide.

If you have the Automatic Response Mapping feature installed, then you can also ask it to analyze the sample and try to automatically construct an appropriate map for you. When the wizard finishes, the new response map file will have been created, and will open in the Response Map editor so you can proceed with your work.
