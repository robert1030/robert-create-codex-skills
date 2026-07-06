# Analysis Rules: Validating Responses > Applying queries to stored responses

Often, you will want to use a value taken from the response to a step that executed earlier in the test.

In this example, the response to an earlier step included the setting for the maximum allowed input queue for the device. Now, you want to use the input queue value in the current step as the controlling limit in a for loop. To do this, you'll insert a query into the for statement that will return the value from the stored response to the earlier step.

In this for statement, we use a query command as a field replacement to supply the upper limit of repetitions for the loop. The value that we need appeared in the response to a step that executed earlier in the test.

![](images/analysis_rules_7.1.jpg) <!-- image_ref -->

The response for the earlier step had been stored in a variable named earlier_response.

The query that can return the value from the response is input_queue_max().

If the query returns a value of 75, then, at runtime, the for statement becomes:

```
{set i 0} {$i < 75} {incr i}
```

This topic provides instructions for the quickest way to insert a field replacement for a query command applied to a stored response. At runtime, the field replacement is replaced by a value returned from the response for an earlier step.
