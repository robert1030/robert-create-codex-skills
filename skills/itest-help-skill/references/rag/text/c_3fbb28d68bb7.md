# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/getnext.html > getNext

Returns the value of the single MIB variable that follows the specified OID. The system uses the Get PDU to get values for scalar MIBs.

The structured data includes the OID value and iTest generates queries for OID and RAW_OID.

Tip: To use getNext in a loop for returning multiple values, the device's agent must implement a variable (the next variable) for loop control. If you intend to get values for all variables in a MIB, use walk instead.

For details, see the online help: Creating SNMP test case steps.
