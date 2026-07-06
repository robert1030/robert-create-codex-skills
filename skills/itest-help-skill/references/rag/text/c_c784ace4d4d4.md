# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/else.html > else

An optional EXEC else step is a part of an if-then-elseif-else construct.

An else step is similar to elseif, but it must come last in the sequence of steps associated with the if construct.

If the assertion associated with the else is True, then its nested steps will be executed as long as no previous associated if or elseif has been actioned

![](../images/if_then_else_example.jpg) <!-- image_ref -->

Note: A legal contiguous sequence of if, then, elseif, and else steps will have one if step, followed by one then step, followed by zero or more elseif steps followed by zero or one else step. Any other sequence is illegal. No other types of steps within the scope can be interleaved in these sequences.

See the online help for tips on adding if-then constructs.
