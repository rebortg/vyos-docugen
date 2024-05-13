.. cfg_cmd:: nat

help: Network Address Translation (NAT) parameters

.. cfg_cmd:: nat destination

help: Destination NAT settings

.. cfg_cmd:: nat destination rule <tag>

help: No help available

.. cfg_cmd:: nat destination rule <tag> description

help: Description

.. cfg_cmd:: nat destination rule <tag> destination

help: NAT destination parameters

.. cfg_cmd:: nat destination rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: nat destination rule <tag> destination group

help: Group

.. cfg_cmd:: nat destination rule <tag> destination group address-group

help: Group of addresses

.. cfg_cmd:: nat destination rule <tag> destination group domain-group

help: Group of domains

.. cfg_cmd:: nat destination rule <tag> destination group mac-group

help: Group of MAC addresses

.. cfg_cmd:: nat destination rule <tag> destination group network-group

help: Group of networks

.. cfg_cmd:: nat destination rule <tag> destination group port-group

help: Group of ports

.. cfg_cmd:: nat destination rule <tag> destination port

help: Port number

.. cfg_cmd:: nat destination rule <tag> disable

help: Disable instance

.. cfg_cmd:: nat destination rule <tag> exclude

help: Exclude packets matching this rule from NAT

.. cfg_cmd:: nat destination rule <tag> inbound-interface

help: Match inbound-interface

.. cfg_cmd:: nat destination rule <tag> inbound-interface group

help: Match interface-group

.. cfg_cmd:: nat destination rule <tag> inbound-interface name

help: Match interface

.. cfg_cmd:: nat destination rule <tag> load-balance

help: Apply NAT load balance

.. cfg_cmd:: nat destination rule <tag> load-balance backend <tag>

help: Translated IP address

.. cfg_cmd:: nat destination rule <tag> load-balance backend <tag> weight

help: Set probability for this output value

.. cfg_cmd:: nat destination rule <tag> load-balance hash

help: Define the parameters of the packet header to apply the hashing
random


.. cfg_cmd:: nat destination rule <tag> log

help: Log packets hitting this rule

.. cfg_cmd:: nat destination rule <tag> packet-type

help: Packet type

.. cfg_cmd:: nat destination rule <tag> protocol

help: Protocol to NAT
all


.. cfg_cmd:: nat destination rule <tag> source

help: NAT source parameters

.. cfg_cmd:: nat destination rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: nat destination rule <tag> source group

help: Group

.. cfg_cmd:: nat destination rule <tag> source group address-group

help: Group of addresses

.. cfg_cmd:: nat destination rule <tag> source group domain-group

help: Group of domains

.. cfg_cmd:: nat destination rule <tag> source group mac-group

help: Group of MAC addresses

.. cfg_cmd:: nat destination rule <tag> source group network-group

help: Group of networks

.. cfg_cmd:: nat destination rule <tag> source group port-group

help: Group of ports

.. cfg_cmd:: nat destination rule <tag> source port

help: Port number

.. cfg_cmd:: nat destination rule <tag> translation

help: Inside NAT IP (destination NAT only)

.. cfg_cmd:: nat destination rule <tag> translation address

help: IP address, subnet, or range

.. cfg_cmd:: nat destination rule <tag> translation options

help: Translation options

.. cfg_cmd:: nat destination rule <tag> translation options address-mapping

help: Address mapping options
random


.. cfg_cmd:: nat destination rule <tag> translation options port-mapping

help: Port mapping options
none


.. cfg_cmd:: nat destination rule <tag> translation port

help: Port number

.. cfg_cmd:: nat destination rule <tag> translation redirect

help: Redirect to local host

.. cfg_cmd:: nat destination rule <tag> translation redirect port

help: Port number

.. cfg_cmd:: nat source

help: Source NAT settings

.. cfg_cmd:: nat source rule <tag>

help: Rule number for NAT

.. cfg_cmd:: nat source rule <tag> description

help: Description

.. cfg_cmd:: nat source rule <tag> destination

help: NAT destination parameters

.. cfg_cmd:: nat source rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: nat source rule <tag> destination group

help: Group

.. cfg_cmd:: nat source rule <tag> destination group address-group

