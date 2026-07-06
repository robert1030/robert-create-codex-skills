# iTest Topology Editor > Velocity command > Commands that return information from Velocity > velocity command syntax > reservedPortList subcommand:

Example Tcl: [velocity reservedPortList]

Example Python: velocity("reservedPortList")

The reservedPortList subcommand retrieves all topology ports (which might be concrete or abstract) of the specified device and then returns the list of their mappings. The return value format is the same as for the allPortList subcommand.

> **Note：** Note The subcommand reservedPortList returns port numbers only and not the port names.

You can specify the device in the same way as the property subcommand.
