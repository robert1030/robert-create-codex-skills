---
{
  "chunk_id": "command_syntax_python__python_syntax_conventions_fd201e89e9bc584a",
  "source_file": "topics/command_syntax_python.htm",
  "source_original_path": "topics/command_syntax_python.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "iTest interpreter and Python commands"
  ],
  "heading_path": [
    "iTest interpreter and Python commands",
    "iTest interpreter and Python commands",
    "Python Syntax conventions"
  ],
  "anchor": "1917521",
  "context_ids": [
    "command_syntax_python"
  ],
  "index_keywords": [
    "char",
    "char command",
    "commands",
    "gget",
    "gget command",
    "gset",
    "gset command",
    "iTest Python interpreter",
    "iTest, Python",
    "interpreter commands",
    "param",
    "param command",
    "profile",
    "profile command",
    "response",
    "response command",
    "xpatheval (Python) command",
    "xpatheval, Python"
  ],
  "index_keyword_paths": [
    "char command",
    "command syntax > iTest Python interpreter",
    "command syntax > iTest, Python",
    "commands > char",
    "commands > gget",
    "commands > gset",
    "commands > param",
    "commands > profile",
    "commands > response",
    "commands > xpatheval, Python",
    "gget command",
    "gset command",
    "iTest > interpreter commands",
    "param command",
    "profile command",
    "response command",
    "syntax > iTest > commands",
    "xpatheval (Python) command"
  ],
  "related_links": [
    "command_char.htm#1897596",
    "test_cases_variables_overview.htm#1266130",
    "test_cases_store_response.htm#1320078",
    "command_for_info.htm#1763095",
    "command_param.htm#1679166",
    "command_profile.htm#1679195",
    "field_replacement_query.htm#1679213",
    "command_response.htm#1698912",
    "command_tbml.htm#1304788",
    "command_velocity.htm#1399167"
  ],
  "images": [],
  "content_hash": "fd201e89e9bc584a",
  "level": 2
}
---

# iTest interpreter and Python commands > iTest interpreter and Python commands > Python Syntax conventions

| Convention | Description |
| --- | --- |
| Convention | Description |
| boldface | Indicates commands and keywords that are entered literally as shown. |
| italics | Indicates arguments for which you supply values; in contexts that do not allow italics, arguments are enclosed within single quotes (' '). |
| ?x | Keywords or arguments that appear after a question mark are optional. |
| [x | y | z] | A choice of required keywords (represented by x, y, and z) appears in square brackets separated by vertical bars. You must select one. |
| [x (y | z)] | Braces and vertical bars within square brackets indicate a required choice within an optional element. You do not need to select one. If you do, you have some required choices. |

| Important: Using square brackets ([]) in Python syntax: Required in session steps and session profiles fields. Not required in non-session steps (eg: eval). |  | Required in session steps and session profiles fields. |  | Not required in non-session steps (eg: eval). |
| --- | --- | --- | --- | --- |
|  | Required in session steps and session profiles fields. |  |  |  |
|  | Not required in non-session steps (eg: eval). |  |  |  |

.

| Command | Description |
| --- | --- |
| char('CharacterCode') | Inserts a non-printing character (for example, tab, Ctrl-C, Esc, or Delete) into a command or property. See char command: Inserting non-printing characters for details. Right-click shortcut: For Non-printing characters, first click on the command description field, then right-click in the field and insert chars. Eg: eval [char("Ctrl-C")] |
| gget('varName', 'defaultValue') | Returns the value of the specified global variable. See the description for Global variable in Local and global variables. and Storing a response into a variable (for use later in the test). Right-click shortcut: Insert > Global Variable > Get |
| gset('varName', 'defaultValue') | Sets the value of the specified global variable. "Lists: gset('a', '[1,2,3]')"creates a list with three elements. See the description for Global variable in Local and global variables. and Storing a response into a variable (for use later in the test). |
| info('subcommand', *arguments) | The info group of commands return information about execution, about values, about the current instance of iTest, and about the user and local computer. You can use an eval action with an info command or can use the command as a field replacement. See Commands for returning information: info. |
| param ('name', default_value) | Inserts the value of a parameter into a test case step or property. For example, the [param ('ping_count')] field replacement text is replaced at runtime by the value of the ping_count parameter. If you specify a defaultValue, then the value is used if the param command does not return a value See param command: Returning parameter values. Right-click shortcut: Insert > Parameter |
| profile('name', 'default_value') | Returns the value of a parameter that is defined in the session profile associated with a particular session. See profile command: Accessing parameters that are defined in session profile. Right-click shortcut: Insert > Parameter |
| query('variable_name', 'mapper_query', alwayslist=False) | Inserts the result of a query into a command or property. See query command: Inserting the results of a query. Right-click shortcut: Insert > Query On Stored Response |
| response('varName', alwaysList=True, regex='', group='number | name') | You can store a response into a variable. Use the response command to access a response that had previously been stored in the specified variable. (Responses are stored by setting the Store response in variable property for a step. SeeStoring a response into a variable (for use later in the test).) A response with zero values or multiple values is always stored in a list. You can specify whether to obtain a single extracted value as a scalar string or in a list. For details, see response command: Accessing response data that is stored in a variable Right-click shortcut: Insert > Stored Response > Local / Global |
| tbml('subcommand', 'arg') #*args | The tbml group of commands returns device and connection information from a topology. See Commands that return information about topologies. |
| velocity('subcommand', 'arg') #*args | The velocity command returns device and connection information from a topology. See Commands that return information from Velocity. |
| xpatheval('query') | The specified Xpath query in a Python script does not return any information as heap and stack frame does not exist. For example, executing a Python script that includes Xpatheval query command (with Agent started in Listening mode), does not return any information as heap and stack frame does not exist. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
