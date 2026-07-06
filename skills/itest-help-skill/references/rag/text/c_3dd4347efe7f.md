# iTest Topology Editor > "tbml" topology commands > Commands that return information about topologies > Example topology > endpoint subcommand: Return resource IDs of two endpoint resources > Issues

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If the link is not found, iTest generates an onInterpreterError execution issue.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The starting link should be unique. If multiple links are found, iTest generates an onInterpreterError execution issue.

Note namePath argument is not supported because link elements cannot be hierarchical.

Note displayNamePath argument is not supported because link elements cannot be hierarchical.

Note The namePath and displayNamePath arguments are not supported because link elements cannot be hierarchical.

| 欄位1 | 欄位2 |
| --- | --- |
| tbml endpoint | Returns TBML endpoint values as specified. |
| tbml endpoint -name name tbml("endpoint", "-name", "name") | Returns the two endpoint resource IDs in a list for any link object given its name. Multiple matches are found if multiple links have the same name. Example tbml endpoint -name upstream tbml("endpoint", "-name", "upstream") Returns resource_0 and resource_1 because the two resources are at either end of the link with a name of upstream. |
| tbml endpoint -displayName displayName tbml("endpoint", "-displayName", "displayName") | Returns the two endpoint resource IDs in a list for the link object specified by its displayName. Multiple matches are found if multiple links have the same displayName. Example tbml endpoint -displayName upstream_displayName tbml("endpoint", "-displayName", "upstream_displayName") Returns resource_0 and resource_1 if the two resources are at either end of the link with a displayName of upstream_displayName. |
| tbml endpoint -id ID tbml("endpoint", "-id", "ID") | Returns the two endpoint resource IDs in a list for the link object that is specified by ID. Example tbml endpoint -id link_0 tbml("endpoint", "-id", "link_0") Returns resource_0 and resource_1 because the two resources are at either end of the link. |
