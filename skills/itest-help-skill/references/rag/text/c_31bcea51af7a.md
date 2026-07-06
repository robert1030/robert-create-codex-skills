# SNMP Sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults > GetTable > iTest 3.1 compatibility mode

For iTest versions after 3.1, the format of the structured data for SNMP tables changed. This setting applies for SNMP getTable actions only.

iTest versions after 3.1 render the structured data with the row identifier (the part that gets suffixed to the OID) added as an attribute. The key attribute is added to the entry element (in the old format, the oid attribute was added to each field). The value for key is the same as the eliminated oid attribute and is up a level.

Each field gets a same-named query which takes key as its single argument. A values query will return all the keys.

Default: Unchecked

![](images/snmp_2.3.jpg) <!-- image_ref -->

For example, MIB-2::at.atTable has a compound key:
