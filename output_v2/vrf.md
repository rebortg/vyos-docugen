.. cfg_cmd:: vrf

help: Virtual Routing and Forwarding

.. cfg_cmd:: vrf bind-to-all

help: Enable binding services to all VRFs

.. cfg_cmd:: vrf name <tag>

help: Virtual Routing and Forwarding instance

.. cfg_cmd:: vrf name <tag> description

help: Description

.. cfg_cmd:: vrf name <tag> disable

help: Administratively disable interface

.. cfg_cmd:: vrf name <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: vrf name <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: vrf name <tag> ip nht

help: Filter Next Hop tracking route resolution

.. cfg_cmd:: vrf name <tag> ip nht no-resolve-via-default

help: Do not resolve via default route

.. cfg_cmd:: vrf name <tag> ip protocol <tag>

help: Filter routing info exchanged between routing protocol and zebra

.. cfg_cmd:: vrf name <tag> ip protocol <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: vrf name <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: vrf name <tag> ipv6 nht

help: Filter Next Hop tracking route resolution

.. cfg_cmd:: vrf name <tag> ipv6 nht no-resolve-via-default

help: Do not resolve via default route

.. cfg_cmd:: vrf name <tag> ipv6 protocol <tag>

help: Filter routing info exchanged between routing protocol and zebra

.. cfg_cmd:: vrf name <tag> ipv6 protocol <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols

help: Routing protocol parameters

.. cfg_cmd:: vrf name <tag> protocols bgp

help: Border Gateway Protocol (BGP)

.. cfg_cmd:: vrf name <tag> protocols bgp address-family

help: BGP address-family parameters

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-flowspec

help: Flowspec IPv4 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-flowspec local-install

help: Apply local policy routing to interface

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-flowspec local-install interface

help: Interface to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast

help: Labeled Unicast IPv4 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast aggregate-address <tag>

help: BGP aggregate network/prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast aggregate-address <tag> as-set

help: Generate AS-set path information for this aggregate address

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast aggregate-address <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast aggregate-address <tag> summary-only

help: Announce the aggregate summary network only

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast maximum-paths

help: Forward packets over multiple paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast maximum-paths ebgp

help: eBGP maximum paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast maximum-paths ibgp

help: iBGP maximum paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast network <tag>

help: Import BGP network/prefix into labeled unicast IPv4 RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast network <tag> backdoor

help: Use BGP network/prefix as a backdoor route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-labeled-unicast network <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast

help: Multicast IPv4 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast aggregate-address <tag>

help: BGP aggregate network/prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast aggregate-address <tag> as-set

help: Generate AS-set path information for this aggregate address

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast aggregate-address <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast aggregate-address <tag> summary-only

help: Announce the aggregate summary network only

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast distance

help: Administrative distances for BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast distance external

help: eBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast distance internal

help: iBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast distance local

help: Locally originated BGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast distance prefix <tag>

help: Administrative distance for a specific BGP prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast distance prefix <tag> distance

help: Administrative distance for prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast network <tag>

help: Import BGP network/prefix into multicast IPv4 RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast network <tag> backdoor

help: Use BGP network/prefix as a backdoor route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-multicast network <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast

help: IPv4 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast aggregate-address <tag>

help: BGP aggregate network

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast aggregate-address <tag> as-set

help: Generate AS-set path information for this aggregate address

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast aggregate-address <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast aggregate-address <tag> summary-only

help: Announce the aggregate summary network only

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast distance

help: Administrative distances for BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast distance external

help: eBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast distance internal

help: iBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast distance local

help: Locally originated BGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast distance prefix <tag>

help: Administrative distance for a specific BGP prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast distance prefix <tag> distance

help: Administrative distance for prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast export

help: Export routes from this address-family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast export vpn

help: to/from default instance VPN RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast import

help: Import routes to this address-family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast import vpn

help: to/from default instance VPN RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast import vrf

help: VRF to import from

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast label

help: Label value for VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast label vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast label vpn allocation-mode

help: Label allocation mode

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast label vpn allocation-mode per-nexthop

help: Allocate a label per connected next-hop in the VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast label vpn export

help: For routes leaked from current address-family to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast maximum-paths

help: Forward packets over multiple paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast maximum-paths ebgp

help: eBGP maximum paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast maximum-paths ibgp

help: iBGP maximum paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast network <tag>

help: BGP network

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast network <tag> backdoor

help: Network as a backdoor route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast network <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast nexthop

help: Specify next hop to use for VRF advertised prefixes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast nexthop vpn

help: Between current address-family and vpn

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast nexthop vpn export

help: For routes leaked from current address-family to vpn

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast rd

help: Specify route distinguisher

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast rd vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast rd vpn export

help: For routes leaked from current address-family to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute

help: Redistribute routes from other protocols into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute babel

help: Redistribute Babel routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute babel metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute connected

help: Redistribute connected routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute connected metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute isis

help: Redistribute IS-IS routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute isis metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute isis route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute kernel

help: Redistribute kernel routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute kernel metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute ospf

help: Redistribute OSPF routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute ospf metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute ospf route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute rip

help: Redistribute RIP routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute rip metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute rip route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute static

help: Redistribute static routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute static metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast redistribute table

help: Redistribute non-main Kernel Routing Table

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-map vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-map vpn export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-map vpn import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-target

help: Specify route target list

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-target vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-target vpn both

help: Route Target both import and export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-target vpn export

help: Route Target export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast route-target vpn import

help: Route Target import

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast sid

help: SID value for VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast sid vpn

help: Between current VRF and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-unicast sid vpn export

help: For routes leaked from current VRF to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-vpn

help: Unicast VPN IPv4 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-vpn network <tag>

help: Import BGP network/prefix into unicast VPN IPv4 RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-vpn network <tag> label

help: MPLS label value assigned to route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv4-vpn network <tag> rd

help: Route Distinguisher

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-flowspec

help: Flowspec IPv6 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-flowspec local-install

help: Apply local policy routing to interface

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-flowspec local-install interface

help: Interface

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast

help: Labeled Unicast IPv6 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast aggregate-address <tag>

help: BGP aggregate network/prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast aggregate-address <tag> as-set

help: Generate AS-set path information for this aggregate address

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast aggregate-address <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast aggregate-address <tag> summary-only

help: Announce the aggregate summary network only

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast network <tag>

help: Import BGP network/prefix into labeled unicast IPv6 RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast network <tag> backdoor

help: Use BGP network/prefix as a backdoor route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-labeled-unicast network <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast

help: Multicast IPv6 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast aggregate-address <tag>

help: BGP aggregate network/prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast aggregate-address <tag> as-set

help: Generate AS-set path information for this aggregate address

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast aggregate-address <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast aggregate-address <tag> summary-only

help: Announce the aggregate summary network only

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast distance

help: Administrative distances for BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast distance external

help: eBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast distance internal

help: iBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast distance local

help: Locally originated BGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast distance prefix <tag>

help: Administrative distance for a specific BGP prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast distance prefix <tag> distance

help: Administrative distance for prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast network <tag>

help: Import BGP network/prefix into multicast IPv6 RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast network <tag> path-limit

help: AS-path hopcount limit

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-multicast network <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast

help: IPv6 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast aggregate-address <tag>

help: BGP aggregate network

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast aggregate-address <tag> as-set

