---
{
  "chunk_id": "test_cases_action_run_exec__display_two_tables_unexpected_followed_b_6472a3f94ad99001",
  "source_file": "topics/test_cases_action_run_exec.htm",
  "source_original_path": "topics/test_cases_action_run_exec.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Running child test cases",
    "Executing a child test case: The ‘run’ action"
  ],
  "heading_path": [
    "Executing a child test case: The ‘run’ action",
    "Executing a child test case: The ‘run’ action",
    "Display two tables: unexpected followed by all tests"
  ],
  "anchor": "1714682",
  "context_ids": [
    "test_cases_action_run_exec"
  ],
  "index_keywords": [
    "defined",
    "run",
    "run action"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > run",
    "actions > run",
    "child test case > defined",
    "external test case > defined",
    "foreign test case > defined",
    "run action"
  ],
  "related_links": [],
  "images": [
    "topics/images/test_cases.6.jpg"
  ],
  "content_hash": "6472a3f94ad99001",
  "level": 4
}
---

# Executing a child test case: The ‘run’ action > Executing a child test case: The ‘run’ action > Display two tables: unexpected followed by all tests

1. 6

1. Parameters: Specify the sources for parameter settings that the child test case should use during execution. In the default configuration, only parameters associated with the test case and no others are used.

| Parameter file to use | This property determines the source of the parameter file. Use specified parameter file: If you want to use a parameter file, then you must specify the file in the Parameter file property. Use parameter file from parent. Use the parameter file specified for the parent test case Default: Use specified parameter file |  | Use specified parameter file: If you want to use a parameter file, then you must specify the file in the Parameter file property. |  | Use parameter file from parent. Use the parameter file specified for the parent test case |
| --- | --- | --- | --- | --- | --- |
|  | Use specified parameter file: If you want to use a parameter file, then you must specify the file in the Parameter file property. |  |  |  |  |
|  | Use parameter file from parent. Use the parameter file specified for the parent test case |  |  |  |  |
| Parameter file | Optional This property is used when you select Use specified parameter file for the Parameter file to use property. Specify the parameter file to use while executing the child test case. If blank, then no parameter file is used. Default: [blank] |  |  |  |  |
| Include parameters that were individually passed to parent test case | Check the box to cause the child test case to use parameter values as specified in the parent test case. This includes Advanced Merging property settings. Default: unchecked |  |  |  |  |
| Parameters | Use the specified parameter values while executing the child test case. Parameters that you specify here take precedence over the parameters from any other source. Type only one name=value pair per line. Specify each parameter setting as <name>=<value>, for example, port=3. |  |  |  |  |
| Initialize using a snapshot of current parameters | Note This option is not recommended because it can cause duplicate parameters to be created. In addition, the snapshot may include parameters from other child test cases. Check the box to cause the child test case to use parameter values as currently in use. This includes Advanced Merging property settings. Default: unchecked | Note | This option is not recommended because it can cause duplicate parameters to be created. In addition, the snapshot may include parameters from other child test cases. |  |  |
| Note | This option is not recommended because it can cause duplicate parameters to be created. In addition, the snapshot may include parameters from other child test cases. |  |  |  |  |

![screenshot](topics/images/test_cases.6.jpg) <!-- image_chunk: img_16083a632c129353 -->
