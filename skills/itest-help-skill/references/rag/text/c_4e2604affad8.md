# iTest Commands > iTest interpreter commands > Adding iTest interpreter commands to steps > Overview: Inserting a command as a field replacement

You can insert any command as a field replacement into an existing step Description or into a property setting. At runtime, before the property or step is interpreted, iTest substitutes the returned value for the field replacement. The generic format for a field replacement is:

[commandName args] in Tcl or commandName('arg') in Python

You do not have to remember the field replacement syntax. Just right-click anywhere that you can add a field replacement and select Insert to insert a properly formatted field replacement with hints about argument usage.

In this example, we have added the first portion of a device’s interface ethernet command (it is not a iTest command, rather a CLI command to the device’s management interface).

![](images/commands_2.3.jpg) <!-- image_ref -->

The interface ethernet command requires a port number as the argument (for example, interface ethernet 9). We want the iTest step to determine the port number dynamically at runtime from a parameter that supplies the value. We will add the port argument to the command text as a iTest param command. During execution, the param command will be replaced by the port number.

So, we place the cursor after “ethernet”, right-click, select Insert, and then select Parameter. The Insert Field tool then helps us to select the particular parameter to use (we chose “port”) and then inserts a param command (within the [ and ] brackets of a field replacement). Now the command will execute as desired.

![](images/commands.4.jpg) <!-- image_ref -->

For more detailed instructions, see Inserting field replacements using the Insert Field tool. Field replacements are fully described in “Field Replacements”.
