.. cfg_cmd:: qos

help: Quality of Service (QoS)

.. cfg_cmd:: qos interface <tag>

help: Interface to apply QoS policy

.. cfg_cmd:: qos interface <tag> egress

help: Interface egress traffic policy

.. cfg_cmd:: qos interface <tag> ingress

help: Interface ingress traffic policy

.. cfg_cmd:: qos policy

help: Service Policy definitions

.. cfg_cmd:: qos policy cake <tag>

help: Common Applications Kept Enhanced (CAKE)

.. cfg_cmd:: qos policy cake <tag> bandwidth

help: Available bandwidth for this policy

.. cfg_cmd:: qos policy cake <tag> description

help: Description

.. cfg_cmd:: qos policy cake <tag> flow-isolation

help: Flow isolation settings

.. cfg_cmd:: qos policy cake <tag> flow-isolation blind

help: Disables flow isolation, all traffic passes through a single queue

.. cfg_cmd:: qos policy cake <tag> flow-isolation dst-host

help: Flows are defined only by destination address

.. cfg_cmd:: qos policy cake <tag> flow-isolation dual-dst-host

help: Flows are defined by the 5-tuple, fairness is applied first over destination addresses, then over individual flows

.. cfg_cmd:: qos policy cake <tag> flow-isolation dual-src-host

help: Flows are defined by the 5-tuple, fairness is applied first over source addresses, then over individual flows

.. cfg_cmd:: qos policy cake <tag> flow-isolation flow

help: Flows are defined by the entire 5-tuple

.. cfg_cmd:: qos policy cake <tag> flow-isolation host

help: Flows are defined by source-destination host pairs

.. cfg_cmd:: qos policy cake <tag> flow-isolation nat

help: Perform NAT lookup before applying flow-isolation rules

.. cfg_cmd:: qos policy cake <tag> flow-isolation src-host

help: Flows are defined only by source address

.. cfg_cmd:: qos policy cake <tag> flow-isolation triple-isolate

help: Flows are defined by the 5-tuple, fairness is applied over source and destination addresses and also over individual flows (default)

.. cfg_cmd:: qos policy cake <tag> rtt

help: Round-Trip-Time for Active Queue Management (AQM)
100


.. cfg_cmd:: qos policy drop-tail <tag>

help: Packet limited First In, First Out queue

.. cfg_cmd:: qos policy drop-tail <tag> description

help: Description

.. cfg_cmd:: qos policy drop-tail <tag> queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy fair-queue <tag>

help: Stochastic Fairness Queueing

.. cfg_cmd:: qos policy fair-queue <tag> description

help: Description

.. cfg_cmd:: qos policy fair-queue <tag> hash-interval

help: Interval in seconds for queue algorithm perturbation
0


.. cfg_cmd:: qos policy fair-queue <tag> queue-limit

help: Upper limit of the SFQ
127


.. cfg_cmd:: qos policy fq-codel <tag>

help: Fair Queuing (FQ) with Controlled Delay (CoDel)

.. cfg_cmd:: qos policy fq-codel <tag> codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy fq-codel <tag> description

help: Description

.. cfg_cmd:: qos policy fq-codel <tag> flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy fq-codel <tag> interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy fq-codel <tag> queue-limit

help: Upper limit of the queue
10240


.. cfg_cmd:: qos policy fq-codel <tag> target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy limiter <tag>

help: Traffic input limiting policy

.. cfg_cmd:: qos policy limiter <tag> class <tag>

help: Class ID

.. cfg_cmd:: qos policy limiter <tag> class <tag> bandwidth

help: Available bandwidth for this policy

.. cfg_cmd:: qos policy limiter <tag> class <tag> burst

help: Burst size for this class
15k


.. cfg_cmd:: qos policy limiter <tag> class <tag> description

help: Description

.. cfg_cmd:: qos policy limiter <tag> class <tag> exceed

help: Default action for packets exceeding the limiter
drop


.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag>

help: Class matching rule name

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> description

help: Description

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ether

help: Ethernet header match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ether destination

help: Ethernet destination address for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ether protocol

