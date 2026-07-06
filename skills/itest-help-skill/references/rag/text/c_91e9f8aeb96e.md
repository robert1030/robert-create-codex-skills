# Field Replacements > Field replacements: Substituting values into properties and commands > Example: Using an iTest Tcl interpreter ‘param’ command in a field replacement

![*](bullet_blue.jpg) <!-- image_ref -->

1. The text strings [param PortType] and [param SubIndex] appear in the following step:

![](images/field_replacements.1.jpg) <!-- image_ref -->

The [param PortType] syntax means “Before running this step, replace all of the text in this field with the value of the PortType parameter”. (We will describe the syntax in a moment.)

1. 2 The test case has the following parameter settings:

```
PortType = FASTETHERNET
```

```
SubIndex = 0
```

1. 3 At runtime, step preprocessing replaces the fields. As a result, iTest issues the following command:

```
show interfaces FASTETHERNET 1/0indicator
```
