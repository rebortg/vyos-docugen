.. cfg_cmd:: interfaces pppoe <tag>

help: Point-to-Point Protocol over Ethernet (PPPoE) Interface

.. cfg_cmd:: interfaces pppoe <tag> access-concentrator

help: Access concentrator name

.. cfg_cmd:: interfaces pppoe <tag> authentication

help: Authentication settings

.. cfg_cmd:: interfaces pppoe <tag> authentication password

help: Password used for authentication

.. cfg_cmd:: interfaces pppoe <tag> authentication username

help: Username used for authentication

.. cfg_cmd:: interfaces pppoe <tag> connect-on-demand

help: Establishment connection automatically when traffic is sent

.. cfg_cmd:: interfaces pppoe <tag> default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces pppoe <tag> description

help: Description

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces pppoe <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces pppoe <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces pppoe <tag> holdoff

help: Delay before re-dial to the access concentrator when PPP session terminated by peer (in seconds)
30


.. cfg_cmd:: interfaces pppoe <tag> host-uniq

help: PPPoE RFC2516 host-uniq tag

.. cfg_cmd:: interfaces pppoe <tag> idle-timeout

help: Delay before disconnecting idle session (in seconds)

.. cfg_cmd:: interfaces pppoe <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces pppoe <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pppoe <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pppoe <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces pppoe <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces pppoe <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces pppoe <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces pppoe <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces pppoe <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces pppoe <tag> local-address

help: IPv4 address of local end of the PPPoE link

.. cfg_cmd:: interfaces pppoe <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces pppoe <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces pppoe <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces pppoe <tag> mru

help: Maximum Receive Unit (MRU) (default: MTU value)

.. cfg_cmd:: interfaces pppoe <tag> mtu

help: Maximum Transmission Unit (MTU)
1492


.. cfg_cmd:: interfaces pppoe <tag> no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces pppoe <tag> no-peer-dns

help: Do not use DNS servers provided by the peer

.. cfg_cmd:: interfaces pppoe <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces pppoe <tag> remote-address

help: IPv4 address of remote end of the PPPoE link

.. cfg_cmd:: interfaces pppoe <tag> service-name

help: Service name, only connect to access concentrators advertising this

.. cfg_cmd:: interfaces pppoe <tag> source-interface

help: Interface used to establish connection

.. cfg_cmd:: interfaces pppoe <tag> vrf

help: VRF instance name

