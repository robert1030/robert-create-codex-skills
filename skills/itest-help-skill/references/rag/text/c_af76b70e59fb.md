# Testing with Emulated Sessions > Emulating sessions in test case steps > 第3段

Tip We recommend that you specify a response map library rather than an particular response map as the External source. In this way, rather than requiring you to specify a response map for each step in a test case, you can take advantage of iTest’s ability to auto-select the appropriate map based on Applicability and Priority property settings.

![*](bullet_blue.jpg) <!-- image_ref -->

1. Set the Sample name property: If you use the External source property to specify a response map library or response map as the external source for the emulated response, then use the Sample name property to specify the name of the response sample to use (that is, the sample from within the appropriate response map).

To enable the test case to dynamically determine the sample response at runtime, field replacements are supported in this field.
