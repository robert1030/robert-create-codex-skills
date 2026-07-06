# Actions > Actions for CLI session types > The ‘writeFile’ action: Write information to a file > Adding a writeFile step

1. 1 Create the step with an Action of writeFile. Do not specify a session.

1. 2 In the Description cell, type or paste the URI or file path of the file to write to. Type a space character and then type or paste the contents to write to the file. Field replacements are supported. For example, the file contents to write can be [query myMultivaluedResponse <myQuery>] where myMultivaluedResponse is storing a response.

1. 3 In the Step Properties section, open the EXEC writeFile Properties > writeFile properties group and specify settings for the following properties:

> **Note：** Note The writeFile action is supported for both TCL and Python.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Text: The data to be written is treated as a sequence of lines. Depending on other property values, line delimiters can be changed on file writing. Binary: The data from specified variable is written as is, without any processing

Note If File type is set to Binary then this property is ignored

Note If File type is set to Binary then this property is ignored

- **If file exists**：This property applies only if the specified file already exists at the time that the test case tries to write to it. Specify whether to overwrite (replace) the file or to append the specified data to the end of the file. Default: Append
- **File type**：This property specifies how file writing is performed. Default: Text
- **Add a new line at the end of the file**：Check the box to add a blank line to the end of the text file after writing the specified data into the file. iTest will add the characters specified in the Line delimiter property Default: checked
- **Line delimiter**：Optional. This property applies only if the specified text file content consists of multiple lines. Specify the delimiter character to use to separate lines of data in the file. Default: Use the default delimiter for this platform
- **Encoding**：Optional. Specify the encoding type for text data to use so that, later, it can be properly parsed. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8

Note If File type is set to Binary then this property is ignored Note Syntax for substitution:

TCL: $path $cont

Python: [path] [cont]
