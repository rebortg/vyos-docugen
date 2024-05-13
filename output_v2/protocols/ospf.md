.. cfg_cmd:: protocols ospf

help: Open Shortest Path First (OSPF)

.. cfg_cmd:: protocols ospf access-list <tag>

help: Access list to filter networks in routing updates

.. cfg_cmd:: protocols ospf access-list <tag> export

help: Filter for outgoing routing update

.. cfg_cmd:: protocols ospf aggregation

help: External route aggregation

.. cfg_cmd:: protocols ospf aggregation timer

help: Delay timer
5


.. cfg_cmd:: protocols ospf area <tag>

help: OSPF area settings

.. cfg_cmd:: protocols ospf area <tag> area-type

help: Area type

.. cfg_cmd:: protocols ospf area <tag> area-type normal

help: Normal OSPF area

.. cfg_cmd:: protocols ospf area <tag> area-type nssa

help: Not-So-Stubby OSPF area

.. cfg_cmd:: protocols ospf area <tag> area-type nssa default-cost

help: Summary-default cost of an NSSA area

.. cfg_cmd:: protocols ospf area <tag> area-type nssa no-summary

help: Do not inject inter-area routes into stub

.. cfg_cmd:: protocols ospf area <tag> area-type nssa translate

help: Configure NSSA-ABR
candidate


.. cfg_cmd:: protocols ospf area <tag> area-type stub

help: Stub OSPF area

.. cfg_cmd:: protocols ospf area <tag> area-type stub default-cost

help: Summary-default cost

.. cfg_cmd:: protocols ospf area <tag> area-type stub no-summary

help: Do not inject inter-area routes into the stub

.. cfg_cmd:: protocols ospf area <tag> authentication

help: OSPF area authentication type

.. cfg_cmd:: protocols ospf area <tag> export-list

help: Set the filter for networks announced to other areas

.. cfg_cmd:: protocols ospf area <tag> import-list

help: Set the filter for networks from other areas announced

.. cfg_cmd:: protocols ospf area <tag> network

help: OSPF network

.. cfg_cmd:: protocols ospf area <tag> range <tag>

help: Summarize routes matching a prefix (border routers only)

.. cfg_cmd:: protocols ospf area <tag> range <tag> cost

help: Metric for this range

.. cfg_cmd:: protocols ospf area <tag> range <tag> not-advertise

help: Do not advertise this range

.. cfg_cmd:: protocols ospf area <tag> range <tag> substitute

help: Advertise area range as another prefix

.. cfg_cmd:: protocols ospf area <tag> shortcut

help: Area shortcut mode

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag>

help: Virtual link

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> authentication

help: Authentication

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> authentication md5

help: MD5 key id

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> authentication md5 key-id <tag>

help: MD5 key id

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> authentication md5 key-id <tag> md5-key

help: MD5 authentication type

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> authentication plaintext-password

help: Plain text password

.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> dead-interval

help: Interval after which a neighbor is declared dead
40


.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> hello-interval

help: Interval between hello packets
10


.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> retransmit-interval

help: Interval between retransmitting lost link state advertisements
5


.. cfg_cmd:: protocols ospf area <tag> virtual-link <tag> transmit-delay

help: Link state transmit delay
1


.. cfg_cmd:: protocols ospf auto-cost

help: Calculate interface cost according to bandwidth

.. cfg_cmd:: protocols ospf auto-cost reference-bandwidth

help: Reference bandwidth method to assign cost
100


.. cfg_cmd:: protocols ospf capability

help: Enable specific OSPF features

.. cfg_cmd:: protocols ospf capability opaque

help: Opaque LSA

.. cfg_cmd:: protocols ospf default-information

help: Default route advertisment settings

.. cfg_cmd:: protocols ospf default-information originate

help: Distribute a default route

.. cfg_cmd:: protocols ospf default-information originate always

help: Always advertise a default route

.. cfg_cmd:: protocols ospf default-information originate metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf default-information originate metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf default-information originate route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf default-metric

help: Metric of redistributed routes

.. cfg_cmd:: protocols ospf distance

help: Administrative distance

.. cfg_cmd:: protocols ospf distance global

help: Administrative distance

.. cfg_cmd:: protocols ospf distance ospf

help: OSPF administrative distance

.. cfg_cmd:: protocols ospf distance ospf external

help: Distance for external routes

.. cfg_cmd:: protocols ospf distance ospf inter-area

help: Distance for inter-area routes

.. cfg_cmd:: protocols ospf distance ospf intra-area

help: Distance for intra-area routes

.. cfg_cmd:: protocols ospf graceful-restart

help: Graceful Restart

.. cfg_cmd:: protocols ospf graceful-restart grace-period

help: Maximum length of the grace period
120


