---
{
  "chunk_id": "field_replacements_tasks__how_field_replacements_operate_e7c51bd5c402baad",
  "source_file": "topics/field_replacements_tasks.htm",
  "source_original_path": "topics/field_replacements_tasks.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Field replacements: Substituting values into properties and commands"
  ],
  "heading_path": [
    "Field replacements: Substituting values into properties and commands",
    "Field replacements: Substituting values into properties and commands",
    "How field replacements operate"
  ],
  "anchor": "1120226",
  "context_ids": [
    "field_replacements_tasks"
  ],
  "index_keywords": [
    "defined",
    "field substitution",
    "guidelines",
    "runtime field replacement",
    "substituting values at runtime",
    "syntax"
  ],
  "index_keyword_paths": [
    "field replacements > defined",
    "field replacements > guidelines",
    "field replacements > syntax",
    "field substitution",
    "runtime field replacement",
    "substituting values at runtime"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "e7c51bd5c402baad",
  "level": 2
}
---

# Field replacements: Substituting values into properties and commands > Field replacements: Substituting values into properties and commands > How field replacements operate

At runtime, before the property or step is interpreted, iTest substitutes the returned value in place of the field replacement text. Field replacements are done in context of the testcase.

Here is how that works in Tcl:

Each executable step is preprocessed immediately before execution. Preprocessing means that all user-defined text associated with the command is searched for any field that starts with [ and ends with ] (this is, iTest searches for field replacements). The entire field, including the brackets, is replaced with a string determined by evaluating the information inside the braces. (User-defined text includes prompts, the command body text — which may be multi-line for some protocols — the command header text, and the user-defined text values in the associated Analysis rules. This means that you can use a field replacement in any of these locations.)

If the operation inside the [ ] braces results in an error, then iTest generates an execution issue and displays a message in the Execution view, the Step Issues view, and in the test report. The text of the field replacement is not substituted for execution.

In the Tcl example, the param command returned the value of the PortType parameter, so that is the value that replaces the [param PortType] text in the show interfaces command.

Here is how it works in Python

Fields with substitution/replacements enabled (for example, the command field for a command action in SSH) will use braces, [ ] as escape characters for interpreter evaluation. iTest evaluates everything between the braces, [ and ] characters, using with the Python interpreter, and replaces with a string determined by evaluating the information inside the braces.

> **Note:** Note It is not necessary to escape [ and ] characters within the braces.

In the example, show interfaces [param('PortType')] 1/[param('SubIndex')] would evaluate PortType and SubIndex defined parameters.

The param command returns the value of the PortType parameter, the value that replaces [param('PortType')] in the show interfaces command.

Example 2: ping -c 3 [hostList[0]]

The ping -c 3 [hostList[0]] command would evaluate to ping the first hostname in a Python list called hostList.

Example 3: Field replacement obtains value required by the command from the test case execution context. That is, to obtain a user mail address in Mail (SMTP) session, use command as follows: [profile('.' ,'Mail/user')] to obtain value from the user profile (not [param(‘mail/user’)], which will obtain value from parameters).

Alternatively you may use [param('.//profile/Mail/user')] to allow xpath to obtain the parameter value.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
