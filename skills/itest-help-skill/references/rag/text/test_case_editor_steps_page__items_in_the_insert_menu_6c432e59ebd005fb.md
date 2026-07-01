---
{
  "chunk_id": "test_case_editor_steps_page__items_in_the_insert_menu_6c432e59ebd005fb",
  "source_file": "topics/test_case_editor_steps_page.htm",
  "source_original_path": "topics/test_case_editor_steps_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Overview",
    "Working with steps on the Steps page"
  ],
  "heading_path": [
    "Working with steps on the Steps page",
    "Working with steps on the Steps page",
    "Items in the Insert menu"
  ],
  "anchor": "1284791",
  "context_ids": [
    "test_case_editor_steps_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "commands_itest_interpreter.htm#",
    "command_expr.htm#1679151",
    "command_param.htm#1679166",
    "insert_parameter_dialog.htm#1135987",
    "command_profile.htm#1679195",
    "insert_query_on_stored_response_dialog.htm#1246379",
    "field_replacement_query.htm#1679213",
    "test_cases_store_response.htm#1320078",
    "command_response.htm#1698912",
    "command_char.htm#1897596",
    "command_for_info.htm#1763095",
    "commands_file.htm#1810683",
    "command_velocity.htm#1399167",
    "command_velocity.htm#1400091",
    "command_velocity.htm#1400140"
  ],
  "images": [],
  "content_hash": "6c432e59ebd005fb",
  "level": 2
}
---

# Working with steps on the Steps page > Working with steps on the Steps page > Items in the Insert menu

For further details on the commands mentioned in the table, see “iTest Commands”

| Inserted item | Description and Syntax |
| --- | --- |
| Local Variable | Insert an entity that returns the value of a local variable, using either: $ syntax of the form $varName A get command of the form [get varName] |
|  | $ syntax of the form $varName |
|  | A get command of the form [get varName] |
| Global Variable | Insert a field replacement that returns the value of a local variable, using a gget command of the form [gget varName] in Tcl or gget(‘varName’) in Python |
| Special Actions | Use a step with the eval Action to perform the following tasks: Concatenate strings Concatenates all of the string representations of the arguments into a single string with whitespace between argument strings. [concat string1 string2 ... stringN] Write strings into step response [puts string] Increment local variable [incr varName] Increment global variable [incr /data/varName] |
| Expression | Use a step with the eval action and the expr command to evaluate the specified expression. The result of the query is converted into a string and inserted in place of the command. [expr mathematicalExpression] See expr command: Evaluating expressions. |
| Math function | Insert a math function like abs, sqrt, round, double, wide, and so on. Note: iTest displays an error ("Cannot convert to number") if the mathematical expression to evaluate is too big. This is a limitation of the TCL interpreter. Workaround: use variables to save the whole expression step by step. Example: set a 29174813892342 set b [math.wide [math.abs [expr 1231-$a]]] In this case b cannot be evaluated. The expression is too large. Workaround: Use another variable to save the result of a piece of the math expression: set c [expr 1231 - $a] set b [math.wide [math.abs $c]] |
| Parameter defined in a test case | Use a step with the eval Action and a param command to insert the value of a parameter that was defined in the test case or in another test case that loaded as a result of a foreign procedure. See param command: Returning parameter values. |
| Parameter | Open the Insert Parameter dialog box to insert a param or a profile command. See Inserting a parameter into a property or test case step See also param command: Returning parameter values See also profile command: Accessing parameters that are defined in session profile [param parameter_name_or_query ?default_value_if_not_found?] [profile sessionID parameter_name_or_query ?default_value_if_not_found?] |
| Query On Stored Response | Open the Insert Query On Stored Response dialog box to insert a query on a response that you had previously stored in a local or global variable. See Applying queries to stored responses. Also see query command: Inserting the results of a query. How responses are stored into a variable Responses are stored by setting the Store response in variable property for a step. See Storing a response into a variable (for use later in the test). |
| Stored Response | The Stored Response option inserts a response command. The response command returns the content of a response that had previously been stored into a local or global variable. For information on using the response command, see response command: Accessing response data that is stored in a variable How responses are stored into a variable Responses are stored by setting the Store response in variable property for a step. See Storing a response into a variable (for use later in the test). |
| Non-printing Character | Use the char command to insert a non-printing character (for example, tab, Ctrl-C, Esc, and so on). By default, iTest sends a carriage return + linefeed sequence when the Command cell is blank, so there is no need to include [char \r\n] in the Command field for blank commands. See char command: Inserting non-printing characters |
| String with no substitution | Insert a fixed string. {string} |
| Information | Insert an info command as described in Commands for returning information: info. |
| File | Insert a file command as described in Commands for managing files and directories. |
| Velocity Core | Insert a Velocity Core command: reservationId, token, URL as described in Commands that return information from Velocity (“reservationId subcommand”, “token subcommand”, reservationId subcommand) Note The Insert > Velocity Core commands are available when language=TCL and language=Python |
| Note | The Insert > Velocity Core commands are available when language=TCL and language=Python |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
