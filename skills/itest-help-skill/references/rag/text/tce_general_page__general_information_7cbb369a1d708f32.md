---
{
  "chunk_id": "tce_general_page__general_information_7cbb369a1d708f32",
  "source_file": "topics/tce_general_page.htm",
  "source_original_path": "topics/tce_general_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "General page on the Test Case Editor",
    "Test Case editor: General page"
  ],
  "heading_path": [
    "Test Case editor: General page",
    "Test Case editor: General page",
    "General Information"
  ],
  "anchor": "1713712",
  "context_ids": [
    "tce_general_page"
  ],
  "index_keywords": [
    "General page",
    "Test Case editor",
    "messaging out",
    "run command responses",
    "specifying",
    "summary reports",
    "summary responses",
    "test suites"
  ],
  "index_keyword_paths": [
    "General page > Test Case editor",
    "Test Case editor > General page",
    "comments > messaging out",
    "run command responses",
    "summary reports",
    "summary responses",
    "test suites",
    "testbeds > specifying"
  ],
  "related_links": [
    "preferences_spirent_velocity.htm#1261444"
  ],
  "images": [
    "topics/images/test_case_editor_general_store_encrypted.png",
    "topics/images/test_case_editor_general_tags_create.png",
    "topics/images/test_case_editor_general_tags_embedded.png"
  ],
  "content_hash": "7cbb369a1d708f32",
  "level": 2
}
---

# Test Case editor: General page > Test Case editor: General page > General Information

The text that you supply in the General Information section appears in:

- The Summary section in the structured data for run and summarize steps

- A column in the Child Test Cases table for responses to summarize steps

- Test report Summary section in the Test Report editor and in exported test reports.

| Headline | Optional. Type a one-line description that documents the usage and function of the test case. In addition to the locations mentioned earlier, this text also appears in the Favorites view to help you when selecting a test case. |
| --- | --- |
| Owner | Optional. Type the unique identifier of the person responsible for developing and/or maintaining the test case (typically, the name, login name, or email address),. |
| Description | Optional. Type additional text that describes the test case to make its usage clear to coworkers. iTest provides a way to encrypt this data and prevent it from being visible outside iTest GUI. See Store encrypted description below. Tip This is an excellent place to paste a copy of the test plan. |
| Tip | This is an excellent place to paste a copy of the test plan. |
| Store encrypted description | Optional. Select Sore encrypted description to mask the notes. iTest encrypts any information stored in the description field of the test case files so it cannot be read outside iTest GUI (this allows you to store test case files on a public GitHub repository). iTest GUI will always show the description in clear text, whether encrypted or not. Note Velocity Core recognizes all uploaded encrypted files and will decrypt the file contents and store it in the test case metadata. |
| Note | Velocity Core recognizes all uploaded encrypted files and will decrypt the file contents and store it in the test case metadata. |
| Tags | A tag is a user-defined text string that provides a way to identify and/or group test cases in the Workspace and project space, as required. You may select and use both Velocity tags and local tags when tagging native iTest assets, e.g., FFTC, FFTP. You may create, edit, and delete test case tags. Add a tag text as required and save the test case. You may also include existing tags to group test cases together. Note When creating a test case tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing tags. Tags listed in auto-completion suggestions contains both Velocity and local tags. iTest allows a maximum of 64 Tag names which you may add to a test case and parameter file. Tag name supports only 64 alpha-numeric (from the UTF8 character set), dash, and underscore characters without space. If you add a tag containing characters not compliant with these requirements or more than 64 tags, a warning message displays. If you enter more than 64 characters in the tag name, the value will be truncated and a message displays saying that only 64 characters are supported. If you add more than 64 tags, the additional tag will not be added and a message displays saying that only 64 tags may be added. Note If you already have tags which are not compliant with the above, a error displays asking you to fix this. You will not be allowed to save these tags until you make the tags compliant with the above requirements. However, you may still run the test case. Add a new tag as required and save the test case. The new tag will be displayed in the Search list after you save the test case. Search Click Search to display the Search Tags dialog. When searching a test case or parameter file tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of tags to select. The Search Tags dialog lists tags from both iTest workspace and Velocity. If iTest resources have been uploaded to Velocity, then the list also displays tags added in Velocity. Note Velocity tags will not be listed when connection to Velocity is not configured (empty URL in Window > Preferences > Spirent > Velocity. See Preferences > Spirent > Velocity). Velocity updates its tag collection whenever iTest tagged resource is uploaded/published to Velocity. Velocity will not be aware of tags that are used by iTest resources that are not uploaded/published to Velocity Select tag(s) as required, click OK, and save the test case. Note Tags in-memory cache will reset when you restart iTest. |
| Note | When creating a test case tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing tags. Tags listed in auto-completion suggestions contains both Velocity and local tags. |
|  | iTest allows a maximum of 64 Tag names which you may add to a test case and parameter file. |
|  | Tag name supports only 64 alpha-numeric (from the UTF8 character set), dash, and underscore characters without space. |
|  | If you enter more than 64 characters in the tag name, the value will be truncated and a message displays saying that only 64 characters are supported. |
|  | If you add more than 64 tags, the additional tag will not be added and a message displays saying that only 64 tags may be added. |
| Note | If you already have tags which are not compliant with the above, a error displays asking you to fix this. You will not be allowed to save these tags until you make the tags compliant with the above requirements. However, you may still run the test case. |
| Note | Velocity tags will not be listed when connection to Velocity is not configured (empty URL in Window > Preferences > Spirent > Velocity. See Preferences > Spirent > Velocity). |
| Note | Tags in-memory cache will reset when you restart iTest. |
| Tags (continued) | Tags included will be embedded in the test case FFTC file (see example below). |
| Test case ID | Information used during test case post-processing |
| Test case name | Information used during test case post-processing |
| Namespace | Information used during test case post-processing |

![screenshot](topics/images/test_case_editor_general_store_encrypted.png) <!-- image_chunk: img_463aa8dd0f03616a -->

![screenshot](topics/images/test_case_editor_general_tags_create.png) <!-- image_chunk: img_c7eefa0c9a93d4cc -->

![screenshot](topics/images/test_case_editor_general_tags_embedded.png) <!-- image_chunk: img_f746c1fa22064896 -->
