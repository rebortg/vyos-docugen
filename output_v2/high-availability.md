.. cfg_cmd:: high-availability

help: High availability settings

.. cfg_cmd:: high-availability disable

help: Disable instance

.. cfg_cmd:: high-availability virtual-server <tag>

help: Load-balancing virtual server alias

.. cfg_cmd:: high-availability virtual-server <tag> address

help: IP address

.. cfg_cmd:: high-availability virtual-server <tag> algorithm

help: Schedule algorithm (default - least-connection)
least-connection


.. cfg_cmd:: high-availability virtual-server <tag> delay-loop

help: Interval between health-checks (in seconds)
10


.. cfg_cmd:: high-availability virtual-server <tag> forward-method

help: Forwarding method
nat


.. cfg_cmd:: high-availability virtual-server <tag> fwmark

help: Match fwmark value

.. cfg_cmd:: high-availability virtual-server <tag> persistence-timeout

help: Timeout for persistent connections
300


.. cfg_cmd:: high-availability virtual-server <tag> port

help: Port number used by connection

.. cfg_cmd:: high-availability virtual-server <tag> protocol

help: Protocol for port checks
tcp


.. cfg_cmd:: high-availability virtual-server <tag> real-server <tag>

help: Real server address

.. cfg_cmd:: high-availability virtual-server <tag> real-server <tag> connection-timeout

help: Server connection timeout

.. cfg_cmd:: high-availability virtual-server <tag> real-server <tag> health-check

help: Health check script

.. cfg_cmd:: high-availability virtual-server <tag> real-server <tag> health-check script

help: Health check script file

.. cfg_cmd:: high-availability virtual-server <tag> real-server <tag> port

help: Port number used by connection

.. cfg_cmd:: high-availability vrrp

help: Virtual Router Redundancy Protocol settings

.. cfg_cmd:: high-availability vrrp global-parameters

help: VRRP global parameters

.. cfg_cmd:: high-availability vrrp global-parameters garp

help: Gratuitous ARP parameters

.. cfg_cmd:: high-availability vrrp global-parameters garp interval

help: Interval between Gratuitous ARP
0


.. cfg_cmd:: high-availability vrrp global-parameters garp master-delay

help: Delay for second set of gratuitous ARPs after transition to master
5


.. cfg_cmd:: high-availability vrrp global-parameters garp master-refresh

help: Minimum time interval for refreshing gratuitous ARPs while beeing master
5


.. cfg_cmd:: high-availability vrrp global-parameters garp master-refresh-repeat

help: Number of gratuitous ARP messages to send at a time while beeing master
1


.. cfg_cmd:: high-availability vrrp global-parameters garp master-repeat

help: Number of gratuitous ARP messages to send at a time after transition to master
5


.. cfg_cmd:: high-availability vrrp global-parameters startup-delay

help: Time VRRP startup process (in seconds)

.. cfg_cmd:: high-availability vrrp global-parameters version

help: Default VRRP version to use, IPv6 always uses VRRP version 3

.. cfg_cmd:: high-availability vrrp group <tag>

help: VRRP group

.. cfg_cmd:: high-availability vrrp group <tag> address <tag>

help: Virtual IP address

.. cfg_cmd:: high-availability vrrp group <tag> address <tag> interface

help: Interface to use

.. cfg_cmd:: high-availability vrrp group <tag> advertise-interval

help: Advertise interval
1


.. cfg_cmd:: high-availability vrrp group <tag> authentication

help: VRRP authentication

.. cfg_cmd:: high-availability vrrp group <tag> authentication password

help: VRRP password

.. cfg_cmd:: high-availability vrrp group <tag> authentication type

help: Authentication type

.. cfg_cmd:: high-availability vrrp group <tag> description

help: Description

.. cfg_cmd:: high-availability vrrp group <tag> disable

help: Disable instance

.. cfg_cmd:: high-availability vrrp group <tag> excluded-address

help: Virtual address (If you need additional IPv4 and IPv6 in same group)

.. cfg_cmd:: high-availability vrrp group <tag> garp

help: Gratuitous ARP parameters

.. cfg_cmd:: high-availability vrrp group <tag> garp interval

help: Interval between Gratuitous ARP
0


.. cfg_cmd:: high-availability vrrp group <tag> garp master-delay

