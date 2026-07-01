---
{
  "chunk_id": "rme_applicability_page__response_map_editor_applicability_page_496bf0cc075a25e1",
  "source_file": "topics/rme_applicability_page.htm",
  "source_original_path": "topics/rme_applicability_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Applicability page"
  ],
  "heading_path": [
    "Response Map editor: Applicability page",
    "Response Map editor: Applicability page"
  ],
  "anchor": "1106102",
  "context_ids": [
    "rme_applicability_page"
  ],
  "index_keywords": [
    "Applicability page",
    "Response Map editor",
    "specifying when to use"
  ],
  "index_keyword_paths": [
    "Applicability page > Response Map editor",
    "Response Map editor > Applicability page",
    "response maps > specifying when to use"
  ],
  "related_links": [],
  "images": [
    "topics/images/rme_applicability_page.png"
  ],
  "content_hash": "496bf0cc075a25e1",
  "level": 1
}
---

# Response Map editor: Applicability page > Response Map editor: Applicability page

Use the Applicability page to specify when to use the current response map to search for matches in a response. For example, you can specify that the response map should be applied to the response whenever a step in a Telnet or SSH session uses a command that includes the text show interfaces*. As a result, iTest applies the response map whenever any of the following commands is executed in a Telnet or SSH session: show interfaces all, show interfaces 2, or show interfaces 2-7.

Here is why you might want to take advantage of this powerful feature: Once you have set the applicability properties and associated the response map with the session profile used in the test cases, you no longer need to explicitly specify this response map for each test case step that should use it. Instead, whenever a test case executes and the applicability conditions are met (for example, a show interfaces all command is issued in an SSH session), then iTest applies this response map (and possibly other applicable maps, in priority order) to the response to extract the data for post-process analysis.

You may also filter the applicable response map list as follows. Add one or more options and filter the list of applicable response maps.

| Session Types | Select one or more session types to filter on session type |
| --- | --- |
| Action | Each session type supports different actions: Use this field to filter on action, e.g, snapshot. |
| Target | Some sessions support targets (e.g. Selenium. See Selenium sessions), this field can be used to filter on a target. |
| Command | This is the most commonly used filter. Use to filter on a particular command. Note You may use wild card characters. For example, a command filter sh* ver* will filter applicable commands: show version and sh version |
| Note | You may use wild card characters. For example, a command filter sh* ver* will filter applicable commands: show version and sh version |

> **Caution:** CAUTION If you do not specify applicability settings for a response map, or move the response map out of a response map library (not recommended), then the map will be used only if it is explicitly specified in the test case.

![screenshot](topics/images/rme_applicability_page.png) <!-- image_chunk: img_149f1d6488ea64b4 -->
