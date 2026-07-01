---
{
  "chunk_id": "prompts_5__example_cisco_7e2c520a8b75a35b",
  "source_file": "topics/prompts.5.htm",
  "source_original_path": "topics/prompts.5.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Editing prompt definitions"
  ],
  "heading_path": [
    "Editing prompt definitions",
    "Editing prompt definitions",
    "Example: Cisco"
  ],
  "anchor": "1120881",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "7e2c520a8b75a35b",
  "level": 2
}
---

# Editing prompt definitions > Editing prompt definitions > Example: Cisco

Let's look at the prompts on a Cisco device. Upon starting a session, no username is required, just a password. Therefore, this device does not require a login0 prompt. The password0 prompt is the same as for the Linux example.

User Access Verification

Password:

3750>enable

Password:

3750#config t

Enter configuration commands, one per line. End with CNTL/Z.

3750(config)#

The normal0 prompt is the device name 3750 followed by a greater than sign >. If we submit the enable command to change to enable mode on the device, the prompt changes to 3750#. If we go into configuration mode, the prompt changes yet again to 3750(config)#.
