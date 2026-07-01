---
{
  "chunk_id": "pal_slc_initialise_setup__standalone_mode_a3993a3c30144d42",
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
    "Standalone mode"
  ],
  "anchor": "1447058",
  "context_ids": [
    "pal_slc_initialise_setup"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a3993a3c30144d42",
  "level": 3
}
---

# Initializing/Setting up the Python Automation Library > Initializing/Setting up the Python Automation Library > Standalone mode

Python API can auto-launch an agent on the local host, run in the background for the duration of the Python session (on port 9002 by default), and uses these (below) environment variables. Ensure that the following environment variables are set on the workstation where the library is installed and on which the script will run:

SPIRENT_SLC_HOST=local

# local is special keyword to startup Velocity Agent locally.

ITAR_PATH=path to folder where iTars are placed, can contain compressed or exploded projects

SPIRENT_SLC_AGENT_PATH=a path to folder where iTest agent is located.

SPIRENT_SLC_LICENSE_SERVER=a license server

ITAR_PATH set on the local environment indicates the folder where the iTars and exploded project folders are placed, so that the local execution agent can find the projects.

ITAR_PATH can be set as an environment variable on agent machine or specified as a command line argument.

The ITAR_PATH is not mandatory when connecting to a running instance of iTest GUI.

from SpirentSLC import SLC

slc = SLC.init()

Calling SLC.init() will initialize the underlying execution agent as a background process with which the library will communicate. An object is returned which is the entry point for further communication with the library.

> **Note:** Note The current release supports only one init() call within one Python interpreter context. An exception displays if unable to initialize the library. Every additional call will return same session object. For example:

>> slc1 = SLC.init()

>> slc2 = SLC.init()

>> slc3 = SLC.init()

The SLC.init() method also accepts two optional parameters to set license server information with the same meaning:

license_server

Example usage:

slc = SLC.init(license_server='testlshost.spirenteng.com:27000')