help: Delay for second set of gratuitous ARPs after transition to master
5


.. cfg_cmd:: high-availability vrrp group <tag> garp master-refresh

help: Minimum time interval for refreshing gratuitous ARPs while beeing master
5


.. cfg_cmd:: high-availability vrrp group <tag> garp master-refresh-repeat

help: Number of gratuitous ARP messages to send at a time while beeing master
1


.. cfg_cmd:: high-availability vrrp group <tag> garp master-repeat

help: Number of gratuitous ARP messages to send at a time after transition to master
5


.. cfg_cmd:: high-availability vrrp group <tag> health-check

help: Health check

.. cfg_cmd:: high-availability vrrp group <tag> health-check failure-count

help: Health check failure count required for transition to fault
3


.. cfg_cmd:: high-availability vrrp group <tag> health-check interval

help: Health check execution interval in seconds
60


.. cfg_cmd:: high-availability vrrp group <tag> health-check ping

help: ICMP ping health check

.. cfg_cmd:: high-availability vrrp group <tag> health-check script

help: Health check script file

.. cfg_cmd:: high-availability vrrp group <tag> hello-source-address

help: VRRP hello source address

.. cfg_cmd:: high-availability vrrp group <tag> interface

help: Interface to use

.. cfg_cmd:: high-availability vrrp group <tag> no-preempt

help: Disable master preemption

.. cfg_cmd:: high-availability vrrp group <tag> peer-address

help: Unicast VRRP peer address

.. cfg_cmd:: high-availability vrrp group <tag> preempt-delay

help: Preempt delay (in seconds)
0


.. cfg_cmd:: high-availability vrrp group <tag> priority

help: Router priority
100


.. cfg_cmd:: high-availability vrrp group <tag> rfc3768-compatibility

help: Use VRRP virtual MAC address as per RFC3768

.. cfg_cmd:: high-availability vrrp group <tag> track

help: Track settings

.. cfg_cmd:: high-availability vrrp group <tag> track exclude-vrrp-interface

help: Disable track state of main interface

.. cfg_cmd:: high-availability vrrp group <tag> track interface

help: Interface name state check

.. cfg_cmd:: high-availability vrrp group <tag> transition-script

help: VRRP transition scripts

.. cfg_cmd:: high-availability vrrp group <tag> transition-script backup

help: Script to run on VRRP state transition to backup

.. cfg_cmd:: high-availability vrrp group <tag> transition-script fault

help: Script to run on VRRP state transition to fault

.. cfg_cmd:: high-availability vrrp group <tag> transition-script master

help: Script to run on VRRP state transition to master

.. cfg_cmd:: high-availability vrrp group <tag> transition-script stop

help: Script to run on VRRP state transition to stop

.. cfg_cmd:: high-availability vrrp group <tag> vrid

help: Virtual router identifier

.. cfg_cmd:: high-availability vrrp snmp

help: Enable SNMP

.. cfg_cmd:: high-availability vrrp sync-group <tag>

help: VRRP sync group

.. cfg_cmd:: high-availability vrrp sync-group <tag> health-check

help: Health check

.. cfg_cmd:: high-availability vrrp sync-group <tag> health-check failure-count

help: Health check failure count required for transition to fault
3


.. cfg_cmd:: high-availability vrrp sync-group <tag> health-check interval

help: Health check execution interval in seconds
60


.. cfg_cmd:: high-availability vrrp sync-group <tag> health-check ping

help: ICMP ping health check

.. cfg_cmd:: high-availability vrrp sync-group <tag> health-check script

help: Health check script file

.. cfg_cmd:: high-availability vrrp sync-group <tag> member

help: Sync group member

.. cfg_cmd:: high-availability vrrp sync-group <tag> transition-script

help: VRRP transition scripts

.. cfg_cmd:: high-availability vrrp sync-group <tag> transition-script backup

help: Script to run on VRRP state transition to backup

.. cfg_cmd:: high-availability vrrp sync-group <tag> transition-script fault

help: Script to run on VRRP state transition to fault

.. cfg_cmd:: high-availability vrrp sync-group <tag> transition-script master

help: Script to run on VRRP state transition to master

.. cfg_cmd:: high-availability vrrp sync-group <tag> transition-script stop

help: Script to run on VRRP state transition to stop

