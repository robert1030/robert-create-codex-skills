# iTest Topology Editor > Velocity command > Commands that return information from Velocity > velocity command syntax > makeReservation subcommand > Example Reservation Priority usage

The following is an example of Velocity makeReservation command usage with reservation priority.

![](images/topologies_9.1.jpg) <!-- image_ref -->

When executing the test, iTest displays an error if the priority specified is greater than the level defined for user (by Admin user in Velocity) and if there is reservation conflict.

The test execution step executes and returns reservation ID if the priority level specified in the test case step is the within the range of priority level assigned to the user. See Velocity Online Help for details of Reservation Priority

![](images/velo_topo_makeReservation_withPriority_testExecution.png) <!-- image_ref -->
