# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/signalall.html > signalAll

signalAll eventName

A signalAll eventName step wakes all of the threads that are waiting on eventName and causes them to continue execution. If no threads are waiting on eventName, then signalAll eventName step does nothing.

Tip: If no threads are currently waiting on eventName and you want the event to “stay around” until explicitly “told not to”, then use signalActivate instead.

In addition to configuring signalAll as an Action in a step, you can specify signalAll as an Action for an Event.

For details, see the online help: signalAll: Wake all threads that are waiting on an event.
