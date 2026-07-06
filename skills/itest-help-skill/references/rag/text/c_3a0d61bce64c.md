# iTest Topology Editor > Velocity command > Commands that return information from Velocity > velocity command syntax > makeReservation subcommand > Example Python usage:

velocity('makeReservation', '-topologyName', 'YK1', '-duration’, '10', ‘-name’, ’reservation_MEDIUM’, ’-priority’, ’MEDIUM’, 'PC.cond=template[PC] and ports(integer[Port Speed]>=10000)>=2', 'Server.cond=template[Server] and [Hostname]="xxxxx.xxxxx.com"' )
