---
{
  "chunk_id": "capture_and_include_secret_type_in_tc_st__captured_secret_type_in_the_test_case_st_f2f6419d0f857072",
  "source_file": "topics/capture_and_include_secret_type_in_tc_step.htm",
  "source_original_path": "topics/capture_and_include_secret_type_in_tc_step.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Captured Secret type in the Test Case step"
  ],
  "heading_path": [
    "Captured Secret type in the Test Case step",
    "Captured Secret type in the Test Case step"
  ],
  "anchor": "1487238",
  "context_ids": [
    "capture_and_include_secret_type_in_tc_step"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "param_parameters_type_secret.htm#1554375",
    "command_param.htm#1679166"
  ],
  "images": [
    "topics/images/capture_secret_type_and_include_in_tc.png"
  ],
  "content_hash": "f2f6419d0f857072",
  "level": 1
}
---

# Captured Secret type in the Test Case step > Captured Secret type in the Test Case step

During interactive terminal sessions, the Secret type parameter entered are not stored in session captures. See About the Parameter Type ‘Secret’

When running a terminal session, if iTest detects a Secrets type parameter (e.g., when you type a string that is not echoed in a terminal session or prompted for a password), the following rule applies.

iTest does not write the Secret type parameter into the capture Database (even as an encrypted string). Also, when you convert the session capture into a test case, a parameter type Secret will be automatically generated and inserted into the test case step (instead of a secret value). The step command will reference the parameter command. (param command: Returning parameter values) and not the Secret type..

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/capture_secret_type_and_include_in_tc.png) <!-- image_chunk: img_41f864012d1410de -->
