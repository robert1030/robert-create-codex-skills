# Making your test case thread-safe > signalActivate: Turn a signal on > Example

![*](bullet_blue.jpg) <!-- image_ref -->

1. The signalWait in step 2 of the main procedure ensures that the date command in step 3 of main does not occur until the DUTOpen event is active.

![*](bullet_blue.jpg) <!-- image_ref -->

1. The DUTOpen event is activated by the signalActivate in step 3 of the initializeDUTs procedure.

![*](bullet_blue.jpg) <!-- image_ref -->

1. As a result, the date command can not occur until it is certain that the session with the DUT is open)

![](images/thread_safe_synch_5.1.jpg) <!-- image_ref -->