help: Generate AS-set path information for this aggregate address

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast aggregate-address <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast aggregate-address <tag> summary-only

help: Announce the aggregate summary network only

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast distance

help: Administrative distances for BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast distance external

help: eBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast distance internal

help: iBGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast distance local

help: Locally originated BGP routes administrative distance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast distance prefix <tag>

help: Administrative distance for a specific BGP prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast distance prefix <tag> distance

help: Administrative distance for prefix

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast export

help: Export routes from this address-family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast export vpn

help: to/from default instance VPN RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast import

help: Import routes to this address-family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast import vpn

help: to/from default instance VPN RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast import vrf

help: VRF to import from

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast label

help: Label value for VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast label vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast label vpn allocation-mode

help: Label allocation mode

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast label vpn allocation-mode per-nexthop

help: Allocate a label per connected next-hop in the VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast label vpn export

help: For routes leaked from current address-family to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast maximum-paths

help: Forward packets over multiple paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast maximum-paths ebgp

help: eBGP maximum paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast maximum-paths ibgp

help: iBGP maximum paths

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast network <tag>

help: BGP network

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast network <tag> path-limit

help: AS-path hopcount limit

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast network <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast nexthop

help: Specify next hop to use for VRF advertised prefixes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast nexthop vpn

help: Between current address-family and vpn

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast nexthop vpn export

help: For routes leaked from current address-family to vpn

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast rd

help: Specify route distinguisher

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast rd vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast rd vpn export

help: For routes leaked from current address-family to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute

help: Redistribute routes from other protocols into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute babel

help: Redistribute Babel routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute babel metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute connected

help: Redistribute connected routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute connected metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute kernel

help: Redistribute kernel routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute kernel metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute ospfv3

help: Redistribute OSPFv3 routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute ospfv3 metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute ospfv3 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute ripng

help: Redistribute RIPng routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute ripng metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute ripng route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute static

help: Redistribute static routes into BGP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute static metric

help: Metric for redistributed routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast redistribute table

help: Redistribute non-main Kernel Routing Table

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-map vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-map vpn export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-map vpn import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-target

help: Specify route target list

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-target vpn

help: Between current address-family and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-target vpn both

help: Route Target both import and export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-target vpn export

help: Route Target export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast route-target vpn import

help: Route Target import

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast sid

help: SID value for VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast sid vpn

help: Between current VRF and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-unicast sid vpn export

help: For routes leaked from current VRF to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-vpn

help: Unicast VPN IPv6 BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-vpn network <tag>

help: Import BGP network/prefix into unicast VPN IPv6 RIB

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-vpn network <tag> label

help: MPLS label value assigned to route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family ipv6-vpn network <tag> rd

help: Route Distinguisher

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn

help: L2VPN EVPN BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise

help: Advertise prefix routes

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise ipv4

help: IPv4 address family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise ipv4 unicast

help: IPv4 address family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise ipv4 unicast route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise ipv6

help: IPv6 address family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise ipv6 unicast

help: IPv4 address family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise ipv6 unicast route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise-all-vni

help: Advertise All local VNIs

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise-default-gw

help: Advertise All default g/w mac-ip routes in EVPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise-pip

help: EVPN system primary IP

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn advertise-svi-ip

help: Advertise svi mac-ip routes in EVPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn default-originate

help: Originate a default route

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn default-originate ipv4

help: IPv4 address family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn default-originate ipv6

help: IPv6 address family

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn disable-ead-evi-rx

help: Activate PE on EAD-ES even if EAD-EVI is not received

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn disable-ead-evi-tx

help: Do not advertise EAD-EVI for local ESs

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn ead-es-frag

help: EAD ES fragment config

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn ead-es-frag evi-limit

help: EVIs per-fragment

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn ead-es-route-target

help: EAD ES Route Target

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn ead-es-route-target export

help: Route Target export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn flooding

help: Specify handling for BUM packets

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn flooding disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn flooding head-end-replication

help: Flood BUM packets using head-end replication

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn mac-vrf

help: EVPN MAC-VRF

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn mac-vrf soo

help: Site-of-Origin extended community

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn rd

help: Route Distinguisher

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn route-target

help: Route Target

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn route-target both

help: Route Target both import and export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn route-target export

help: Route Target export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn route-target import

help: Route Target import

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn rt-auto-derive

help: Auto derivation of Route Target (RFC8365)

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag>

help: VXLAN Network Identifier

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> advertise-default-gw

help: Advertise All default g/w mac-ip routes in EVPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> advertise-svi-ip

help: Advertise svi mac-ip routes in EVPN

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> rd

help: Route Distinguisher

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> route-target

help: Route Target

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> route-target both

help: Route Target both import and export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> route-target export

help: Route Target export

.. cfg_cmd:: vrf name <tag> protocols bgp address-family l2vpn-evpn vni <tag> route-target import

help: Route Target import

.. cfg_cmd:: vrf name <tag> protocols bgp bmp

help: BGP Monitoring Protocol (BMP)

.. cfg_cmd:: vrf name <tag> protocols bgp bmp mirror-buffer-limit

help: Maximum memory used for buffered mirroring messages (in bytes)

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag>

help: BMP target

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> address

help: IP address

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> max-retry

help: Maximum connection retry interval
2000


.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> min-retry

help: Minimum connection retry interval (in milliseconds)
1000


.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> mirror

help: Send BMP route mirroring messages

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor

help: Send BMP route monitoring messages

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor ipv4-unicast

help: Address family IPv4 unicast

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor ipv4-unicast post-policy

help: Send state with policy and filters applied

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor ipv4-unicast pre-policy

help: Send state before policy and filter processing

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor ipv6-unicast

help: Address family IPv6 unicast

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor ipv6-unicast post-policy

help: Send state with policy and filters applied

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> monitor ipv6-unicast pre-policy

help: Send state before policy and filter processing

.. cfg_cmd:: vrf name <tag> protocols bgp bmp target <tag> port

help: Port number used by connection
5000


.. cfg_cmd:: vrf name <tag> protocols bgp interface <tag>

help: Configure interface related parameters, e.g. MPLS

.. cfg_cmd:: vrf name <tag> protocols bgp interface <tag> mpls

help: MPLS options

.. cfg_cmd:: vrf name <tag> protocols bgp interface <tag> mpls forwarding

help: Enable MPLS forwarding for eBGP directly connected peers

.. cfg_cmd:: vrf name <tag> protocols bgp listen

help: Listen for and accept BGP dynamic neighbors from range

.. cfg_cmd:: vrf name <tag> protocols bgp listen limit

help: Maximum number of dynamic neighbors that can be created

.. cfg_cmd:: vrf name <tag> protocols bgp listen range <tag>

help: BGP dynamic neighbors listen range

.. cfg_cmd:: vrf name <tag> protocols bgp listen range <tag> peer-group

help: Peer group for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag>

help: BGP neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family

help: Address-family parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec

help: IPv4 Flow Specification BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-flowspec soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast

help: IPv4 Labeled Unicast BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast capability

help: Advertise capabilities to this neighbor (IPv4)

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-labeled-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast

help: IPv4 Multicast BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast capability

help: Advertise capabilities to this neighbor (IPv4)

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-multicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast

help: IPv4 BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast capability

help: Advertise capabilities to this neighbor (IPv4)

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn

help: IPv4 VPN BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv4-vpn weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec

help: IPv6 Flow Specification BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-flowspec soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast

