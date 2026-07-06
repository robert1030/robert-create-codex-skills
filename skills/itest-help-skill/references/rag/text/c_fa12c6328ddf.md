# Spirent TestCenter sessions > Spirent TestCenter session window > Device commands > ARP packet actions > 第1段

For all of the following ARP actions:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Click the button that captures the action in the main toolbar to apply the action to all ports. Click the button on the “local” toolbar (on pages that enable you to select ports) to apply the action to the selected ports.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can specify the listOfPortIdentifiers argument values in any mix of formats separated by spaces. For example, slot:port mixed with sequential portIndex — 1:1 1:2 3 6

See To specify a list of port locations.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If listOfPortIdentifiers is not specified, then the command is applied to all ports and returns data for all ports.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The returned ARP/ND state is one of the following:

IDLE — Idle

WAITING — ARP/ND is in progress

SUCCESSFUL — All attempted ARP/NDs were resolved successfully

FAILURE — Some attempted ARP/NDs could not be resolved successfully

CONGESTED — Some attempted ARP/NDs are congested

![](images/spirent_testcenter_gui_2.10.jpg) <!-- image_ref -->

![](images/spirent_testcenter_gui_3.11.jpg) <!-- image_ref -->

![](images/spirent_testcenter_gui_3.12.jpg) <!-- image_ref -->

![](images/spirent_testcenter_gui_3.13.jpg) <!-- image_ref -->

![](images/spirent_testcenter_gui_3.14.jpg) <!-- image_ref -->
