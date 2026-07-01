---
{
  "chunk_id": "command_tbml__issues_30c67cfdcd176109",
  "source_file": "topics/command_tbml.htm",
  "source_original_path": "topics/command_tbml.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "\"tbml\" topology commands",
    "Commands that return information about topologies"
  ],
  "heading_path": [
    "Commands that return information about topologies",
    "Commands that return information about topologies",
    "Example topology",
    "property subcommand: Return value of a property",
    "Issues"
  ],
  "anchor": "1380049",
  "context_ids": [
    "command_tbml"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/tbmlPythonCurlyBrackets.png",
    "topics/images/topologies_5.3.jpg"
  ],
  "content_hash": "30c67cfdcd176109",
  "level": 4
}
---

# Commands that return information about topologies > Commands that return information about topologies > Example topology > property subcommand: Return value of a property > Issues

- If a resource or link with the specified id, name, or displayName is not found, and a default value is not specified using the -default (Tcl) default (Python) argument, then iTest generates an onInterpreterError execution issue.

- In the event that the resource was not found for the specified ID, name, or displayName, iTest generates an onInterpreterError execution issue.

- The starting resource should be unique. If multiple resources are found, iTest generates an onInterpreterError execution issue.

| tbml property | Returns property value, Id, etc., as specified |
| --- | --- |
| tbml property -id ID propertyPath tbml("property", "-id", "ID", "propertyPath") | For a resource or link with ID of ID, returns the value of the property at propertyPath. propertyPath is the path to a property using the name of the property. Example tbml property -id resource_0 name tbml("property", "-id", "resource_0", "name") tbml('property', '-name', 'REST', 'ipAddressV4') returns the value of the name property for the resource with ID resource_0. In the example, returns myRouter Note In Python, list unnamed arguments first and then a named argument in any order. An unnamed argument cannot be listed after a named.argument. E.g., name=value arguments can only be at the end of a procedure call. For e.g., my_procedure(arg1, arg2, ..., argN, kwArg1=val1, ... k2ArgN=valN) |
| Note | In Python, list unnamed arguments first and then a named argument in any order. An unnamed argument cannot be listed after a named.argument. E.g., name=value arguments can only be at the end of a procedure call. |
| tbml property -name namePath propertyPath (Valid only in iTest Topology editor) tbml(’property’, ’-name’, ’namePath’, ’propertyPath’’,) | Returns the value of the property specified by propertyPath for the resource or link specified by namePath. Example tbml(’property’ ’-name’ ’myRouter card1’ ’{System Identification} [list ’my property collection’ myCustomProperty]’) tbml(’property’, ’-name’, ’myRouter card1’, ’System Identification} myCustomProperty’) tbml('property', '-name', 'myPC', '{System Identification} ipAddress') First, finds the resource card1.We specified the full name path starting from the top level resource which is myRouter. 2. Then finds the value for myCustomProperty, which is a child of the property collection group called my property collection. In the example, returns the value hello world Python supports complex tbml commands that allows use of braces to surround a string with space characters. See Examples below. tbml(’property’, ’-name’, ’{My PC}’, ’{My New Property}’) tbml(’property’, ’-name’, ’FRR {vnic 1}’, ’Networking {IP address}’) |
|  | First, finds the resource card1.We specified the full name path starting from the top level resource which is myRouter. |
| 2. | Then finds the value for myCustomProperty, which is a child of the property collection group called my property collection. |
| tbml property -displayName DisplayNamePath propertyPath tbml("property", "-displayName", "DisplayNamePath", "propertyPath") | Returns the value of the property specified by propertyPath on the resource that is specified by DisplayNamePath. Example tbml property -displayName "myRouter_displayName card1_displayName port1_displayName" ipAddressV4 tbml('property', '-id', 'resource_0', '-displayName', 'card1_displayName port1_displayName', 'ipAddressV4'] First, finds the resource port1 (because we specified the resource or link full name path starting from the top‑level resource myRouter). 2. Now that port1 is found, finds the ipAddressV4 property on port1. In the example, returns the value 10.100.2.3 |
|  | First, finds the resource port1 (because we specified the resource or link full name path starting from the top‑level resource myRouter). |
| 2. | Now that port1 is found, finds the ipAddressV4 property on port1. In the example, returns the value 10.100.2.3 |
| tbml property -id ID -name namePath propertyPath tbml("property", "-id", "ID", "-name", "namePath", "propertyPath") | For a resource or link with ID of ID, returns the value of the property at propertyPath. namePath is the hierarchical path using the name property relative to the resource or link with the specified ID. propertyPath is the path to a property using the name of the property. Example tbml property -id resource_0 -name "card1 port1" ipAddressV4 tbml("property", "-id", "resource_0", "-name", "card1 port1", "ipAddressV4") First, finds the resource with ID resource_0. 2. Next, finds a child resource of resource_0 that has the name card1. 3. Then finds a child resource of card1 that has name port1. 4. Now that port1 is found, finds the ipAddressV4 property for port1. In the example, returns the value 10.100.2.3 |
|  | First, finds the resource with ID resource_0. |
| 2. | Next, finds a child resource of resource_0 that has the name card1. |
| 3. | Then finds a child resource of card1 that has name port1. |
| 4. | Now that port1 is found, finds the ipAddressV4 property for port1. In the example, returns the value 10.100.2.3 |
| tbml property -id ID -displayName displayNamePath propertyPath tbml("property", "-id", "ID" "-displayName", "displayNamePath", "propertyPath") | For a resource or link with ID of ID and for a property on the resource with a displayName of DisplayNamePath, returns the value of the property specified by propertyPath. displayNamePath is the hierarchical path using displayName property relative to the resource or link with the specified ID Example tbml property -id resourece_0 -displayName "card1_displayName" "port1_displayName" ipAddressV4 tbml('property', '-id', 'resourece_0', '-displayName', '"card1_displayName"', '"port1_displayName"', 'ipAddressV4') First, finds the resource with ID resource_0. 2. Next, finds a child resource of resource_0 that has a displayName of card1_displayName. 3. Then finds a child resource of card1 that has a displayName of port1_displayName. 4. Now that port1 is found, it finds the ipAddressV4 property on port1 and returns the value 10.100.2.3 |
|  | First, finds the resource with ID resource_0. |
| 2. | Next, finds a child resource of resource_0 that has a displayName of card1_displayName. |
| 3. | Then finds a child resource of card1 that has a displayName of port1_displayName. |
| 4. | Now that port1 is found, it finds the ipAddressV4 property on port1 and returns the value 10.100.2.3 |
| tbml property propertyPath tbml("property", "propertyPath") | Returns the value of the specified property for the topology itself (Expressed another way; returns the value of the specified property that appears in the tbml file's header element). Examples [tbml property description] tbml("property", "description") Returns the value of the description property for the topology. tbml property [list "my collection"] myProperty In the example, returns the value of the myProperty property, which is a child of the property collection called "my collection". |
| tbml property -vendorId?vendorID? <any other arguments> tbml("property", "-vendorId", "vendorID", "any other arguments") | For all variations of the property subcommand, you can specify an optional -vendorId argument to find all properties with the vendor ID specified by vendorID. If the vendorID value is specified and a property match exists but has a different vendor ID, then returns an empty list. If no vendorID value is specified and multiple properties match, each with different or no vendor ID, then returns all matches. If a vendorID value is specified and a property match exists but does not have a vendorID, then returns an empty list. If the property is a member of a property collection, then, in the case that the collection includes other collections, the vendorID match test is applied only to the top-level property collection. In this example, if you specify vendorA, then propertyC-vendorC is returned even though it is a vendorC property. Example tbml property -vendorId com.spirent -id resource_0 author tbml("property", "-vendorId", "com.spirent-id", "resource_0", "author") Returns the values of all properties named author whose vendorID is set to com.spirent on the resource with ID of resource_0. |
|  | If the vendorID value is specified and a property match exists but has a different vendor ID, then returns an empty list. |
|  | If no vendorID value is specified and multiple properties match, each with different or no vendor ID, then returns all matches. |
|  | If a vendorID value is specified and a property match exists but does not have a vendorID, then returns an empty list. |
|  | If the property is a member of a property collection, then, in the case that the collection includes other collections, the vendorID match test is applied only to the top-level property collection. In this example, if you specify vendorA, then propertyC-vendorC is returned even though it is a vendorC property. |
| tbml property -default defaultValue <any other arguments> tbml("property", "-default", "defaultValue", "any other arguments") | For all variations of the property subcommand, you can specify a default value to return in the case that no property value was found. If the -default option is not used and no property was found, iTest generates an onInterpreterError execution issue. Example tbml property -default Sam -id resource_0 author tbml("property", "-default", "Sam", "-id", "resource_0", "author") Returns the values of all author properties on resource with ID resource_0. In the example, if no value is returned for the author property, returns Sam |

![screenshot](topics/images/tbmlPythonCurlyBrackets.png) <!-- image_chunk: img_aba8ad7e95b876ad -->

![screenshot](topics/images/topologies_5.3.jpg) <!-- image_chunk: img_8447da31ebeb8393 -->
