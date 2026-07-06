# Analysis Rules: Validating Responses > Analysis Rule Wizard: Actions page > 第2段

- **When the response should contain a particular string, then:**：and
- **When the response should not contain a particular string, then:**：and
- **When you specified a comparison between the value from the response and an expected value, then:**：and For example, the assertion $value == 04:00:00 tests whether the extracted value is equal to “04:00:00”. If the value is indeed equal to “04:00:00”, then the assertion is True. If the value is not equal to “04:00:00”, then the assertion is False. To specify the actions that should occur upon True and False results, you specify two sets of actions to take: and Note that some extractor types can return multiple values.
