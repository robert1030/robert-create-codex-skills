---
{
  "chunk_id": "procedures_advanced_users_about_procedur__how_itest_passes_arguments_to_procedures_e7cd7154d419176e",
  "source_file": "topics/procedures_advanced_users_about_procedures.htm",
  "source_original_path": "topics/procedures_advanced_users_about_procedures.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Advanced Users: About procedures"
  ],
  "heading_path": [
    "Advanced Users: About procedures",
    "Advanced Users: About procedures",
    "How iTest passes arguments to procedures"
  ],
  "anchor": "1400096",
  "context_ids": [
    "procedures_advanced_users_about_procedures"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/proc_tcl_data_node.png",
    "topics/images/proc_python_data_node.png"
  ],
  "content_hash": "e7cd7154d419176e",
  "level": 2
}
---

# Advanced Users: About procedures > Advanced Users: About procedures > How iTest passes arguments to procedures

iTest passes arguments to procedures “by value”, not “by reference”. That means that if you pass an argument to a procedure and the procedure modifies the data, the caller will not have access to the changes.

There are three ways to accomplish passing information back to calling procedure:

- Use a return or write step in the procedure to return a value to the caller. The returned value becomes the response to the call step in the caller. Now you can extract the data using a response map, or simply store the data in a variable and use it in the calling procedure. (Remember that each variable is local to its procedure.)

- Use global variables. Not recommended.

- iTest does not have uplevel or upvar like Tcl does, but if you understand iTest’s variable positioning in the heap, you can modify variables in the parent scope from the called procedure. For iTest, a variable is an XPath query used to extract data from the heap (which is an XML document). The root from which iTest searches this variable depends on the scope. If you are inside a procedure, iTest will search for this XPath query from certain node in the tree. This allows iTest to implement variable scoping.

iTest stores all global variables under the /data node. So if you do gset i 0 (Tcl), gset('i', 0) (Python) you will see a node in the Data view: /data/i whose value is zero.

iTest stores procedure variables at each appropriate stack level.

Tcl: You can see stack nodes that are organized like: /data/stacks/stack/frame/frame/variable for the first procedure, /data/stacks/stack/frame/frame/frame/variable for the second procedure. You can use this information to do equivalent of Tcl uplevel. To modify a variable in the calling procedure from the called procedure, do set {../variable_in_calling_proc} 5.

set {/data/stacks/stack [@id='1']/frame/frame[@id='main']/i} 8

Python:

set ("/data/stacks/stack [@id='1']/frame/frame[@id='main']/i", 8

The key is that all iTest variables are a shortcut way to represent access to data in an XML tree. This provides a lot of power, but should be used cautiously making sure that readability and debugability of the test cases do not suffer.

![screenshot](topics/images/proc_tcl_data_node.png) <!-- image_chunk: img_c65817beffe592fd -->

![screenshot](topics/images/proc_python_data_node.png) <!-- image_chunk: img_4e8a5f25f06da467 -->
