# SNMP Sessions > Loading your proprietary MIB files into iTest > Two options

There are two options for specifying which MIBs to load:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Specifying a different folder for MIBs: You set a property that causes iTest to look in another folder. This option has the advantage that the MIB definitions are independent of the computer on which iTest is running (for example, when your test group uses a standard location for MIB files). Subfolders are not supported, so all of the individual MIB definition files must appear in the specified folder. If you want to use the standard MIB files that iTest provides, then you must copy them to the folder.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Copying your MIBs into the default folder (Not recommended): You copy your MIBs into the default folder (resources/SNMP/Mibs). Subfolders are not supported, so you copy the individual MIB definition files. This option is not recommended because it has the following disadvantage: If you discover problems with the custom MIBs, it might not be easy to locate and remove them.

> **Tip：** Tip To ensure good performance, add only the MIBs that you expect to use for testing.
