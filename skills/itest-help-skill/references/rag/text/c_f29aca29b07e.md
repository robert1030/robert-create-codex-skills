# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/foreach.html > foreach

A foreach loop performs the steps within the loop for each value in a specified set of values.

The statement in the Description cell (the value of the Command property) of a foreach step follows Tcl foreach syntax. The simplest usage takes two lists. The first is a list of variables and the second is the list of values that the variables take on.

A foreach loop is composed of all of the steps that are indented under the foreach clause.

Example 1: foreach A {1 3 5} In this example, the first list has a single member, A. The loop will execute 3 times with: A = 1, A = 3, and A = 5

foreach also supports updating multiple variables in the same way as Tcl does, as shown in the following examples:

Example 2: foreach {A B C} {a1 b1 c1 a2 b2 c2 a3 b3} Notice that the second list "runs out" in the last round, so C will be equal to an empty string on the last round. The loop executes for 3 iterations where A, B, C equals a1, b1, c1 --- a2, b2, c2 --- a3, b3

Example 3: foreach A {1 3 5} B {2 4 6 8 10} The loop will execute for the number of iterations based on the largest value pair specified The example loop executes for 5 iterations where A, B equals: 1, 2 --- 3, 4 --- 5, 6 --- <no A value>, 8 --- <no A value>, 10

Nested loops (if, for, foreach, and while) are supported.

For details, see the online help: The foreach action.
