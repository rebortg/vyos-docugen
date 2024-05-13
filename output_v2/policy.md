.. cfg_cmd:: policy

help: Routing policy

.. cfg_cmd:: policy access-list <tag>

help: IP access-list filter

.. cfg_cmd:: policy access-list <tag> description

help: Description

.. cfg_cmd:: policy access-list <tag> rule <tag>

help: Rule for this access-list

.. cfg_cmd:: policy access-list <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy access-list <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy access-list <tag> rule <tag> destination

help: Destination network or address

.. cfg_cmd:: policy access-list <tag> rule <tag> destination any

help: Any IP address to match

.. cfg_cmd:: policy access-list <tag> rule <tag> destination host

help: Single host IP address to match

.. cfg_cmd:: policy access-list <tag> rule <tag> destination inverse-mask

help: Network/netmask to match (requires network be defined)

.. cfg_cmd:: policy access-list <tag> rule <tag> destination network

help: Network/netmask to match (requires inverse-mask be defined)

.. cfg_cmd:: policy access-list <tag> rule <tag> source

help: Source network or address to match

.. cfg_cmd:: policy access-list <tag> rule <tag> source any

help: Any IP address to match

.. cfg_cmd:: policy access-list <tag> rule <tag> source host

help: Single host IP address to match

.. cfg_cmd:: policy access-list <tag> rule <tag> source inverse-mask

help: Network/netmask to match (requires network be defined)

.. cfg_cmd:: policy access-list <tag> rule <tag> source network

help: Network/netmask to match (requires inverse-mask be defined)

.. cfg_cmd:: policy access-list6 <tag>

help: IPv6 access-list filter

.. cfg_cmd:: policy access-list6 <tag> description

help: Description

.. cfg_cmd:: policy access-list6 <tag> rule <tag>

help: Rule for this access-list6

.. cfg_cmd:: policy access-list6 <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy access-list6 <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy access-list6 <tag> rule <tag> source

help: Source IPv6 network to match

.. cfg_cmd:: policy access-list6 <tag> rule <tag> source any

help: Any IP address to match

.. cfg_cmd:: policy access-list6 <tag> rule <tag> source exact-match

help: Exact match of the network prefixes

.. cfg_cmd:: policy access-list6 <tag> rule <tag> source network

help: Network/netmask to match

.. cfg_cmd:: policy as-path-list <tag>

help: Add a BGP autonomous system path filter

.. cfg_cmd:: policy as-path-list <tag> description

help: Description

.. cfg_cmd:: policy as-path-list <tag> rule <tag>

help: Rule for this as-path-list

.. cfg_cmd:: policy as-path-list <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy as-path-list <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy as-path-list <tag> rule <tag> regex

help: Regular expression to match against an AS path

.. cfg_cmd:: policy community-list <tag>

help: Add a BGP community list entry

.. cfg_cmd:: policy community-list <tag> description

help: Description

.. cfg_cmd:: policy community-list <tag> rule <tag>

help: Rule for this BGP community list

.. cfg_cmd:: policy community-list <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy community-list <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy community-list <tag> rule <tag> regex

help: Regular expression to match against a community-list

.. cfg_cmd:: policy extcommunity-list <tag>

help: Add a BGP extended community list entry

.. cfg_cmd:: policy extcommunity-list <tag> description

help: Description

.. cfg_cmd:: policy extcommunity-list <tag> rule <tag>

help: Rule for this BGP extended community list

.. cfg_cmd:: policy extcommunity-list <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy extcommunity-list <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy extcommunity-list <tag> rule <tag> regex

help: Regular expression to match against an extended community list

.. cfg_cmd:: policy large-community-list <tag>

help: Add a BGP large community list entry

.. cfg_cmd:: policy large-community-list <tag> description

help: Description

.. cfg_cmd:: policy large-community-list <tag> rule <tag>

help: Rule for this BGP extended community list

.. cfg_cmd:: policy large-community-list <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy large-community-list <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy large-community-list <tag> rule <tag> regex

help: Regular expression to match against a large community list

.. cfg_cmd:: policy local-route

help: IPv4 policy route of local traffic

.. cfg_cmd:: policy local-route rule <tag>

help: Policy local-route rule set number

.. cfg_cmd:: policy local-route rule <tag> destination

help: Destination parameters

.. cfg_cmd:: policy local-route rule <tag> destination address

help: IPv4 address or prefix

.. cfg_cmd:: policy local-route rule <tag> destination port

