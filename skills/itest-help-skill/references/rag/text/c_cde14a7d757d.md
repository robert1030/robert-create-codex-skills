# Analysis Rules: Validating Responses > Analysis rules: Properties of the processor > Store processor > 第1段

The store processor stores the data that is extracted while processing the rule as a variable or a response value.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A response with zero values or multiple values is always stored in a list.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can specify whether to store a single extracted value in a scalar string or in a list. See the Always store data in a list property for recommendations when a single extracted value can contain whitespace.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Store processor also supports response value from the JSON response (see Procedure Properties > Inputs and Outputs > Response in section Defining a procedure of “Procedures”).

> **Tip：** Tip You can store a value from the response to a step (e.g., step 12). In a later step (e.g., step 19), you can add a rule about a token in step 19 and compare its value to the value of the token extracted in step 12. So, for step 19, you can create an assertion like: $value > $tokenStep12 * 2

> **Note：** Note You may open the context specific information—Processor Properties section in the Properties pane. Right-click and select the Show Properties View option from the menu. You may edit properties using either the Processor Properties section (within the Test Case Editor) or via the Properties View tab.
