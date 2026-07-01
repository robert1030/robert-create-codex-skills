---
{
  "chunk_id": "python_execute_test_case__execute_python_session_test_case_8b044d30b51a398e",
  "source_file": "topics/python_execute_test_case.htm",
  "source_original_path": "topics/python_execute_test_case.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Sessions",
    "Execute Python session Test Case"
  ],
  "heading_path": [
    "Execute Python session Test Case",
    "Execute Python session Test Case"
  ],
  "anchor": "1440853",
  "context_ids": [
    "python_execute_test_case"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "python_sessions.htm#1453451"
  ],
  "images": [
    "topics/images/py_run_rendered_TC.png",
    "topics/images/py_init_script_execution_import_script.png",
    "topics/images/py_init_script_execution.png"
  ],
  "content_hash": "8b044d30b51a398e",
  "level": 1
}
---

# Execute Python session Test Case > Execute Python session Test Case

You may run the Python command steps captured to a Test Case as any the other test case. When the execution completed, the test report will be generated.

Open the test case, click Start Execution in New Window. iTest Python terminal session opens and starts executing the steps in the test case. When the execution completed, the test report will be generated.

If you have defined any Initialization script, iTest will invoke the Initialization script (in section Create and run a Python Session) automatically when launching the Python session.

> **Note:** Note If any exceptions occur due to the Initialization script execution, the open step fails and an error message displays.

Also, if you have specified Additional module paths, iTest will import the script from the absolutely path or the relative path as defined (Additional Modules in section Create and run a Python Session).

> **Note:** Note iTest also includes any/all paths specified in the PYTHONPATH environment variable in the module search path list.

When the Initialization script executes, the output from the script will be shown as part of Python session open step as shown below.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/py_run_rendered_TC.png) <!-- image_chunk: img_6640fef2064b7cf6 -->

![screenshot](topics/images/py_init_script_execution_import_script.png) <!-- image_chunk: img_29fd5cb593e7b127 -->

![screenshot](topics/images/py_init_script_execution.png) <!-- image_chunk: img_1e0283a6bab7ab41 -->
