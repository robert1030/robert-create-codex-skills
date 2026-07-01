---
{
  "chunk_id": "cloudstress_session_command_set__result_commands_313e67a790e54cb2",
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
    "Result commands"
  ],
  "anchor": "1292865",
  "context_ids": [
    "cloudstress_session_command_set"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "313e67a790e54cb2",
  "level": 2
}
---

# CloudStress Session Command Set > CloudStress Session Command Set > Result commands

| Commands | Description | Arguments |
| --- | --- | --- |
| GenerateReportDocument | Download a document using report id Supported types: PDF, DOCX, XLSX | report_id location file_name document_type |
| GenerateReportDocumentByTestId | Download a latest document of test using test id Supported types: PDF, DOCX, XLSX | test_id location file_name document_type |
| ListReports | List test reports of specified test | id name test_id metadata_only |
| getReport | Get report as JSON document | test_id report_id |
| ListProfiles | List all profiles | id name owner_id type metadata_only |