help: IPv6 Labeled Unicast BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast capability

help: Advertise capabilities to this neighbor (IPv6)

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-labeled-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast

help: IPv6 Multicast BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-multicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast

help: IPv6 BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast capability

help: Advertise capabilities to this neighbor (IPv6)

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn

help: IPv6 VPN BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family ipv6-vpn weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn

help: L2VPN EVPN BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> address-family l2vpn-evpn soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> advertisement-interval

help: Minimum interval for sending routing updates

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD) support

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> bfd check-control-plane-failure

help: Allow to write CBIT independence in BFD outgoing packets and read both C-BIT value of BFD and lookup BGP peer status

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> capability

help: Advertise capabilities to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> capability dynamic

help: Advertise dynamic capability to this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> capability extended-nexthop

help: Advertise extended-nexthop capability to this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> capability software-version

help: Advertise Software Version capability to the peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> description

help: Description

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> disable-capability-negotiation

help: Disable capability negotiation with this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> disable-connected-check

help: Disable check to see if eBGP peer address is a connected route

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> ebgp-multihop

help: Allow this EBGP neighbor to not be on a directly connected network

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> enforce-first-as

help: Ensure the first AS in the AS path matches the peer AS

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> graceful-restart

help: BGP graceful restart functionality

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface

help: Interface parameters

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface peer-group

help: Peer group for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface remote-as

help: Neighbor BGP AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface source-interface

help: Interface used to establish connection

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface v6only

help: Enable BGP with v6 link-local only

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface v6only peer-group

help: Peer group for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> interface v6only remote-as

help: Neighbor BGP AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> local-as <tag>

help: Specify alternate ASN for this BGP process

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> local-as <tag> no-prepend

help: Disable prepending local-as from/to updates for eBGP peers

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> local-as <tag> no-prepend replace-as

help: Prepend only local-as from/to updates for eBGP peers

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> local-role <tag>

help: Local role for BGP neighbor (RFC9234)

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> local-role <tag> strict

help: Neighbor must send this exact capability, otherwise a role missmatch notification will be sent

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> override-capability

help: Ignore capability negotiation with specified neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> passive

help: Do not initiate a session with this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> password

help: BGP MD5 password

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> path-attribute

help: Manipulate path attributes from incoming UPDATE messages

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> path-attribute discard

help: Drop specified attributes from incoming UPDATE messages

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> path-attribute treat-as-withdraw

help: Treat-as-withdraw any incoming BGP UPDATE messages that contain the specified attribute

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> peer-group

help: Peer group for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> port

help: Port number used by connection

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> remote-as

help: Neighbor BGP AS number

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> shutdown

help: Administratively shutdown this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> solo

help: Do not send back prefixes learned from the neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> strict-capability-match

help: Enable strict capability negotiation

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> timers

help: Neighbor timers

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> timers connect

help: BGP connect timer for this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> timers holdtime

help: Hold timer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> timers keepalive

help: BGP keepalive interval for this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> ttl-security

help: Ttl security mechanism

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> ttl-security hops

help: Number of the maximum number of hops to the BGP peer

.. cfg_cmd:: vrf name <tag> protocols bgp neighbor <tag> update-source

help: Source IP of routing updates

.. cfg_cmd:: vrf name <tag> protocols bgp parameters

help: BGP parameters

.. cfg_cmd:: vrf name <tag> protocols bgp parameters allow-martian-nexthop

help: Allow Martian nexthops to be received in the NLRI from a peer

.. cfg_cmd:: vrf name <tag> protocols bgp parameters always-compare-med

help: Always compare MEDs from different neighbors

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath

help: Default bestpath selection mechanism

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath as-path

help: AS-path attribute comparison parameters

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath as-path confed

help: Compare AS-path lengths including confederation sets and sequences

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath as-path ignore

help: Ignore AS-path length in selecting a route

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath as-path multipath-relax

help: Allow load sharing across routes that have different AS paths (but same length)

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath bandwidth

help: Link Bandwidth attribute

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath compare-routerid

help: Compare the router-id for identical EBGP paths

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath med

help: MED attribute comparison parameters

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath peer-type

help: Peer type

.. cfg_cmd:: vrf name <tag> protocols bgp parameters bestpath peer-type multipath-relax

help: Allow load sharing across routes learned from different peer types

.. cfg_cmd:: vrf name <tag> protocols bgp parameters cluster-id

help: Route-reflector cluster-id

.. cfg_cmd:: vrf name <tag> protocols bgp parameters conditional-advertisement

help: Conditional advertisement settings

.. cfg_cmd:: vrf name <tag> protocols bgp parameters conditional-advertisement timer

help: Set period to rescan BGP table to check if condition is met
60


.. cfg_cmd:: vrf name <tag> protocols bgp parameters confederation

help: AS confederation parameters

.. cfg_cmd:: vrf name <tag> protocols bgp parameters confederation identifier

help: Confederation AS identifier

.. cfg_cmd:: vrf name <tag> protocols bgp parameters confederation peers

help: Peer ASs in the BGP confederation

.. cfg_cmd:: vrf name <tag> protocols bgp parameters dampening

help: Enable route-flap dampening

.. cfg_cmd:: vrf name <tag> protocols bgp parameters dampening half-life

help: Half-life time for dampening

.. cfg_cmd:: vrf name <tag> protocols bgp parameters dampening max-suppress-time

help: Maximum duration to suppress a stable route

.. cfg_cmd:: vrf name <tag> protocols bgp parameters dampening re-use

help: Threshold to start reusing a route

.. cfg_cmd:: vrf name <tag> protocols bgp parameters dampening start-suppress-time

help: When to start suppressing a route

.. cfg_cmd:: vrf name <tag> protocols bgp parameters default

help: BGP defaults

.. cfg_cmd:: vrf name <tag> protocols bgp parameters default local-pref

help: Default local preference

.. cfg_cmd:: vrf name <tag> protocols bgp parameters deterministic-med

help: Compare MEDs between different peers in the same AS

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance

help: Administratives distances for BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance global

help: Global administratives distances for BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance global external

help: Administrative distance for external BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance global internal

help: Administrative distance for internal BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance global local

help: Administrative distance for local BGP routes

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance prefix <tag>

help: Administrative distance for a specific BGP prefix

.. cfg_cmd:: vrf name <tag> protocols bgp parameters distance prefix <tag> distance

help: Administrative distance for prefix

.. cfg_cmd:: vrf name <tag> protocols bgp parameters ebgp-requires-policy

help: Require in and out policy for eBGP peers (RFC8212)

.. cfg_cmd:: vrf name <tag> protocols bgp parameters fast-convergence

help: Teardown sessions immediately whenever peer becomes unreachable

.. cfg_cmd:: vrf name <tag> protocols bgp parameters graceful-restart

help: Graceful restart capability parameters

.. cfg_cmd:: vrf name <tag> protocols bgp parameters graceful-restart stalepath-time

help: Maximum time to hold onto restarting neighbors stale paths

.. cfg_cmd:: vrf name <tag> protocols bgp parameters graceful-shutdown

help: Graceful shutdown

.. cfg_cmd:: vrf name <tag> protocols bgp parameters labeled-unicast

help: BGP Labeled-unicast options

.. cfg_cmd:: vrf name <tag> protocols bgp parameters log-neighbor-changes

help: Log neighbor up/down changes and reset reason

.. cfg_cmd:: vrf name <tag> protocols bgp parameters minimum-holdtime

help: BGP minimum holdtime

