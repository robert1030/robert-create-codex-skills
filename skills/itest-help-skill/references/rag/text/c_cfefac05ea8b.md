# Analysis Rules: Validating Responses > About deferred actions

Because some analysis rule actions alter the flow of execution, they are deferred — they are placed in a queue and are not executed until all other actions for the step are executed.

Such an action is deferred even if it appears before other actions in the list of actions for the event and if there are additional analysis rules listed for the step after the current rule. For example, CallProcedure actions are deferred because other actions may need to occur before a CallProcedure should happen.