help: Ethernet protocol for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ether source

help: Ethernet source address for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> interface

help: Interface to use

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip

help: Match IP protocol header

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip destination

help: Match on destination port or address

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip destination address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip destination port

help: Port number used by connection

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip max-length

help: Maximum packet length

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip protocol

help: Protocol

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip source

help: Match on source port or address

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip source address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip source port

help: Port number used by connection

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ip tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6

help: Match IPv6 protocol header

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 destination

help: Match on destination port or address

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 destination address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 destination port

help: Port number used by connection

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 max-length

help: Maximum packet length

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 protocol

help: Protocol

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 source

help: Match on source port or address

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 source address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 source port

help: Port number used by connection

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> ipv6 tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> mark

help: Match on mark applied by firewall

.. cfg_cmd:: qos policy limiter <tag> class <tag> match <tag> vif

help: Virtual Local Area Network (VLAN) ID for this match

.. cfg_cmd:: qos policy limiter <tag> class <tag> mtu

help: MTU size for this class

.. cfg_cmd:: qos policy limiter <tag> class <tag> not-exceed

help: Default action for packets not exceeding the limiter
ok


.. cfg_cmd:: qos policy limiter <tag> class <tag> priority

help: Priority for rule evaluation
20


.. cfg_cmd:: qos policy limiter <tag> default

help: Default policy

.. cfg_cmd:: qos policy limiter <tag> default bandwidth

help: Available bandwidth for this policy

.. cfg_cmd:: qos policy limiter <tag> default burst

help: Burst size for this class
15k


.. cfg_cmd:: qos policy limiter <tag> default exceed

help: Default action for packets exceeding the limiter
drop


.. cfg_cmd:: qos policy limiter <tag> default mtu

help: MTU size for this class

.. cfg_cmd:: qos policy limiter <tag> default not-exceed

help: Default action for packets not exceeding the limiter
ok


.. cfg_cmd:: qos policy limiter <tag> description

help: Description

.. cfg_cmd:: qos policy network-emulator <tag>

help: Network emulator policy

.. cfg_cmd:: qos policy network-emulator <tag> bandwidth

help: Available bandwidth for this policy

.. cfg_cmd:: qos policy network-emulator <tag> corruption

help: Introducing error in a random position for chosen percent of packets

.. cfg_cmd:: qos policy network-emulator <tag> delay

help: Adds delay to packets outgoing to chosen network interface

.. cfg_cmd:: qos policy network-emulator <tag> description

help: Description

.. cfg_cmd:: qos policy network-emulator <tag> duplicate

help: Cosen percent of packets is duplicated before queuing them

.. cfg_cmd:: qos policy network-emulator <tag> loss

help: Add independent loss probability to the packets outgoing to chosen network interface

.. cfg_cmd:: qos policy network-emulator <tag> queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy network-emulator <tag> reordering

help: Emulated packet reordering percentage

.. cfg_cmd:: qos policy priority-queue <tag>

help: Priority queuing based policy

.. cfg_cmd:: qos policy priority-queue <tag> class <tag>

help: Class Handle

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy priority-queue <tag> class <tag> description

help: Description

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy priority-queue <tag> class <tag> interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag>

help: Class matching rule name

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> description

help: Description

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ether

help: Ethernet header match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ether destination

help: Ethernet destination address for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ether protocol

help: Ethernet protocol for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ether source

help: Ethernet source address for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> interface

help: Interface to use

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip

help: Match IP protocol header

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip destination

help: Match on destination port or address

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip destination address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip destination port

help: Port number used by connection

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip max-length

help: Maximum packet length

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip protocol

help: Protocol

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip source

help: Match on source port or address

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip source address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip source port

help: Port number used by connection

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ip tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6

help: Match IPv6 protocol header

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 destination

help: Match on destination port or address

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 destination address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 destination port

help: Port number used by connection

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 max-length

help: Maximum packet length

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 protocol

help: Protocol

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 source

help: Match on source port or address

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 source address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 source port

help: Port number used by connection

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> ipv6 tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> mark