.. cfg_cmd:: vrf name <tag> protocols bgp parameters network-import-check

help: Enable IGP route check for network statements

.. cfg_cmd:: vrf name <tag> protocols bgp parameters no-client-to-client-reflection

help: Disable client to client route reflection

.. cfg_cmd:: vrf name <tag> protocols bgp parameters no-fast-external-failover

help: Disable immediate session reset on peer link down event

.. cfg_cmd:: vrf name <tag> protocols bgp parameters no-hard-administrative-reset

help: Do not send hard reset CEASE Notification for 'Administrative Reset'

.. cfg_cmd:: vrf name <tag> protocols bgp parameters no-suppress-duplicates

help: Disable suppress duplicate updates if the route actually not changed

.. cfg_cmd:: vrf name <tag> protocols bgp parameters reject-as-sets

help: Reject routes with AS_SET or AS_CONFED_SET flag

.. cfg_cmd:: vrf name <tag> protocols bgp parameters route-reflector-allow-outbound-policy

help: Route reflector client allow policy outbound

.. cfg_cmd:: vrf name <tag> protocols bgp parameters router-id

help: Override default router identifier

.. cfg_cmd:: vrf name <tag> protocols bgp parameters shutdown

help: Administrative shutdown of the BGP instance

.. cfg_cmd:: vrf name <tag> protocols bgp parameters suppress-fib-pending

help: Advertise only routes that are programmed in kernel to peers

.. cfg_cmd:: vrf name <tag> protocols bgp parameters tcp-keepalive

help: TCP keepalive parameters

.. cfg_cmd:: vrf name <tag> protocols bgp parameters tcp-keepalive idle

help: TCP keepalive idle time

.. cfg_cmd:: vrf name <tag> protocols bgp parameters tcp-keepalive interval

help: TCP keepalive interval

.. cfg_cmd:: vrf name <tag> protocols bgp parameters tcp-keepalive probes

help: TCP keepalive maximum probes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag>

help: Name of peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family

help: Address-family parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast

help: IPv4 Labeled Unicast BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast capability

help: Advertise capabilities to this neighbor (IPv4)

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-labeled-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast

help: IPv4 BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast capability

help: Advertise capabilities to this neighbor (IPv4)

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn

help: IPv4 VPN BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn prefix-list

help: IPv4-Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn prefix-list export

help: IPv4-Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn prefix-list import

help: IPv4-Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv4-vpn weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast

help: IPv6 Labeled Unicast BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast capability

help: Advertise capabilities to this neighbor (IPv6)

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-labeled-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast

help: IPv6 BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast capability

help: Advertise capabilities to this neighbor (IPv6)

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast capability orf

help: Advertise ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast capability orf prefix-list

help: Advertise prefix-list ORF capability to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast capability orf prefix-list receive

help: Capability to receive the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast capability orf prefix-list send

help: Capability to send the ORF

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast default-originate

help: Originate default route to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast default-originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-unicast weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn

help: IPv6 VPN BGP neighbor parameters

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn addpath-tx-all

help: Use addpath to advertise all paths to a neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn addpath-tx-per-as

help: Use addpath to advertise the bestpath per each neighboring AS

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn as-override

help: Override ASN in outbound updates to configured neighbor local-as

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn conditionally-advertise

help: Use route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn conditionally-advertise advertise-map

help: Route-map to conditionally advertise routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn conditionally-advertise exist-map

help: Advertise routes only if prefixes in exist-map are installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn conditionally-advertise non-exist-map

help: Advertise routes only if prefixes in non-exist-map are not installed in BGP table

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn disable-send-community

help: Disable sending community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn disable-send-community extended

help: Disable sending extended community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn disable-send-community standard

help: Disable sending standard community attributes to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn distribute-list

help: Access-list to filter route updates to/from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn distribute-list export

help: Access-list to filter outgoing route updates to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn distribute-list import

help: Access-list to filter incoming route updates from this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn filter-list

help: as-path-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn filter-list export

help: As-path-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn filter-list import

help: As-path-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn maximum-prefix

help: Maximum number of prefixes to accept from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn maximum-prefix-out

help: Maximum number of prefixes to be sent to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn nexthop-local

help: Nexthop attributes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn nexthop-local unchanged

help: Leave link-local nexthop unchanged for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn prefix-list

help: Prefix-list to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn prefix-list export

help: Prefix-list to filter outgoing route updates to this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn prefix-list import

help: Prefix-list to filter incoming route updates from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn remove-private-as

help: Remove private AS numbers from AS path in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn remove-private-as all

help: Remove private AS numbers to all AS numbers in outbound route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn unsuppress-map

help: Route-map to selectively unsuppress suppressed routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family ipv6-vpn weight

help: Default weight for routes from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn

help: L2VPN EVPN BGP settings

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn allowas-in

help: Accept route that contains the local-as in the as-path

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn allowas-in number

help: Number of occurrences of AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn attribute-unchanged

help: BGP attributes are sent unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn attribute-unchanged as-path

help: Send AS path unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn attribute-unchanged med

help: Send multi-exit discriminator unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn attribute-unchanged next-hop

help: Send nexthop unchanged

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn nexthop-self

help: Disable the next hop calculation for this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn nexthop-self force

help: Set the next hop to self for reflected routes

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn route-map

help: Route-map to filter route updates to/from this peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn route-map export

help: Route-map to filter outgoing route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn route-map import

help: Route-map to filter incoming route updates

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn route-reflector-client

help: Peer is a route reflector client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn route-server-client

help: Peer is a route server client

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn soft-reconfiguration

help: Soft reconfiguration for peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> address-family l2vpn-evpn soft-reconfiguration inbound

help: Enable inbound soft reconfiguration

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD) support

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> bfd check-control-plane-failure

help: Allow to write CBIT independence in BFD outgoing packets and read both C-BIT value of BFD and lookup BGP peer status

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> capability

help: Advertise capabilities to this peer-group

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> capability dynamic

help: Advertise dynamic capability to this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> capability extended-nexthop

help: Advertise extended-nexthop capability to this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> capability software-version

help: Advertise Software Version capability to the peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> description

help: Description

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> disable-capability-negotiation

help: Disable capability negotiation with this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> disable-connected-check

help: Disable check to see if eBGP peer address is a connected route

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> ebgp-multihop

help: Allow this EBGP neighbor to not be on a directly connected network

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> graceful-restart

help: BGP graceful restart functionality

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> local-as <tag>

help: Specify alternate ASN for this BGP process

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> local-as <tag> no-prepend

help: Disable prepending local-as from/to updates for eBGP peers

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> local-as <tag> no-prepend replace-as

help: Prepend only local-as from/to updates for eBGP peers

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> local-role <tag>

help: Local role for BGP neighbor (RFC9234)

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> local-role <tag> strict

help: Neighbor must send this exact capability, otherwise a role missmatch notification will be sent

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> override-capability

help: Ignore capability negotiation with specified neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> passive

help: Do not initiate a session with this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> password

help: BGP MD5 password

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> path-attribute

help: Manipulate path attributes from incoming UPDATE messages

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> path-attribute discard

help: Drop specified attributes from incoming UPDATE messages

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> path-attribute treat-as-withdraw

help: Treat-as-withdraw any incoming BGP UPDATE messages that contain the specified attribute

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> port

help: Port number used by connection

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> remote-as

help: Neighbor BGP AS number

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> shutdown

help: Administratively shutdown this neighbor

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> ttl-security

help: Ttl security mechanism

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> ttl-security hops

help: Number of the maximum number of hops to the BGP peer

