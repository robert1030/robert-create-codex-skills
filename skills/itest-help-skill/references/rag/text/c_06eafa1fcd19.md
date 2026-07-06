# iTest Topology Editor > "tbml" topology commands > Commands that return information about topologies > Example topology > remoteEndpoint subcommand: Return the resource ID of connected resource > Issues

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If the resource is not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The starting resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| 欄位1 | 欄位2 |
| --- | --- |
| tbml remoteEndpoint | Returns TBML remoteEndpointvalues as specified. |
| tbml remoteEndpoint -name namePath tbml("remoteEndpoint", "-name", "namePath") | Example tbml remoteEndpoint -name "myRouter card1" tbml("remoteEndpoint", "-name", "myRouter card1") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -displayName displayNamePath tbml("remoteEndpoint", "-displayName", "displayNamePath") | Example tbml remoteEndpoint -displayName "myRouter_displayName card1_displayName" tbml("remoteEndpoint", "-DisplayName", "myRouter_displayName card1_displayName") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -id ID tbml("remoteEndpoint", "-id", "ID") | Example tbml remoteEndpoint -id resource_0_0 tbml("remoteEndpoint", "-id", "resource_0_0") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -id ID -name namePath tbml("remoteEndpoint", "-id", "ID", "-name", "namePath") | Example tbml remoteEndpoint -id resource_0 -name card1 tbml("remoteEndpoint", "-id", "resource_0", "-name", "card1") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
| tbml remoteEndpoint -id ID -displayName displayNamePath tbml("remoteEndpoint", "-id", "ID" "-displayName", "displayNamePath") | Example tbml remoteEndpoint -id resource_0 -displayName card1_displayName tbml("remoteEndpoint", "-id", "resource_0", "-displayName", "card1_displayName") Returns resource_1_0 because card1 is connected to card1 on mySwitch |