help: Match on mark applied by firewall

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> match <tag> vif

help: Virtual Local Area Network (VLAN) ID for this match

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy priority-queue <tag> class <tag> queue-type

help: Queue type for default traffic
drop-tail


.. cfg_cmd:: qos policy priority-queue <tag> class <tag> target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy priority-queue <tag> default

help: Default policy

.. cfg_cmd:: qos policy priority-queue <tag> default codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy priority-queue <tag> default flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy priority-queue <tag> default interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy priority-queue <tag> default queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy priority-queue <tag> default queue-type

help: Queue type for default traffic
drop-tail


.. cfg_cmd:: qos policy priority-queue <tag> default target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy priority-queue <tag> description

help: Description

.. cfg_cmd:: qos policy random-detect <tag>

help: Weighted Random Early Detect policy

.. cfg_cmd:: qos policy random-detect <tag> bandwidth

help: Available bandwidth for this policy
auto


.. cfg_cmd:: qos policy random-detect <tag> description

help: Description

.. cfg_cmd:: qos policy random-detect <tag> precedence <tag>

help: IP precedence

.. cfg_cmd:: qos policy random-detect <tag> precedence <tag> average-packet

help: Average packet size (bytes)
1024


.. cfg_cmd:: qos policy random-detect <tag> precedence <tag> mark-probability

help: Mark probability for this precedence
10


.. cfg_cmd:: qos policy random-detect <tag> precedence <tag> maximum-threshold

help: Maximum threshold for random detection
18


.. cfg_cmd:: qos policy random-detect <tag> precedence <tag> minimum-threshold

help: Minimum  threshold for random detection

.. cfg_cmd:: qos policy random-detect <tag> precedence <tag> queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy rate-control <tag>

help: Rate limiting policy (Token Bucket Filter)

.. cfg_cmd:: qos policy rate-control <tag> bandwidth

help: Available bandwidth for this policy

.. cfg_cmd:: qos policy rate-control <tag> burst

help: Burst size for this class
15k


.. cfg_cmd:: qos policy rate-control <tag> description

help: Description

.. cfg_cmd:: qos policy rate-control <tag> latency

help: Maximum latency
50


.. cfg_cmd:: qos policy round-robin <tag>

help: Deficit Round Robin Scheduler

.. cfg_cmd:: qos policy round-robin <tag> class <tag>

help: Class ID

.. cfg_cmd:: qos policy round-robin <tag> class <tag> codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy round-robin <tag> class <tag> description

help: Description

.. cfg_cmd:: qos policy round-robin <tag> class <tag> flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy round-robin <tag> class <tag> interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag>

help: Class matching rule name

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> description

help: Description

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ether

help: Ethernet header match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ether destination

help: Ethernet destination address for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ether protocol

help: Ethernet protocol for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ether source

help: Ethernet source address for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> interface

help: Interface to use

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip

help: Match IP protocol header

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip destination

help: Match on destination port or address

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip destination address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip destination port

help: Port number used by connection

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip max-length

help: Maximum packet length

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip protocol

help: Protocol

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip source

help: Match on source port or address

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip source address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip source port

help: Port number used by connection

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ip tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6

help: Match IPv6 protocol header

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 destination

help: Match on destination port or address

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 destination address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 destination port

help: Port number used by connection

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 max-length

help: Maximum packet length

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 protocol

help: Protocol

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 source

help: Match on source port or address

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 source address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 source port

help: Port number used by connection

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> ipv6 tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> mark

help: Match on mark applied by firewall

.. cfg_cmd:: qos policy round-robin <tag> class <tag> match <tag> vif

help: Virtual Local Area Network (VLAN) ID for this match

.. cfg_cmd:: qos policy round-robin <tag> class <tag> quantum

help: Packet scheduling quantum

.. cfg_cmd:: qos policy round-robin <tag> class <tag> queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy round-robin <tag> class <tag> queue-type

help: Queue type for default traffic
drop-tail


.. cfg_cmd:: qos policy round-robin <tag> class <tag> target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy round-robin <tag> default

