---
{
  "chunk_id": "field_replacements_2__property_inheritance_0918d36835e45316",
  "source_file": "topics/field_replacements.2.htm",
  "source_original_path": "topics/field_replacements.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Where you can use field replacements"
  ],
  "heading_path": [
    "Where you can use field replacements",
    "Where you can use field replacements",
    "Enabling and disabling runtime substitution of field replacements",
    "Property inheritance"
  ],
  "anchor": "1146029",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "inheritance_property.htm#1128847"
  ],
  "images": [
    "topics/images/field_replacements.12.jpg"
  ],
  "content_hash": "0918d36835e45316",
  "level": 3
}
---

# Where you can use field replacements > Where you can use field replacements > Enabling and disabling runtime substitution of field replacements > Property inheritance

For a property that inherits its value, you must turn off inheritance before changing the substitution/no substitution setting (because the setting is also inherited).

In this example, we want to change the Connect timeout value from its inherited value of 30 to a param command whose value is determined at runtime (as a result, depending on a parameter value, the test case can wait 45 seconds to connect to DeviceA and 120 seconds to connect to DeviceB, for example).

Before we can change the (do not substitute) setting to the (substitute) setting, we must first click the inheritance button to turn off inheritance. (For more information on how properties inherit their settings, see Property values: Inheriting settings.)

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/field_replacements.12.jpg) <!-- image_chunk: img_f26508c540b44bba -->