help: Port number used by connection

.. cfg_cmd:: policy local-route rule <tag> fwmark

help: Match fwmark value

.. cfg_cmd:: policy local-route rule <tag> inbound-interface

help: Inbound Interface

.. cfg_cmd:: policy local-route rule <tag> protocol

help: Protocol to match (protocol name or number)

.. cfg_cmd:: policy local-route rule <tag> set

help: Packet modifications

.. cfg_cmd:: policy local-route rule <tag> set table

help: Routing table to forward packet with

.. cfg_cmd:: policy local-route rule <tag> source

help: Source parameters

.. cfg_cmd:: policy local-route rule <tag> source address

help: IPv4 address or prefix

.. cfg_cmd:: policy local-route rule <tag> source port

help: Port number used by connection

.. cfg_cmd:: policy local-route6

help: IPv6 policy route of local traffic

.. cfg_cmd:: policy local-route6 rule <tag>

help: IPv6 policy local-route rule set number

.. cfg_cmd:: policy local-route6 rule <tag> destination

help: Destination parameters

.. cfg_cmd:: policy local-route6 rule <tag> destination address

help: IPv6 address or prefix

.. cfg_cmd:: policy local-route6 rule <tag> destination port

help: Port number used by connection

.. cfg_cmd:: policy local-route6 rule <tag> fwmark

help: Match fwmark value

.. cfg_cmd:: policy local-route6 rule <tag> inbound-interface

help: Inbound Interface

.. cfg_cmd:: policy local-route6 rule <tag> protocol

help: Protocol to match (protocol name or number)

.. cfg_cmd:: policy local-route6 rule <tag> set

help: Packet modifications

.. cfg_cmd:: policy local-route6 rule <tag> set table

help: Routing table to forward packet with

.. cfg_cmd:: policy local-route6 rule <tag> source

help: Source parameters

.. cfg_cmd:: policy local-route6 rule <tag> source address

help: IPv6 address or prefix

.. cfg_cmd:: policy local-route6 rule <tag> source port

help: Port number used by connection

.. cfg_cmd:: policy prefix-list <tag>

help: IP prefix-list filter

.. cfg_cmd:: policy prefix-list <tag> description

help: Description

.. cfg_cmd:: policy prefix-list <tag> rule <tag>

help: Rule for this prefix-list

.. cfg_cmd:: policy prefix-list <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy prefix-list <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy prefix-list <tag> rule <tag> ge

help: Prefix length to match a netmask greater than or equal to it

.. cfg_cmd:: policy prefix-list <tag> rule <tag> le

help: Prefix length to match a netmask less than or equal to it

.. cfg_cmd:: policy prefix-list <tag> rule <tag> prefix

help: Prefix to match

.. cfg_cmd:: policy prefix-list6 <tag>

help: IPv6 prefix-list filter

.. cfg_cmd:: policy prefix-list6 <tag> description

help: Description

.. cfg_cmd:: policy prefix-list6 <tag> rule <tag>

help: Rule for this prefix-list6

.. cfg_cmd:: policy prefix-list6 <tag> rule <tag> action

help: Action to take on entries matching this rule

.. cfg_cmd:: policy prefix-list6 <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy prefix-list6 <tag> rule <tag> ge

help: Prefix length to match a netmask greater than or equal to it

.. cfg_cmd:: policy prefix-list6 <tag> rule <tag> le

help: Prefix length to match a netmask less than or equal to it

.. cfg_cmd:: policy prefix-list6 <tag> rule <tag> prefix

help: Prefix to match

.. cfg_cmd:: policy route <tag>

help: Policy route rule set name for IPv4

.. cfg_cmd:: policy route <tag> default-log

help: Log packets hitting default-action

.. cfg_cmd:: policy route <tag> description

help: Description

.. cfg_cmd:: policy route <tag> interface

help: Interface to use

.. cfg_cmd:: policy route <tag> rule <tag>

help: Policy rule number

.. cfg_cmd:: policy route <tag> rule <tag> action

help: Rule action

.. cfg_cmd:: policy route <tag> rule <tag> connection-mark

help: Connection mark

.. cfg_cmd:: policy route <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy route <tag> rule <tag> destination

help: Destination parameters

.. cfg_cmd:: policy route <tag> rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: policy route <tag> rule <tag> destination group

help: Group

.. cfg_cmd:: policy route <tag> rule <tag> destination group address-group

help: Group of addresses