help: Group of addresses

.. cfg_cmd:: nat source rule <tag> destination group domain-group

help: Group of domains

.. cfg_cmd:: nat source rule <tag> destination group mac-group

help: Group of MAC addresses

.. cfg_cmd:: nat source rule <tag> destination group network-group

help: Group of networks

.. cfg_cmd:: nat source rule <tag> destination group port-group

help: Group of ports

.. cfg_cmd:: nat source rule <tag> destination port

help: Port number

.. cfg_cmd:: nat source rule <tag> disable

help: Disable instance

.. cfg_cmd:: nat source rule <tag> exclude

help: Exclude packets matching this rule from NAT

.. cfg_cmd:: nat source rule <tag> load-balance

help: Apply NAT load balance

.. cfg_cmd:: nat source rule <tag> load-balance backend <tag>

help: Translated IP address

.. cfg_cmd:: nat source rule <tag> load-balance backend <tag> weight

help: Set probability for this output value

.. cfg_cmd:: nat source rule <tag> load-balance hash

help: Define the parameters of the packet header to apply the hashing
random


.. cfg_cmd:: nat source rule <tag> log

help: Log packets hitting this rule

.. cfg_cmd:: nat source rule <tag> outbound-interface

help: Match outbound-interface

.. cfg_cmd:: nat source rule <tag> outbound-interface group

help: Match interface-group

.. cfg_cmd:: nat source rule <tag> outbound-interface name

help: Match interface

.. cfg_cmd:: nat source rule <tag> packet-type

help: Packet type

.. cfg_cmd:: nat source rule <tag> protocol

help: Protocol to NAT
all


.. cfg_cmd:: nat source rule <tag> source

help: NAT source parameters

.. cfg_cmd:: nat source rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: nat source rule <tag> source group

help: Group

.. cfg_cmd:: nat source rule <tag> source group address-group

help: Group of addresses

.. cfg_cmd:: nat source rule <tag> source group domain-group

help: Group of domains

.. cfg_cmd:: nat source rule <tag> source group mac-group

help: Group of MAC addresses

.. cfg_cmd:: nat source rule <tag> source group network-group

help: Group of networks

.. cfg_cmd:: nat source rule <tag> source group port-group

help: Group of ports

.. cfg_cmd:: nat source rule <tag> source port

help: Port number

.. cfg_cmd:: nat source rule <tag> translation

help: Outside NAT IP (source NAT only)

.. cfg_cmd:: nat source rule <tag> translation address

help: IP address, subnet, or range

.. cfg_cmd:: nat source rule <tag> translation options

help: Translation options

.. cfg_cmd:: nat source rule <tag> translation options address-mapping

help: Address mapping options
random


.. cfg_cmd:: nat source rule <tag> translation options port-mapping

help: Port mapping options
none


.. cfg_cmd:: nat source rule <tag> translation port

help: Port number

.. cfg_cmd:: nat static

help: Static NAT (one-to-one)

.. cfg_cmd:: nat static rule <tag>

help: Rule number for NAT

.. cfg_cmd:: nat static rule <tag> description

help: Description

.. cfg_cmd:: nat static rule <tag> destination

help: NAT destination parameters

.. cfg_cmd:: nat static rule <tag> destination address

help: IP address, prefix

.. cfg_cmd:: nat static rule <tag> inbound-interface

help: Inbound interface of NAT traffic

.. cfg_cmd:: nat static rule <tag> translation

help: Translation address or prefix

.. cfg_cmd:: nat static rule <tag> translation address

help: IP address, prefix

.. cfg_cmd:: nat64

help: Network Address Translation (NAT64) parameters

.. cfg_cmd:: nat64 source

help: IPv6 source to IPv4 destination address translation

.. cfg_cmd:: nat64 source rule <tag>

help: Source NAT64 rule number

.. cfg_cmd:: nat64 source rule <tag> description

help: Description

.. cfg_cmd:: nat64 source rule <tag> disable

help: Disable instance

.. cfg_cmd:: nat64 source rule <tag> match

help: Match

.. cfg_cmd:: nat64 source rule <tag> match mark

help: Match fwmark value

