---
{
  "chunk_id": "python_script_generation_from_capture_st__add_to_python_script_1b96608c0de7766a",
  "source_file": "topics/python_script_generation_from_capture_steps.htm",
  "source_original_path": "topics/python_script_generation_from_capture_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Script Generation",
    "Generate/Copy Python Script from Captured Steps"
  ],
  "heading_path": [
    "Generate/Copy Python Script from Captured Steps",
    "Generate/Copy Python Script from Captured Steps",
    "Add to Python Script"
  ],
  "anchor": "1451018",
  "context_ids": [
    "python_script_generation_from_capture_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/ps_add_to_python_script_wiz.png",
    "topics/images/ps_drag_capture_items_into_python_script.png",
    "topics/images/ps_preferenes_change_script_generated.png"
  ],
  "content_hash": "1b96608c0de7766a",
  "level": 2
}
---

# Generate/Copy Python Script from Captured Steps > Generate/Copy Python Script from Captured Steps > Add to Python Script

Clicking this option on the Capture View toolbar or from the right-click menu, renders script that contains initialization code and all necessary import in addition to the steps.

- Includes the selected open steps and the import commands. Where applicable, includes the topology used.

The test session object names used in the exported Python script uses the same session names shown in the capture view.

> **Note:** Note You may specify a name and a documentation string of the procedure that will contain captured steps.

- The generated Python script will contain code for all selected captured steps, including the necessary import code for imports and library initialization, e.g., from SpirentSLC import SLC, and init() method to connect to the localhost iTest GUI.

The Python Script includes custom step properties, that is,

- step properties are rendered in the generated Python code

- includes step properties in the session commands

This is to ensure the commands, for example, REST POST, that include custom step properties to be complete, are also included in the Python Script.

> **Note:** Note The content of the script conforms to a logical mapping from the XML content to their corresponding commands in Python syntax.

- The selected captured steps are converted into Procedures with the name specified by you in the Add to Python Script Wizard.

- iTest converts regular session actions and quick-calls (e.g., print_hello quick-call for tcl-session).

- The Python script generator supports sessions with individual profiles and sessions associated with topology devices (e.g., router session initialization).

- Script will also open all required projects.

- Variables of different sessions with the same profile will have unique names.

You may drag step(s) into an open file in the text editor. In this case, only the steps will be inserted into the Python Script file and not the import command and the init() method.

By default, SLC initialization code connects to the iTest GUI on localhost, for example SLC.init(host="localhost:9005"). You may remove host="localhost:9005" in your Python script editor if you wish to connect to the background agent. The port ID number comes from the Preferences settings.

![screenshot](topics/images/ps_add_to_python_script_wiz.png) <!-- image_chunk: img_52a61824e7cfc625 -->

![screenshot](topics/images/ps_drag_capture_items_into_python_script.png) <!-- image_chunk: img_e0e66d641ae75b73 -->

![screenshot](topics/images/ps_preferenes_change_script_generated.png) <!-- image_chunk: img_cecebce679c87120 -->