.. cfg_cmd:: vrf name <tag> protocols bgp peer-group <tag> update-source

help: Source IP of routing updates

.. cfg_cmd:: vrf name <tag> protocols bgp sid

help: SID value for VRF

.. cfg_cmd:: vrf name <tag> protocols bgp sid vpn

help: Between current VRF and VPN

.. cfg_cmd:: vrf name <tag> protocols bgp sid vpn per-vrf

help: SID per-VRF (both IPv4 and IPv6 address families)

.. cfg_cmd:: vrf name <tag> protocols bgp sid vpn per-vrf export

help: For routes leaked from current VRF to VPN

.. cfg_cmd:: vrf name <tag> protocols bgp srv6

help: Segment-Routing SRv6 configuration

.. cfg_cmd:: vrf name <tag> protocols bgp srv6 locator

help: Specify SRv6 locator

.. cfg_cmd:: vrf name <tag> protocols bgp system-as

help: Autonomous System Number (ASN)

.. cfg_cmd:: vrf name <tag> protocols bgp timers

help: BGP protocol timers

.. cfg_cmd:: vrf name <tag> protocols bgp timers holdtime

help: Hold timer

.. cfg_cmd:: vrf name <tag> protocols bgp timers keepalive

help: BGP keepalive interval for this neighbor

.. cfg_cmd:: vrf name <tag> protocols eigrp

help: Enhanced Interior Gateway Routing Protocol (EIGRP)

.. cfg_cmd:: vrf name <tag> protocols eigrp maximum-paths

help: Forward packets over multiple paths

.. cfg_cmd:: vrf name <tag> protocols eigrp metric

help: Modify metrics and parameters for advertisement

.. cfg_cmd:: vrf name <tag> protocols eigrp metric weights

help: Modify metric coefficients

.. cfg_cmd:: vrf name <tag> protocols eigrp network

help: Enable routing on an IP network

.. cfg_cmd:: vrf name <tag> protocols eigrp passive-interface

help: Suppress routing updates on an interface

.. cfg_cmd:: vrf name <tag> protocols eigrp redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: vrf name <tag> protocols eigrp router-id

help: Override default router identifier

.. cfg_cmd:: vrf name <tag> protocols eigrp system-as

help: Autonomous System Number (ASN)

.. cfg_cmd:: vrf name <tag> protocols eigrp variance

help: Control load balancing variance

.. cfg_cmd:: vrf name <tag> protocols isis

help: Intermediate System to Intermediate System (IS-IS)

.. cfg_cmd:: vrf name <tag> protocols isis advertise-high-metrics

help: Advertise high metric value on all interfaces

.. cfg_cmd:: vrf name <tag> protocols isis advertise-passive-only

help: Advertise prefixes of passive interfaces only

.. cfg_cmd:: vrf name <tag> protocols isis area-password

help: Configure the authentication password for an area

.. cfg_cmd:: vrf name <tag> protocols isis area-password md5

help: MD5 authentication type

.. cfg_cmd:: vrf name <tag> protocols isis area-password plaintext-password

help: Plain-text authentication type

.. cfg_cmd:: vrf name <tag> protocols isis default-information

help: Control distribution of default information

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate

help: Distribute a default route

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4

help: Distribute default route for IPv4

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-1

help: Distribute default route into level-1

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-1 always

help: Always advertise default route

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-2

help: Distribute default route into level-2

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-2 always

help: Always advertise default route

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv4 level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6

help: Distribute default route for IPv6

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-1

help: Distribute default route into level-1

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-1 always

help: Always advertise default route

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-2

help: Distribute default route into level-2

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-2 always

help: Always advertise default route

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis default-information originate ipv6 level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis domain-password

help: Set the authentication password for a routing domain

.. cfg_cmd:: vrf name <tag> protocols isis domain-password md5

help: MD5 authentication type

.. cfg_cmd:: vrf name <tag> protocols isis domain-password plaintext-password

help: Plain-text authentication type

.. cfg_cmd:: vrf name <tag> protocols isis dynamic-hostname

help: Dynamic hostname for IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute

help: IS-IS fast reroute configuration

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa

help: Loop free alternate functionality

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local

help: Local loop free alternate options

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local load-sharing

help: Load share prefixes across multiple backups

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local load-sharing disable

help: Disable load sharing

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local load-sharing disable level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local load-sharing disable level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit

help: Limit backup computation up to the prefix priority

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit critical

help: Compute for critical priority prefixes only

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit critical level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit critical level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit high

help: Compute for critical, and high priority prefixes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit high level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit high level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit medium

help: Compute for critical, high, and medium priority prefixes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit medium level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local priority-limit medium level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker

help: Configure tiebreaker for multiple backups

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker downstream

help: Prefer backup path via downstream node

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker downstream index <tag>

help: Set preference order among tiebreakers

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker downstream index <tag> level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker downstream index <tag> level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker lowest-backup-metric

help: Prefer backup path with lowest total metric

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker lowest-backup-metric index <tag>

help: Set preference order among tiebreakers

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker lowest-backup-metric index <tag> level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker lowest-backup-metric index <tag> level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker node-protecting

help: Prefer node protecting backup path

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker node-protecting index <tag>

help: Set preference order among tiebreakers

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker node-protecting index <tag> level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa local tiebreaker node-protecting index <tag> level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa remote

help: Remote loop free alternate options

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa remote prefix-list <tag>

help: Filter PQ node router ID based on prefix list

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa remote prefix-list <tag> level-1

help: Match on IS-IS level-1 routes

.. cfg_cmd:: vrf name <tag> protocols isis fast-reroute lfa remote prefix-list <tag> level-2

help: Match on IS-IS level-2 routes

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag>

help: Interface params

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> circuit-type

help: Configure circuit type for interface

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> hello-interval

help: Set Hello interval

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> hello-multiplier

help: Set Hello interval

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> hello-padding

help: Add padding to IS-IS hello packets

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> ldp-sync

help: LDP-IGP synchronization configuration for interface

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> ldp-sync disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> ldp-sync holddown

help: Hold down timer for LDP-IGP cost restoration

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> network

help: Set network type

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> network point-to-point

help: point-to-point network type

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> no-three-way-handshake

help: Disable three-way handshake

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> passive

help: Configure passive mode for interface

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> password

help: Configure the authentication password for a circuit

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> password md5

help: MD5 authentication type

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> password plaintext-password

help: Plain-text authentication type

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> priority

help: Set priority for Designated Router election

.. cfg_cmd:: vrf name <tag> protocols isis interface <tag> psnp-interval

help: Set PSNP interval

.. cfg_cmd:: vrf name <tag> protocols isis ldp-sync

help: Protocol wide LDP-IGP synchronization configuration

.. cfg_cmd:: vrf name <tag> protocols isis ldp-sync holddown

help: Hold down timer for LDP-IGP cost restoration

.. cfg_cmd:: vrf name <tag> protocols isis level

help: IS-IS level number

.. cfg_cmd:: vrf name <tag> protocols isis log-adjacency-changes

help: Log adjacency state changes

.. cfg_cmd:: vrf name <tag> protocols isis lsp-gen-interval

help: Minimum interval between regenerating same LSP

.. cfg_cmd:: vrf name <tag> protocols isis lsp-mtu

help: Configure the maximum size of generated LSPs
1497


.. cfg_cmd:: vrf name <tag> protocols isis lsp-refresh-interval

help: LSP refresh interval

.. cfg_cmd:: vrf name <tag> protocols isis max-lsp-lifetime

help: Maximum LSP lifetime

.. cfg_cmd:: vrf name <tag> protocols isis metric-style

