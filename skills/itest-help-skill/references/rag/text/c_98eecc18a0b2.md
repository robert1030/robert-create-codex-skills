# Python Script Generation > Generate/Copy Python Script from Captured Steps > Edit Python Script

You may edit the generated Python Script and include the Python Automation Library commands as required. See also Basic Python Automation Library Commands.

If a test case with a Secret Parameter type is exported to Python, the script displays None as the secret parameter value. You may use any value or retrieve them from any source by editing script after export.

```
param = Params({
```

```
'secretParam': None,
```

```
})
```
