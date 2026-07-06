# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/elseif.html > elseif

An optional EXEC elseif step is a part of an if-then-elseif-else construct.

An EXEC elseif step is legal only when it immediately follows an if statement or another elseif statement. The command for elseif contains an assertion. If no previous if or elseif step that is associated with the elseif was True and the elseif assertion is True, then its nested steps will be executed.

![](../images/if_then_else_example.jpg) <!-- image_ref -->

If a previous if or elseif assertion was True, then the elseif assertion not tested.

See the online help for tips on adding if-then constructs.
