---
{
  "chunk_id": "emulation_2__controlling_emulation_de42b4b2184c2e84",
  "source_file": "topics/emulation.2.htm",
  "source_original_path": "topics/emulation.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Overview: Using emulation"
  ],
  "heading_path": [
    "Overview: Using emulation",
    "Overview: Using emulation",
    "Controlling emulation"
  ],
  "anchor": "1170793",
  "context_ids": [],
  "index_keywords": [
    "configuring",
    "emulation",
    "enabling",
    "test simulation",
    "virtual testbeds"
  ],
  "index_keyword_paths": [
    "configuring > emulation",
    "configuring > test simulation",
    "configuring > virtual testbeds",
    "emulation > configuring",
    "emulation > enabling",
    "simulation > configuring",
    "virtual testbeds > configuring"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "de42b4b2184c2e84",
  "level": 2
}
---

# Overview: Using emulation > Overview: Using emulation > Controlling emulation

To cause iTest to return an emulated response for any particular step, you must set the following property settings:

- Emulation must be enabled for the test case (emulation must be “allowed”) — this is not the default setting.

- Emulation must be activated for the step (emulation must be explicitly “turned on” for the step) — again, this is not the default setting.

- Optional, but typical: You specify the text of the emulated response (you can tell iTest to use the response that was returned during the most recent execution against the actual device session). We discuss additional options in the following section.
