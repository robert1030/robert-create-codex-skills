# Controlling execution flow: Loops, If/Then, and Switch > For and ForEach loops > The foreach action: Execute a group of steps in a loop > How foreach loops work > Example 2: foreach {A B C} {a1 b1 c1 a2 b2 c2 a3 b3 c3 a4 b4 c4}

foreach also supports updating multiple variables in the same way as Tcl does. The following steps

foreach { A B C} {a1 b1 c1 a2 b2 c2 a3 b3 c3 a4 b4}

comment "A = $A" "B = $B" "C = $C"

result in four comment steps being executed. Notice that the second list “runs out” in the middle on the last round, so C will be equal to an empty string on the last round.
