.. cfg_cmd:: interfaces tunnel <tag>

help: Tunnel interface

.. cfg_cmd:: interfaces tunnel <tag> 6rd-prefix

help: 6rd network prefix

.. cfg_cmd:: interfaces tunnel <tag> 6rd-relay-prefix

help: 6rd relay prefix

.. cfg_cmd:: interfaces tunnel <tag> address

help: IP address

.. cfg_cmd:: interfaces tunnel <tag> description

help: Description

.. cfg_cmd:: interfaces tunnel <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces tunnel <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces tunnel <tag> enable-multicast

help: Enable multicast operation over tunnel

.. cfg_cmd:: interfaces tunnel <tag> encapsulation

help: Encapsulation of this tunnel interface

.. cfg_cmd:: interfaces tunnel <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces tunnel <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces tunnel <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces tunnel <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces tunnel <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces tunnel <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces tunnel <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces tunnel <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces tunnel <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces tunnel <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces tunnel <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces tunnel <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces tunnel <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces tunnel <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces tunnel <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces tunnel <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces tunnel <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces tunnel <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces tunnel <tag> mtu

help: Maximum Transmission Unit (MTU)
1476


.. cfg_cmd:: interfaces tunnel <tag> parameters

help: Tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan

help: ERSPAN tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan direction

help: Mirrored traffic direction

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan hw-id

help: Unique identifier of an ERSPAN engine within a system

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan index

help: ERSPAN version 1 index field

.. cfg_cmd:: interfaces tunnel <tag> parameters erspan version

help: Protocol version
1


.. cfg_cmd:: interfaces tunnel <tag> parameters ip

help: IPv4-specific tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters ip ignore-df

help: Ignore the DF (don't fragment) bit

.. cfg_cmd:: interfaces tunnel <tag> parameters ip key

help: Tunnel key (only GRE tunnels)

.. cfg_cmd:: interfaces tunnel <tag> parameters ip no-pmtu-discovery

help: Disable path MTU discovery

.. cfg_cmd:: interfaces tunnel <tag> parameters ip tos

help: Specifies TOS value to use in outgoing packets
inherit


.. cfg_cmd:: interfaces tunnel <tag> parameters ip ttl

help: Specifies TTL value to use in outgoing packets
64


.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6

help: IPv6-specific tunnel parameters

.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 encaplimit

help: Set fixed encapsulation limit
4


.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 flowlabel

help: Specifies the flow label to use in outgoing packets

.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 hoplimit

help: Hoplimit
64


.. cfg_cmd:: interfaces tunnel <tag> parameters ipv6 tclass

help: Traffic class (Tclass)
inherit


.. cfg_cmd:: interfaces tunnel <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces tunnel <tag> remote

help: Tunnel remote address

.. cfg_cmd:: interfaces tunnel <tag> source-address

help: Source IP address used to initiate connection

.. cfg_cmd:: interfaces tunnel <tag> source-interface

help: Interface used to establish connection

.. cfg_cmd:: interfaces tunnel <tag> vrf

help: VRF instance name

