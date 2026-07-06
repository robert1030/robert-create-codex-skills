# QuickCalls: Defining and using a library of custom actions > Executing a QuickCall during a manual (interactive) session > Executing a QuickCall during an interactive session > Executing QuickCalls with secret type parameter

When Python SLC connected to iTest GUI and try access QuickCalls with secret values will trigger iTest GUI to show dialog to enter this secret values.

Executing QuickCalls that required secret value when iTest GUI is configured in listening mode (see Configure Listening Mode (Listen for incoming Python connections)), a dialog displays for entering the secret value. However, no output will be sent to the SLC library as response for any QuickCalls that use secret value.

![](images/qc_secretParameter_inSLCMode.png) <!-- image_ref -->

See About the Parameter Type ‘Secret’.
