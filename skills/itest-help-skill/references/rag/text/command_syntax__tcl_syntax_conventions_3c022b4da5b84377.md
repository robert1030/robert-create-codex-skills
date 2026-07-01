---
{
  "chunk_id": "command_syntax__tcl_syntax_conventions_3c022b4da5b84377",
  "source_file": "topics/command_syntax.htm",
  "source_original_path": "topics/command_syntax.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "iTest Tcl interpreter commands"
  ],
  "heading_path": [
    "iTest Tcl interpreter commands",
    "iTest Tcl interpreter commands",
    "Tcl Syntax conventions"
  ],
  "anchor": "1801815",
  "context_ids": [
    "command_syntax"
  ],
  "index_keywords": [
    "array",
    "array command",
    "char",
    "char command",
    "clock",
    "clock command",
    "commands",
    "concat",
    "concat command",
    "expr",
    "expr command",
    "format",
    "get",
    "get command",
    "gget",
    "gget command",
    "gset",
    "gset command",
    "gunset",
    "gunset command",
    "iTest",
    "iTest interpreter",
    "incr",
    "incr command",
    "interpreter commands",
    "join",
    "join command",
    "lappend",
    "lappend command",
    "lassign",
    "lassign command",
    "lcompare",
    "lcompare command",
    "lindex",
    "lindex command",
    "linsert",
    "linsert command",
    "list",
    "list command",
    "llength",
    "llength command",
    "lrange",
    "lrange command",
    "lrepeat",
    "lrepeat command",
    "lreplace",
    "lreplace command",
    "lreverse",
    "lreverse command",
    "lsearch",
    "lsearch command",
    "lset",
    "lset command",
    "lsort",
    "lsort command",
    "math",
    "math commands",
    "param",
    "param command",
    "parray",
    "parray command",
    "profile",
    "profile command",
    "puts",
    "puts command",
    "regexp",
    "regexp command",
    "regsub",
    "regsub command",
    "response",
    "response command",
    "rmat command",
    "scan",
    "scan command",
    "set",
    "set command",
    "split",
    "split command",
    "string",
    "string command",
    "string concat",
    "string concat command",
    "subst",
    "subst command",
    "unset",
    "unset command",
    "xpatheval",
    "xpatheval command"
  ],
  "index_keyword_paths": [
    "array command",
    "char command",
    "clock command",
    "command syntax > iTest",
    "command syntax > iTest interpreter",
    "commands > array",
    "commands > char",
    "commands > clock",
    "commands > concat",
    "commands > expr",
    "commands > format",
    "commands > get",
    "commands > gget",
    "commands > gset",
    "commands > gunset",
    "commands > incr",
    "commands > join",
    "commands > lappend",
    "commands > lassign",
    "commands > lcompare",
    "commands > lindex",
    "commands > linsert",
    "commands > list",
    "commands > llength",
    "commands > lrange",
    "commands > lrepeat",
    "commands > lreplace",
    "commands > lreverse",
    "commands > lsearch",
    "commands > lset",
    "commands > lsort",
    "commands > math",
    "commands > param",
    "commands > parray",
    "commands > profile",
    "commands > puts",
    "commands > regexp",
    "commands > regsub",
    "commands > response",
    "commands > scan",
    "commands > set",
    "commands > split",
    "commands > string",
    "commands > string concat",
    "commands > subst",
    "commands > unset",
    "commands > xpatheval",
    "concat command",
    "expr command",
    "get command",
    "gget command",
    "gset command",
    "gunset command",
    "iTest > interpreter commands",
    "incr command",
    "join command",
    "lappend command",
    "lassign command",
    "lcompare command",
    "lindex command",
    "linsert command",
    "list command",
    "llength command",
    "lrange command",
    "lrepeat command",
    "lreplace command",
    "lreverse command",
    "lsearch command",
    "lset command",
    "lsort command",
    "math commands",
    "param command",
    "parray command",
    "profile command",
    "puts command",
    "regexp command",
    "regsub command",
    "response command",
    "rmat command",
    "scan command",
    "set command",
    "split command",
    "string command",
    "string concat command",
    "subst command",
    "syntax > iTest > commands",
    "unset command",
    "xpatheval command"
  ],
  "related_links": [
    "command_char.htm#1897596",
    "command_expr.htm#1679151",
    "commands_file.htm#1810683",
    "test_case_editor_steps_page.htm#1284791",
    "command_for_info.htm#1763095",
    "command_param.htm#1679166",
    "command_profile.htm#1679195",
    "field_replacement_query.htm#1679213",
    "test_cases_store_response.htm#1320078",
    "command_response.htm#1698912",
    "command_tbml.htm#1304788",
    "command_tcl.htm#1698948",
    "command_tclexpr.htm#1698922"
  ],
  "images": [],
  "content_hash": "3c022b4da5b84377",
  "level": 2
}
---