help: Use old-style (ISO 10589) or new-style packet formats

.. cfg_cmd:: vrf name <tag> protocols isis net

help: A Network Entity Title for this process (ISO only)

.. cfg_cmd:: vrf name <tag> protocols isis purge-originator

help: Use the RFC 6232 purge-originator

.. cfg_cmd:: vrf name <tag> protocols isis redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4

help: Redistribute IPv4 routes

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel

help: Redistribute Babel routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 babel level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp

help: Border Gateway Protocol (BGP)

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 bgp level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected

help: Redistribute connected routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 connected level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel

help: Redistribute kernel routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 kernel level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf

help: Redistribute OSPF routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 ospf level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip

help: Redistribute RIP routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 rip level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static

help: Redistribute static routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv4 static level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6

help: Redistribute IPv6 routes

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel

help: Redistribute Babel routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 babel level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp

help: Redistribute BGP routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 bgp level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected

help: Redistribute connected routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 connected level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel

help: Redistribute kernel routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 kernel level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6

help: Redistribute OSPFv3 routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6 level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6 level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6 level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6 level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6 level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ospf6 level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng

help: Redistribute RIPng routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 ripng level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static

help: Redistribute static routes into IS-IS

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static level-1

help: Redistribute into level-1

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static level-1 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static level-1 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static level-2

help: Redistribute into level-2

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static level-2 metric

help: Set default metric for circuit

.. cfg_cmd:: vrf name <tag> protocols isis redistribute ipv6 static level-2 route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing

help: Segment-Routing (SPRING) settings

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing global-block

help: Segment Routing Global Block label range

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing global-block high-label-value

help: MPLS label upper bound

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing global-block low-label-value

help: MPLS label lower bound

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing local-block

help: Segment Routing Local Block label range

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing local-block high-label-value

help: MPLS label upper bound

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing local-block low-label-value

help: MPLS label lower bound

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing maximum-label-depth

help: Maximum MPLS labels allowed for this router

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag>

help: Static IPv4/IPv6 prefix segment/label mapping

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> absolute

help: Specify the absolute value of prefix segment/label ID

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> absolute explicit-null

help: Request upstream neighbor to replace segment/label with explicit null label

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> absolute no-php-flag

help: Do not request penultimate hop popping for segment/label

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> absolute value

help: Specify the absolute value of prefix segment/label ID

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> index

help: Specify the index value of prefix segment/label ID

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> index explicit-null

help: Request upstream neighbor to replace segment/label with explicit null label

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> index no-php-flag

help: Do not request penultimate hop popping for segment/label

.. cfg_cmd:: vrf name <tag> protocols isis segment-routing prefix <tag> index value

help: Specify the index value of prefix segment/label ID

.. cfg_cmd:: vrf name <tag> protocols isis set-attached-bit

help: Set attached bit to identify as L1/L2 router for inter-area traffic

.. cfg_cmd:: vrf name <tag> protocols isis set-overload-bit

help: Set overload bit to avoid any transit traffic

.. cfg_cmd:: vrf name <tag> protocols isis spf-delay-ietf

help: IETF SPF delay algorithm

.. cfg_cmd:: vrf name <tag> protocols isis spf-delay-ietf holddown

help: Time with no received IGP events before considering IGP stable

.. cfg_cmd:: vrf name <tag> protocols isis spf-delay-ietf init-delay

help: Delay used while in QUIET state

.. cfg_cmd:: vrf name <tag> protocols isis spf-delay-ietf long-delay

help: Delay used while in LONG_WAIT

.. cfg_cmd:: vrf name <tag> protocols isis spf-delay-ietf short-delay

help: Delay used while in SHORT_WAIT state

.. cfg_cmd:: vrf name <tag> protocols isis spf-delay-ietf time-to-learn

help: Maximum duration needed to learn all the events related to a single failure

.. cfg_cmd:: vrf name <tag> protocols isis spf-interval

help: Minimum interval between SPF calculations

.. cfg_cmd:: vrf name <tag> protocols isis traffic-engineering

help: IS-IS traffic engineering extensions

.. cfg_cmd:: vrf name <tag> protocols isis traffic-engineering address

help: MPLS traffic engineering router ID

.. cfg_cmd:: vrf name <tag> protocols isis traffic-engineering enable

help: Enable MPLS traffic engineering extensions

.. cfg_cmd:: vrf name <tag> protocols ospf

help: Open Shortest Path First (OSPF)

.. cfg_cmd:: vrf name <tag> protocols ospf access-list <tag>

help: Access list to filter networks in routing updates

.. cfg_cmd:: vrf name <tag> protocols ospf access-list <tag> export

help: Filter for outgoing routing update

.. cfg_cmd:: vrf name <tag> protocols ospf aggregation

help: External route aggregation

.. cfg_cmd:: vrf name <tag> protocols ospf aggregation timer

help: Delay timer
5


.. cfg_cmd:: vrf name <tag> protocols ospf area <tag>

help: OSPF area settings

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type

help: Area type

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type normal

help: Normal OSPF area

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type nssa

help: Not-So-Stubby OSPF area

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type nssa default-cost

help: Summary-default cost of an NSSA area

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type nssa no-summary

help: Do not inject inter-area routes into stub

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type nssa translate

help: Configure NSSA-ABR
candidate


.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type stub

help: Stub OSPF area

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type stub default-cost

help: Summary-default cost

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> area-type stub no-summary

help: Do not inject inter-area routes into the stub

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> authentication

help: OSPF area authentication type

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> export-list

help: Set the filter for networks announced to other areas

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> import-list

help: Set the filter for networks from other areas announced

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> network

help: OSPF network

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> range <tag>

help: Summarize routes matching a prefix (border routers only)

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> range <tag> cost

help: Metric for this range

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> range <tag> not-advertise

help: Do not advertise this range

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> range <tag> substitute

help: Advertise area range as another prefix

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> shortcut

help: Area shortcut mode

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag>

help: Virtual link

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> authentication

help: Authentication

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> authentication md5

help: MD5 key id

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> authentication md5 key-id <tag>

help: MD5 key id

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> authentication md5 key-id <tag> md5-key

help: MD5 authentication type

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> authentication plaintext-password

help: Plain text password

.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> dead-interval

help: Interval after which a neighbor is declared dead
40


.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> hello-interval

help: Interval between hello packets
10


.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> retransmit-interval

help: Interval between retransmitting lost link state advertisements
5


.. cfg_cmd:: vrf name <tag> protocols ospf area <tag> virtual-link <tag> transmit-delay

help: Link state transmit delay
1


.. cfg_cmd:: vrf name <tag> protocols ospf auto-cost

help: Calculate interface cost according to bandwidth

.. cfg_cmd:: vrf name <tag> protocols ospf auto-cost reference-bandwidth

help: Reference bandwidth method to assign cost
100


.. cfg_cmd:: vrf name <tag> protocols ospf capability

help: Enable specific OSPF features

.. cfg_cmd:: vrf name <tag> protocols ospf capability opaque

help: Opaque LSA

.. cfg_cmd:: vrf name <tag> protocols ospf default-information

help: Default route advertisment settings

.. cfg_cmd:: vrf name <tag> protocols ospf default-information originate

help: Distribute a default route

.. cfg_cmd:: vrf name <tag> protocols ospf default-information originate always

help: Always advertise a default route

.. cfg_cmd:: vrf name <tag> protocols ospf default-information originate metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf default-information originate metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf default-information originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf default-metric

help: Metric of redistributed routes

