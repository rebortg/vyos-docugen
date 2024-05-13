.. cfg_cmd:: policy route-map <tag>

help: IP route-map

.. cfg_cmd:: policy route-map <tag> description

help: Description

.. cfg_cmd:: policy route-map <tag> rule <tag>

help: Rule for this route-map

.. cfg_cmd:: policy route-map <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy route-map <tag> rule <tag> call

help: Call another route-map on match

.. cfg_cmd:: policy route-map <tag> rule <tag> continue

help: Jump to a different rule in this route-map on a match

.. cfg_cmd:: policy route-map <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy route-map <tag> rule <tag> match

help: Route parameters to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match as-path

help: BGP as-path-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match community

help: BGP community-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match community community-list

help: BGP community-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match community exact-match

help: Community-list to exactly match

.. cfg_cmd:: policy route-map <tag> rule <tag> match evpn

help: Ethernet Virtual Private Network

.. cfg_cmd:: policy route-map <tag> rule <tag> match evpn default-route

help: Default EVPN type-5 route

.. cfg_cmd:: policy route-map <tag> rule <tag> match evpn rd

help: Route Distinguisher

.. cfg_cmd:: policy route-map <tag> rule <tag> match evpn route-type

help: Match route-type

.. cfg_cmd:: policy route-map <tag> rule <tag> match evpn vni

help: Virtual Network Identifier

.. cfg_cmd:: policy route-map <tag> rule <tag> match extcommunity

help: BGP extended community to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match interface

help: Interface to use

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip

help: IP prefix parameters to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip address

help: IP address of route to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip address access-list

help: IP access-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip address prefix-len

help: IP prefix-length to match (can be used for kernel routes only)

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip address prefix-list

help: IP prefix-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip nexthop

help: IP next-hop of route to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip nexthop access-list

help: IP access-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip nexthop address

help: IP address to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip nexthop prefix-len

help: IP prefix-length to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip nexthop prefix-list

help: IP prefix-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip nexthop type

help: Match type

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip route-source

help: Match advertising source address of route

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip route-source access-list

help: IP access-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ip route-source prefix-list

help: IP prefix-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6

help: IPv6 prefix parameters to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 address

help: IPv6 address of route to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 address access-list

help: IPv6 access-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 address prefix-len

help: IPv6 prefix-length to match (can be used for kernel routes only)

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 address prefix-list

help: IPv6 prefix-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 nexthop

help: IPv6 next-hop of route to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 nexthop access-list

help: IPv6 access-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 nexthop address

help: IPv6 address of next-hop

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 nexthop prefix-list

help: IPv6 prefix-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match ipv6 nexthop type

help: Match type

.. cfg_cmd:: policy route-map <tag> rule <tag> match large-community

help: Match BGP large communities

.. cfg_cmd:: policy route-map <tag> rule <tag> match large-community large-community-list

help: BGP large-community-list to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match local-preference

help: Local Preference

.. cfg_cmd:: policy route-map <tag> rule <tag> match metric

help: Metric of route to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match origin

help: BGP origin code to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match peer

help: Peer address to match

.. cfg_cmd:: policy route-map <tag> rule <tag> match protocol

help: Match protocol via which the route was learnt

.. cfg_cmd:: policy route-map <tag> rule <tag> match rpki

help: Match RPKI validation result

.. cfg_cmd:: policy route-map <tag> rule <tag> match tag

help: Route tag value

.. cfg_cmd:: policy route-map <tag> rule <tag> on-match

help: Exit policy on matches

.. cfg_cmd:: policy route-map <tag> rule <tag> on-match goto

help: Rule number to goto on match

.. cfg_cmd:: policy route-map <tag> rule <tag> on-match next

help: Next sequence number to goto on match

.. cfg_cmd:: policy route-map <tag> rule <tag> set

help: Route parameters

.. cfg_cmd:: policy route-map <tag> rule <tag> set aggregator

help: BGP aggregator attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set aggregator as

help: AS number of an aggregation

.. cfg_cmd:: policy route-map <tag> rule <tag> set aggregator ip

help: IP address of an aggregation

.. cfg_cmd:: policy route-map <tag> rule <tag> set as-path

help: Transform BGP AS_PATH attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set as-path exclude

