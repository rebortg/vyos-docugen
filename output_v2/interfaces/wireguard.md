.. cfg_cmd:: interfaces wireguard <tag>

help: WireGuard Interface

.. cfg_cmd:: interfaces wireguard <tag> address

help: IP address

.. cfg_cmd:: interfaces wireguard <tag> description

help: Description

.. cfg_cmd:: interfaces wireguard <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireguard <tag> fwmark

help: A 32-bit fwmark value set on all outgoing packets
0


.. cfg_cmd:: interfaces wireguard <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireguard <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireguard <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireguard <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireguard <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireguard <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireguard <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireguard <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireguard <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireguard <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireguard <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireguard <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireguard <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireguard <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireguard <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireguard <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireguard <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireguard <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireguard <tag> mtu

help: Maximum Transmission Unit (MTU)
1420


.. cfg_cmd:: interfaces wireguard <tag> peer <tag>

help: peer alias

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> address

help: IP address of tunnel endpoint

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> allowed-ips

help: IP addresses allowed to traverse the peer

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> description

help: Description

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> disable

help: Disable instance

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> persistent-keepalive

help: Interval to send keepalive messages

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> port

help: Port number used by connection

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> preshared-key

help: base64 encoded preshared key

.. cfg_cmd:: interfaces wireguard <tag> peer <tag> public-key

help: base64 encoded public key

.. cfg_cmd:: interfaces wireguard <tag> per-client-thread

help: Process traffic from each client in a dedicated thread

.. cfg_cmd:: interfaces wireguard <tag> port

help: Port number used by connection

.. cfg_cmd:: interfaces wireguard <tag> private-key

help: Base64 encoded private key

.. cfg_cmd:: interfaces wireguard <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireguard <tag> vrf

help: VRF instance name

