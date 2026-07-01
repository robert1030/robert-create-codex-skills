---
{
  "chunk_id": "test_cases_store_response_file__storing_response_text_into_a_file_173297a7ea6cb1b4",
  "source_file": "topics/test_cases_store_response_file.htm",
  "source_original_path": "topics/test_cases_store_response_file.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Overview: Creating a test case",
    "Storing response text into a file"
  ],
  "heading_path": [
    "Storing response text into a file",
    "Storing response text into a file"
  ],
  "anchor": "1801165",
  "context_ids": [
    "test_cases_store_response_file"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "arules_processor_properties.htm#1186331",
    "arules_processor_properties.htm#1641520",
    "field_replacements_tasks.htm#"
  ],
  "images": [
    "topics/images/test_cases_2.1.jpg"
  ],
  "content_hash": "173297a7ea6cb1b4",
  "level": 1
}
---

# Storing response text into a file > Storing response text into a file

You might want to save the response for a step to a file so that you can later review the response while debugging your test case or test suite. Here is an example text file for an ls command:

> **Note:** Note For SNMP sessions, you have the option to conserve memory by specifying not to capture the SNMP response and/or SNMP statistics for the response (in the Step Defaults properties group). When you configure a step to save a response to a file, the settings are ignored and all SNMP responses and statistics are always written to the file.



To store response text into a file

1. Select the step. In the Step Properties section, open the Other Post-processing > Store Response property group.

> **Note:** Note The property settings that you can configure here for the step are all inherited from the open step for the session. To log the responses for all steps in a session, therefore, configure the properties for the open step.

1. 2

1. Specify the path and name of the File to write response to.

If you have selected to hide value of the parameter type Secret (see Analysis rules: Properties of the processor, section Store processor) the data is masked and stores as **** (asterisks) in the response file.

1. 3

1. In the Response header box, specify the text that should appear at the beginning of the text of the response (this is the beginning of the file if you uncheck the Append response to file property). In the example, the header text is Here is the directory listing.

> **Note:** Note By default, substitution of field replacements is disabled for both the File to write response to and the Response header properties. You have the option to enable substitution so that, for example, the text [param headerText] is replaced with the value of the headerText parameter. (Field replacements are described in “Field Replacements”.)

1. 4

1. Configure additional settings as appropriate:

| Append response to file | Check the box to add the response text to the end of the existing file. Uncheck to overwrite the file. Caution If you uncheck the box, then the response for a single step can overwrite a file that contains many appended responses. Default: checked | Caution | If you uncheck the box, then the response for a single step can overwrite a file that contains many appended responses. |
| --- | --- | --- | --- |
| Caution | If you uncheck the box, then the response for a single step can overwrite a file that contains many appended responses. |  |  |
| Note All of the following text items will appear before the response text for the current step. The items appear in the listed order. | Note | All of the following text items will appear before the response text for the current step. The items appear in the listed order. |  |
| Note | All of the following text items will appear before the response text for the current step. The items appear in the listed order. |  |  |
| Prepend step action | Check the box to add a line of the form action:<actionName> Default: unchecked |  |  |
| Prepend Session ID | Check the box to add a line of the form session: <sessionID> Default: unchecked |  |  |
| Prepend command body | The command body is the text that appears in the Command property (and the Description cell) for a step. Check the box to add a line of the form command:<commandBodyText> Default: checked |  |  |
| Prepend timestamp | Check the box to add an execution timestamp for the current step. Default: checked |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/test_cases_2.1.jpg) <!-- image_chunk: img_6b4d40311b4a15a4 -->
