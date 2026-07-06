# Analysis Rules: Validating Responses > The structure of an analysis rule > The processor

The processor is the second line in the rule — it specifies the type of action to take and the details of the action to take on the extracted data.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The type of action to take appears in the Action cell. In the example, the action is to use the assert processor to test an assertion about the extracted value. Other processors chart the value, display an execution message, or store the value in a variable.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The details of the action to take appear in the Description cell. In the example, we specify the assertion to be tested: test whether the extracted data equals 42. The When True and When False substeps are a part of the assert processor that tell iTest to take a particular action when the assertion is true and a different action when the assertion is false.

If we had specified a message processor, the details of the action would be the text to display in the message.
