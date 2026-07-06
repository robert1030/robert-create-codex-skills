# CloudStress Session > CloudStress Session Command Set > Template commands

| 欄位1 | 欄位2 | 欄位3 |
| --- | --- | --- |
| Commands | Description | Arguments |
| CreateTemplate | Creating a Template | template_name owner_id res_id cloud_id agent_ips discovery_id model_name nodes instances is_consistent is_credentials_saved is_shared force |
| CreateTemplateFromDiscover | Creating a template | discover_id template_name res_id |
| GetTemplate | Get a template by id | template_id |
| UpdateTemplate | Update existing template | template_id* template_name owner_id res_id cloud_id agent_ips discovery_id model_name nodes instances is_save_credentials is_consistent is_shared force |
| ListTemplates | Get list of template | id name metadata_only |
| DeleteTemplate | Delete a template | template_id |
