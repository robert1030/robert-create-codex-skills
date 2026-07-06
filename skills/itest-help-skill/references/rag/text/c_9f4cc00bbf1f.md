# Analysis Rules: Validating Responses > Applying queries to stored responses > Inserting a query that returns a value from a stored response > 第2段

```
Tcl: table/row[1]/fieldB
```

```
Python: query("myResponse", "table/row[1]/fieldB")
```

In this case, the square brackets will not be appropriate for interpreter substitution, use:

```
[query myResponse table/row[1]/fieldB]
```

Note Even though the response to the current step may appear in the Stored Responses list, it makes no sense to select it for this purpose – the step will not have been executed when the field replacements are made and there is therefore no response for the step.

If a special character (“ \ [ ] $ or the space character) appears in the query, then, in the Field replacement text box, the \ character is inserted to escape the special character. The result is a properly-formatted field replacement.
