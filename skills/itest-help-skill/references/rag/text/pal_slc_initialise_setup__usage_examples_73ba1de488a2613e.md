---
{
  "chunk_id": "pal_slc_initialise_setup__usage_examples_73ba1de488a2613e",
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
    "Remote Velocity Agent",
    "Usage examples:"
  ],
  "anchor": "1471444",
  "context_ids": [
    "pal_slc_initialise_setup"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "73ba1de488a2613e",
  "level": 4
}
---

# Initializing/Setting up the Python Automation Library > Initializing/Setting up the Python Automation Library > Remote Velocity Agent > Usage examples:

velocity-agent.bat --agentVelocityHost localhost --sfAgentServerPort 9002 --listeningMode --licenseServer 10.100.86.1 --itar z:\downloads\itar

OR

set ITAR_PATH=z:\downloads\itar

velocity-agent.bat --agentVelocityHost localhost --sfAgentServerPort 9002 --listeningMode --licenseServer 10.100.86.1

> **Note:** Note Ensure that you escape (backslash ( \ ) character) all strings with backslash (\).

- Ensure escape (backslash ( \ ) character) ITAR_PATH path when setting up the path from python script. For example:

if __name__ == '__main__':

with SLC.init(itar_path='C:\\Users\\spirent\\Desktop\\testing', license_server='velocity-testlshost.spirenteng.com') as slc:

main(slc)

> **Note:** See https://docs.python.org/2.0/ref/strings.html for more information about working with string in Python.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
