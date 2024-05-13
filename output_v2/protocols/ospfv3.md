.. cfg_cmd:: protocols ospfv3

help: Open Shortest Path First (OSPF) for IPv6

.. cfg_cmd:: protocols ospfv3 area <tag>

help: OSPFv3 Area

.. cfg_cmd:: protocols ospfv3 area <tag> area-type

help: OSPFv3 Area type

.. cfg_cmd:: protocols ospfv3 area <tag> area-type nssa

help: NSSA OSPFv3 area

.. cfg_cmd:: protocols ospfv3 area <tag> area-type nssa default-information-originate

help: Originate Type 7 default into NSSA area

.. cfg_cmd:: protocols ospfv3 area <tag> area-type nssa no-summary

help: Do not inject inter-area routes into the stub

.. cfg_cmd:: protocols ospfv3 area <tag> area-type stub

help: Stub OSPFv3 area

.. cfg_cmd:: protocols ospfv3 area <tag> area-type stub no-summary

help: Do not inject inter-area routes into the stub

.. cfg_cmd:: protocols ospfv3 area <tag> export-list

help: Name of export-list

.. cfg_cmd:: protocols ospfv3 area <tag> import-list

help: Name of import-list

.. cfg_cmd:: protocols ospfv3 area <tag> range <tag>

help: Specify IPv6 prefix (border routers only)

.. cfg_cmd:: protocols ospfv3 area <tag> range <tag> advertise

help: Advertise this range

.. cfg_cmd:: protocols ospfv3 area <tag> range <tag> not-advertise

help: Do not advertise this range

.. cfg_cmd:: protocols ospfv3 auto-cost

help: Calculate interface cost according to bandwidth

.. cfg_cmd:: protocols ospfv3 auto-cost reference-bandwidth

help: Reference bandwidth method to assign cost
100


.. cfg_cmd:: protocols ospfv3 default-information

help: Default route advertisment settings

.. cfg_cmd:: protocols ospfv3 default-information originate

help: Distribute a default route

.. cfg_cmd:: protocols ospfv3 default-information originate always

help: Always advertise a default route

.. cfg_cmd:: protocols ospfv3 default-information originate metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 default-information originate metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 default-information originate route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 distance

help: Administrative distance

.. cfg_cmd:: protocols ospfv3 distance global

help: Administrative distance

.. cfg_cmd:: protocols ospfv3 distance ospfv3

help: OSPFv3 administrative distance

.. cfg_cmd:: protocols ospfv3 distance ospfv3 external

help: Distance for external routes

.. cfg_cmd:: protocols ospfv3 distance ospfv3 inter-area

help: Distance for inter-area routes

.. cfg_cmd:: protocols ospfv3 distance ospfv3 intra-area

help: Distance for intra-area routes

.. cfg_cmd:: protocols ospfv3 graceful-restart

help: Graceful Restart

.. cfg_cmd:: protocols ospfv3 graceful-restart grace-period

help: Maximum length of the grace period
120


.. cfg_cmd:: protocols ospfv3 graceful-restart helper

help: OSPF graceful-restart helpers

.. cfg_cmd:: protocols ospfv3 graceful-restart helper enable

help: Enable helper support

.. cfg_cmd:: protocols ospfv3 graceful-restart helper enable router-id

help: Advertising Router-ID

.. cfg_cmd:: protocols ospfv3 graceful-restart helper lsa-check-disable

help: Disable strict LSA check

.. cfg_cmd:: protocols ospfv3 graceful-restart helper planned-only

help: Supported only planned restart

.. cfg_cmd:: protocols ospfv3 graceful-restart helper supported-grace-time

help: Supported grace timer

.. cfg_cmd:: protocols ospfv3 interface <tag>

help: Enable routing on an IPv6 interface

.. cfg_cmd:: protocols ospfv3 interface <tag> area

help: Enable OSPF on this interface

.. cfg_cmd:: protocols ospfv3 interface <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: protocols ospfv3 interface <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols ospfv3 interface <tag> cost

help: Interface cost

.. cfg_cmd:: protocols ospfv3 interface <tag> dead-interval

help: Interval after which a neighbor is declared dead
40


.. cfg_cmd:: protocols ospfv3 interface <tag> hello-interval

help: Interval between hello packets
10


.. cfg_cmd:: protocols ospfv3 interface <tag> ifmtu

help: Interface MTU

.. cfg_cmd:: protocols ospfv3 interface <tag> instance-id

help: Instance ID
0


.. cfg_cmd:: protocols ospfv3 interface <tag> mtu-ignore

help: Disable Maximum Transmission Unit (MTU) mismatch detection

.. cfg_cmd:: protocols ospfv3 interface <tag> network

help: Network type

.. cfg_cmd:: protocols ospfv3 interface <tag> passive

help: Configure passive mode for interface

.. cfg_cmd:: protocols ospfv3 interface <tag> priority

help: Router priority
1


.. cfg_cmd:: protocols ospfv3 interface <tag> retransmit-interval

help: Interval between retransmitting lost link state advertisements
5


.. cfg_cmd:: protocols ospfv3 interface <tag> transmit-delay

help: Link state transmit delay
1


.. cfg_cmd:: protocols ospfv3 log-adjacency-changes

help: Log adjacency state changes

.. cfg_cmd:: protocols ospfv3 log-adjacency-changes detail

help: Log all state changes

.. cfg_cmd:: protocols ospfv3 parameters

help: OSPFv3 specific parameters

.. cfg_cmd:: protocols ospfv3 parameters router-id

help: Override default router identifier

.. cfg_cmd:: protocols ospfv3 redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: protocols ospfv3 redistribute babel

help: Redistribute Babel routes

.. cfg_cmd:: protocols ospfv3 redistribute babel metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute babel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 redistribute bgp

help: Redistribute BGP routes

.. cfg_cmd:: protocols ospfv3 redistribute bgp metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute bgp metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute bgp route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 redistribute connected

help: Redistribute connected routes

.. cfg_cmd:: protocols ospfv3 redistribute connected metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute connected metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 redistribute isis

help: Redistribute IS-IS routes

.. cfg_cmd:: protocols ospfv3 redistribute isis metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute isis metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute isis route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 redistribute kernel

help: Redistribute kernel routes

.. cfg_cmd:: protocols ospfv3 redistribute kernel metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute kernel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 redistribute ripng

help: Redistribute RIPNG routes

.. cfg_cmd:: protocols ospfv3 redistribute ripng metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute ripng metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute ripng route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospfv3 redistribute static

help: Redistribute static routes

.. cfg_cmd:: protocols ospfv3 redistribute static metric

help: OSPF default metric

.. cfg_cmd:: protocols ospfv3 redistribute static metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospfv3 redistribute static route-map

help: Specify route-map name to use

