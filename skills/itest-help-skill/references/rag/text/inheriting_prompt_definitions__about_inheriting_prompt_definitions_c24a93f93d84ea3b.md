---
{
  "chunk_id": "inheriting_prompt_definitions__about_inheriting_prompt_definitions_c24a93f93d84ea3b",
  "source_file": "topics/inheriting_prompt_definitions.htm",
  "source_original_path": "topics/inheriting_prompt_definitions.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "About inheriting prompt definitions"
  ],
  "heading_path": [
    "About inheriting prompt definitions",
    "About inheriting prompt definitions"
  ],
  "anchor": "1114781",
  "context_ids": [
    "inheriting_prompt_definitions"
  ],
  "index_keywords": [
    "inheriting",
    "prompt definitions"
  ],
  "index_keyword_paths": [
    "inheriting > prompt definitions",
    "prompt definitions > inheriting"
  ],
  "related_links": [],
  "images": [
    "topics/images/prompts_4.1.jpg"
  ],
  "content_hash": "c24a93f93d84ea3b",
  "level": 1
}
---

# About inheriting prompt definitions > About inheriting prompt definitions

Because you typically add a new prompt definitions to the existing set of definitions for a session profile or topology device, you usually choose to inherit the existing prompt definitions into the session profile and perhaps add to or delete from the inherited prompt definitions. You can use any of the following methods (detailed instructions follow):

- Inherit prompt definitions from the Reference session profile that you specified. The prompts from the reference profile are added to this profile. (This is the default behavior when you base one session profile on another.)

> **Note:** Note Inheritance can nest as deeply as needed.

- If session profile B is based on profile A (and therefore inherits A’s property settings),

- and profile Z is based on B,

- then Z inherits property settings from both A and B.

- Inherit prompt definitions and add new prompt definitions to the list of inherited prompts. If you decide to add prompts, then the inherited prompts become a part of the current session profile, but are not shown on the Prompts page in the list of prompts for the current profile.

The inherited prompts are updated when the definitions in the reference session profile change.

- Start with the prompt definitions from the reference session profile and edit/delete them as needed. In addition, you can define new prompts for the session profile.

Because the inherited prompts are now a part of the new profile, they are not updated when the prompts in the reference session profile change.

![screenshot](topics/images/prompts_4.1.jpg) <!-- image_chunk: img_1d94600feee25097 -->
