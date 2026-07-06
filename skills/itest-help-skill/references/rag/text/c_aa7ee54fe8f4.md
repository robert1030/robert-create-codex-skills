# Testing with Emulated Sessions > Emulating sessions in test case steps > How the sample is determined at runtime > 第2段

- The Use step response option is selected

![*](bullet_blue.jpg) <!-- image_ref -->

- The Use external source option is selected, but the External source is not specified for the step or in the session profile or device associated with the step

![*](bullet_blue.jpg) <!-- image_ref -->

- The Use external source option is selected and the External source is a response map library, but iTest cannot identify an appropriate response map based on Applicability and Priority property settings.

![](images/emulation.3.jpg) <!-- image_ref -->

On the Emulation > Step Response page for the step, configure the following properties. Remember that iTest can perform runtime substitution for any properties marked by the field replacements indicator .

![](images/emulation.4.jpg) <!-- image_ref -->

Note For more information, see Configuring sessions and test case steps for TL1 devices.

Note iTest emulates only the structured data from the response; it does not emulate structured data that is appended by response mapping.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

The value “step” means the response came from the Step Response properties A value of “<source_uri>#<sample_name>” appears when the response came from a sample in a response map
