# Response Maps: Returning Data from Responses > Making use of existing response map libraries: Chaining response maps > Requirements for response map chaining

A response map is chained only when the following conditions are true:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The step specifies a particular response map library. That is, for the step in the Test Case editor, the Other Post-processing > Expected Response property is set to Use the response map library configured for the session

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- For the session profile associated with the step's session, a response map library is specified on the Session Profile editor's Misc page.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The response map is applicable to the step. That is, on the Response Map editor's Applicability page, the settings result in the map being applicable to the step

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The response map library project is eligible to be chained. Response map chaining uses iTest Project Natures to determine whether a project is eligible to be chained. Only projects with the following natures can be chained:

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/response_mapping_2.2.jpg) <!-- image_ref -->

- iTest Default Project nature (For this nature, the icon for the project includes the iTest logo )

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/response_mapping.3.jpg) <!-- image_ref -->

- iTest Response Map Library nature (For this nature, the icon for the project includes an ‘R’ logo )
