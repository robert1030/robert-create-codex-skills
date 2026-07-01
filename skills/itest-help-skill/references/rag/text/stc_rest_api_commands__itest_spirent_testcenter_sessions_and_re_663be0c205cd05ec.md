---
{
  "chunk_id": "stc_rest_api_commands__itest_spirent_testcenter_sessions_and_re_663be0c205cd05ec",
  "source_file": "topics/stc_rest_api_commands.htm",
  "source_original_path": "topics/stc_rest_api_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session window",
    "REST API Commands"
  ],
  "heading_path": [
    "REST API Commands",
    "REST API Commands",
    "iTest Spirent TestCenter Sessions and REST API"
  ],
  "anchor": "1420396",
  "context_ids": [
    "stc_rest_api_commands"
  ],
  "index_keywords": [
    "stc_sessions_and_rest_api_mapping"
  ],
  "index_keyword_paths": [
    "stc_sessions_and_rest_api_mapping"
  ],
  "related_links": [
    "tgen_nonsequencer_cmds_harness.htm#1416999",
    "spirent_testcenter_gui.10.htm#1378100",
    "spirent_testcenter_gui.05.htm#1358947",
    "stc_rest_get_save_rest_commands.htm#1474242"
  ],
  "images": [],
  "content_hash": "663be0c205cd05ec",
  "level": 2
}
---

# REST API Commands > REST API Commands > iTest Spirent TestCenter Sessions and REST API

| Category | STC Session commands | STC REST Session Commands | REST API |
| --- | --- | --- | --- |
| Analyzers | startAnalyzer stopAnalyzer | startAnalyzer stopAnalyzer | PUT http://domain:port/stcapi/v1/perform/analyzerStart/ " analyzerList:analyzer1" PUT http://domain:port/stcapi/v1/perform/analyzerStop/ " analyzerList:analyzer1" |
| Apply | N/A | performApply | PUT http://domain:port/stcapi/apply |
| Captures | startCapture stopCapture | startCapture stopCapture | PUT http://domain:port/stcapi/perform/captureStart "handle:capture1" PUT http://domain:port/stcapi/perform/captureStop "handle:capture1" |
| Configure | saveConfigurationFile | saveConfigurationFile | PUT /files/&file_name --binary data --.content-type: application/octet-stream, content-disposition: attachment; filename=myconfig.tcc GET /files/&file_name Accept: application/octet-stream |
| Devices | addHost/Router deleteHost/Router showHosts/Routers/Devices configureHost/Router/Device | addHost/Router deleteHost/Router showHosts/Routers/Devices configureHost/Router/Device | POST http://domain:port/stcapi/objects/ "object_type:Host/Router, under:project1" DELETE http://domain:port/stcapi/objects/&deviceHandle GET http://domain:port/stcapi/objects/&parenthandle?children-host/router PUT http://domain:port/stcapi/objects/&deviceHandle "propertyname:value" |
| Generators | startGenerator stopGenerator | startGenerator stopGenerator | PUT http://domain:port/stcapi/v1/perform/generatorStart/ "generatorList:generator1" PUT http://domain:port/stcapi/v1/perform/generatorStop/ "generatorList:generator1" |
| Help | N/A | N/A | GET /help/ command GET /help/&object_type GET /help/&handle GET /help/list?help_search_subject&pattern |
| Non-sequencer | 98 See Non-Sequencer action commands. |  | POST /perform/ "command" |
| perform | N/A | performCommand performConfig performCreate performDelete performGet | POST http://domain:port/stcapi/perform/ "command:&commandName, optionals...." PUT http://domain:port/stcapi/objects/$objectHandle "key:value" POST http://domain:port/stcapi/objects/ "object_type":"$objectType","under":"&parent" DELETE http://domain:port/stcapi/objects/&objectHandle GET http://domain:port/stcapi/objects/&objectHandle |
| Port | showPorts addPort breakLink restoreLink mapPort configurePort | showPorts addPort breakLink restoreLink mapPort configurePort | GET objects/project1?children-port POST http://domain:port/stcapi/perform/ReservePortCommand/ "object_type:port,under:project1" PUT http://domain:port/stcapi/perform/L2TestBreakLink "port: &porthandle" PUT http://domain:port/stcapi/perform/L2TestRestoreLink "port: &porthandle" POST http://domain:port/stcapi/perform "command:setupPortMappings" PUT http://domain:port/stcapi/objects/&portHandle "body" |
| Results | subscribeView showResults saveResults unsubscribeView N/A | subscribeView showResults saveResults unsubscribeView showSubscriptionViews | PUT http://domain:port/stcapi/v1/perform/ResultsSubscribeCommand/ "parent:project1, resultParent:port1, configType:generator, resultType:generatorPortResults" PUT http://domain:port/stcapi/perform/ExportResults"ExecuteSynchronous":"true","ColumnHeaderStyle":"DISPLAY","OutputFormat":"XML","ResultView":"&dataHandle" PUT http://domain:port/stcapi/perform/ResultDataSetUnsubscribe "ExecuteSynchronous":"true","ResultDataSet":"&dataHandle" |
| Sequencer command | 470 commands See Sequencer action commands. |  | POST /perform/ "command" |
| StreamBlocks | showStreamBlocks addStreamBock configureStreamBlock deleteStreamBlock See Stream block commands. | showStreamBlocks addStreamBock configureStreamBlock deleteStreamBlock | GET http://domain:port/stcapi/objects/&streamblockHandle POST http://domain:port/stcapi/objects/ "object_type:treamblock, under:port1" PUT http://domain:port/stcapi/objects/&streamblockHandle "Streamblock properties" DELETE http://domain:port/stcapi/objects/&streamblockHandle |
| Files |  | getFiles saveFile See Commands available only for REST sessions | GET http://.../stcapi/files GET http://.../stcapi/files/file_name |

The following commands require a full path for STC web as the target location:

- SaveResultCommand

- SavetoTccCommand

- FrameLengthDistributionSaveAsTemplateCommand

- SaveResultsCommand

- L2TestSaveTemplateCommand

- SaveResultCommandCommand

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
