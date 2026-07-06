# Testing with Emulated Sessions > Controlling emulation for devices in a topology > To control emulation for a particular device in a topology

This method is useful for controlling emulation in any test case that uses the device with a single setting.

In the Topology editor, right-click the device and select one of the following options:

Use Test Case Emulation Settings: (default) Use the settings that are currently configured in any test case that uses the device.

![](images/emulation_2.4.jpg) <!-- image_ref -->

Always: Regardless of the setting for the topology or for any test case that uses the device, use emulated responses if available. (the device is shaded in teal)

![](images/emulation.5.jpg) <!-- image_ref -->

Never: Regardless of the setting for the topology or for any test case that uses the device, do not use the emulated responses. (the device is shaded in lilac)
