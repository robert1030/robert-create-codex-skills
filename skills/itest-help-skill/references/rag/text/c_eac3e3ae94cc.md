# iTest Topology Editor > "tbml" topology commands > Commands that return information about topologies > Example topology > property subcommand: Return value of a property

The tbml property command returns the value of a property on a resource or on a link.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The property subcommand can return multiple values if multiple properties match.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Because the property subcommand applies to both resources and link elements, the resource element takes precedence over link elements. If a property is not found in a resource element, then the link element is searched.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- To identify a property, use its id or name or displayName or a combination of id and one of name or displayName.

See tbml command syntax

TBML usage syntax

When using tbml commands, any strings that include spaces need to be surrounded with curly braces.

The following examples show the correct and incorrect usage:

Correct syntax

tbml property -id $deviceId {{System Identification} ipAddress}

OR the following in Python

tbml('property', '-id' , 'deviceId', '{System Identification}ipAddress')

Incorrect syntax

tbml property -id $deviceId {"System Identification" ipAddress}

OR

[tbml property -id $deviceId "System Identification" ipAddress]

or

tbml('property', '-id' , 'deviceId', ipAddress)

Error:

Unable to substitute " Device IP: tbml property -id $deviceId {"System Identification" ipAddress}": Cannot find property: com.fnfr.svt.iTestInterpreter.model.SubstString@e19679/ipAddress