help: Default policy

.. cfg_cmd:: qos policy round-robin <tag> default codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy round-robin <tag> default flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy round-robin <tag> default interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy round-robin <tag> default queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy round-robin <tag> default queue-type

help: Queue type for default traffic
fair-queue


.. cfg_cmd:: qos policy round-robin <tag> default target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy round-robin <tag> description

help: Description

.. cfg_cmd:: qos policy shaper <tag>

help: Traffic shaping based policy (Hierarchy Token Bucket)

.. cfg_cmd:: qos policy shaper <tag> bandwidth

help: Available bandwidth for this policy
auto


.. cfg_cmd:: qos policy shaper <tag> class <tag>

help: Class ID

.. cfg_cmd:: qos policy shaper <tag> class <tag> bandwidth

help: Available bandwidth for this policy
auto


.. cfg_cmd:: qos policy shaper <tag> class <tag> burst

help: Burst size for this class
15k


.. cfg_cmd:: qos policy shaper <tag> class <tag> ceiling

help: Bandwidth limit for this class

.. cfg_cmd:: qos policy shaper <tag> class <tag> codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy shaper <tag> class <tag> description

help: Description

.. cfg_cmd:: qos policy shaper <tag> class <tag> flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy shaper <tag> class <tag> interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag>

help: Class matching rule name

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> description

help: Description

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ether

help: Ethernet header match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ether destination

help: Ethernet destination address for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ether protocol

help: Ethernet protocol for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ether source

help: Ethernet source address for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> interface

help: Interface to use

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip

help: Match IP protocol header

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip destination

help: Match on destination port or address

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip destination address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip destination port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip max-length

help: Maximum packet length

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip protocol

help: Protocol

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip source

help: Match on source port or address

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip source address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip source port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ip tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6

help: Match IPv6 protocol header

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 destination

help: Match on destination port or address

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 destination address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 destination port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 max-length

help: Maximum packet length

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 protocol

help: Protocol

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 source

help: Match on source port or address

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 source address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 source port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> ipv6 tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> mark

help: Match on mark applied by firewall

.. cfg_cmd:: qos policy shaper <tag> class <tag> match <tag> vif

help: Virtual Local Area Network (VLAN) ID for this match

.. cfg_cmd:: qos policy shaper <tag> class <tag> priority

help: Priority for rule evaluation

.. cfg_cmd:: qos policy shaper <tag> class <tag> queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy shaper <tag> class <tag> queue-type

help: Queue type for default traffic
fq-codel


.. cfg_cmd:: qos policy shaper <tag> class <tag> set-dscp

help: Change the Differentiated Services (DiffServ) field in the IP header

.. cfg_cmd:: qos policy shaper <tag> class <tag> target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy shaper <tag> default

help: Default policy

.. cfg_cmd:: qos policy shaper <tag> default bandwidth

help: Available bandwidth for this policy

.. cfg_cmd:: qos policy shaper <tag> default burst

help: Burst size for this class
15k


.. cfg_cmd:: qos policy shaper <tag> default ceiling

help: Bandwidth limit for this class

.. cfg_cmd:: qos policy shaper <tag> default codel-quantum

help: Deficit in the fair queuing algorithm
1514


.. cfg_cmd:: qos policy shaper <tag> default flows

help: Number of flows into which the incoming packets are classified
1024


.. cfg_cmd:: qos policy shaper <tag> default interval

help: Interval used to measure the delay
100


.. cfg_cmd:: qos policy shaper <tag> default priority

help: Priority for usage of excess bandwidth
20


.. cfg_cmd:: qos policy shaper <tag> default queue-limit

help: Maximum queue size

.. cfg_cmd:: qos policy shaper <tag> default queue-type

help: Queue type for default traffic
fq-codel


.. cfg_cmd:: qos policy shaper <tag> default set-dscp

help: Change the Differentiated Services (DiffServ) field in the IP header

.. cfg_cmd:: qos policy shaper <tag> default target

help: Acceptable minimum standing/persistent queue delay
5


