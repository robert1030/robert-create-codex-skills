# Process Sessions > Session profile property settings for Process sessions > Terminal > Font > Example Process session on Microsoft Windows

```
Spirent Process command interpreter.
```

```
Copyright (c) 2005 - 2011, Spirent Communications, Inc.
```

```
process>help
```

```
cd - Show current working directory
```

```
cd <working directory> - Change working directory
```

```
exit - Exit process application
```

```
help - Display application commands
```

```
help <prefix> - Display application commands
```

```
kill - Kill all running processes
```

```
kill <process ID list> - Kill the process
```

```
run <command> - Start the process and wait for termination. Use -q[uiet] to display only command output
```

```
show platform - Show platform information
```

```
show process - Show information about all processes
```

```
show process <process ID list> - Show process information
```

```
start <command> - Start the process
```

```
wait <process ID> - Wait for a process termination
```

```
process>show platform
```

```
name: Windows XP
```

```
ver: 5.1
```

```
arch: x86
```

```
type: win32
```

```
process>start notepad
```

```
Process started, ID: 0
```

```
process>show 0
```

```
Invalid arguments. Type "show ?" for a list of subcommands.
```

```
process>show process 0
```

```
ID | Command | State | Exit Code
```

```
----------------------------------------------------------------------------
```

```
0 | notepad | RUNNING | N/A
```

```
process>start cmd
```

```
Process started, ID: 1
```

```
process>show process 1
```

```
ID | Command | State | Exit Code
```

```
----------------------------------------------------------------------------
```

```
1 | cmd | RUNNING | N/A
```

```
process>kill 1
```

```
Process 1 terminated, exit code: 1
```

```
process>wait 0
```

```
Waiting for process 0 to terminate...
```

```
Process 0 terminated, exit code: 0
```

```
process>cd
```

```
Working directory: 'c:\'
```

```
process>cd c:\temp
```

```
process>cd
```

```
Working directory: 'c:\temp'
```

```
process>exit
```
