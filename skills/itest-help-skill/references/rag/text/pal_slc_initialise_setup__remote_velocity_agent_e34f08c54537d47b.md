---
{
  "chunk_id": "pal_slc_initialise_setup__remote_velocity_agent_e34f08c54537d47b",
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
    "Remote Velocity Agent"
  ],
  "anchor": "1449442",
  "context_ids": [
    "pal_slc_initialise_setup"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "e34f08c54537d47b",
  "level": 3
}
---

# Initializing/Setting up the Python Automation Library > Initializing/Setting up the Python Automation Library > Remote Velocity Agent

The Velocity agent can be started manually in ‘listening’ mode to serve local and remote Python Automation Library clients.

Follow these steps.

1. Start a Velocity agent

./velocity-agent --agentVelocityHost localhost --sfAgentServerPort 9005 --listeningMode --licenseServer mylic-server

> **Note:** Note The host and the port must be the same as those specified in the environment variables.

1. 2

1. Set the following environment variable from the Python Automation Library host machine:

SPIRENT_SLC_HOST=myhost:myport # a host and port of velocity agent

1. 3

1. Initialize SLC:

from SpirentSLC import SLC

slc = SLC.init() # will take all values from environment variables

# alternatively values may be provided in the init() call:

slc = SLC.init(host='localhost:9005')

> **Tip:** Tip The host and the port must be the same as those specified in the environment variables.
