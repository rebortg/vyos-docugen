.. cfg_cmd:: interfaces wireless <tag>

help: Wireless (WiFi/WLAN) Network Interface

.. cfg_cmd:: interfaces wireless <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> capabilities

help: HT and VHT capabilities for your card

.. cfg_cmd:: interfaces wireless <tag> capabilities ht

help: HT (High Throughput) settings

.. cfg_cmd:: interfaces wireless <tag> capabilities ht 40mhz-incapable

help: 40MHz intolerance, use 20MHz only!

.. cfg_cmd:: interfaces wireless <tag> capabilities ht auto-powersave

help: Enable WMM-PS unscheduled automatic power aave delivery [U-APSD]

.. cfg_cmd:: interfaces wireless <tag> capabilities ht channel-set-width

help: Supported channel set width

.. cfg_cmd:: interfaces wireless <tag> capabilities ht delayed-block-ack

help: Enable HT-delayed block ack

.. cfg_cmd:: interfaces wireless <tag> capabilities ht dsss-cck-40

help: Enable DSSS_CCK-40

.. cfg_cmd:: interfaces wireless <tag> capabilities ht greenfield

help: Enable HT-greenfield

.. cfg_cmd:: interfaces wireless <tag> capabilities ht ldpc

help: Enable LDPC coding capability

.. cfg_cmd:: interfaces wireless <tag> capabilities ht lsig-protection

help: Enable L-SIG TXOP protection capability

.. cfg_cmd:: interfaces wireless <tag> capabilities ht max-amsdu

help: Set maximum A-MSDU length

.. cfg_cmd:: interfaces wireless <tag> capabilities ht short-gi

help: Short GI capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities ht smps

help: Spatial Multiplexing Power Save (SMPS) settings

.. cfg_cmd:: interfaces wireless <tag> capabilities ht stbc

help: Support for sending and receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities ht stbc rx

help: Enable receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities ht stbc tx

help: Enable sending PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities require-ht

help: Require stations to support HT PHY (reject association if they do not)

.. cfg_cmd:: interfaces wireless <tag> capabilities require-vht

help: Require stations to support VHT PHY (reject association if they do not)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht

help: VHT (Very High Throughput) settings

.. cfg_cmd:: interfaces wireless <tag> capabilities vht antenna-count

help: Number of antennas on this card

.. cfg_cmd:: interfaces wireless <tag> capabilities vht antenna-pattern-fixed

help: Set if antenna pattern does not change during the lifetime of an association

.. cfg_cmd:: interfaces wireless <tag> capabilities vht beamform

help: Beamforming capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities vht center-channel-freq

help: VHT operating channel center frequency

.. cfg_cmd:: interfaces wireless <tag> capabilities vht center-channel-freq freq-1

help: VHT operating channel center frequency - center freq 1 (for use with 80, 80+80 and 160 modes)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht center-channel-freq freq-2

help: VHT operating channel center frequency - center freq 2 (for use with the 80+80 mode)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht channel-set-width

help: VHT operating Channel width

.. cfg_cmd:: interfaces wireless <tag> capabilities vht ldpc

help: Enable LDPC (Low Density Parity Check) coding capability

.. cfg_cmd:: interfaces wireless <tag> capabilities vht link-adaptation

help: VHT link adaptation capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities vht max-mpdu

help: Increase Maximum MPDU length to 7991 or 11454 octets (otherwise: 3895 octets)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht max-mpdu-exp

help: Set the maximum length of A-MPDU pre-EOF padding that the station can receive

.. cfg_cmd:: interfaces wireless <tag> capabilities vht short-gi

help: Short GI capabilities

.. cfg_cmd:: interfaces wireless <tag> capabilities vht stbc

help: Support for sending and receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht stbc rx

help: Enable receiving PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht stbc tx

help: Enable sending PPDU using STBC (Space Time Block Coding)

.. cfg_cmd:: interfaces wireless <tag> capabilities vht tx-powersave

help: Enable VHT TXOP Power Save Mode

.. cfg_cmd:: interfaces wireless <tag> capabilities vht vht-cf

help: Station supports receiving VHT variant HT Control field

.. cfg_cmd:: interfaces wireless <tag> channel

help: Wireless radio channel
0


.. cfg_cmd:: interfaces wireless <tag> country-code

help: Indicate country in which device is operating

.. cfg_cmd:: interfaces wireless <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> disable-broadcast-ssid

help: Disable broadcast of SSID from access-point

.. cfg_cmd:: interfaces wireless <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> expunge-failing-stations

help: Disassociate stations based on excessive transmission failures

.. cfg_cmd:: interfaces wireless <tag> hw-id

help: Associate Ethernet Interface with given Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> isolate-stations

help: Isolate stations on the AP so they cannot see each other

.. cfg_cmd:: interfaces wireless <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> max-stations

help: Maximum number of wireless radio stations. Excess stations will be rejected upon authentication request.

.. cfg_cmd:: interfaces wireless <tag> mgmt-frame-protection

help: Management Frame Protection (MFP) according to IEEE 802.11w
disabled


.. cfg_cmd:: interfaces wireless <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> mode

help: Wireless radio mode
g


.. cfg_cmd:: interfaces wireless <tag> per-client-thread

help: Process traffic from each client in a dedicated thread

.. cfg_cmd:: interfaces wireless <tag> physical-device

help: Wireless physical device
phy0


.. cfg_cmd:: interfaces wireless <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> reduce-transmit-power