.. cfg_cmd:: vrf name <tag> protocols ospf distance

help: Administrative distance

.. cfg_cmd:: vrf name <tag> protocols ospf distance global

help: Administrative distance

.. cfg_cmd:: vrf name <tag> protocols ospf distance ospf

help: OSPF administrative distance

.. cfg_cmd:: vrf name <tag> protocols ospf distance ospf external

help: Distance for external routes

.. cfg_cmd:: vrf name <tag> protocols ospf distance ospf inter-area

help: Distance for inter-area routes

.. cfg_cmd:: vrf name <tag> protocols ospf distance ospf intra-area

help: Distance for intra-area routes

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart

help: Graceful Restart

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart grace-period

help: Maximum length of the grace period
120


.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart helper

help: OSPF graceful-restart helpers

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart helper enable

help: Enable helper support

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart helper enable router-id

help: Advertising Router-ID

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart helper no-strict-lsa-checking

help: Disable strict LSA check

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart helper planned-only

help: Supported only planned restart

.. cfg_cmd:: vrf name <tag> protocols ospf graceful-restart helper supported-grace-time

help: Supported grace timer

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag>

help: Interface configuration

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> area

help: Enable OSPF on this interface

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> authentication

help: Authentication

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> authentication md5

help: MD5 key id

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> authentication md5 key-id <tag>

help: MD5 key id

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> authentication md5 key-id <tag> md5-key

help: MD5 authentication type

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> authentication plaintext-password

help: Plain text password

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> bandwidth

help: Interface bandwidth (Mbit/s)

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> cost

help: Interface cost

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> dead-interval

help: Interval after which a neighbor is declared dead
40


.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> hello-interval

help: Interval between hello packets
10


.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> hello-multiplier

help: Hello multiplier factor

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> ldp-sync

help: LDP-IGP synchronization configuration for interface

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> ldp-sync disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> ldp-sync holddown

help: Hold down timer for LDP-IGP cost restoration

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> mtu-ignore

help: Disable Maximum Transmission Unit (MTU) mismatch detection

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> network

help: Network type

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> passive

help: Suppress routing updates on an interface

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> passive disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> priority

help: Router priority
1


.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> retransmit-interval

help: Interval between retransmitting lost link state advertisements
5


.. cfg_cmd:: vrf name <tag> protocols ospf interface <tag> transmit-delay

help: Link state transmit delay
1


.. cfg_cmd:: vrf name <tag> protocols ospf ldp-sync

help: Protocol wide LDP-IGP synchronization configuration

.. cfg_cmd:: vrf name <tag> protocols ospf ldp-sync holddown

help: Hold down timer for LDP-IGP cost restoration

.. cfg_cmd:: vrf name <tag> protocols ospf log-adjacency-changes

help: Log adjacency state changes

.. cfg_cmd:: vrf name <tag> protocols ospf log-adjacency-changes detail

help: Log all state changes

.. cfg_cmd:: vrf name <tag> protocols ospf max-metric

help: OSPF maximum and infinite-distance metric

.. cfg_cmd:: vrf name <tag> protocols ospf max-metric router-lsa

help: Advertise own Router-LSA with infinite distance (stub router)

.. cfg_cmd:: vrf name <tag> protocols ospf max-metric router-lsa administrative

help: Administratively apply, for an indefinite period

.. cfg_cmd:: vrf name <tag> protocols ospf max-metric router-lsa on-shutdown

help: Advertise stub-router prior to full shutdown of OSPF

.. cfg_cmd:: vrf name <tag> protocols ospf max-metric router-lsa on-startup

help: Automatically advertise stub Router-LSA on startup of OSPF

.. cfg_cmd:: vrf name <tag> protocols ospf maximum-paths

help: Maximum multiple paths (ECMP)

.. cfg_cmd:: vrf name <tag> protocols ospf mpls-te

help: MultiProtocol Label Switching-Traffic Engineering (MPLS-TE) parameters

.. cfg_cmd:: vrf name <tag> protocols ospf mpls-te enable

help: Enable MPLS-TE functionality

.. cfg_cmd:: vrf name <tag> protocols ospf mpls-te router-address

help: Stable IP address of the advertising router
0.0.0.0


.. cfg_cmd:: vrf name <tag> protocols ospf neighbor <tag>

help: Specify neighbor router

.. cfg_cmd:: vrf name <tag> protocols ospf neighbor <tag> poll-interval

help: Dead neighbor polling interval
60


.. cfg_cmd:: vrf name <tag> protocols ospf neighbor <tag> priority

help: Neighbor priority in seconds
0


.. cfg_cmd:: vrf name <tag> protocols ospf parameters

help: OSPF specific parameters

.. cfg_cmd:: vrf name <tag> protocols ospf parameters abr-type

help: OSPF ABR type
cisco


.. cfg_cmd:: vrf name <tag> protocols ospf parameters opaque-lsa

help: Enable the Opaque-LSA capability (rfc2370)

.. cfg_cmd:: vrf name <tag> protocols ospf parameters rfc1583-compatibility

help: Enable RFC1583 criteria for handling AS external routes

.. cfg_cmd:: vrf name <tag> protocols ospf parameters router-id

help: Override default router identifier

.. cfg_cmd:: vrf name <tag> protocols ospf passive-interface

help: Suppress routing updates on an interface

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute babel

help: Redistribute Babel routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute babel metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute babel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute bgp

help: Redistribute BGP routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute bgp metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute bgp metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute bgp route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute connected

help: Redistribute connected routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute connected metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute connected metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute isis

help: Redistribute IS-IS routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute isis metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute isis metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute isis route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute kernel

help: Redistribute Kernel routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute kernel metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute kernel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute rip

help: Redistribute RIP routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute rip metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute rip metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute rip route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute static

help: Redistribute statically configured routes

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute static metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute static metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute table <tag>

help: Redistribute non-main Kernel Routing Table

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute table <tag> metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospf redistribute table <tag> metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospf redistribute table <tag> route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospf refresh

help: Adjust refresh parameters

.. cfg_cmd:: vrf name <tag> protocols ospf refresh timers

help: Refresh timer

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing

help: Segment-Routing (SPRING) settings

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing global-block

help: Segment Routing Global Block label range

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing global-block high-label-value

help: MPLS label upper bound

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing global-block low-label-value

help: MPLS label lower bound

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing local-block

help: Segment Routing Local Block label range

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing local-block high-label-value

help: MPLS label upper bound

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing local-block low-label-value

help: MPLS label lower bound

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing maximum-label-depth

help: Maximum MPLS labels allowed for this router

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing prefix <tag>

help: Static IPv4 prefix segment/label mapping

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing prefix <tag> index

help: Specify the index value of prefix segment/label ID

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing prefix <tag> index explicit-null

help: Request upstream neighbor to replace segment/label with explicit null label

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing prefix <tag> index no-php-flag

help: Do not request penultimate hop popping for segment/label

.. cfg_cmd:: vrf name <tag> protocols ospf segment-routing prefix <tag> index value

help: Specify the index value of prefix segment/label ID

.. cfg_cmd:: vrf name <tag> protocols ospf summary-address <tag>

help: External summary address

.. cfg_cmd:: vrf name <tag> protocols ospf summary-address <tag> no-advertise

help: Don not advertise summary route

.. cfg_cmd:: vrf name <tag> protocols ospf summary-address <tag> tag

help: Router tag

.. cfg_cmd:: vrf name <tag> protocols ospf timers

help: Adjust routing timers

