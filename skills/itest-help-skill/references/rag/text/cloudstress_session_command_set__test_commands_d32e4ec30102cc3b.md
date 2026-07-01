---
{
  "chunk_id": "cloudstress_session_command_set__test_commands_d32e4ec30102cc3b",
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
    "Test commands"
  ],
  "anchor": "1292507",
  "context_ids": [
    "cloudstress_session_command_set"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d32e4ec30102cc3b",
  "level": 2
}
---

# CloudStress Session Command Set > CloudStress Session Command Set > Test commands

| Commands | Description | Arguments |
| --- | --- | --- |
| CreateTest | Create a test | name description owner_id last_report_id methodology_version methodology_key(CLOUDSTRESS_CPUBENCHMARK_FIXEDCOUNT, CLOUDSTRESS_MEMORYBENCHMARK_FIXEDCOUNT, CLOUDSTRESS_STORAGEBENCHMARK_FIXEDCOUNT, CLOUDSTRESS_NETWORKBENCHMARK_FIXEDCOUNT, CLOUDSTRESS_BENCHMARK_FIXEDCOUNT, CLOUDSTRESS_CPUBENCHMARK_FIXEDLOAD, CLOUDSTRESS_MEMORYBENCHMARK_FIXEDLOAD, CLOUDSTRESS_STORAGEBENCHMARK_FIXEDLOAD, CLOUDSTRESS_NETWORKBENCHMARK_FIXEDLOAD, CLOUDSTRESS_BENCHMARK_FIXEDLOAD) force |
| UpdateTest | Update test's properties | test_id name description owner_id last_report_id methodology_key methodology_version IterationDuration InitialSearchValue SearchResolution WaitAfterStop ProviderRespMaxWaitTime ProviderRespPollTime DeployMaxWaitTime DeployPollTime TearDownMaxWaitTime TearDownPollTime DeployBatchSize TearDownBatchSize EnableEotDeleteInstances |
| ConfigureTestProperty | Configure a specified property of test. | test_id*: String property*: String property_value: String |
| ConfigStorageBenchmarkTestProperties | Configure Storage Benchmark Test's Properties | MinMaxStorageLoadParams WaitAfterStop IterationDuration InitialSearchValue MaxSearchValue MinSearchValue SearchResolution AcceptableStorageReadVariance AcceptableStorageReadLatency AcceptableStorageWriteVariance AcceptableStorageWriteLatency StorageReadVarianceSuccessThreshold StorageReadLatencySuccessThreshold StorageWriteVarianceSuccessThreshold StorageWriteLatencySuccessThreshold |
| ConfigCPUBenchmarkTestProperties | Configure CPU Benchmark Test's Properties | MinMaxCpuLoadParam WaitAfterStop SearchResolution InitialSearchValue MinSearchValue MaxSearchValue IterationDuration AcceptableVariance SuccessThreshold |
| ConfigNetworkBenchmarkTestProperties | Configure Network Benchmark Test's Properties | MinMaxNetworkLoadParams WaitAfterStop SearchResolution InitialSearchValue MinSearchValue MaxSearchValue IterationDuration AcceptableNetworkReadVariance AcceptableNetworkReadLatency AcceptableNetworkWriteVariance AcceptableNetworkWriteLatency NetworkReadVarianceSuccessThreshold NetworkReadLatencySuccessThreshold NetworkWriteVarianceSuccessThreshold NetworkWriteLatencySuccessThreshold |
| ConfigMemoryBenchmarkTestProperties | Configure Memory Benchmark Test's Properties | MinMaxMemoryLoadParams WaitAfterStop IterationDuration InitialSearchValue MaxSearchValue MinSearchValue SearchResolution AcceptableMemoryReadVariance AcceptableMemoryReadLatency AcceptableMemoryWriteVariance AcceptableMemoryWriteLatency MemoryReadVarianceSuccessThreshold MemoryReadLatencySuccessThreshold MemoryWriteVarianceSuccessThreshold MemoryWriteLatencySuccessThreshold |
| ConfigBenchmarkTestProperties (continued on the next row) | Configure Benchmark Test's Properties | EnableCpuLoad EnableCpuTestCriteria EnableMemoryLoad EnableMemoryTestCriteria EnableNetworkLoad EnableNetworkTestCriteria EnableStorageLoad EnableStorageTestCriteria IterationDuration InitialSearchValue SearchResolution WaitAfterStop ProviderRespMaxWaitTime ProviderRespPollTime DeployMaxWaitTime DeployPollTime TearDownMaxWaitTime TearDownPollTime DeployBatchSize TearDownBatchSize EnableEotDeleteInstances MinMaxCpuLoadParam MinMaxMemoryLoadParams MinMaxNetworkLoadParams MinMaxStorageLoadParams AcceptableCpuLoadVariance CpuLoadVarianceSuccessThreshold |
| ConfigBenchmarkTestProperties (continued from the previous row) |  | AcceptableMemoryReadVariance AcceptableMemoryReadLatency AcceptableMemoryWriteVariance AcceptableMemoryWriteLatency MemoryReadVarianceSuccessThreshold MemoryReadLatencySuccessThreshold MemoryWriteVarianceSuccessThreshold MemoryWriteLatencySuccessThreshold AcceptableNetworkReadVariance AcceptableNetworkReadLatency AcceptableNetworkWriteVariance AcceptableNetworkWriteLatency NetworkReadVarianceSuccessThreshold NetworkReadLatencySuccessThreshold NetworkWriteVarianceSuccessThreshold NetworkWriteLatencySuccessThreshold AcceptableStorageReadVariance AcceptableStorageReadLatency AcceptableStorageWriteVariance AcceptableStorageWriteLatency StorageReadVarianceSuccessThreshold StorageReadLatencySuccessThreshold StorageWriteVarianceSuccessThreshold StorageWriteLatencySuccessThreshold |
| GetTest | Get a test by id | test_id |
| ListTests | Get list of test | id name cursor metadata_only page_size |
| SaveTest | After the test has been configured, it can be saved by performing a POST To save or update an existing test perform a PUT | test_id Response: |
| StartTest | Run an existing test | test_id |
| GetTestStatus | Retrieve information on the execution status of the test | test_id |
| StopTest | Test can be stopped before completion if needed. This can be accomplished by deleting the execution resource associated with a running test | execution_id |
| ApplyProfileToTest | Add a specified profile to a specified test | test_id template_id profile_id |
| ConfigureTemplatesInTest | Change machine's properties of test | test_id template_index machine_id count machine_name |
| AddTemplateToTest | Add specified template to specified test | test_id index template_id count |
| DeleteTemplatesInTest | Remove test's machines | test_id template_index |
