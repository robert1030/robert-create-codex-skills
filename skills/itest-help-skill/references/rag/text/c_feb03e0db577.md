# iTest Views > Favorites view > Starting a session using a device

When you start a session using the device in the Favorites view and then save the session into a test case, you make the test case more portable because the resulting open step refers to a device rather than a session profile. See Overview: Creating a test case.

If the test case specifies a different topology, then the open step refers to the session profile (or session type URI) that is specified in the Inherits from property for the device. The properties of the open step are taken from the device definition in the topology file.
