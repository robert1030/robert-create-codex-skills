---
{
  "chunk_id": "command_response__syntax_85604778c1d78ab5",
  "source_file": "topics/command_response.htm",
  "source_original_path": "topics/command_response.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "response command: Accessing response data that is stored in a variable"
  ],
  "heading_path": [
    "response command: Accessing response data that is stored in a variable",
    "response command: Accessing response data that is stored in a variable",
    "Syntax"
  ],
  "anchor": "1679261",
  "context_ids": [
    "command_response"
  ],
  "index_keywords": [
    "accessing response text stored in",
    "creating assertions",
    "response",
    "response command",
    "stored in variables",
    "using response command to create"
  ],
  "index_keyword_paths": [
    "assertion > using response command to create",
    "commands > response",
    "field replacements > response command",
    "response command",
    "response command > creating assertions",
    "response content > stored in variables",
    "variables > accessing response text stored in"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "85604778c1d78ab5",
  "level": 2
}
---

# response command: Accessing response data that is stored in a variable > response command: Accessing response data that is stored in a variable > Syntax

Tcl: response ?-alwayslist? ?-group numberOrName? varName ?regex?

? surrounding an argument means optional

Python: response('varName', alwaysList=True, regex='', group='number | name')

The optional -alwaysList (Tcl) or alwayslist (Python) flag is useful when you use the return data as the argument in a foreach statement. The flag causes a single returned value to be stored in a list with a single element, rather than in a scalar string. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single returned value can contain whitespace. When you use the -alwaysList (Tcl) or alwayslist (Python) flag, a foreach statement that iterates over the stored variable will loop once for the match (rather than once for each word in the match).

The optional -group flag and numberOrName argument is a regular expression that defines something more specific to return from the response text.

varName/variable_name Is the name of the variable containing the stored response. If varName includes whitespace, it must be surrounded by double-quotes (which will be excluded from the location query before use).

The optional regex argument is a regular expression that defines something more specific to return from the response text.

> **Note:** Recommendations

In any field that supports field replacements, the fastest way to insert a response command is to right-click at the intended location and select Stored Response.

If the regular expression in the command does not use substitution, then surround it with { } (Tcl) braces.

> **Note:** If there is a mismatched closing brace in the regex, then place double-quotes around the entire regex and place backslashes in front of all special characters (", [, ], $, \) except where you actually want substitution.
