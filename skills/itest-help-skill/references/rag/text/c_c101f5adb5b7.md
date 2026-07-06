# SNMP Sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults

Note When you configure a step to save a response to a file (in the Other Post-processing > Store Response property group), this setting is ignored and all SNMP responses and statistics are always written to the file.

Note When you configure a step to save a response to a file (in the Other Post-processing > Store Response property group), this setting is ignored and all SNMP responses and statistics are always written to the file.

| General options |  |
| --- | --- |
| Timeout (ms) | Specify the timeout in milliseconds for any single send/receive transaction. Default: 5000 |
| Retries | Specify the number of times to retry send/receive transactions. Default: 2 |
| Do not capture SNMP response | Check the box to conserve memory by not capturing the SNMP response. Default: unchecked (False) |
| Do not capture SNMP statistics | Check the box to conserve memory by not capturing the SNMP statistics for the response. Default: checked (True) |
| Get Bulk options |  |
| Use GETBULK | When applicable for a get, use GETBULK to collect the response. Default: checked (True) |
| Max repetitions | Specifies the number of variables requested for each GETBULK request. Default: 50 Most agents make a best effort to fill their response with 50 variables, but may do fewer if they cannot fit 50 into a single PDU (which is dependent on the network configuration and other factors). In a situation like this, there is no harm in asking for 100 or more because iTest returns as many as possible. In other situations, you may need to lower the number to something the agent can handle. |
