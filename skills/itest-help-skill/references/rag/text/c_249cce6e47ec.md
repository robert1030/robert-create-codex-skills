# Analysis Rules: Validating Responses > About deferred actions > Example 1

The example step has two analysis rules. Each of the rules includes one action of a kind that is deferred and several other actions that are immediate (can be performed immediately).

Here is the step before execution:

step

analysis rule 1

actionA

actionB (deferred)

actionC

actionD

analysis rule 2

actionE (deferred)

actionF

When the step finishes executing, the analysis rules are evaluated in the order that they appear. When a rule is evaluated, the immediate actions are performed and all deferred actions for all analysis rules are added to the queue. After all of the immediate actions are performed, deferred actions are performed in the sequence that they were added to the queue.

Here is the order in which the actions are performed:

step

analysis rule 1

actionA

actionC

actionD

analysis rule 2

actionF

--- now that all of the other actions are finished, the deferred actions are performed ---

actionB

actionE