.. cfg_cmd:: policy route <tag> rule <tag> destination group domain-group

help: Group of domains

.. cfg_cmd:: policy route <tag> rule <tag> destination group mac-group

help: Group of MAC addresses

.. cfg_cmd:: policy route <tag> rule <tag> destination group network-group

help: Group of networks

.. cfg_cmd:: policy route <tag> rule <tag> destination group port-group

help: Group of ports

.. cfg_cmd:: policy route <tag> rule <tag> destination port

help: Port

.. cfg_cmd:: policy route <tag> rule <tag> disable

help: Disable instance

.. cfg_cmd:: policy route <tag> rule <tag> dscp

help: DSCP value

.. cfg_cmd:: policy route <tag> rule <tag> dscp-exclude

help: DSCP value not to match

.. cfg_cmd:: policy route <tag> rule <tag> fragment

help: IP fragment match

.. cfg_cmd:: policy route <tag> rule <tag> fragment match-frag

help: Second and further fragments of fragmented packets

.. cfg_cmd:: policy route <tag> rule <tag> fragment match-non-frag

help: Head fragments or unfragmented packets

.. cfg_cmd:: policy route <tag> rule <tag> icmp

help: ICMP type and code information

.. cfg_cmd:: policy route <tag> rule <tag> icmp code

help: ICMP code (0-255)

.. cfg_cmd:: policy route <tag> rule <tag> icmp type

help: ICMP type (0-255)

.. cfg_cmd:: policy route <tag> rule <tag> icmp type-name

help: ICMP type-name

.. cfg_cmd:: policy route <tag> rule <tag> ipsec

help: Inbound IPsec packets

.. cfg_cmd:: policy route <tag> rule <tag> ipsec match-ipsec

help: Inbound IPsec packets

.. cfg_cmd:: policy route <tag> rule <tag> ipsec match-none

help: Inbound non-IPsec packets

.. cfg_cmd:: policy route <tag> rule <tag> limit

help: Rate limit using a token bucket filter

.. cfg_cmd:: policy route <tag> rule <tag> limit burst

help: Maximum number of packets to allow in excess of rate

.. cfg_cmd:: policy route <tag> rule <tag> limit rate

help: Maximum average matching rate

.. cfg_cmd:: policy route <tag> rule <tag> log

help: Log packets hitting this rule

.. cfg_cmd:: policy route <tag> rule <tag> mark

help: Firewall mark

.. cfg_cmd:: policy route <tag> rule <tag> packet-length

help: Payload size in bytes, including header and data to match

.. cfg_cmd:: policy route <tag> rule <tag> packet-length-exclude

help: Payload size in bytes, including header and data not to match

.. cfg_cmd:: policy route <tag> rule <tag> packet-type

help: Packet type

.. cfg_cmd:: policy route <tag> rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")
all


.. cfg_cmd:: policy route <tag> rule <tag> recent

help: Parameters for matching recently seen sources

.. cfg_cmd:: policy route <tag> rule <tag> recent count

help: Source addresses seen more than N times

.. cfg_cmd:: policy route <tag> rule <tag> recent time

help: Source addresses seen in the last N seconds

.. cfg_cmd:: policy route <tag> rule <tag> set

help: Packet modifications

.. cfg_cmd:: policy route <tag> rule <tag> set connection-mark

help: Connection marking

.. cfg_cmd:: policy route <tag> rule <tag> set dscp

help: Packet Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: policy route <tag> rule <tag> set mark

help: Packet marking

.. cfg_cmd:: policy route <tag> rule <tag> set table

help: Routing table to forward packet with

.. cfg_cmd:: policy route <tag> rule <tag> set tcp-mss

help: TCP Maximum Segment Size

.. cfg_cmd:: policy route <tag> rule <tag> source

help: Source parameters

.. cfg_cmd:: policy route <tag> rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: policy route <tag> rule <tag> source group

help: Group

.. cfg_cmd:: policy route <tag> rule <tag> source group address-group

help: Group of addresses

.. cfg_cmd:: policy route <tag> rule <tag> source group domain-group

help: Group of domains

.. cfg_cmd:: policy route <tag> rule <tag> source group mac-group

help: Group of MAC addresses

.. cfg_cmd:: policy route <tag> rule <tag> source group network-group

help: Group of networks

.. cfg_cmd:: policy route <tag> rule <tag> source group port-group

help: Group of ports

.. cfg_cmd:: policy route <tag> rule <tag> source mac-address

