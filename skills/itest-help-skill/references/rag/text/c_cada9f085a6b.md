# Spirent Avalanche sessions > Spirent Avalanche session window > Test Control section

The buttons in this section control test operation.

![](images/spirent_avalanche.03.jpg) <!-- image_ref -->

1. Click Configure. 2. In the Configure Test Parameters dialog box, select the parameter value in the Value cell and type the new value. Change as many values as needed. Parameters are described in Parameters (Available when you click Configure).

3. Click OK to apply the settings. iTest captures a single setParameter action that sets all the values.

- **Start**：Start the Avalanche test. iTest captures a start action.
- **Stop**：Stop the Avalanche test. The test ends and returns results. iTest captures a stop action. The button is disabled if you specify Use Avalanche Tcl test files for the session. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode) for details.
- **Abort**：The test ends and does not return results. iTest captures an abort action.
- **Configure**：The configuration settings for the current session are taken from the configuration script that was specified in the session profile or device. Click Configure to change any number of parameter settings for the duration of the current session only — the configuration script is not modified. The button is disabled if you specify Use Avalanche Tcl test files for the session. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode) for details. Changing a setting To find a particular parameter quickly, you can type a search string in the filter text box at the top. You can use the * wildcard character. Only parameters with matching text then appear in the list. Click Clear to remove the filter text. To revert to the settings that were in place when you opened the Configure Test Parameters dialog box, click Restore Defaults. Once you click OK, you cannot click Restore Defaults to revert to earlier settings.
