---
{
  "chunk_id": "emulation_5__emulation_quick_instructions_e6855c5fcbb31f00",
  "source_file": "topics/emulation.5.htm",
  "source_original_path": "topics/emulation.5.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Emulation: Quick instructions"
  ],
  "heading_path": [
    "Emulation: Quick instructions",
    "Emulation: Quick instructions"
  ],
  "anchor": "1164772",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "e6855c5fcbb31f00",
  "level": 1
}
---

# Emulation: Quick instructions > Emulation: Quick instructions

| To: | Do this: |
| --- | --- |
| Create a response “from scratch” when there is not yet anything to test | Select the step and then type the text into the Response view. |
| Enable emulation for the test case so that any step for which emulation is activated will execute with the emulated response | Either one of the following: In the Test Case menu, click Emulator > Enable Emulation for the Test Case On the Test Case editor General page, check Enable emulation for the test case |
|  | In the Test Case menu, click Emulator > Enable Emulation for the Test Case |
|  | On the Test Case editor General page, check Enable emulation for the test case |
| Turn off emulation for the test case so you can run a test against the actual devices | Either one of the following: In the Test Case menu, click Emulator > Disable Emulation for the Test Case On the Test Case editor General page, uncheck Enable emulation for the test case |
|  | In the Test Case menu, click Emulator > Disable Emulation for the Test Case |
|  | On the Test Case editor General page, uncheck Enable emulation for the test case |
| Emulate all responses for a particular session, regardless of whether any particular step has activated emulation | Select the open step for the session. 2. On the Emulation properties page, for the Emulate property, select Always. 3. Repeat as needed for any other sessions. |
|  | Select the open step for the session. |
| 2. | On the Emulation properties page, for the Emulate property, select Always. |
| 3. | Repeat as needed for any other sessions. |
| Using an existing response map library to provide emulated responses for all steps in a session (some steps might currently use the response map for analysis) | in the session profile or device for the session, set the External source property to the response map library and then enable emulation for the session’s open step. Note If you had already specified particular response text on the Emulation > Step Response page for some steps, then you can easily reset all emulation settings to make use of the external source (in particular, checking the Use External source checkbox for all steps): In the Emulation menu, select Clear Emulation For All Steps. |
| Note | If you had already specified particular response text on the Emulation > Step Response page for some steps, then you can easily reset all emulation settings to make use of the external source (in particular, checking the Use External source checkbox for all steps): In the Emulation menu, select Clear Emulation For All Steps. |
| Remove all emulation from the test case (in the case, for example, that the test case is fully debugged and ready for use) | In the Test Case menu, click Emulator > Clear All Emulation Properties for the Test Case Note If you want to keep a version of the test case that uses emulation, save a copy of the test case before performing this operation. |
| Note | If you want to keep a version of the test case that uses emulation, save a copy of the test case before performing this operation. |
| Update all steps that use emulation to use the responses from the latest execution against actual devices | In the Test Case menu, click Emulator > Update Emulation Responses for All Steps |
| Activate emulation for all sessions in the test case or for most sessions — all session responses are emulated | In the Test Case menu, click Emulator > Activate Emulation for All ‘open’ Steps. This sets the Emulate property to Always for all open steps and also enables emulation for the test case. To emulate responses for only particular sessions, click the menu item and then, for each session that should not be emulated: Select the open step. 2. On the Emulation properties page, for the Emulate property, select No. 3. Repeat as needed for any session. |
|  | Select the open step. |
| 2. | On the Emulation properties page, for the Emulate property, select No. |
| 3. | Repeat as needed for any session. |
| Disable emulation for all sessions in the test case — steps (other than ‘open’ steps) that have emulation turned on will still be emulated | In the Test Case menu, click Emulator > Deactivate Emulation for All ‘open’ Steps. This sets the Emulate property to No for all open steps. You can return to emulating all sessions by clicking Emulator > Activate Emulation for All ‘open’ Steps |
| Execute the emulated test case as fast as possible (ignore the duration for execution against actual devices) | On the Test Case editor General page, uncheck Enable emulation duration for the test case |
| Execute the emulated test case at the same speed as a execution against actual devices | On the Test Case editor General page, check Enable emulation duration for the test case During execution, iTest executes all emulated steps in the same amount of time as it took for the step in the actual session. As a reference, iTest uses the execution that you specified as the basis for the settings in the Emulation properties group. You can modify the Duration setting for any particular step as needed. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
