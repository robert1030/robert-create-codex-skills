---
{
  "chunk_id": "cloudstress_session_command_set__template_commands_b880f703f37aa495",
  "source_file": "topics/cloudstress_session_command_set.htm",
  "source_original_path": "topics/cloudstress_session_command_set.htm",
  "toc_path": [
    "iTest Online Help",
    "CloudStress Session",
    "CloudStress Session Command Set"
  ],
  "heading_path": [
    "CloudStress Session Command Set",
    "CloudStress Session Command Set",
    "Template commands"
  ],
  "anchor": "1292375",
  "context_ids": [
    "cloudstress_session_command_set"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "b880f703f37aa495",
  "level": 2
}
---

# CloudStress Session Command Set > CloudStress Session Command Set > Template commands

| Commands | Description | Arguments |
| --- | --- | --- |
| CreateTemplate | Creating a Template | template_name owner_id res_id cloud_id agent_ips discovery_id model_name nodes instances is_consistent is_credentials_saved is_shared force |
| CreateTemplateFromDiscover | Creating a template | discover_id template_name res_id |
| GetTemplate | Get a template by id | template_id |
| UpdateTemplate | Update existing template | template_id* template_name owner_id res_id cloud_id agent_ips discovery_id model_name nodes instances is_save_credentials is_consistent is_shared force |
| ListTemplates | Get list of template | id name metadata_only |
| DeleteTemplate | Delete a template | template_id |