.. cfg_cmd:: nat64 source rule <tag> source

help: IPv6 source prefix options

.. cfg_cmd:: nat64 source rule <tag> source prefix

help: IPv6 prefix to be translated

.. cfg_cmd:: nat64 source rule <tag> translation

help: Translated IPv4 address options

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag>

help: Translation IPv4 pool number

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> address

help: IPv4 address or prefix to translate to

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> description

help: Description

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> disable

help: Disable instance

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> port

help: Port number

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> protocol

help: Apply translation address to a specfic protocol

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> protocol icmp

help: Internet Control Message Protocol

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> protocol tcp

help: Transmission Control Protocol

.. cfg_cmd:: nat64 source rule <tag> translation pool <tag> protocol udp

help: User Datagram Protocol

.. cfg_cmd:: nat66

help: Network Prefix Translation (NAT66/NPTv6) parameters

.. cfg_cmd:: nat66 destination

help: Prefix mapping for IPv6 destination address translation

.. cfg_cmd:: nat66 destination rule <tag>

help: Destination NAT66 rule number

.. cfg_cmd:: nat66 destination rule <tag> description

help: Description

.. cfg_cmd:: nat66 destination rule <tag> destination

help: IPv6 destination prefix options

.. cfg_cmd:: nat66 destination rule <tag> destination address

help: IPv6 address or prefix to be translated

.. cfg_cmd:: nat66 destination rule <tag> destination port

help: Port number

.. cfg_cmd:: nat66 destination rule <tag> disable

help: Disable instance

.. cfg_cmd:: nat66 destination rule <tag> exclude

help: Exclude packets matching this rule from NAT

.. cfg_cmd:: nat66 destination rule <tag> inbound-interface

help: Match inbound-interface

.. cfg_cmd:: nat66 destination rule <tag> inbound-interface name

help: Match interface

.. cfg_cmd:: nat66 destination rule <tag> log

help: NAT66 rule logging

.. cfg_cmd:: nat66 destination rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")

.. cfg_cmd:: nat66 destination rule <tag> source

help: IPv6 source prefix options

.. cfg_cmd:: nat66 destination rule <tag> source address

help: IPv6 address or prefix to be translated

.. cfg_cmd:: nat66 destination rule <tag> source port

help: Port number

.. cfg_cmd:: nat66 destination rule <tag> translation

help: Translated IPv6 address options

.. cfg_cmd:: nat66 destination rule <tag> translation address

help: IPv6 address or prefix to translate to

.. cfg_cmd:: nat66 destination rule <tag> translation port

help: Port number

.. cfg_cmd:: nat66 source

help: Prefix mapping of IPv6 source address translation

.. cfg_cmd:: nat66 source rule <tag>

help: Source NAT66 rule number

.. cfg_cmd:: nat66 source rule <tag> description

help: Description

.. cfg_cmd:: nat66 source rule <tag> destination

help: IPv6 destination prefix options

.. cfg_cmd:: nat66 source rule <tag> destination port

help: Port number

.. cfg_cmd:: nat66 source rule <tag> destination prefix

help: IPv6 prefix to be translated

.. cfg_cmd:: nat66 source rule <tag> disable

help: Disable instance

.. cfg_cmd:: nat66 source rule <tag> exclude

help: Exclude packets matching this rule from NAT

.. cfg_cmd:: nat66 source rule <tag> log

help: Log packets hitting this rule

.. cfg_cmd:: nat66 source rule <tag> outbound-interface

help: Match outbound-interface

.. cfg_cmd:: nat66 source rule <tag> outbound-interface name

help: Match interface

.. cfg_cmd:: nat66 source rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")

.. cfg_cmd:: nat66 source rule <tag> source

help: IPv6 source prefix options

.. cfg_cmd:: nat66 source rule <tag> source port

help: Port number

.. cfg_cmd:: nat66 source rule <tag> source prefix

help: IPv6 prefix to be translated

.. cfg_cmd:: nat66 source rule <tag> translation

help: Translated IPv6 address options

.. cfg_cmd:: nat66 source rule <tag> translation address

help: IPv6 address to translate to

.. cfg_cmd:: nat66 source rule <tag> translation port

help: Port number