# iTest Tcl interpreter commands > iTest Tcl interpreter commands > Tcl Syntax conventions

| Convention | Description |
| --- | --- |
| boldface | Indicates commands and keywords that are entered literally as shown. |
| italics | Indicates arguments for which you supply values; in contexts that do not allow italics, arguments are enclosed in angle brackets (< >). |
| ?x? | Keywords or arguments that appear within question marks are optional. |
| {x | y | z} | A choice of required keywords (represented by x, y, and z) appears in braces separated by vertical bars. You must select one. |
| [x {y | z}] | Braces and vertical bars within square brackets indicate a required choice within an optional element. You do not need to select one. If you do, you have some required choices. |

| Command | Description |
| --- | --- |
| array ?-g? subcommand arrayName ?arg arg ...? | Performs an operation on the existing array variable specified by arrayName. The iTest array command is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/ The optional -g argument indicates a global array. Subcommands The following subcommands are supported: [array ?-g? compare array1 array2] Returns -1 if array1 is less than array2 Returns 0 if array1 is equal to array2 Returns 1 if array1 is bigger than array2 Arrays are compared recursively. [array ?-g? exists arrayName] Returns 1 if arrayName is an array variable, 0 if there is no variable by that name or if it is a scalar variable. [array ?-g? get arrayName ?pattern?] In the optional pattern, only the * and ? wildcard characters are supported. The [chars] and \x options are not supported. [array ?-g? names arrayName ?pattern?] Returns a list containing the names of all of the elements in the array that match pattern. The syntax differs from Tcl syntax: Tcl: array names arrayName ?mode? ?pattern? iTest: array names arrayName ?pattern? (mode always defaults to glob) In the optional pattern, only the * and ? wildcard characters are supported. The [chars] and \x options are not supported. [array ?-g? set arrayName list] Sets the values of one or more elements in arrayName. [array ?-g? size arrayName] Returns a decimal string giving the number of elements in the array. If arrayName isn't the name of an array then 0 is returned. [array ?-g? unset arrayName ?pattern?] Unsets all of the elements in the array that match pattern. In the optional pattern, only the * and ? wildcard characters are supported. The [chars] and \x options are not supported. |
| char characterCode | Inserts a non-printing character (for example, tab, Ctrl-C, Esc, or Delete) into a command or property. See char command: Inserting non-printing characters for details. Right-click shortcut: Insert > Non-Printing Character |
| clock option ?arg arg ...? | Return the time between one iTest step and another. Return elapsed time by comparing two timestamps. For example timestamps taken from a log file (the format may vary) Add or subtract from a time. For example, given a starting time, if I add 2 hours (or minutes, or days, and so on) what is the new time? The epoch (starting date and time) is 12/31/1969 16:00:00 clock clicks -milliseconds Returns the number of milliseconds elapsed (High resolution timer not based on any epoch) clock format clockValue ?-format string? ?-gmt boolean? Formats clockValue with the specified format string format: Specifies the format of the string to be printed gmt: An optional boolean variable that specifies whether or not the time is GMT clock seconds Returns the number of seconds elapsed since the epoch clock milliseconds Returns the number of milliseconds elapsed since the epoch clock microseconds Returns the number of microseconds elapsed since the epoch clock scan dateString ?-base clockVal? ?-gmt boolean? Scans dateString and converts it to the number of seconds since the epoch base: The beginning date to start the clock (Default is the epoch date) gmt: An optional boolean variable that specifies whether or not the time is GMT For further details, see: http://www.tcl.tk/man/ |
|  | Return the time between one iTest step and another. |
|  | Return elapsed time by comparing two timestamps. For example timestamps taken from a log file (the format may vary) |
|  | Add or subtract from a time. For example, given a starting time, if I add 2 hours (or minutes, or days, and so on) what is the new time? |
|  | format: Specifies the format of the string to be printed |
|  | gmt: An optional boolean variable that specifies whether or not the time is GMT |
|  | base: The beginning date to start the clock (Default is the epoch date) |
|  | gmt: An optional boolean variable that specifies whether or not the time is GMT |
| concat ?arg arg ...? | Concatenates all of the string representations of the arguments into a single string with whitespace between argument strings. The concat command joins each of its arguments together with spaces after trimming leading and trailing white-space from each of them. If all the arguments are lists, this has the same effect as concatenating them into a single list. It permits any number of arguments; if no arguments are supplied, the result is an empty string. The iTest concat command is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/ Right-click shortcut: Insert > Special Actions > Concatenate Strings |
| expr arg ?arg arg ...? | Evaluates the specified expression into a command or property. The result of the query is converted into a string and inserted in place of this command. Examples [expr 5 + 5]: replaced by 10 [expr $i + 1]: $i is first substituted. If i has value 10, then the result of this command is 11. See expr command: Evaluating expressions Right-click shortcut: Insert > Special Actions > Expression |
| File and directory management commands The file commands enable you to manage files and directories, whether in the workspace or elsewhere on the file system. Full descriptions appear in Commands for managing files and directories. |  |
| format formatString ?arg arg ...? | Generates a formatted string in a fashion similar to the ANSI C sprintf procedure. formatString indicates how to format the result, using % conversion specifiers as in sprint. The additional arguments, if any, provide values to be substituted into the result. The return value from format is the formatted string. The format command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| get varName ?defaultValue? | Returns the value of the specified local variable. If the specified variable is not found, then the command returns the default value, if specified. Alternative syntax for returning the value: ${varName}. The expressions $i and [get i] are identical in operation; they both return the value of the variable i. Right-click shortcut: Insert > Local Variable > Get using command See the description for Local variable in Items in the Insert menu. |
| gget varName ?defaultValue? | Returns the value of the specified global variable. Alternative syntax for returning the value: ${/data/varName} The expressions $/data/i and [gget i] are identical in operation; they both return the value of the variable i. If the specified variable is not found, then the command returns the default value if specified. See the description for Global variable in Items in the Insert menu. Right-click shortcut: Insert > Global Variable > Get |
| gset varName ?defaultValue? | Sets the value of the specified global variable. Arrays: Use set a(1,2) foo syntax. (To create an array with one element, use the array command.) Lists: gset a {1,2 foo} creates a list with two elements, the first element is “1,2” and the second is “foo”. See the description for Global variable in Items in the Insert menu. |
| gunset varName | Removes one global variable. Limitation: No additional arguments are allowed. The command is otherwise compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/ |
| incr varName | Increments the specified local or global variable. Right-click shortcuts: Insert > Special Actions > Increment Local Variable Insert > Special Actions > Increment Global Variable |
| info subcommand ?arguments? | The info group of commands return information about execution, about values, about the current instance of iTest, and about the user and local computer. You can use an eval action with an info command or can use the command as a field replacement. See Commands for returning information: info. |
| join list ?joinString? | Creates a string by joining together list elements. The list argument must be a valid Tcl list. The command returns the string formed by joining all of the elements of list together with joinString separating each adjacent pair of elements. The joinString argument defaults to a space character. The join command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| The list commands all start with the letter l. |  |
| lappend varName ?value value ...? | Treats the varName variable as a list and appends each of the value arguments to the list as a separate element, with spaces between elements. The lappend command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lassign list varName ?varName ...? | Assigns list elements to variables. The command treats the value list as a list and assigns successive elements from that list to the varName variables in order. If there are more variable names than list elements, the remaining variables are set to the empty string. If there are more list elements than variables, a list of unassigned elements is returned. The lassign command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lcompare list1 list2 | Returns -1 if list1 is less than list2 Returns 0 if list1 is equal to list2 Returns 1 if list1 is bigger than list2 Lists are compared recursively. |
| lindex list ?index? | Retrieves an element from a list. The lindex command accepts a parameter, list, which it treats as a Tcl list. It also accepts zero or more indexes into the list. The indexes may be presented either consecutively on the command line, or grouped in a Tcl list and presented as a single argument. You can specify end?-n? as an index, so lindex {a b c} end will return c lindex {a b c} end-1 will return b If no indexes are present, then the return value of lindex is the value of the list parameter. The lindex command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| linsert list index element ?element element ...? | Inserts elements into a list. The command produces a new list from list by inserting all of the element arguments just before the index'th element of list. Each element argument will become a separate element of the new list. If index is less than or equal to zero, then the new elements are inserted at the beginning of the list. The interpretation of the index value is the same as for the command string index, supporting simple index arithmetic and indexes relative to the end of the list. The linsert command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| list ?arg ... arg? | Returns a list comprised of all the args, or an empty string if no args are specified. Braces and backslashes get added as necessary, so that the lindex command may be used on the result to re-extract the original arguments, and also so that eval may be used to execute the resulting list, with arg1 comprising the command's name and the other args comprising its arguments. list produces slightly different results than concat: concat removes one level of grouping before forming the list, while list works directly from the original arguments. The list command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| llength list | Counts the number of elements in a list. The command treats list as a list and returns a decimal string giving the number of elements in it. The llength command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lrange list first last | Returns one or more adjacent elements from a list. list must be a valid Tcl list. The command returns a new list consisting of elements first through last, inclusive. The index values first and last are interpreted the same as index values for the command string index, supporting simple index arithmetic and indexes relative to the end of the list. The lrange command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lrepeat number element1 ?element2 element3 ...? | Builds a list by repeating elements. The command creates a list of size number * number of elements by repeating number times the sequence of elements element1 element2 .... number must be a positive integer, elementn can be any Tcl value. Note that lrepeat 1 arg ... is identical to list arg ..., though the arg is required with lrepeat. The lrepeat command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lreplace list first last ?element element ...? | Replaces elements in a list with new elements. lreplace returns a new list formed by replacing one or more elements of list with the element arguments. first and last are index values specifying the first and last elements of the range to replace. The index values first and last are interpreted the same as index values for the command string index, supporting simple index arithmetic and indexes relative to the end of the list. 0 refers to the first element of the list, and end refers to the last element of the list. If list is empty, then first and last are ignored. If first is less than zero, it is considered to refer to before the first element of the list. For non-empty lists, the element indicated by first must exist or first must indicate before the start of the list. If last is less than first, then any specified elements will be inserted into the list at the point specified by first with no elements being deleted. The element arguments specify zero or more new arguments to be added to the list in place of those that were deleted. Each element argument will become a separate element of the list. If no element arguments are specified, then the elements between first and last are simply deleted. If list is empty, any element arguments are added to the end of the list. The lreplace command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lreverse list | Reverses the order of a list. The command returns a list that has the same elements as the input list, except with the elements in the reverse order. |
| lsearch ?-inline? list pattern | Determines whether a list contains a specified element. If found, returns the zero-based index of the matching item. If you use the optional ‑inline switch, then returns the matching item. If not found, returns -1. pattern supports regex matching and exact matching. Wildcard (glob-style) matching supports using only the * and ? wildcard characters and does not support [chars] and \x. The lsearch command is compatible with its Tcl counterpart, as more fully described at: http://www.tcl.tk/man/ |
| lset varName ?index...? newValue | Accepts a parameter, varName, which it interprets as the name of a variable containing a Tcl list. The command also accepts zero or more indices into the list. The indices may be presented either consecutively on the command line, or grouped in a Tcl list and presented as a single argument. Finally, the command accepts a new value for an element of varName. For additional detail, see the fuller description at: http://www.tcl.tk/man/ |
| lsort ?options? list | Sorts the elements of list, returning a new list in sorted order. The lsort command performs O(n log n) sort. ASCII sorting is used by default, with the result returned in increasing order. However, any of several options may be specified to control the sorting process. Limitation The -command option is not supported. Aside from the stated limitation, the lsort command is compatible with its Tcl counterpart, as more fully described at:http://www.tcl.tk/man/ |
| Limitation | The -command option is not supported. |
| math.abs arg math.acos arg math.asin arg math.atan arg math.avg ?arg ... arg math.c?eil arg math.cos arg math.cosh arg math.double arg math.exp arg math.floor arg math.fmod x y math.hypot x y math.int arg math.log arg math.log10 arg math.max arg ... arg math.min arg ... arg math.pow x y math.rand math.round arg math.sin arg math.sinh arg math.sqrt arg math.srand arg math.tan arg math.tanh arg | Each of the iTest math function commands is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/tcl8.4/TclCmd/expr.htm#M20 Example 1 expr {[math.sin $i]/2}: In this example, notice that the syntax for the iTest expr command differs from the Tcl syntax: expr {sin($i)/2} Example 2: Converting Hex value to Decimal You have 0x2e9 in a iTest variable called i eval set i 0x2e9 To convert the hex string to its integer value, use math.int: eval set j [math.int $i] Right-click shortcut: Insert > Math Function > function_name Note: iTest displays an error ("Cannot convert to number") if the mathematical expression to evaluate is too big. This is a limitation of the TCL interpreter. Workaround: use variables to save the whole expression step by step. Example: set a 29174813892342 set b [math.wide [math.abs [expr 1231-$a]]] In this case b cannot be evaluated. The expression is too large. Workaround: Use another variable to save the result of a piece of the math expression: set c [expr 1231 - $a] set b [math.wide [math.abs $c]] |
| param paramNameOrQuery ?defaultValue? | Inserts the value of a parameter into a test case step or property. For example, the [param ping_count] field replacement text is replaced at runtime by the value of the ping_count parameter. If you specify a defaultValue, then the value is used if the param command does not return a value See param command: Returning parameter values. Right-click shortcut: Insert > Parameter |
| parray ?-g? arrayName ?pattern? | Returns an array's keys and values. In the optional pattern, only the * and ? wildcard characters are supported. The [chars] and \x options are not supported. Example response: fruit(best) = peach fruit(2nd) = apple fruit(ok) = banana fruit(worst) = fly The iTest parray command is compatible with its Tcl counterpart as more fully described at: http://wiki.tcl.tk/man |
| profile sessionID paramNameOrQuery ?defaultValue? | Returns the value of a parameter that is defined in the session profile associated with a particular session. See profile command: Accessing parameters that are defined in session profile. Right-click shortcut: Insert > Parameter |
| puts {string} | Writes the string characters to stdout. puts normally outputs a newline character after string, but this feature may be suppressed by specifying the -nonewline switch. Tip puts returns the string into the response. Using a get or gget command substitution in the string itself is a convenient way to display a variable value. Right-click shortcut: Insert > Special Actions > Write string into step response |
| Tip | puts returns the string into the response. Using a get or gget command substitution in the string itself is a convenient way to display a variable value. |
| query ?-alwayslist? varName mapperQuery | Inserts the result of a query into a command or property. See query command: Inserting the results of a query. Right-click shortcut: Insert > Query On Stored Response |
| regexp ?switches? regexp string ?matchVar? ?subMatchVar subMatchVar ...? | Matches a regular expression against a string. Returns 1 if the expression matches, 0 otherwise. The command uses Java regexps to implement the command. The the syntax of regexp patterns is described at: http://java.sun.com/javase/6/docs/api/java/util/regex/Pattern.html The iTest regexp command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man/ |
| regsub ?switches? regExp string subSpec ?varName? | Performs substitutions based on regular expression pattern matching. The command matches the regular expression regExp against string, and either copies string to the variable whose name is given by varName or returns string if varName is not present. The the syntax of regexp patterns is described at: http://java.sun.com/javase/6/docs/api/java/util/regex/Pattern.html The iTest regsub command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man/ |
| response ?-alwayslist? ?-group number_or_name? varName ?regex? | You can store a response into a variable. Use the response command to access a response that had previously been stored in the specified variable. (Responses are stored by setting the Store response in variable property for a step. SeeStoring a response into a variable (for use later in the test).) A response with zero values or multiple values is always stored in a list. You can specify whether to obtain a single extracted value as a scalar string or in a list. For details, see response command: Accessing response data that is stored in a variable Right-click shortcut: Insert > Stored Response > Local / Global |
| scan string format ?varName varName ...? | Parses substrings from an input string in a fashion similar to the ANSI C sscanf procedure. The command returns a count of the number of conversions performed, or -1 if the end of the input string is reached before any conversions have been performed. String gives the input to be parsed and format indicates how to parse it, using % conversion specifiers as in sscanf. Each varName gives the name of a variable; when a substring is scanned from string that matches a conversion specifier, the substring is assigned to the corresponding variable. If no varName variables are specified, then scan works in an inline manner, returning the data that would otherwise be stored in the variables as a list. In the inline case, an empty string is returned when the end of the input string is reached before any conversions have been performed. The iTest scan command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man/ |
| set varName ?value? | Sets a local variable to the specified value. Arrays: Use set a(1,2) foo syntax. (To create an array with one element, use the array command.) Lists: set a {1,2 foo} creates a list with two elements, the first element is "1,2" and the second is "foo". |
| split string ?splitChars? | Splits a string into a proper Tcl list. The command returns a list created by splitting string at each character that is in the splitChars argument. Each element of the result list will consist of the characters from string that lie between instances of the characters in splitChars. Empty list elements will be generated if string contains adjacent characters in splitChars, or if the first or last character of string is in splitChars. If splitChars is an empty string then each character of string becomes a separate element of the result list. SplitChars defaults to the standard white-space characters. The iTest split command is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/ |
| string option arg ?arg? | Manipulates strings by performing the string operation specified by option. The iTest string command is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/ Limitations: [string match args] supports only * and ? glob pattern sequences and does not support [chars] and \x. [string replace] does not accept Tcl's end. [string trim $attrs , ] is not supported. string concat arg arg … In addition to the standard string options, the iTest interpreter supports the [string concat arg arg ...] command which concatenates the string representations of all of the arguments into a single string. If all of the arguments are lists, this has the same effect as concatenating them into a single list. The command permits any number of arguments; if no arguments are supplied, the result is an empty string. |
| subst arg | Performs backslash, command, and variable substitutions on the string argument. The substitutions are performed in exactly the same way as for Tcl commands. As a result, the string argument is actually substituted twice; once by the Tcl parser in the usual fashion for Tcl commands, and again by the subst command. Limitations: No additional arguments are allowed. The command is otherwise compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man// If an error occurs during substitution, then subst will return the error. If a break exception occurs during command or variable substitution, the result of the whole substitution will be the string (as substituted) up to the start of the substitution that raised the exception. If a continue exception occurs during the evaluation of a command or variable substitution, an empty string will be substituted for that entire command or variable substitution (as long as it is well-formed Tcl.) If a return exception occurs, or any other return code is returned during command or variable substitution, then the returned value is substituted for that substitution. See the examples. In this way, all exceptional return codes are ``caught'' by subst. The subst command itself will either return an error or will complete successfully. Examples When it performs its substitutions, subst does not give any special treatment to double quotes or curly braces (except within command substitutions) so the script set a 44 subst {xyz {$a}} returns ``xyz {44}'', not ``xyz {$a}'' and the script When command substitution is performed, it includes any variable substitution necessary to evaluate the script. |
| tbml subcommand arg ?arg? | The tbml group of commands returns device and connection information from a topology. See Commands that return information about topologies. |
| tcl {statement} | Calls on the execution kernel's Tcl interpreter, evaluates the argument in the Description cell as a statement, and then returns the result of that evaluation. STDOUT and STDERR are not used. See tcl command: Evaluating Tcl statements in the execution kernel's Tcl interpreter. |
| tclexpr {expression} | Calls on the execution kernel's Tcl interpreter, evaluates the argument in the Description cell as an expression, and then returns the result of that evaluation. STDOUT and STDERR are not used. See tclexpr command: Evaluating Tcl expressions in the execution kernel's Tcl interpreter. |
| unset varName | Removes one local variable. Limitation: No additional arguments are allowed. The command is otherwise compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man/ |
| xpatheval xpathQuery | Evaluates the specified XPath query as applied to the root node of the current stack frame in the heap. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
