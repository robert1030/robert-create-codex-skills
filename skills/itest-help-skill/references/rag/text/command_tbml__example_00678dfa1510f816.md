---
{
  "chunk_id": "command_tbml__example_00678dfa1510f816",
  "source_file": "topics/command_tbml.htm",
  "source_original_path": "topics/command_tbml.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "\"tbml\" topology commands",
    "Commands that return information about topologies"
  ],
  "heading_path": [
    "Commands that return information about topologies",
    "Commands that return information about topologies",
    "Example topology",
    "query subcommand: Return XPath query result",
    "Example:"
  ],
  "anchor": "1498486",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/tbml_topology_sess_profile.png",
    "topics/images/tbml_subs_TC_sess_profile.png",
    "topics/images/tbml_subs_inside_testCase.png",
    "topics/images/tbml_eval.png"
  ],
  "content_hash": "00678dfa1510f816",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > query subcommand: Return XPath query result > Example:

The table below lists the example use-cases where tbml command is used. All these use cases uses tbml file's property to determine the XPath version used to evaluate the tbml command.

| Source of the tbml() command: Substitutions in the topology's device session profile. |
| --- |
| iTest execution scenario: A session is started interactively from iTest topology editor. for example: Create a topology in iTest, and add some properties to the topology Create a topology device and a session for the device Include session properties substituted with tbml command, which retrieve topology properties. Start the session and the session substitutes the properties from topology and starts as expected. |
|  |
|  |
|  |
|  |
| iTest execution scenario: A session is opened from the main testcase, and the testcase inherits the substitutions from the session profile. PythonSLC support: An open step from the screenshot will be converted into: my_project.my_local_topo_tbml.pc1.local_ssh.open() All inherited substitutions are resolved on SLC agent side. |
| iTest execution scenario: The main testcase invokes a quickcall/external procedure, which opens the session and inherits the substitutions from the session profile. PythonSLC Support: Any QuickCall/external procedure call is converted into: my_project.qc_lib_fftc.my_quickall() my_project.proc_lib_fftc.my_procedure() All steps of the QuickCall/external procedure are executed on SLC agent. |
| Source of the tbml() command: Substitutions inside the testcase iTest execution scenario: Substitution appears in the main testcase. In particular, user can override inherited values in the open step of the session: PythonSLC Support: When the test case is converted to python, test case's substitutions are converted into Python statements: An open step from the screenshot will be converted into: my_project.my_local_topo_tbml.pc2.local_ssh2.open( properties={ 'port': str(tbml('query', '//tbml/header/property[@name = "host"]')) }) Which means [tbml] substitution is converted into tbml() python method call. iTest execution scenario: The main testcase invokes a quickcall/external procedure, which contains the substitution PythonSLC Support: Same as explained above for QuickCalls |
| Source of the tbml() command: eval command iTest execution scenario: The main testcase contains an eval step with tbml command. PythonSLC Support: eval step content is convered into python statement: tbml('query', '//tbml/header/property[@name = "host"]') iTest execution scenario: The main testcase invokes a QuickCall/external procedure, which contains an eval step with tbml command PythonSLC Support: Same as explained above for QuickCalls |

![diagram](topics/images/tbml_topology_sess_profile.png) <!-- image_chunk: img_bf590bf260e6d935 -->

![screenshot](topics/images/tbml_subs_TC_sess_profile.png) <!-- image_chunk: img_6037d0a4e1e20f59 -->

![screenshot](topics/images/tbml_subs_inside_testCase.png) <!-- image_chunk: img_92a8378a61886ce6 -->

![screenshot](topics/images/tbml_eval.png) <!-- image_chunk: img_38e692bd90fc02c1 -->
