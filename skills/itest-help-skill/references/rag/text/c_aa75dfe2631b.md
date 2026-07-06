# Actions > Actions for CLI session types > The command action: Submit a command

The command action is available only for CLI sessions and submits the text that appears in the Description cell (the value of the Command property). command is the most commonly used action in CLI test cases.

> **Note：** Note By default, iTest sends a carriage return + linefeed sequence when the Command cell is blank, so there is no need to include [char \r\n] in the Command or Description cell for blank commands.

In the example, step 2 submits the show ip traffic command to the 3750telnet session.

![](images/actions_3.1.jpg) <!-- image_ref -->
