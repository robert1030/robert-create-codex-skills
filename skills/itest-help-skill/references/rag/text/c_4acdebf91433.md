# Controlling execution flow: Loops, If/Then, and Switch > For and ForEach loops > The for action: Execute a group of steps in a loop > Advanced users: Using a device parameter to set the loop count dynamically

In a more advanced case, you might use a parameter defined for the device that specifies the number of ports on the device (instead of the hard-coded number 10, as in the previous example).

![*](bullet_blue.jpg) <!-- image_ref -->

1. Let's say that, for the session profile named router, we have defined a parameter named port_count, and, for this particular device, given it the value 4.

1. 2 Now, in the Command for the for step, we can replace the hard-coded value 10 with a param command that evaluates the port_count parameter. (The appropriate session must be specified for the steps in the for loop.)

```
{set port_number 0} {$port_number [param port_count]} {incr port_number}
```

As a result, the Command evaluates to:

```
{set port_number 0} {$port_number<4} {incr port_number}
```

So, the loop now repeats for exactly the number of ports on the device. The test can now be used with a device with any number of ports because the port count used to control the loop dynamically takes on the port count defined for the device by the port_count parameter.