help: Transmission power reduction in dBm

.. cfg_cmd:: interfaces wireless <tag> security

help: Wireless security settings

.. cfg_cmd:: interfaces wireless <tag> security station-address

help: Station MAC address based authentication

.. cfg_cmd:: interfaces wireless <tag> security station-address accept

help: Accept station MAC address

.. cfg_cmd:: interfaces wireless <tag> security station-address accept mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> security station-address deny

help: Deny station MAC address

.. cfg_cmd:: interfaces wireless <tag> security station-address deny mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> security station-address mode

help: Select security operation mode
accept


.. cfg_cmd:: interfaces wireless <tag> security wep

help: Wired Equivalent Privacy (WEP) parameters

.. cfg_cmd:: interfaces wireless <tag> security wep key

help: WEP encryption key

.. cfg_cmd:: interfaces wireless <tag> security wpa

help: Wifi Protected Access (WPA) parameters

.. cfg_cmd:: interfaces wireless <tag> security wpa cipher

help: Cipher suite for WPA unicast packets

.. cfg_cmd:: interfaces wireless <tag> security wpa group-cipher

help: Cipher suite for WPA multicast and broadcast packets

.. cfg_cmd:: interfaces wireless <tag> security wpa mode

help: WPA mode
wpa+wpa2


.. cfg_cmd:: interfaces wireless <tag> security wpa passphrase

help: WPA personal shared pass phrase. If you are using special characters in the WPA passphrase then single quotes are required.

.. cfg_cmd:: interfaces wireless <tag> security wpa radius

help: RADIUS based user authentication

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag>

help: No help available

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> accounting

help: Enable RADIUS server to receive accounting info

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> disable

help: Disable instance

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> key

help: Shared secret key

.. cfg_cmd:: interfaces wireless <tag> security wpa radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: interfaces wireless <tag> security wpa radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: interfaces wireless <tag> ssid

help: Wireless access-point service set identifier (SSID)

.. cfg_cmd:: interfaces wireless <tag> type

help: Wireless device type for this interface
monitor


.. cfg_cmd:: interfaces wireless <tag> vif <tag>

help: Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces wireless <tag> vif <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> vif <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> vif <tag> egress-qos

help: VLAN egress QoS

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ingress-qos

help: VLAN ingress QoS

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> vif <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces wireless <tag> vif <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> vif <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag>

help: QinQ TAG-S Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> protocol

help: Protocol used for service VLAN (default: 802.1ad)
802.1ad


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag>

help: QinQ TAG-C Virtual Local Area Network (VLAN) ID

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> address

help: IP address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> description

help: Description

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options

help: DHCP client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options client-id

help: Identifier used by client to identify itself to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options default-route-distance

help: Distance for installed default route
210


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options host-name

help: Override system host-name sent to DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options mtu

help: Use MTU value from DHCP server - ignore interface setting

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options no-default-route

help: Do not install default route to system

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options reject

help: IP addresses or subnets from which to reject DHCP leases

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options user-class

help: Identify to the DHCP server, user configurable option

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcp-options vendor-class-id

help: Identify the vendor client type to the DHCP server

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options

help: DHCPv6 client settings/options

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options no-release

help: Do not send a release message on client exit

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options parameters-only

help: Acquire only config parameters, no address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag>

help: DHCPv6 prefix delegation interface statement

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag>

help: Delegate IPv6 prefix from provider to this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> address

help: Local interface address assigned to interface (default: EUI-64)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> interface <tag> sla-id

help: Interface site-Level aggregator (SLA)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options pd <tag> length

help: Request IPv6 prefix length from peer
64


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options rapid-commit

help: Wait for immediate reply instead of advertisements

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> dhcpv6-options temporary

help: IPv6 temporary address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> disable

help: Administratively disable interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> disable-link-detect

help: Ignore link state changes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip

help: IPv4 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip arp-cache-timeout

help: ARP cache entry timeout in seconds
30


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip disable-arp-filter

help: Disable ARP filter on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-arp-accept

help: Enable ARP accept on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-arp-announce

help: Enable ARP announce on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-arp-ignore

help: Enable ARP ignore on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-directed-broadcast

help: Enable directed broadcast forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip enable-proxy-arp

help: Enable proxy-arp on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip proxy-arp-pvlan

help: Enable private VLAN proxy ARP on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ip source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6

help: IPv6 routing parameters

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 accept-dad

help: Accept Duplicate Address Detection
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address

help: IPv6 address configuration modes

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address autoconf

help: Enable acquisition of IPv6 address using stateless autoconfig (SLAAC)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address eui64

help: Prefix for IPv6 address with MAC-based EUI-64

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 address no-default-link-local

help: Remove the default link-local address from the interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 adjust-mss

help: Adjust TCP MSS value

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 disable-forwarding

help: Disable IP forwarding on this interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 dup-addr-detect-transmits

help: Number of NS messages to send while performing DAD
1


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> ipv6 source-validation

help: Source validation by reversed path (RFC3704)

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mirror

help: Mirror ingress/egress packets

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mirror egress

help: Mirror egress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mirror ingress

help: Mirror ingress traffic to destination interface

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> mtu

help: Maximum Transmission Unit (MTU)
1500


.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> redirect

help: Redirect incoming packet to destination

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vif-c <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag> vif-s <tag> vrf

help: VRF instance name

.. cfg_cmd:: interfaces wireless <tag> vrf

help: VRF instance name