help: MAC address

.. cfg_cmd:: policy route <tag> rule <tag> source port

help: Port

.. cfg_cmd:: policy route <tag> rule <tag> state

help: Session state

.. cfg_cmd:: policy route <tag> rule <tag> tcp

help: TCP options to match

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags

help: TCP flags to match

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags ack

help: Acknowledge flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags cwr

help: Congestion Window Reduced flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags ecn

help: Explicit Congestion Notification flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags fin

help: Finish flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not

help: Match flags not set

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not ack

help: Acknowledge flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not cwr

help: Congestion Window Reduced flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not ecn

help: Explicit Congestion Notification flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not fin

help: Finish flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not psh

help: Push flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not rst

help: Reset flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not syn

help: Synchronise flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags not urg

help: Urgent flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags psh

help: Push flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags rst

help: Reset flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags syn

help: Synchronise flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp flags urg

help: Urgent flag

.. cfg_cmd:: policy route <tag> rule <tag> tcp mss

help: Maximum segment size (MSS)

.. cfg_cmd:: policy route <tag> rule <tag> time

help: Time to match rule

.. cfg_cmd:: policy route <tag> rule <tag> time monthdays

help: Monthdays to match rule on

.. cfg_cmd:: policy route <tag> rule <tag> time startdate

help: Date to start matching rule

.. cfg_cmd:: policy route <tag> rule <tag> time starttime

help: Time of day to start matching rule

.. cfg_cmd:: policy route <tag> rule <tag> time stopdate

help: Date to stop matching rule

.. cfg_cmd:: policy route <tag> rule <tag> time stoptime

help: Time of day to stop matching rule

.. cfg_cmd:: policy route <tag> rule <tag> time utc

help: Interpret times for startdate, stopdate, starttime and stoptime to be UTC

.. cfg_cmd:: policy route <tag> rule <tag> time weekdays

help: Weekdays to match rule on

.. cfg_cmd:: policy route <tag> rule <tag> ttl

help: Time to live limit

.. cfg_cmd:: policy route <tag> rule <tag> ttl eq

help: Match on equal value

.. cfg_cmd:: policy route <tag> rule <tag> ttl gt

help: Match on greater then value

.. cfg_cmd:: policy route <tag> rule <tag> ttl lt

help: Match on less then value

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

.. cfg_cmd:: policy route6 <tag>

help: Policy route rule set name for IPv6

.. cfg_cmd:: policy route6 <tag> default-log

help: Log packets hitting default-action

.. cfg_cmd:: policy route6 <tag> description

help: Description

.. cfg_cmd:: policy route6 <tag> interface

help: Interface to use

.. cfg_cmd:: policy route6 <tag> rule <tag>

help: Policy rule number

.. cfg_cmd:: policy route6 <tag> rule <tag> action

help: Rule action

.. cfg_cmd:: policy route6 <tag> rule <tag> connection-mark

help: Connection mark

.. cfg_cmd:: policy route6 <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy route6 <tag> rule <tag> destination

help: Destination parameters

.. cfg_cmd:: policy route6 <tag> rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group

help: Group

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group address-group

help: Group of addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group domain-group

help: Group of domains

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group mac-group

help: Group of MAC addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group network-group

help: Group of networks

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group port-group

help: Group of ports

.. cfg_cmd:: policy route6 <tag> rule <tag> destination port

help: Port

.. cfg_cmd:: policy route6 <tag> rule <tag> disable

help: Disable instance

.. cfg_cmd:: policy route6 <tag> rule <tag> dscp

help: DSCP value

.. cfg_cmd:: policy route6 <tag> rule <tag> dscp-exclude

help: DSCP value not to match

.. cfg_cmd:: policy route6 <tag> rule <tag> fragment

help: IP fragment match

.. cfg_cmd:: policy route6 <tag> rule <tag> fragment match-frag

help: Second and further fragments of fragmented packets

.. cfg_cmd:: policy route6 <tag> rule <tag> fragment match-non-frag

help: Head fragments or unfragmented packets

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit

help: Hop limit

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit eq

help: Match on equal value

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit gt

help: Match on greater then value

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit lt

help: Match on less then value

.. cfg_cmd:: policy route6 <tag> rule <tag> icmpv6

help: ICMPv6 type and code information

.. cfg_cmd:: policy route6 <tag> rule <tag> icmpv6 type

help: ICMP type-name

