# Spirent Avalanche sessions > Avalanche API Commands > av_apply > Comments

The apply command saves the configuration, performs validation, uploads test configuration to devices, and runs (or reruns) the test. This call is asynchronous, so the client will get control right after the call. The standard async_method_completed event will be sent after the test is started; the specific test state events will also be sent. For more information, please refer to Avalanche™ Automation Programmers’ Reference guide.
