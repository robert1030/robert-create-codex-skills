---
{
  "chunk_id": "quickcalls_arguments_in_quickcall_steps__fixing_the_empty_argument_list_ad61d2c79012d04f",
  "source_file": "topics/quickcalls_arguments_in_quickcall_steps.htm",
  "source_original_path": "topics/quickcalls_arguments_in_quickcall_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Adding a test case step that executes a QuickCall",
    "About arguments in QuickCall steps"
  ],
  "heading_path": [
    "About arguments in QuickCall steps",
    "About arguments in QuickCall steps",
    "Fixing steps with empty Argument list in Python testcases",
    "Fixing the empty argument list"
  ],
  "anchor": "1533614",
  "context_ids": [
    "quickcalls_arguments_in_quickcall_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1535703"
  ],
  "images": [
    "topics/images/qc_tclSyn_inPython_emptyArgList_ProblemView.png",
    "topics/images/quickcalls_3.08.jpg",
    "topics/images/qc_tclSyn_inPyhton_buildProject.png"
  ],
  "content_hash": "ad61d2c79012d04f",
  "level": 4
}
---

# About arguments in QuickCall steps > About arguments in QuickCall steps > Fixing steps with empty Argument list in Python testcases > Fixing the empty argument list

iTest provides a Quick Fix in the Problem View option to convert TCL syntax with empty argument list into Python syntax as shown below.

- The Problem View displays the Quick Fix option message (as shown above) only for TCL call steps and TCL CallProcedure event handlers for step/testcase with empty argument list in Python testcases.

- The Problem View does not display the Quick Fix option for individual error message (as shown above) displayed due to syntax error on call/QuickCall steps with non-empty argument list.

You may fix markers either individually or by grouping them into categories by clicking Group By > Type. For ease of search and reference, iTest displays all TCL warning markers that may be resolved (Empty Call Arguments Problem and Empty QuickCall Arguments Problem type) under the category Resolvable Python Syntax Mismatch Problems (see the screenshot example below).

> **Note:** Important Before you Apply Quick Fix for markers, it is recommended to do the following:

- Save all resources related to the error markers.

All resources related to markers must be saved if you opened and modified them in the Testcase Editor or Text editors.

If not saved, iTest skips resolving the error markers. If the resolution is skipped, a warning dialog will be shown indicating the reason.

- Ensure the Build automatically option is enabled (See iTest > Project > Build Automatically). To Build automatically, select the Build automatically option.

If Build automatically option is disabled, rebuild projects containing testcases with TCL syntax warnings. To rebuild, select iTest > Project > Build All or Build Project. See the example screenshot below.

If not rebuilt (or build automatically not enabled), markers may become outdated and it might not be possible to apply marker resolution on the test cases with TCL syntax warnings and the resolution will be skipped.

![screenshot](topics/images/qc_tclSyn_inPython_emptyArgList_ProblemView.png) <!-- image_chunk: img_9ba7a2ab22626548 -->

![screenshot](topics/images/quickcalls_3.08.jpg) <!-- image_chunk: img_7fd7a55f2710178b -->

![screenshot](topics/images/qc_tclSyn_inPyhton_buildProject.png) <!-- image_chunk: img_883aeca5011564cc -->