.. cfg_cmd:: policy route6 <tag> rule <tag> ipsec

help: Inbound IPsec packets

.. cfg_cmd:: policy route6 <tag> rule <tag> ipsec match-ipsec

help: Inbound IPsec packets

.. cfg_cmd:: policy route6 <tag> rule <tag> ipsec match-none

help: Inbound non-IPsec packets

.. cfg_cmd:: policy route6 <tag> rule <tag> limit

help: Rate limit using a token bucket filter

.. cfg_cmd:: policy route6 <tag> rule <tag> limit burst

help: Maximum number of packets to allow in excess of rate

.. cfg_cmd:: policy route6 <tag> rule <tag> limit rate

help: Maximum average matching rate

.. cfg_cmd:: policy route6 <tag> rule <tag> log

help: Log packets hitting this rule

.. cfg_cmd:: policy route6 <tag> rule <tag> mark

help: Firewall mark

.. cfg_cmd:: policy route6 <tag> rule <tag> packet-length

help: Payload size in bytes, including header and data to match

.. cfg_cmd:: policy route6 <tag> rule <tag> packet-length-exclude

help: Payload size in bytes, including header and data not to match

.. cfg_cmd:: policy route6 <tag> rule <tag> packet-type

help: Packet type

.. cfg_cmd:: policy route6 <tag> rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")
all


.. cfg_cmd:: policy route6 <tag> rule <tag> recent

help: Parameters for matching recently seen sources

.. cfg_cmd:: policy route6 <tag> rule <tag> recent count

help: Source addresses seen more than N times

.. cfg_cmd:: policy route6 <tag> rule <tag> recent time

help: Source addresses seen in the last N seconds

.. cfg_cmd:: policy route6 <tag> rule <tag> set

help: Packet modifications

.. cfg_cmd:: policy route6 <tag> rule <tag> set connection-mark

help: Connection marking

.. cfg_cmd:: policy route6 <tag> rule <tag> set dscp

help: Packet Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: policy route6 <tag> rule <tag> set mark

help: Packet marking

.. cfg_cmd:: policy route6 <tag> rule <tag> set table

help: Routing table to forward packet with

.. cfg_cmd:: policy route6 <tag> rule <tag> set tcp-mss

help: TCP Maximum Segment Size

.. cfg_cmd:: policy route6 <tag> rule <tag> source

help: Source parameters

.. cfg_cmd:: policy route6 <tag> rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: policy route6 <tag> rule <tag> source group

help: Group

.. cfg_cmd:: policy route6 <tag> rule <tag> source group address-group

help: Group of addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> source group domain-group

help: Group of domains

.. cfg_cmd:: policy route6 <tag> rule <tag> source group mac-group

help: Group of MAC addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> source group network-group

help: Group of networks

.. cfg_cmd:: policy route6 <tag> rule <tag> source group port-group

help: Group of ports

.. cfg_cmd:: policy route6 <tag> rule <tag> source mac-address

help: MAC address

.. cfg_cmd:: policy route6 <tag> rule <tag> source port

help: Port

.. cfg_cmd:: policy route6 <tag> rule <tag> state

help: Session state

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp

help: TCP options to match

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags

help: TCP flags to match

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags ack

help: Acknowledge flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags cwr

help: Congestion Window Reduced flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags ecn

help: Explicit Congestion Notification flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags fin

help: Finish flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not

help: Match flags not set

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not ack

help: Acknowledge flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not cwr

help: Congestion Window Reduced flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not ecn

help: Explicit Congestion Notification flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not fin

help: Finish flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not psh

help: Push flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not rst

help: Reset flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not syn

help: Synchronise flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not urg

help: Urgent flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags psh

help: Push flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags rst

help: Reset flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags syn

help: Synchronise flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags urg

help: Urgent flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp mss

help: Maximum segment size (MSS)

.. cfg_cmd:: policy route6 <tag> rule <tag> time

help: Time to match rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time monthdays

help: Monthdays to match rule on

.. cfg_cmd:: policy route6 <tag> rule <tag> time startdate

help: Date to start matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time starttime

help: Time of day to start matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time stopdate

help: Date to stop matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time stoptime

help: Time of day to stop matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time utc

help: Interpret times for startdate, stopdate, starttime and stoptime to be UTC

.. cfg_cmd:: policy route6 <tag> rule <tag> time weekdays

help: Weekdays to match rule on