.. cfg_cmd:: protocols ospf graceful-restart helper

help: OSPF graceful-restart helpers

.. cfg_cmd:: protocols ospf graceful-restart helper enable

help: Enable helper support

.. cfg_cmd:: protocols ospf graceful-restart helper enable router-id

help: Advertising Router-ID

.. cfg_cmd:: protocols ospf graceful-restart helper no-strict-lsa-checking

help: Disable strict LSA check

.. cfg_cmd:: protocols ospf graceful-restart helper planned-only

help: Supported only planned restart

.. cfg_cmd:: protocols ospf graceful-restart helper supported-grace-time

help: Supported grace timer

.. cfg_cmd:: protocols ospf interface <tag>

help: Interface configuration

.. cfg_cmd:: protocols ospf interface <tag> area

help: Enable OSPF on this interface

.. cfg_cmd:: protocols ospf interface <tag> authentication

help: Authentication

.. cfg_cmd:: protocols ospf interface <tag> authentication md5

help: MD5 key id

.. cfg_cmd:: protocols ospf interface <tag> authentication md5 key-id <tag>

help: MD5 key id

.. cfg_cmd:: protocols ospf interface <tag> authentication md5 key-id <tag> md5-key

help: MD5 authentication type

.. cfg_cmd:: protocols ospf interface <tag> authentication plaintext-password

help: Plain text password

.. cfg_cmd:: protocols ospf interface <tag> bandwidth

help: Interface bandwidth (Mbit/s)

.. cfg_cmd:: protocols ospf interface <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: protocols ospf interface <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols ospf interface <tag> cost

help: Interface cost

.. cfg_cmd:: protocols ospf interface <tag> dead-interval

help: Interval after which a neighbor is declared dead
40


.. cfg_cmd:: protocols ospf interface <tag> hello-interval

help: Interval between hello packets
10


.. cfg_cmd:: protocols ospf interface <tag> hello-multiplier

help: Hello multiplier factor

.. cfg_cmd:: protocols ospf interface <tag> ldp-sync

help: LDP-IGP synchronization configuration for interface

.. cfg_cmd:: protocols ospf interface <tag> ldp-sync disable

help: Disable instance

.. cfg_cmd:: protocols ospf interface <tag> ldp-sync holddown

help: Hold down timer for LDP-IGP cost restoration

.. cfg_cmd:: protocols ospf interface <tag> mtu-ignore

help: Disable Maximum Transmission Unit (MTU) mismatch detection

.. cfg_cmd:: protocols ospf interface <tag> network

help: Network type

.. cfg_cmd:: protocols ospf interface <tag> passive

help: Suppress routing updates on an interface

.. cfg_cmd:: protocols ospf interface <tag> passive disable

help: Disable instance

.. cfg_cmd:: protocols ospf interface <tag> priority

help: Router priority
1


.. cfg_cmd:: protocols ospf interface <tag> retransmit-interval

help: Interval between retransmitting lost link state advertisements
5


.. cfg_cmd:: protocols ospf interface <tag> transmit-delay

help: Link state transmit delay
1


.. cfg_cmd:: protocols ospf ldp-sync

help: Protocol wide LDP-IGP synchronization configuration

.. cfg_cmd:: protocols ospf ldp-sync holddown

help: Hold down timer for LDP-IGP cost restoration

.. cfg_cmd:: protocols ospf log-adjacency-changes

help: Log adjacency state changes

.. cfg_cmd:: protocols ospf log-adjacency-changes detail

help: Log all state changes

.. cfg_cmd:: protocols ospf max-metric

help: OSPF maximum and infinite-distance metric

.. cfg_cmd:: protocols ospf max-metric router-lsa

help: Advertise own Router-LSA with infinite distance (stub router)

.. cfg_cmd:: protocols ospf max-metric router-lsa administrative

help: Administratively apply, for an indefinite period

.. cfg_cmd:: protocols ospf max-metric router-lsa on-shutdown

help: Advertise stub-router prior to full shutdown of OSPF

.. cfg_cmd:: protocols ospf max-metric router-lsa on-startup

help: Automatically advertise stub Router-LSA on startup of OSPF

.. cfg_cmd:: protocols ospf maximum-paths

help: Maximum multiple paths (ECMP)

.. cfg_cmd:: protocols ospf mpls-te

help: MultiProtocol Label Switching-Traffic Engineering (MPLS-TE) parameters

.. cfg_cmd:: protocols ospf mpls-te enable

help: Enable MPLS-TE functionality

.. cfg_cmd:: protocols ospf mpls-te router-address

help: Stable IP address of the advertising router
0.0.0.0


.. cfg_cmd:: protocols ospf neighbor <tag>

help: Specify neighbor router

