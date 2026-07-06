# SNMP Sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults > Set

Note If you check the box, the Value type property is ignored.

Note It is typically best to set this property for an individual step in the Test Case editor.

- **Execute a get action before executing set**：Check the box to cause iTest to execute a get action before executing any set action.This option enables you to correctly set a variable whose type you do not know before execution — the type returned by the get action is used to perform the set action. Uncheck the box to execute only a set action for a set step. You specify the type using the Value type property. Default: unchecked
- **Value type**：If you know the type of the value to set for any set action, then you can specify the type here. (This option is available only if you uncheck the Execute a get action before executing set check box.) Default: [blank] (that is, no type is specified)
