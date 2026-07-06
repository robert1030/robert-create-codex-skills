# Procedures > Creating a ‘call’ step using the Procedure Call wizard > To add a call step > 第1段

Start the Procedure Call wizard using one of the following methods:

![*](bullet_blue.jpg) <!-- image_ref -->

1. Select the step just before where the call step should go.

1. 2 Now, do one of the following:

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/procedures_2.1.jpg) <!-- image_ref -->

- In the toolbar, select the arrow on the Insert button and select Insert Procedure Call Using Wizard

![*](bullet_blue.jpg) <!-- image_ref -->

- Right‑click the step and select Insert > Insert Procedure Call Using Wizard

![*](bullet_blue.jpg) <!-- image_ref -->

- In the Test Case menu, select Insert > Insert Procedure Call Using Wizard

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/procedures.2.jpg) <!-- image_ref -->

- Add a step with an Action of call. Optional: If you know the name of the procedure to call, you can specify its name in the Description cell (as described in Step 2: Specify the procedure to call). As a result, the wizard page will be “filled in” with information about the procedure. Click in the Description cell to start the Procedure Call wizard.

Now, work in the Procedure Call wizard

![](images/procedures.3.jpg) <!-- image_ref -->

1. 3 In the Test Case box, select the test case (procedure library) that contains the procedure.

1. 4 In the Procedure box, select the procedure.

1. 5 Now you can view and edit argument settings.

As you work, you will notice that the Command text box is updated to reflect your changes. The text in the Command text box is usually exactly what you need, but if necessary, you can edit the text directly (for example, to add numbered arguments).

> **Note：** Note The text in the Command Text box follows the normal convention for procedure calls; an argument that uses its default value does not appear. When the call step executes, however, the default value will be passed to the procedure in the normal way.

![*](bullet_blue.jpg) <!-- image_ref -->

- When you select an argument, the Description box displays the argument name and other property settings for the argument. If the person who defined the argument set the appropriate values, then this information should help you to understand the argument and its usage.

![*](bullet_blue.jpg) <!-- image_ref -->

- The Arguments table lists all named arguments. An argument’s default value (if defined) appears in the Value cell.

![*](bullet_blue.jpg) <!-- image_ref -->

- To change a value, click in the Value cell and type the new value.