.. cfg_cmd:: protocols ospf neighbor <tag> poll-interval

help: Dead neighbor polling interval
60


.. cfg_cmd:: protocols ospf neighbor <tag> priority

help: Neighbor priority in seconds
0


.. cfg_cmd:: protocols ospf parameters

help: OSPF specific parameters

.. cfg_cmd:: protocols ospf parameters abr-type

help: OSPF ABR type
cisco


.. cfg_cmd:: protocols ospf parameters opaque-lsa

help: Enable the Opaque-LSA capability (rfc2370)

.. cfg_cmd:: protocols ospf parameters rfc1583-compatibility

help: Enable RFC1583 criteria for handling AS external routes

.. cfg_cmd:: protocols ospf parameters router-id

help: Override default router identifier

.. cfg_cmd:: protocols ospf passive-interface

help: Suppress routing updates on an interface

.. cfg_cmd:: protocols ospf redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: protocols ospf redistribute babel

help: Redistribute Babel routes

.. cfg_cmd:: protocols ospf redistribute babel metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute babel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute bgp

help: Redistribute BGP routes

.. cfg_cmd:: protocols ospf redistribute bgp metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute bgp metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute bgp route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute connected

help: Redistribute connected routes

.. cfg_cmd:: protocols ospf redistribute connected metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute connected metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute isis

help: Redistribute IS-IS routes

.. cfg_cmd:: protocols ospf redistribute isis metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute isis metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute isis route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute kernel

help: Redistribute Kernel routes

.. cfg_cmd:: protocols ospf redistribute kernel metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute kernel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute rip

help: Redistribute RIP routes

.. cfg_cmd:: protocols ospf redistribute rip metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute rip metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute rip route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute static

help: Redistribute statically configured routes

.. cfg_cmd:: protocols ospf redistribute static metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute static metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf redistribute table <tag>

help: Redistribute non-main Kernel Routing Table

.. cfg_cmd:: protocols ospf redistribute table <tag> metric

help: OSPF default metric

.. cfg_cmd:: protocols ospf redistribute table <tag> metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: protocols ospf redistribute table <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ospf refresh

help: Adjust refresh parameters

.. cfg_cmd:: protocols ospf refresh timers

help: Refresh timer

.. cfg_cmd:: protocols ospf segment-routing

help: Segment-Routing (SPRING) settings

.. cfg_cmd:: protocols ospf segment-routing global-block

help: Segment Routing Global Block label range

.. cfg_cmd:: protocols ospf segment-routing global-block high-label-value

help: MPLS label upper bound

.. cfg_cmd:: protocols ospf segment-routing global-block low-label-value

help: MPLS label lower bound

.. cfg_cmd:: protocols ospf segment-routing local-block

help: Segment Routing Local Block label range

.. cfg_cmd:: protocols ospf segment-routing local-block high-label-value

help: MPLS label upper bound

.. cfg_cmd:: protocols ospf segment-routing local-block low-label-value

help: MPLS label lower bound

.. cfg_cmd:: protocols ospf segment-routing maximum-label-depth

help: Maximum MPLS labels allowed for this router

.. cfg_cmd:: protocols ospf segment-routing prefix <tag>

help: Static IPv4 prefix segment/label mapping

.. cfg_cmd:: protocols ospf segment-routing prefix <tag> index

help: Specify the index value of prefix segment/label ID

.. cfg_cmd:: protocols ospf segment-routing prefix <tag> index explicit-null

help: Request upstream neighbor to replace segment/label with explicit null label

.. cfg_cmd:: protocols ospf segment-routing prefix <tag> index no-php-flag

help: Do not request penultimate hop popping for segment/label

.. cfg_cmd:: protocols ospf segment-routing prefix <tag> index value

help: Specify the index value of prefix segment/label ID

.. cfg_cmd:: protocols ospf summary-address <tag>

help: External summary address

.. cfg_cmd:: protocols ospf summary-address <tag> no-advertise

help: Don not advertise summary route

.. cfg_cmd:: protocols ospf summary-address <tag> tag

help: Router tag

.. cfg_cmd:: protocols ospf timers

help: Adjust routing timers

.. cfg_cmd:: protocols ospf timers throttle

help: Throttling adaptive timers

.. cfg_cmd:: protocols ospf timers throttle spf

help: OSPF SPF timers

.. cfg_cmd:: protocols ospf timers throttle spf delay

help: Delay from the first change received to SPF calculation
200


.. cfg_cmd:: protocols ospf timers throttle spf initial-holdtime

help: Initial hold time between consecutive SPF calculations
1000


.. cfg_cmd:: protocols ospf timers throttle spf max-holdtime

help: Maximum hold time
10000


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

