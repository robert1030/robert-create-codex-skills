# Run iTest as Network DevOps agent > Start and Stop NDO server > Network DevOps Agent API Calls > Executions using iTest NDO Agent > Reports

The report page displays with Result as pass when execution completes in the format specified (text, XML, HTML). You may also retrieve the report using the API (GET /executions/{id}/report REST API).

Note When execution completes, the debug window is not closed automatically. This to ensure that you have access to data of the completed (or canceled test for analysis of data from views in debug window—data, response, structure, etc).

The report does not persists between iTest NDO restarts. That is, if you stop, then start iTest NDO Agent, the Get Archive report does not find the report (the reports are not archived).