.. cfg_cmd:: vrf name <tag> protocols ospf timers throttle

help: Throttling adaptive timers

.. cfg_cmd:: vrf name <tag> protocols ospf timers throttle spf

help: OSPF SPF timers

.. cfg_cmd:: vrf name <tag> protocols ospf timers throttle spf delay

help: Delay from the first change received to SPF calculation
200


.. cfg_cmd:: vrf name <tag> protocols ospf timers throttle spf initial-holdtime

help: Initial hold time between consecutive SPF calculations
1000


.. cfg_cmd:: vrf name <tag> protocols ospf timers throttle spf max-holdtime

help: Maximum hold time
10000


.. cfg_cmd:: vrf name <tag> protocols ospfv3

help: Open Shortest Path First (OSPF) for IPv6

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag>

help: OSPFv3 Area

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> area-type

help: OSPFv3 Area type

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> area-type nssa

help: NSSA OSPFv3 area

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> area-type nssa default-information-originate

help: Originate Type 7 default into NSSA area

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> area-type nssa no-summary

help: Do not inject inter-area routes into the stub

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> area-type stub

help: Stub OSPFv3 area

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> area-type stub no-summary

help: Do not inject inter-area routes into the stub

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> export-list

help: Name of export-list

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> import-list

help: Name of import-list

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> range <tag>

help: Specify IPv6 prefix (border routers only)

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> range <tag> advertise

help: Advertise this range

.. cfg_cmd:: vrf name <tag> protocols ospfv3 area <tag> range <tag> not-advertise

help: Do not advertise this range

.. cfg_cmd:: vrf name <tag> protocols ospfv3 auto-cost

help: Calculate interface cost according to bandwidth

.. cfg_cmd:: vrf name <tag> protocols ospfv3 auto-cost reference-bandwidth

help: Reference bandwidth method to assign cost
100


.. cfg_cmd:: vrf name <tag> protocols ospfv3 default-information

help: Default route advertisment settings

.. cfg_cmd:: vrf name <tag> protocols ospfv3 default-information originate

help: Distribute a default route

.. cfg_cmd:: vrf name <tag> protocols ospfv3 default-information originate always

help: Always advertise a default route

.. cfg_cmd:: vrf name <tag> protocols ospfv3 default-information originate metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 default-information originate metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 default-information originate route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 distance

help: Administrative distance

.. cfg_cmd:: vrf name <tag> protocols ospfv3 distance global

help: Administrative distance

.. cfg_cmd:: vrf name <tag> protocols ospfv3 distance ospfv3

help: OSPFv3 administrative distance

.. cfg_cmd:: vrf name <tag> protocols ospfv3 distance ospfv3 external

help: Distance for external routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 distance ospfv3 inter-area

help: Distance for inter-area routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 distance ospfv3 intra-area

help: Distance for intra-area routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart

help: Graceful Restart

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart grace-period

help: Maximum length of the grace period
120


.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart helper

help: OSPF graceful-restart helpers

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart helper enable

help: Enable helper support

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart helper enable router-id

help: Advertising Router-ID

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart helper lsa-check-disable

help: Disable strict LSA check

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart helper planned-only

help: Supported only planned restart

.. cfg_cmd:: vrf name <tag> protocols ospfv3 graceful-restart helper supported-grace-time

help: Supported grace timer

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag>

help: Enable routing on an IPv6 interface

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> area

help: Enable OSPF on this interface

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> cost

help: Interface cost

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> dead-interval

help: Interval after which a neighbor is declared dead
40


.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> hello-interval

help: Interval between hello packets
10


.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> ifmtu

help: Interface MTU

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> instance-id

help: Instance ID
0


.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> mtu-ignore

help: Disable Maximum Transmission Unit (MTU) mismatch detection

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> network

help: Network type

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> passive

help: Configure passive mode for interface

.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> priority

help: Router priority
1


.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> retransmit-interval

help: Interval between retransmitting lost link state advertisements
5


.. cfg_cmd:: vrf name <tag> protocols ospfv3 interface <tag> transmit-delay

help: Link state transmit delay
1


.. cfg_cmd:: vrf name <tag> protocols ospfv3 log-adjacency-changes

help: Log adjacency state changes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 log-adjacency-changes detail

help: Log all state changes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 parameters

help: OSPFv3 specific parameters

.. cfg_cmd:: vrf name <tag> protocols ospfv3 parameters router-id

help: Override default router identifier

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute babel

help: Redistribute Babel routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute babel metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute babel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute bgp

help: Redistribute BGP routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute bgp metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute bgp metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute bgp route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute connected

help: Redistribute connected routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute connected metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute connected metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute isis

help: Redistribute IS-IS routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute isis metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute isis metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute isis route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute kernel

help: Redistribute kernel routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute kernel metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute kernel metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute ripng

help: Redistribute RIPNG routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute ripng metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute ripng metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute ripng route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute static

help: Redistribute static routes

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute static metric

help: OSPF default metric

.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute static metric-type

help: OSPF metric type for default routes
2


.. cfg_cmd:: vrf name <tag> protocols ospfv3 redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: vrf name <tag> protocols static

help: Static Routing

.. cfg_cmd:: vrf name <tag> protocols static route <tag>

help: Static IPv4 route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> blackhole

help: Silently discard pkts when matched

.. cfg_cmd:: vrf name <tag> protocols static route <tag> blackhole distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> blackhole tag

help: Tag value for this route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> description

help: Description

.. cfg_cmd:: vrf name <tag> protocols static route <tag> dhcp-interface

help: DHCP interface supplying next-hop IP address

.. cfg_cmd:: vrf name <tag> protocols static route <tag> interface <tag>

help: Next-hop IPv4 router interface

.. cfg_cmd:: vrf name <tag> protocols static route <tag> interface <tag> disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols static route <tag> interface <tag> distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> interface <tag> vrf

help: VRF to leak route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag>

help: Next-hop IPv4 router address

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> bfd

help: BFD monitoring

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> bfd multi-hop

help: Use BFD multi hop session

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> bfd multi-hop source <tag>

help: Use source for BFD session

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> bfd multi-hop source <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: vrf name <tag> protocols static route <tag> next-hop <tag> vrf

help: VRF to leak route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> reject

help: Emit an ICMP unreachable when matched

.. cfg_cmd:: vrf name <tag> protocols static route <tag> reject distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route <tag> reject tag

help: Tag value for this route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag>

help: Static IPv6 route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> blackhole

help: Silently discard pkts when matched

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> blackhole distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> blackhole tag

help: Tag value for this route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> description

help: Description

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> interface <tag>

help: IPv6 gateway interface name

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> interface <tag> disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> interface <tag> distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> interface <tag> segments

help: SRv6 segments

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> interface <tag> vrf

help: VRF to leak route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag>

help: IPv6 gateway address

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> bfd

help: BFD monitoring

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> bfd multi-hop

help: Use BFD multi hop session

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> bfd multi-hop source <tag>

help: Use source for BFD session

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> bfd multi-hop source <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> disable

help: Disable instance

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> segments

help: SRv6 segments

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> next-hop <tag> vrf

help: VRF to leak route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> reject

help: Emit an ICMP unreachable when matched

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> reject distance

help: Distance for this route

.. cfg_cmd:: vrf name <tag> protocols static route6 <tag> reject tag

help: Tag value for this route

.. cfg_cmd:: vrf name <tag> table

help: Routing table associated with this instance

.. cfg_cmd:: vrf name <tag> vni

help: Virtual Network Identifier

