# Controlling execution flow: Loops, If/Then, and Switch > Overview: Loops and flow‑control logic > Overview: Loops and flow‑control logic > Substitutions in the Command text

The command for while, forEach, for, and if actions is directed at the iTest interpreter. To ensure that iTest commands like [tcl ] or [tclexpr ] will be correctly interpreted, the text for the Command property (that appears in the Description cell) is interpreted as literal text. The property that controls substitution for the step is disabled (the For the Command field, perform command, variable, and backslash substitution property).

As a result, the text is not processed for the following substitution types before the step is executed (substitution occurs during execution):

![*](bullet_blue.jpg) <!-- image_ref -->

- Command field replacements (for example, char, expr, param, query, or response)

![*](bullet_blue.jpg) <!-- image_ref -->

- Variables

![*](bullet_blue.jpg) <!-- image_ref -->

- Backslash characters used to escape special characters
