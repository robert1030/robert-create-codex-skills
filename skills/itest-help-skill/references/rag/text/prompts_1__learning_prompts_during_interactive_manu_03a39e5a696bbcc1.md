---
{
  "chunk_id": "prompts_1__learning_prompts_during_interactive_manu_03a39e5a696bbcc1",
  "source_file": "topics/prompts.1.htm",
  "source_original_path": "topics/prompts.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Overview: Prompts in iTest"
  ],
  "heading_path": [
    "Overview: Prompts in iTest",
    "Overview: Prompts in iTest",
    "How iTest distinguishes prompts from responses during execution",
    "Learning prompts during interactive (manual) testing"
  ],
  "anchor": "1116726",
  "context_ids": [],
  "index_keywords": [
    "how iTest notices"
  ],
  "index_keyword_paths": [
    "command prompts > how iTest notices",
    "prompts > how iTest notices"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "03a39e5a696bbcc1",
  "level": 3
}
---

# Overview: Prompts in iTest > Overview: Prompts in iTest > How iTest distinguishes prompts from responses during execution > Learning prompts during interactive (manual) testing

iTest identifies possible prompts by noticing when the session returns text and then goes silent for a significant period of time.

When you close a session, iTest starts the Update Session Profile wizard to show you the list of possible prompts that it noticed during the session. This gives you the opportunity to identify the text strings that actually are prompts. When you finish the wizard, the new prompt definitions are added to the session profile. If needed, you can then use the Session Profile editor to customize the property settings for the prompt.
