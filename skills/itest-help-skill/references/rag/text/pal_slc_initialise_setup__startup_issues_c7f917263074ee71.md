---
{
  "chunk_id": "pal_slc_initialise_setup__startup_issues_c7f917263074ee71",
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
    "Standalone mode",
    "Startup issues"
  ],
  "anchor": "1459281",
  "context_ids": [
    "pal_slc_initialise_setup"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "c7f917263074ee71",
  "level": 4
}
---

# Initializing/Setting up the Python Automation Library > Initializing/Setting up the Python Automation Library > Standalone mode > Startup issues

If you encounter standalone agent startup issues, enable the verbose mode parameter and review the log.

SPIRENT_SLC_VERBOSE=True

Example of velocity agent startup output.

--->Agent verbose output

Starting velocity agent:

PATH: /Users/user/example/spirent/velocity-agent.app/Contents/Eclipse/

LOG FILE: /var/folders/_m/dd5mtytd1zx9x8dx7vh7v7w40000gn/T/tmpzwzvd30xvelocity_agent/agent.log

ITARPATH: /Users/user01/Develop/git/spirent/itest/dev/src/non-plugins/SpirentSLC/examples/itars/

ARGUMENTS:

--agentVelocityHost

localhost

--sfAgentServerPort

9002

--listeningMode

library

--sfAgentDisableSslValidation

--licenseServer

itest-lic

--itar

/Users/user/example/git/spirent/itest/dev/src/non-plugins/SpirentSLC/examples/itars/

--->

> **Note:** Note The log folder and log file will be automatically deleted after the session is closed and all resources used by the Python Automation Library is released successfully.

> **Note:** slc.close()
