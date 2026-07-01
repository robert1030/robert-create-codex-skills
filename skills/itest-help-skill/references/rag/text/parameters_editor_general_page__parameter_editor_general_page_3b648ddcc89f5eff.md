---
{
  "chunk_id": "parameters_editor_general_page__parameter_editor_general_page_3b648ddcc89f5eff",
  "source_file": "topics/parameters_editor_general_page.htm",
  "source_original_path": "topics/parameters_editor_general_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Pages on the Parameter editor",
    "Parameter editor: General page"
  ],
  "heading_path": [
    "Parameter editor: General page",
    "Parameter editor: General page"
  ],
  "anchor": "1331156",
  "context_ids": [
    "parameters_editor_general_page"
  ],
  "index_keywords": [
    "General page",
    "Parameter editor"
  ],
  "index_keyword_paths": [
    "General page > Parameter editor",
    "Parameter editor > General page"
  ],
  "related_links": [
    "preferences_spirent_velocity.htm#1261444"
  ],
  "images": [
    "topics/images/param_tags_paramter_files.png",
    "topics/images/param_test_execution_report_parameter_file_tag.png"
  ],
  "content_hash": "3b648ddcc89f5eff",
  "level": 1
}
---

# Parameter editor: General page > Parameter editor: General page

Use the General page to supply text that helps test case developers to understand how the parameter file is used. In addition, use Tags to identify and/or group parameter files.

| Headline | Optional. Type a one-line description that documents the usage and function of the parameter file. The text appears in the Favorites view to help you when selecting a parameter file. |
| --- | --- |
| Description | Optional. Type text that describes the parameter file to make its usage clear to coworkers. |
| Tags | A tag is a user-defined text string that provides a way to identify and/or group parameter files in the Workspace and attached to test cases, as required. You may select and use both Velocity tags and local tags when tagging native iTest assets, e.g., FFTC, FFTP. You may create, edit, and delete parameter file tags. Add a tag text as required and save the parameter file. You may also include existing tags to group parameter files. Note When creating a parameter file tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing tags. Tags listed in auto-completion suggestions contains both Velocity and local tags. iTest allows a maximum of 64 Tag names which you may add to a test case and parameter file. Tag name supports only 64 alpha-numeric (from the UTF8 character set), dash, and underscore characters without spaces. If you add a tag containing characters not compliant with these requirements or more than 64 tags, a warning message displays. If you enter more than 64 characters in the tag name, the value will be truncated and a message displays saying that only 64 characters are supported. If you add more than 64 tags, the additional tag will not be added and a message displays saying that only 64 tags may be added. Note If you already have tags which are not compliant with the above, a error displays asking you to fix this. You will not be allowed to save these tags until you make the tags compliant with the above requirements. However, you may still run the test case. Add a new tag as required and save the parameter file. The new tag will display in the Search list after you save the parameter file. Search When searching a test case or parameter file tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing tags to select. The Search Tag dialog displays tags from both iTest workspace and Velocity. If iTest resources have been uploaded to Velocity, then the list also displays tags added in Velocity. Note Velocity tags will not be listed when connection to Velocity is not configured (empty URL in Window > Preferences > Spirent > Velocity. See Preferences > Spirent > Velocity). Velocity updates its tag collection whenever iTest tagged resource is uploaded/published to Velocity. Velocity will not be aware of tags that are used by iTest resources that are not uploaded/published to Velocity Select tag(s) as required, click OK, and save the parameter file. Note Tags in-memory cache will reset when you restart iTest. Tags included will be embedded in the parameter FFTP file (see example below). |
| Note | When creating a parameter file tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing tags. Tags listed in auto-completion suggestions contains both Velocity and local tags. |
|  | iTest allows a maximum of 64 Tag names which you may add to a test case and parameter file. |
|  | Tag name supports only 64 alpha-numeric (from the UTF8 character set), dash, and underscore characters without spaces. |
|  | If you enter more than 64 characters in the tag name, the value will be truncated and a message displays saying that only 64 characters are supported. |
|  | If you add more than 64 tags, the additional tag will not be added and a message displays saying that only 64 tags may be added. |
| Note | If you already have tags which are not compliant with the above, a error displays asking you to fix this. You will not be allowed to save these tags until you make the tags compliant with the above requirements. However, you may still run the test case. |
| Note | Velocity tags will not be listed when connection to Velocity is not configured (empty URL in Window > Preferences > Spirent > Velocity. See Preferences > Spirent > Velocity). |
| Note | Tags in-memory cache will reset when you restart iTest. |

If a test case includes parameters from a Parameters File then its tags will be included in Test Report.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/param_tags_paramter_files.png) <!-- image_chunk: img_b8b67527434525d5 -->

![screenshot](topics/images/param_test_execution_report_parameter_file_tag.png) <!-- image_chunk: img_d0570fa2864534f1 -->
