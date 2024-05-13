.. cfg_cmd:: protocols babel

help: Babel Routing Protocol

.. cfg_cmd:: protocols babel distribute-list

help: Filter networks in routing updates

.. cfg_cmd:: protocols babel distribute-list ipv4

help: Filter IPv4 routes

.. cfg_cmd:: protocols babel distribute-list ipv4 access-list

help: Access-list

.. cfg_cmd:: protocols babel distribute-list ipv4 access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv4 access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag>

help: Apply filtering to an interface

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag> access-list

help: Access-list

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag> access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag> access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag> prefix-list

help: Prefix-list

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag> prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv4 interface <tag> prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv4 prefix-list

help: Prefix-list

.. cfg_cmd:: protocols babel distribute-list ipv4 prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv4 prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv6

help: Filter IPv6 routes

.. cfg_cmd:: protocols babel distribute-list ipv6 access-list

help: Access-list

.. cfg_cmd:: protocols babel distribute-list ipv6 access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv6 access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag>

help: Apply filtering to an interface

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag> access-list

help: Access-list

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag> access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag> access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag> prefix-list

help: Prefix-list

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag> prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv6 interface <tag> prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols babel distribute-list ipv6 prefix-list

help: Prefix-list

.. cfg_cmd:: protocols babel distribute-list ipv6 prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols babel distribute-list ipv6 prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols babel interface <tag>

help: Interface name

.. cfg_cmd:: protocols babel interface <tag> channel

help: Channel number for diversity routing

.. cfg_cmd:: protocols babel interface <tag> enable-timestamps

help: Enable timestamps with each Hello and IHU message in order to compute RTT values

.. cfg_cmd:: protocols babel interface <tag> hello-interval

help: Time between scheduled hellos
4000


.. cfg_cmd:: protocols babel interface <tag> max-rtt-penalty

help: Maximum additional cost due to RTT
150


.. cfg_cmd:: protocols babel interface <tag> rtt-decay

help: Decay factor for exponential moving average of RTT samples
42


.. cfg_cmd:: protocols babel interface <tag> rtt-max

help: Maximum RTT
120


.. cfg_cmd:: protocols babel interface <tag> rtt-min

help: Minimum RTT
10


.. cfg_cmd:: protocols babel interface <tag> rxcost

help: Base receive cost for this interface

.. cfg_cmd:: protocols babel interface <tag> split-horizon

help: Split horizon parameters
default


.. cfg_cmd:: protocols babel interface <tag> type

help: Interface type
auto


.. cfg_cmd:: protocols babel interface <tag> update-interval

help: Time between scheduled updates
20000


.. cfg_cmd:: protocols babel parameters

help: Babel-specific parameters

.. cfg_cmd:: protocols babel parameters diversity

help: Enable diversity-aware routing

.. cfg_cmd:: protocols babel parameters diversity-factor

help: Multiplicative factor used for diversity routing
256


.. cfg_cmd:: protocols babel parameters resend-delay

help: Time before resending a message
2000


.. cfg_cmd:: protocols babel parameters smoothing-half-life

help: Smoothing half-life
4


.. cfg_cmd:: protocols babel redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: protocols babel redistribute ipv4

help: Redistribute IPv4 routes

.. cfg_cmd:: protocols babel redistribute ipv4 bgp

help: Redistribute BGP routes

.. cfg_cmd:: protocols babel redistribute ipv4 connected

help: Redistribute connected routes

.. cfg_cmd:: protocols babel redistribute ipv4 eigrp

help: Redistribute EIGRP routes

.. cfg_cmd:: protocols babel redistribute ipv4 isis

help: Redistribute IS-IS routes

.. cfg_cmd:: protocols babel redistribute ipv4 kernel

help: Redistribute kernel routes

.. cfg_cmd:: protocols babel redistribute ipv4 nhrp

help: Redistribute NHRP routes

.. cfg_cmd:: protocols babel redistribute ipv4 ospf

help: Redistribute OSPF routes

.. cfg_cmd:: protocols babel redistribute ipv4 rip

help: Redistribute RIP routes

.. cfg_cmd:: protocols babel redistribute ipv4 static

help: Redistribute static routes

.. cfg_cmd:: protocols babel redistribute ipv6

help: Redistribute IPv6 routes

.. cfg_cmd:: protocols babel redistribute ipv6 bgp

help: Redistribute BGP routes

.. cfg_cmd:: protocols babel redistribute ipv6 connected

help: Redistribute connected routes

.. cfg_cmd:: protocols babel redistribute ipv6 isis

help: Redistribute IS-IS routes

.. cfg_cmd:: protocols babel redistribute ipv6 kernel

help: Redistribute kernel routes

.. cfg_cmd:: protocols babel redistribute ipv6 nhrp

help: Redistribute NHRP routes

.. cfg_cmd:: protocols babel redistribute ipv6 ospfv3

help: Redistribute OSPFv3 routes

.. cfg_cmd:: protocols babel redistribute ipv6 ripng

help: Redistribute RIPng routes

.. cfg_cmd:: protocols babel redistribute ipv6 static

help: Redistribute static routes

