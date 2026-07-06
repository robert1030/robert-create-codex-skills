# Making your test case thread-safe > signalWaitAll: Wait until all specified events have been signaled or activated

The action signalWaitAll causes the currently executing thread to sleep until all specified events have been signaled or activated (by signal, signalAll, or signalActivate).

> **Note：** Note In contrast to Java’s implementation, threads that are waiting do not release locks and threads do not need to be inside locked blocks to call a wait.

| 欄位1 | 欄位2 |
| --- | --- |
| Action | Command property value (in the Description cell) |
| signalWaitAll | eventName [, eventName, ...] |