help: Remove/exclude from the as-path attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set as-path prepend

help: Prepend to the as-path

.. cfg_cmd:: policy route-map <tag> rule <tag> set as-path prepend-last-as

help: Use the last AS-number in the as-path

.. cfg_cmd:: policy route-map <tag> rule <tag> set atomic-aggregate

help: BGP atomic aggregate attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set community

help: BGP community attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set community add

help: Add communities to a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set community delete

help: Remove communities defined in a list from a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set community none

help: Completely remove communities attribute from a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set community replace

help: Set communities for a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set distance

help: Locally significant administrative distance

.. cfg_cmd:: policy route-map <tag> rule <tag> set evpn

help: Ethernet Virtual Private Network

.. cfg_cmd:: policy route-map <tag> rule <tag> set evpn gateway

help: Set gateway IP for prefix advertisement route

.. cfg_cmd:: policy route-map <tag> rule <tag> set evpn gateway ipv4

help: Set gateway IPv4 address

.. cfg_cmd:: policy route-map <tag> rule <tag> set evpn gateway ipv6

help: Set gateway IPv6 address

.. cfg_cmd:: policy route-map <tag> rule <tag> set extcommunity

help: BGP extended community attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set extcommunity bandwidth

help: Bandwidth value in Mbps

.. cfg_cmd:: policy route-map <tag> rule <tag> set extcommunity bandwidth-non-transitive

help: The link bandwidth extended community is encoded as non-transitive

.. cfg_cmd:: policy route-map <tag> rule <tag> set extcommunity none

help: Completely remove communities attribute from a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set extcommunity rt

help: Set route target value

.. cfg_cmd:: policy route-map <tag> rule <tag> set extcommunity soo

help: Set Site of Origin value

.. cfg_cmd:: policy route-map <tag> rule <tag> set ip-next-hop

help: Nexthop IP address

.. cfg_cmd:: policy route-map <tag> rule <tag> set ipv6-next-hop

help: Nexthop IPv6 address

.. cfg_cmd:: policy route-map <tag> rule <tag> set ipv6-next-hop global

help: Nexthop IPv6 global address

.. cfg_cmd:: policy route-map <tag> rule <tag> set ipv6-next-hop local

help: Nexthop IPv6 local address

.. cfg_cmd:: policy route-map <tag> rule <tag> set ipv6-next-hop peer-address

help: Use peer address (for BGP only)

.. cfg_cmd:: policy route-map <tag> rule <tag> set ipv6-next-hop prefer-global

help: Prefer global address as the nexthop

.. cfg_cmd:: policy route-map <tag> rule <tag> set l3vpn-nexthop

help: Next hop Information

.. cfg_cmd:: policy route-map <tag> rule <tag> set l3vpn-nexthop encapsulation

help: Encapsulation options (for BGP only)

.. cfg_cmd:: policy route-map <tag> rule <tag> set l3vpn-nexthop encapsulation gre

help: Accept L3VPN traffic over GRE encapsulation

.. cfg_cmd:: policy route-map <tag> rule <tag> set large-community

help: BGP large community attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set large-community add

help: Add large communities to a prefix ;

.. cfg_cmd:: policy route-map <tag> rule <tag> set large-community delete

help: Remove communities defined in a list from a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set large-community none

help: Completely remove communities attribute from a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set large-community replace

help: Set large communities for a prefix

.. cfg_cmd:: policy route-map <tag> rule <tag> set local-preference

help: BGP local preference attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set metric

help: Destination routing protocol metric

.. cfg_cmd:: policy route-map <tag> rule <tag> set metric-type

help: Open Shortest Path First (OSPF) external metric-type

.. cfg_cmd:: policy route-map <tag> rule <tag> set origin

help: Border Gateway Protocl (BGP) origin code

.. cfg_cmd:: policy route-map <tag> rule <tag> set originator-id

help: BGP originator ID attribute

.. cfg_cmd:: policy route-map <tag> rule <tag> set src

help: Source address for route

.. cfg_cmd:: policy route-map <tag> rule <tag> set table

help: Set prefixes to table

.. cfg_cmd:: policy route-map <tag> rule <tag> set tag

help: Route tag value

.. cfg_cmd:: policy route-map <tag> rule <tag> set weight

help: BGP weight attribute

