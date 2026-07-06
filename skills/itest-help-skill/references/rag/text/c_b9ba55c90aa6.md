# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/signalactivate.html > signalActivate

signalActivate eventName

A signalActivate eventName step turns on the event called eventName. While an event signal is activated, any threads currently waiting for the event will be allowed to continue and any threads that begin waiting for the event are allowed to continue until the event is deactivated by a signalClear action.

In addition to configuring signalActivate as an Action in a step, you can specify signalActivate as an Action for an Event.

For details, see the online help: signalActivate: Turn a signal on.