.. cfg_cmd:: qos policy shaper <tag> description

help: Description

.. cfg_cmd:: qos policy shaper-hfsc <tag>

help: Hierarchical Fair Service Curve's policy

.. cfg_cmd:: qos policy shaper-hfsc <tag> bandwidth

help: Available bandwidth for this policy
auto


.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag>

help: Class ID

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> description

help: Description

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> linkshare

help: Linkshare class settings

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> linkshare d

help: Service curve delay

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> linkshare m1

help: Linkshare m1 parameter for class traffic
0bit


.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> linkshare m2

help: Linkshare m2 parameter for class traffic
100%


.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag>

help: Class matching rule name

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> description

help: Description

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ether

help: Ethernet header match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ether destination

help: Ethernet destination address for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ether protocol

help: Ethernet protocol for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ether source

help: Ethernet source address for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> interface

help: Interface to use

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip

help: Match IP protocol header

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip destination

help: Match on destination port or address

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip destination address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip destination port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip max-length

help: Maximum packet length

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip protocol

help: Protocol

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip source

help: Match on source port or address

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip source address

help: IPv4 destination address for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip source port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ip tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6

help: Match IPv6 protocol header

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 destination

help: Match on destination port or address

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 destination address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 destination port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 dscp

help: Match on Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 max-length

help: Maximum packet length

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 protocol

help: Protocol

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 source

help: Match on source port or address

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 source address

help: IPv6 destination address for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 source port

help: Port number used by connection

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 tcp

help: TCP Flags matching

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 tcp ack

help: Match TCP ACK

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> ipv6 tcp syn

help: Match TCP SYN

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> mark

help: Match on mark applied by firewall

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> match <tag> vif

help: Virtual Local Area Network (VLAN) ID for this match

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> realtime

help: Realtime class settings

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> realtime d

help: Service curve delay

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> realtime m1

help: Linkshare m1 parameter for class traffic
0bit


.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> realtime m2

help: Linkshare m2 parameter for class traffic
100%


.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> upperlimit

help: Upperlimit class settings

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> upperlimit d

help: Service curve delay

.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> upperlimit m1

help: Linkshare m1 parameter for class traffic
0bit


.. cfg_cmd:: qos policy shaper-hfsc <tag> class <tag> upperlimit m2

help: Linkshare m2 parameter for class traffic
100%


.. cfg_cmd:: qos policy shaper-hfsc <tag> default

help: Default policy

.. cfg_cmd:: qos policy shaper-hfsc <tag> default linkshare

help: Linkshare class settings

.. cfg_cmd:: qos policy shaper-hfsc <tag> default linkshare d

help: Service curve delay

.. cfg_cmd:: qos policy shaper-hfsc <tag> default linkshare m1

help: Linkshare m1 parameter for class traffic
0bit


.. cfg_cmd:: qos policy shaper-hfsc <tag> default linkshare m2

help: Linkshare m2 parameter for class traffic
100%


.. cfg_cmd:: qos policy shaper-hfsc <tag> default realtime

help: Realtime class settings

.. cfg_cmd:: qos policy shaper-hfsc <tag> default realtime d

help: Service curve delay

.. cfg_cmd:: qos policy shaper-hfsc <tag> default realtime m1

help: Linkshare m1 parameter for class traffic
0bit


.. cfg_cmd:: qos policy shaper-hfsc <tag> default realtime m2

help: Linkshare m2 parameter for class traffic
100%


.. cfg_cmd:: qos policy shaper-hfsc <tag> default upperlimit

help: Upperlimit class settings

.. cfg_cmd:: qos policy shaper-hfsc <tag> default upperlimit d

help: Service curve delay

.. cfg_cmd:: qos policy shaper-hfsc <tag> default upperlimit m1

help: Linkshare m1 parameter for class traffic
0bit


.. cfg_cmd:: qos policy shaper-hfsc <tag> default upperlimit m2

help: Linkshare m2 parameter for class traffic
100%


.. cfg_cmd:: qos policy shaper-hfsc <tag> description

help: Description

