---
{
  "chunk_id": "pal_slc_initialise_setup__itest_gui_mode_8d14f5d20c6c8818",
  "source_file": "topics/pal_slc_initialise_setup.htm",
  "source_original_path": "topics/pal_slc_initialise_setup.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Initializing/Setting up the Python Automation Library"
  ],
  "heading_path": [
    "Initializing/Setting up the Python Automation Library",
    "Initializing/Setting up the Python Automation Library",
    "iTest GUI mode"
  ],
  "anchor": "1447068",
  "context_ids": [
    "pal_slc_initialise_setup"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "8d14f5d20c6c8818",
  "level": 3
}
---

# Initializing/Setting up the Python Automation Library > Initializing/Setting up the Python Automation Library > iTest GUI mode

Ensure that the following environment variables are set on the workstation where the Python Automation Library is installed and the script will run:

SPIRENT_SLC_HOST=localhost:port # must be host and port of the configured instance of iTest GUI

For example, if the GUI is configured with defaults, the environment variable would be set to:

SPIRENT_SLC_HOST=localhost:9005

An instance of iTest must be running on the specified host and must be configured to accept connections at the desired port.

from SpirentSLC import SLC

slc = SLC.init() # will take all values from environment variables

# alternatively values may be provided in the init() call:

slc = SLC.init(host='localhost:9005')

An exception will display if the library is unable to connect to the iTest GUI instance.
