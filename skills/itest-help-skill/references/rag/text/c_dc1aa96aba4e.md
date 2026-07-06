# CloudStress Session > CloudStress Session Command Set > Result commands

| 欄位1 | 欄位2 | 欄位3 |
| --- | --- | --- |
| Commands | Description | Arguments |
| GenerateReportDocument | Download a document using report id Supported types: PDF, DOCX, XLSX | report_id location file_name document_type |
| GenerateReportDocumentByTestId | Download a latest document of test using test id Supported types: PDF, DOCX, XLSX | test_id location file_name document_type |
| ListReports | List test reports of specified test | id name test_id metadata_only |
| getReport | Get report as JSON document | test_id report_id |
| ListProfiles | List all profiles | id name owner_id type metadata_only |
