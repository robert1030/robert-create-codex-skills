# Spirent Avalanche sessions > Avalanche API Commands > av_get > Comments > 第1段

The av_get command returns the value of one or more object attributes, or, in the case of relation references, one or more object handles.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The handle identifies the object from which data will be retrieved. If you do not specify any attributes, Avalanche Automation returns the values for all attributes and all relations defined for the object.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The attributeName identifies an attribute for the specified object.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The DANPath (Descendant Attribute Notation path) is a dotted path name beginning with a sequence of one or more relation names, and ending with an attribute name. A relation name may have an index suffix (an integer in parenthesis) to reference one of multiple children of the same type. Avalanche Automation combines the handle (or the DDNPath) with the DANPath to resolve the attribute reference. The path must identify a valid sequence of objects in the test hierarchy. For example:

```
av_get $project test(1).name
```

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Avalanche Automation combines the object and attribute specifications to retrieve the value of the attribute for the first Test object child of the $project.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The DDNPath (Direct Descendant Notation path) is a dotted path name sequence. The sequence begins with an object handle, followed by one or more relation names. The path must identify a valid sequence of objects in the data model hierarchy. Avalanche Automation returns data for the object identified by the last name in the sequence. For example:

```
av_get $project1.test -name
```

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- In this case, Avalanche Automation returns the value of the name attribute for the first Test child of the specified Project object.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If there is more than one instance of a particular object type, as children of the specified object, use an index notation. (In the example above, the index value 1 is implied.) Avalanche Automation assigns index values in the order of object creation. For example:

```
av_get $project.test(2)
```

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Avalanche Automation returns the attributes and all relations for the second Test object child of the specified Project object.
