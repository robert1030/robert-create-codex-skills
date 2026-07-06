# iTest Commands > Commands that are commonly used in field replacements > response command: Accessing response data that is stored in a variable > Syntax

Tcl: response ?-alwayslist? ?-group numberOrName? varName ?regex?

? surrounding an argument means optional

Python: response('varName', alwaysList=True, regex='', group='number | name')

The optional -alwaysList (Tcl) or alwayslist (Python) flag is useful when you use the return data as the argument in a foreach statement. The flag causes a single returned value to be stored in a list with a single element, rather than in a scalar string. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single returned value can contain whitespace. When you use the -alwaysList (Tcl) or alwayslist (Python) flag, a foreach statement that iterates over the stored variable will loop once for the match (rather than once for each word in the match).

The optional -group flag and numberOrName argument is a regular expression that defines something more specific to return from the response text.

varName/variable_name Is the name of the variable containing the stored response. If varName includes whitespace, it must be surrounded by double-quotes (which will be excluded from the location query before use).

The optional regex argument is a regular expression that defines something more specific to return from the response text.

Recommendations

In any field that supports field replacements, the fastest way to insert a response command is to right-click at the intended location and select Stored Response.

If the regular expression in the command does not use substitution, then surround it with { } (Tcl) braces.

If there is a mismatched closing brace in the regex, then place double-quotes around the entire regex and place backslashes in front of all special characters (", [, ], $, \) except where you actually want substitution.
