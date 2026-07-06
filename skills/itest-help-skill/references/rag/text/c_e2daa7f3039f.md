# Spirent Avalanche sessions > Specifying cards, slots, port groups, and ports/virtual ports > Examples of invalid port organization

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Using one or more port groups for both Client and Server Cluster Unit, for example:

![*](bullet_blue.jpg) <!-- image_ref -->

- Server Cluster Units: 2,1;0 2,3;0 and Client Cluster Units: 2,2;0 2,1;0 (STC)

![*](bullet_blue.jpg) <!-- image_ref -->

- Server Cluster Units: 2 3 and Client Cluster Units: 1 3 (Appliance)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Port provision List not belonging to Server or Client Cluster Unit:

Server Cluster Units: 2,1;0 and Client Cluster Units: 2,2;0

Port Provision List:

![*](bullet_blue.jpg) <!-- image_ref -->

- Port 1: Card 2, Port 1 -> group 1 belongs to Server Cluster Units

![*](bullet_blue.jpg) <!-- image_ref -->

- Port 2: Card 1, Port 2: invalid, not belong to both Server and Client Units

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Number of usable ports not equal to number of ports in config.tcl file.

In config.tcl file: Ports {10.47.73.51/2/1 10.47.73.51/2/3} (2 ports)

However, in Port Provision List (Server Cluster Units: 2,1;0 and Client Cluster Units: 2,2;0):

![*](bullet_blue.jpg) <!-- image_ref -->

- Port 1: Card 2 port 1

![*](bullet_blue.jpg) <!-- image_ref -->

- Port 2: Card 1 port 2 -> Unusable
