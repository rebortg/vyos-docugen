.. cfg_cmd:: service

help: System services

.. cfg_cmd:: service aws

help: Amazon Web Service

.. cfg_cmd:: service aws glb

help: Gateway load-balancer tunnel handler

.. cfg_cmd:: service aws glb script

help: Script executed on create or destroy tunnel

.. cfg_cmd:: service aws glb script on-create

help: Script to run when interface is created

.. cfg_cmd:: service aws glb script on-destroy

help: Script to run when interface is destroyed

.. cfg_cmd:: service aws glb status

help: Status

.. cfg_cmd:: service aws glb status format

help: Statistic format

.. cfg_cmd:: service aws glb status port

help: Port number used by connection

.. cfg_cmd:: service aws glb threads

help: Threads settings

.. cfg_cmd:: service aws glb threads tunnel

help: Number of threads for each tunnel processor

.. cfg_cmd:: service aws glb threads tunnel-affinity

help: List of cores worker threads

.. cfg_cmd:: service aws glb threads udp

help: Number of threads for UDP receiver

.. cfg_cmd:: service aws glb threads udp-affinity

help: List of cores worker threads

.. cfg_cmd:: service broadcast-relay

help: UDP broadcast relay service

.. cfg_cmd:: service broadcast-relay disable

help: Disable instance

.. cfg_cmd:: service broadcast-relay id <tag>

help: Unique ID for each UDP port to forward

.. cfg_cmd:: service broadcast-relay id <tag> address

help: Set source IP of forwarded packets, otherwise original senders address is used

.. cfg_cmd:: service broadcast-relay id <tag> description

help: Description

.. cfg_cmd:: service broadcast-relay id <tag> disable

help: Disable instance

.. cfg_cmd:: service broadcast-relay id <tag> interface

help: Interface to use

.. cfg_cmd:: service broadcast-relay id <tag> port

help: Port number used by connection

.. cfg_cmd:: service config-sync

help: Configuration synchronization

.. cfg_cmd:: service config-sync mode

help: Synchronization mode

.. cfg_cmd:: service config-sync secondary

help: Secondary server parameters

.. cfg_cmd:: service config-sync secondary address

help: IP address

.. cfg_cmd:: service config-sync secondary key

help: HTTP API key

.. cfg_cmd:: service config-sync secondary timeout

help: Connection API timeout
60


.. cfg_cmd:: service config-sync section

help: Section for synchronization

.. cfg_cmd:: service config-sync section firewall

help: Firewall

.. cfg_cmd:: service config-sync section interfaces

help: Interfaces

.. cfg_cmd:: service config-sync section interfaces bonding

help: Bonding interface

.. cfg_cmd:: service config-sync section interfaces bridge

help: Bridge interface

.. cfg_cmd:: service config-sync section interfaces dummy

help: Dummy interface

.. cfg_cmd:: service config-sync section interfaces ethernet

help: Ethernet interface

.. cfg_cmd:: service config-sync section interfaces geneve

help: GENEVE interface

.. cfg_cmd:: service config-sync section interfaces input

help: Input interface

.. cfg_cmd:: service config-sync section interfaces l2tpv3

help: L2TPv3 interface

.. cfg_cmd:: service config-sync section interfaces loopback

help: Loopback interface

.. cfg_cmd:: service config-sync section interfaces macsec

help: MACsec interface

.. cfg_cmd:: service config-sync section interfaces openvpn

help: OpenVPN interface

.. cfg_cmd:: service config-sync section interfaces pppoe

help: PPPoE interface

.. cfg_cmd:: service config-sync section interfaces pseudo-ethernet

help: Pseudo-Ethernet interface

.. cfg_cmd:: service config-sync section interfaces sstpc

help: SSTP client interface

.. cfg_cmd:: service config-sync section interfaces tunnel

help: Tunnel interface

.. cfg_cmd:: service config-sync section interfaces virtual-ethernet

help: Virtual Ethernet interface

.. cfg_cmd:: service config-sync section interfaces vti

help: Virtual tunnel interface

.. cfg_cmd:: service config-sync section interfaces vxlan

help: VXLAN interface

.. cfg_cmd:: service config-sync section interfaces wireguard

help: Wireguard interface

.. cfg_cmd:: service config-sync section interfaces wireless

help: Wireless interface

.. cfg_cmd:: service config-sync section interfaces wwan

help: WWAN interface

.. cfg_cmd:: service config-sync section nat

help: NAT

.. cfg_cmd:: service config-sync section nat66

help: NAT66

.. cfg_cmd:: service config-sync section pki

help: Public key infrastructure (PKI)

.. cfg_cmd:: service config-sync section policy

help: Routing policy

.. cfg_cmd:: service config-sync section protocols

help: Routing protocols

.. cfg_cmd:: service config-sync section protocols babel

help: Babel Routing Protocol

.. cfg_cmd:: service config-sync section protocols bfd

help: Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: service config-sync section protocols bgp

help: Border Gateway Protocol (BGP)

.. cfg_cmd:: service config-sync section protocols failover

help: Failover route

.. cfg_cmd:: service config-sync section protocols igmp-proxy

help: Internet Group Management Protocol (IGMP) proxy

.. cfg_cmd:: service config-sync section protocols isis

help: Intermediate System to Intermediate System (IS-IS)

.. cfg_cmd:: service config-sync section protocols mpls

help: Multiprotocol Label Switching (MPLS)

.. cfg_cmd:: service config-sync section protocols nhrp

help: Next Hop Resolution Protocol (NHRP) parameters

.. cfg_cmd:: service config-sync section protocols ospf

help: Open Shortest Path First (OSPF)

.. cfg_cmd:: service config-sync section protocols ospfv3

help: Open Shortest Path First (OSPF) for IPv6

.. cfg_cmd:: service config-sync section protocols pim

help: Protocol Independent Multicast (PIM) and IGMP

.. cfg_cmd:: service config-sync section protocols pim6

help: Protocol Independent Multicast for IPv6 (PIMv6) and MLD

.. cfg_cmd:: service config-sync section protocols rip

help: Routing Information Protocol (RIP) parameters

.. cfg_cmd:: service config-sync section protocols ripng

help: Routing Information Protocol (RIPng) parameters

.. cfg_cmd:: service config-sync section protocols rpki

help: Resource Public Key Infrastructure (RPKI)

.. cfg_cmd:: service config-sync section protocols segment-routing

help: Segment Routing

.. cfg_cmd:: service config-sync section protocols static

help: Static Routing

.. cfg_cmd:: service config-sync section service

help: System services

.. cfg_cmd:: service config-sync section service console-server

help: Serial Console Server

.. cfg_cmd:: service config-sync section service dhcp-relay

help: Host Configuration Protocol (DHCP) relay agent

.. cfg_cmd:: service config-sync section service dhcp-server

help: Dynamic Host Configuration Protocol (DHCP) for DHCP server

.. cfg_cmd:: service config-sync section service dhcpv6-relay

help: DHCPv6 Relay Agent parameters

.. cfg_cmd:: service config-sync section service dhcpv6-server

help: DHCP for IPv6 (DHCPv6) server

.. cfg_cmd:: service config-sync section service dns

help: Domain Name System (DNS) related services

.. cfg_cmd:: service config-sync section service lldp

help: LLDP settings

.. cfg_cmd:: service config-sync section service mdns

help: Multicast DNS (mDNS) parameters

.. cfg_cmd:: service config-sync section service monitoring

help: Monitoring services

.. cfg_cmd:: service config-sync section service ndp-proxy

help: Neighbor Discovery Protocol (NDP) Proxy

.. cfg_cmd:: service config-sync section service ntp

help: Network Time Protocol (NTP) configuration

.. cfg_cmd:: service config-sync section service snmp

help: Simple Network Management Protocol (SNMP)

.. cfg_cmd:: service config-sync section service tftp-server

help: Trivial File Transfer Protocol (TFTP) server

.. cfg_cmd:: service config-sync section service webproxy

help: Webproxy service settings

.. cfg_cmd:: service config-sync section vpn

help: Virtual Private Network (VPN)

.. cfg_cmd:: service config-sync section vrf

help: Virtual Routing and Forwarding

.. cfg_cmd:: service conntrack-sync

help: Connection tracking synchronization

.. cfg_cmd:: service conntrack-sync accept-protocol

help: Protocols for which local conntrack entries will be synced

.. cfg_cmd:: service conntrack-sync disable-external-cache

help: Directly injects the flow-states into the in-kernel Connection Tracking System of the backup firewall.

.. cfg_cmd:: service conntrack-sync disable-syslog

help: Disable connection logging via Syslog

.. cfg_cmd:: service conntrack-sync event-listen-queue-size

help: Queue size for local conntrack events
8


.. cfg_cmd:: service conntrack-sync expect-sync

help: Protocol for which expect entries need to be synchronized

.. cfg_cmd:: service conntrack-sync failover-mechanism

help: Failover mechanism to use for conntrack-sync

.. cfg_cmd:: service conntrack-sync failover-mechanism vrrp

help: VRRP as failover-mechanism to use for conntrack-sync

.. cfg_cmd:: service conntrack-sync failover-mechanism vrrp sync-group

help: VRRP sync group

.. cfg_cmd:: service conntrack-sync ignore-address

help: IP addresses for which local conntrack entries will not be synced

.. cfg_cmd:: service conntrack-sync interface <tag>

help: Interface to use for syncing conntrack entries

.. cfg_cmd:: service conntrack-sync interface <tag> peer

help: IP address of the peer to send the UDP conntrack info too. This disable multicast.

.. cfg_cmd:: service conntrack-sync interface <tag> port

help: Port number used by connection

.. cfg_cmd:: service conntrack-sync listen-address

help: Local IPv4 addresses to listen on

.. cfg_cmd:: service conntrack-sync mcast-group

help: Multicast group to use for syncing conntrack entries
225.0.0.50


.. cfg_cmd:: service conntrack-sync sync-queue-size

help: Queue size for syncing conntrack entries
1


.. cfg_cmd:: service console-server

help: Serial Console Server

.. cfg_cmd:: service console-server device <tag>

help: System serial interface name (ttyS or ttyUSB)

.. cfg_cmd:: service console-server device <tag> alias

help: Human-readable name for this console

.. cfg_cmd:: service console-server device <tag> data-bits

help: Serial port data bits
8


.. cfg_cmd:: service console-server device <tag> description

help: Description

.. cfg_cmd:: service console-server device <tag> parity

help: Parity setting
none


.. cfg_cmd:: service console-server device <tag> speed

help: Serial port baud rate

.. cfg_cmd:: service console-server device <tag> ssh

help: SSH remote access to this console

.. cfg_cmd:: service console-server device <tag> ssh port

help: Port number used by connection

.. cfg_cmd:: service console-server device <tag> stop-bits

help: Serial port stop bits
1


.. cfg_cmd:: service dhcp-relay

help: Host Configuration Protocol (DHCP) relay agent

.. cfg_cmd:: service dhcp-relay disable

help: Disable instance

.. cfg_cmd:: service dhcp-relay interface

help: Interface to use

.. cfg_cmd:: service dhcp-relay listen-interface

help: Interface for DHCP Relay Agent to listen for requests

.. cfg_cmd:: service dhcp-relay relay-options

help: Relay options

.. cfg_cmd:: service dhcp-relay relay-options hop-count

help: Policy to discard packets that have reached specified hop-count
10


.. cfg_cmd:: service dhcp-relay relay-options max-size

help: Maximum packet size to send to a DHCPv4/BOOTP server
576


.. cfg_cmd:: service dhcp-relay relay-options relay-agents-packets

help: Policy to handle incoming DHCPv4 packets which already contain relay agent options
forward


.. cfg_cmd:: service dhcp-relay server

help: DHCP server address

.. cfg_cmd:: service dhcp-relay upstream-interface

help: Interface for DHCP Relay Agent forward requests out

.. cfg_cmd:: service dhcp-server

help: Dynamic Host Configuration Protocol (DHCP) for DHCP server

.. cfg_cmd:: service dhcp-server disable

help: Disable instance

.. cfg_cmd:: service dhcp-server dynamic-dns-update

help: Dynamically update Domain Name System (RFC4702)

.. cfg_cmd:: service dhcp-server failover

help: DHCP failover configuration

.. cfg_cmd:: service dhcp-server failover ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: service dhcp-server failover certificate

help: Certificate in PKI configuration

.. cfg_cmd:: service dhcp-server failover name

help: Peer name used to identify connection

.. cfg_cmd:: service dhcp-server failover remote

help: IPv4 remote address used for connectio

.. cfg_cmd:: service dhcp-server failover source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: service dhcp-server failover status

help: Failover hierarchy

.. cfg_cmd:: service dhcp-server hostfile-update

help: Updating /etc/hosts file (per client lease)

.. cfg_cmd:: service dhcp-server listen-address

help: Local IPv4 addresses to listen on

.. cfg_cmd:: service dhcp-server listen-interface

help: Interface to listen on

.. cfg_cmd:: service dhcp-server shared-network-name <tag>

help: Name of DHCP shared network

.. cfg_cmd:: service dhcp-server shared-network-name <tag> authoritative

help: Option to make DHCP server authoritative for this physical network

.. cfg_cmd:: service dhcp-server shared-network-name <tag> description

help: Description

.. cfg_cmd:: service dhcp-server shared-network-name <tag> disable

help: Disable instance

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option

help: DHCP option

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option bootfile-name

help: Bootstrap file name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option bootfile-server

help: Server from which the initial boot file is to be loaded

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option bootfile-size

help: Bootstrap file size

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option client-prefix-length

help: Specifies the clients subnet mask as per RFC 950. If unset, subnet declaration is used.

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option default-router

help: IP address of default router

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option domain-name

help: Client Domain Name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option ip-forwarding

help: Enable IP forwarding on client

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option ipv6-only-preferred

help: Disable IPv4 on IPv6 only hosts (RFC 8925)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option ntp-server

help: IP address of NTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option pop-server

help: IP address of POP3 server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option server-identifier

help: Address for DHCP server identifier

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option smtp-server

help: IP address of SMTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option static-route <tag>

help: Classless static route destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option static-route <tag> next-hop

help: IP address of router to be used to reach the destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option tftp-server-name

help: TFTP server name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option time-offset

help: Client subnet offset in seconds from Coordinated Universal Time (UTC)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option time-server

help: IP address of time server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option time-zone

help: Time zone to send to clients. Uses RFC4833 options 100 and 101

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option vendor-option ubiquiti

help: Ubiquiti specific parameters

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option vendor-option ubiquiti unifi-controller

help: Address of UniFi controller

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option wins-server

help: IP address for Windows Internet Name Service (WINS) server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> option wpad-url

help: Web Proxy Autodiscovery (WPAD) URL

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag>

help: DHCP subnet for shared network

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> description

help: Description

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> disable

help: Disable instance

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> exclude

help: IP address to exclude from DHCP lease range

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> ignore-client-id

help: Ignore client identifier for lease lookups

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> lease

help: Lease timeout in seconds
86400


.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option

help: DHCP option

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option bootfile-name

help: Bootstrap file name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option bootfile-server

help: Server from which the initial boot file is to be loaded

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option bootfile-size

help: Bootstrap file size

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option client-prefix-length

help: Specifies the clients subnet mask as per RFC 950. If unset, subnet declaration is used.

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option default-router

help: IP address of default router

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option domain-name

help: Client Domain Name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option ip-forwarding

help: Enable IP forwarding on client

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option ipv6-only-preferred

help: Disable IPv4 on IPv6 only hosts (RFC 8925)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option ntp-server

help: IP address of NTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option pop-server

help: IP address of POP3 server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option server-identifier

help: Address for DHCP server identifier

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option smtp-server

help: IP address of SMTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option static-route <tag>

help: Classless static route destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option static-route <tag> next-hop

help: IP address of router to be used to reach the destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option tftp-server-name

help: TFTP server name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option time-offset

help: Client subnet offset in seconds from Coordinated Universal Time (UTC)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option time-server

help: IP address of time server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option time-zone

help: Time zone to send to clients. Uses RFC4833 options 100 and 101

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option vendor-option ubiquiti

help: Ubiquiti specific parameters

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option vendor-option ubiquiti unifi-controller

help: Address of UniFi controller

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option wins-server

help: IP address for Windows Internet Name Service (WINS) server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> option wpad-url

help: Web Proxy Autodiscovery (WPAD) URL

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag>

help: DHCP lease range

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option

help: DHCP option

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option bootfile-name

help: Bootstrap file name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option bootfile-server

help: Server from which the initial boot file is to be loaded

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option bootfile-size

help: Bootstrap file size

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option client-prefix-length

help: Specifies the clients subnet mask as per RFC 950. If unset, subnet declaration is used.

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option default-router

help: IP address of default router

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option domain-name

help: Client Domain Name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option ip-forwarding

help: Enable IP forwarding on client

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option ipv6-only-preferred

help: Disable IPv4 on IPv6 only hosts (RFC 8925)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option ntp-server

help: IP address of NTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option pop-server

help: IP address of POP3 server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option server-identifier

help: Address for DHCP server identifier

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option smtp-server

help: IP address of SMTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option static-route <tag>

help: Classless static route destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option static-route <tag> next-hop

help: IP address of router to be used to reach the destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option tftp-server-name

help: TFTP server name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option time-offset

help: Client subnet offset in seconds from Coordinated Universal Time (UTC)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option time-server

help: IP address of time server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option time-zone

help: Time zone to send to clients. Uses RFC4833 options 100 and 101

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option vendor-option ubiquiti

help: Ubiquiti specific parameters

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option vendor-option ubiquiti unifi-controller

help: Address of UniFi controller

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option wins-server

help: IP address for Windows Internet Name Service (WINS) server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> option wpad-url

help: Web Proxy Autodiscovery (WPAD) URL

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> start

help: First IP address for DHCP lease range

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> range <tag> stop

help: Last IP address for DHCP lease range

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag>

help: Hostname for static mapping reservation

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> description

help: Description

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> disable

help: Disable instance

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> ip-address

help: Fixed IP address of static mapping

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option

help: DHCP option

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option bootfile-name

help: Bootstrap file name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option bootfile-server

help: Server from which the initial boot file is to be loaded

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option bootfile-size

help: Bootstrap file size

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option client-prefix-length

help: Specifies the clients subnet mask as per RFC 950. If unset, subnet declaration is used.

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option default-router

help: IP address of default router

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option domain-name

help: Client Domain Name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option ip-forwarding

help: Enable IP forwarding on client

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option ipv6-only-preferred

help: Disable IPv4 on IPv6 only hosts (RFC 8925)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option ntp-server

help: IP address of NTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option pop-server

help: IP address of POP3 server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option server-identifier

help: Address for DHCP server identifier

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option smtp-server

help: IP address of SMTP server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option static-route <tag>

help: Classless static route destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option static-route <tag> next-hop

help: IP address of router to be used to reach the destination subnet

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option tftp-server-name

help: TFTP server name

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option time-offset

help: Client subnet offset in seconds from Coordinated Universal Time (UTC)

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option time-server

help: IP address of time server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option time-zone

help: Time zone to send to clients. Uses RFC4833 options 100 and 101

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option vendor-option ubiquiti

help: Ubiquiti specific parameters

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option vendor-option ubiquiti unifi-controller

help: Address of UniFi controller

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option wins-server

help: IP address for Windows Internet Name Service (WINS) server

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> static-mapping <tag> option wpad-url

help: Web Proxy Autodiscovery (WPAD) URL

.. cfg_cmd:: service dhcp-server shared-network-name <tag> subnet <tag> subnet-id

help: Unique ID mapped to leases in the lease file

.. cfg_cmd:: service dhcpv6-relay

help: DHCPv6 Relay Agent parameters

.. cfg_cmd:: service dhcpv6-relay disable

help: Disable instance

.. cfg_cmd:: service dhcpv6-relay listen-interface <tag>

help: Interface for DHCPv6 Relay Agent to listen for requests

.. cfg_cmd:: service dhcpv6-relay listen-interface <tag> address

help: IPv6 address on listen-interface listen for requests on

.. cfg_cmd:: service dhcpv6-relay max-hop-count

help: Maximum hop count for which requests will be processed
10


.. cfg_cmd:: service dhcpv6-relay upstream-interface <tag>

help: Interface for DHCPv6 Relay Agent forward requests out

.. cfg_cmd:: service dhcpv6-relay upstream-interface <tag> address

help: IPv6 address to forward requests to

.. cfg_cmd:: service dhcpv6-relay use-interface-id-option

help: Option to set DHCPv6 interface-ID option

.. cfg_cmd:: service dhcpv6-server

help: DHCP for IPv6 (DHCPv6) server

.. cfg_cmd:: service dhcpv6-server disable

help: Disable instance

.. cfg_cmd:: service dhcpv6-server disable-route-autoinstall

help: Do not install routes for delegated prefixes

.. cfg_cmd:: service dhcpv6-server global-parameters

help: Additional global parameters for DHCPv6 server

.. cfg_cmd:: service dhcpv6-server global-parameters name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcpv6-server listen-interface

help: Interface to listen on

.. cfg_cmd:: service dhcpv6-server preference

help: Preference of this DHCPv6 server compared with others

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag>

help: DHCPv6 shared network name

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> common-options

help: Common options to distribute to all clients, including stateless clients

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> common-options domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> common-options info-refresh-time

help: Time (in seconds) that stateless clients should wait between refreshing the information they were given

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> common-options name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> description

help: Description

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> disable

help: Disable instance

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> interface

help: Optional interface for this shared network to accept requests from

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag>

help: IPv6 DHCP subnet for this shared network

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> interface

help: Optional interface for this subnet to accept requests from

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> lease-time

help: Parameters relating to the lease time

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> lease-time default

help: Default time (in seconds) that will be assigned to a lease

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> lease-time maximum

help: Maximum time (in seconds) that will be assigned to a lease

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> lease-time minimum

help: Minimum time (in seconds) that will be assigned to a lease

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option

help: DHCPv6 option

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option nis-domain

help: NIS domain name for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option nis-server

help: IPv6 address of a NIS Server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option nisplus-domain

help: NIS+ domain name for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option nisplus-server

help: IPv6 address of a NIS+ Server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option sip-server

help: IPv6 address of SIP server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option sntp-server

help: IPv6 address of an SNTP server for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option vendor-option cisco

help: Cisco specific parameters

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> option vendor-option cisco tftp-server

help: TFTP server name

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> prefix-delegation

help: Parameters relating to IPv6 prefix delegation

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> prefix-delegation prefix <tag>

help: IPv6 prefix to be used in prefix delegation

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> prefix-delegation prefix <tag> delegated-length

help: Length in bits of prefixes to be delegated

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> prefix-delegation prefix <tag> excluded-prefix

help: IPv6 prefix to be excluded from prefix delegation

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> prefix-delegation prefix <tag> excluded-prefix-length

help: Length in bits of excluded prefix

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> prefix-delegation prefix <tag> prefix-length

help: Length in bits of prefix

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag>

help: Parameters setting ranges for assigning IPv6 addresses

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option

help: DHCPv6 option

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option nis-domain

help: NIS domain name for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option nis-server

help: IPv6 address of a NIS Server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option nisplus-domain

help: NIS+ domain name for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option nisplus-server

help: IPv6 address of a NIS+ Server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option sip-server

help: IPv6 address of SIP server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option sntp-server

help: IPv6 address of an SNTP server for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option vendor-option cisco

help: Cisco specific parameters

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> option vendor-option cisco tftp-server

help: TFTP server name

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> prefix

help: IPv6 prefix defining range of addresses to assign

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> start

help: First in range of consecutive IPv6 addresses to assign

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> range <tag> stop

help: Last in range of consecutive IPv6 addresses

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag>

help: Hostname for static mapping reservation

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> disable

help: Disable instance

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> duid

help: DHCP unique identifier (DUID) to be sent by client

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> ipv6-address

help: Client IPv6 address for this static mapping

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> ipv6-prefix

help: Client IPv6 prefix for this static mapping

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option

help: DHCPv6 option

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option captive-portal

help: Captive portal API endpoint

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option domain-search

help: Client Domain Name search list

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option nis-domain

help: NIS domain name for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option nis-server

help: IPv6 address of a NIS Server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option nisplus-domain

help: NIS+ domain name for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option nisplus-server

help: IPv6 address of a NIS+ Server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option sip-server

help: IPv6 address of SIP server

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option sntp-server

help: IPv6 address of an SNTP server for client to use

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option vendor-option

help: Vendor Specific Options

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option vendor-option cisco

help: Cisco specific parameters

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> static-mapping <tag> option vendor-option cisco tftp-server

help: TFTP server name

.. cfg_cmd:: service dhcpv6-server shared-network-name <tag> subnet <tag> subnet-id

help: Unique ID mapped to leases in the lease file

.. cfg_cmd:: service dns

help: Domain Name System (DNS) related services

.. cfg_cmd:: service dns dynamic

help: Dynamic DNS

.. cfg_cmd:: service dns dynamic interval

help: Interval in seconds to wait between Dynamic DNS updates
300


.. cfg_cmd:: service dns dynamic name <tag>

help: Dynamic DNS configuration

.. cfg_cmd:: service dns dynamic name <tag> address

help: Obtain IP address to send Dynamic DNS update for

.. cfg_cmd:: service dns dynamic name <tag> address interface

help: Interface to use

.. cfg_cmd:: service dns dynamic name <tag> address web

help: HTTP(S) web request to use

.. cfg_cmd:: service dns dynamic name <tag> address web skip

help: Pattern to skip from the HTTP(S) respose

.. cfg_cmd:: service dns dynamic name <tag> address web url

help: Remote URL

.. cfg_cmd:: service dns dynamic name <tag> description

help: Description

.. cfg_cmd:: service dns dynamic name <tag> expiry-time

help: Time in seconds for the hostname to be marked expired in cache

.. cfg_cmd:: service dns dynamic name <tag> host-name

help: Hostname to register with Dynamic DNS service

.. cfg_cmd:: service dns dynamic name <tag> ip-version

help: IP address version to use
ipv4


.. cfg_cmd:: service dns dynamic name <tag> key

help: File containing TSIG authentication key for RFC2136 nsupdate on remote DNS server

.. cfg_cmd:: service dns dynamic name <tag> password

help: Password used for authentication

.. cfg_cmd:: service dns dynamic name <tag> protocol

help: ddclient protocol used for Dynamic DNS service

.. cfg_cmd:: service dns dynamic name <tag> server

help: Remote Dynamic DNS server to send updates to

.. cfg_cmd:: service dns dynamic name <tag> ttl

help: Time-to-live (TTL)

.. cfg_cmd:: service dns dynamic name <tag> username

help: Username used for authentication

.. cfg_cmd:: service dns dynamic name <tag> wait-time

help: Time in seconds to wait between update attempts

.. cfg_cmd:: service dns dynamic name <tag> zone

help: DNS zone to be updated

.. cfg_cmd:: service dns dynamic vrf

help: VRF instance name

.. cfg_cmd:: service dns forwarding

help: DNS forwarding

.. cfg_cmd:: service dns forwarding allow-from

help: Networks allowed to query this server

.. cfg_cmd:: service dns forwarding authoritative-domain <tag>

help: Domain to host authoritative records for

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records

help: DNS zone records

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag>

help: A record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag> address

help: IPv4 address

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag>

help: AAAA record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag> address

help: IPv6 address

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag>

help: CNAME record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag> target

help: Target DNS name

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag>

help: MX record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> server <tag>

help: Mail server

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> server <tag> priority

help: Server priority
10


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag>

help: NAPTR record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag>

help: NAPTR rule

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> lookup-a

help: A flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> lookup-srv

help: S flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> order

help: Rule order

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> preference

help: Rule preference
0


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> protocol-specific

help: P flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> regexp

help: Regular expression

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> replacement

help: Replacement DNS name

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> resolve-uri

help: U flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> service

help: Service type

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag>

help: NS record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag> target

help: Target DNS server authoritative for subdomain

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag>

help: PTR record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag> target

help: Target DNS name

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag>

help: SPF record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag> value

help: Record contents

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag>

help: SRV record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag>

help: Service entry

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> hostname

help: Server hostname

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> port

help: Port number

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> priority

help: Entry priority
10


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> weight

help: Entry weight
0


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag>

help: TXT record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag> value

help: Record contents

.. cfg_cmd:: service dns forwarding cache-size

help: DNS forwarding cache size
10000


.. cfg_cmd:: service dns forwarding dhcp

help: Interfaces whose DHCP client nameservers to forward requests to

.. cfg_cmd:: service dns forwarding dns64-prefix

help: Help to communicate between IPv6-only client and IPv4-only server

.. cfg_cmd:: service dns forwarding dnssec

help: DNSSEC mode
process-no-validate


.. cfg_cmd:: service dns forwarding domain <tag>

help: Domain to forward to a custom DNS server

.. cfg_cmd:: service dns forwarding domain <tag> addnta

help: Add NTA (negative trust anchor) for this domain (must be set if the domain does not support DNSSEC)

.. cfg_cmd:: service dns forwarding domain <tag> name-server <tag>

help: Domain Name Servers (DNS) addresses to forward queries to

.. cfg_cmd:: service dns forwarding domain <tag> name-server <tag> port

help: Port number used by connection
53


.. cfg_cmd:: service dns forwarding domain <tag> recursion-desired

help: Set the "recursion desired" bit in requests to the upstream nameserver

.. cfg_cmd:: service dns forwarding exclude-throttle-address

help: IP address or subnet

.. cfg_cmd:: service dns forwarding ignore-hosts-file

help: Do not use local /etc/hosts file in name resolution

.. cfg_cmd:: service dns forwarding listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service dns forwarding name-server <tag>

help: Domain Name Servers (DNS) addresses to forward queries to

.. cfg_cmd:: service dns forwarding name-server <tag> port

help: Port number used by connection
53


.. cfg_cmd:: service dns forwarding negative-ttl

help: Maximum amount of time negative entries are cached
3600


.. cfg_cmd:: service dns forwarding no-serve-rfc1918

help: Makes the server authoritatively not aware of RFC1918 addresses

.. cfg_cmd:: service dns forwarding options

help: DNS server options

.. cfg_cmd:: service dns forwarding options ecs-add-for

help: Client netmask for which EDNS Client Subnet will be added

.. cfg_cmd:: service dns forwarding options ecs-ipv4-bits

help: Number of bits of IPv4 address to pass for EDNS Client Subnet

.. cfg_cmd:: service dns forwarding options edns-subnet-allow-list

help: Netmask or domain that we should enable EDNS subnet for

.. cfg_cmd:: service dns forwarding port

help: Port number used by connection
53


.. cfg_cmd:: service dns forwarding serve-stale-extension

help: Number of times the expired TTL of a record is extended by 30 seconds when serving stale
0


.. cfg_cmd:: service dns forwarding source-address

help: Source IP address used to initiate connection
0.0.0.0 ::


.. cfg_cmd:: service dns forwarding system

help: Use system name servers

.. cfg_cmd:: service dns forwarding timeout

help: Number of milliseconds to wait for a remote authoritative server to respond
1500


.. cfg_cmd:: service event-handler

help: Service event handler

.. cfg_cmd:: service event-handler event <tag>

help: Event handler name

.. cfg_cmd:: service event-handler event <tag> filter

help: Logs filter settings

.. cfg_cmd:: service event-handler event <tag> filter pattern

help: Match pattern (regex)

.. cfg_cmd:: service event-handler event <tag> filter syslog-identifier

help: Identifier of a process in syslog (string)

.. cfg_cmd:: service event-handler event <tag> script

help: Event handler script file

.. cfg_cmd:: service event-handler event <tag> script arguments

help: Script arguments

.. cfg_cmd:: service event-handler event <tag> script environment <tag>

help: Script environment arguments

.. cfg_cmd:: service event-handler event <tag> script environment <tag> value

help: Environment value

.. cfg_cmd:: service event-handler event <tag> script path

help: Path to the script

.. cfg_cmd:: service https

help: HTTPS configuration

.. cfg_cmd:: service https allow-client

help: Restrict to allowed IP client addresses

.. cfg_cmd:: service https allow-client address

help: Allowed IP client addresses

.. cfg_cmd:: service https api

help: VyOS HTTP API configuration

.. cfg_cmd:: service https api cors

help: Set CORS options

.. cfg_cmd:: service https api cors allow-origin

help: Allow resource request from origin

.. cfg_cmd:: service https api debug

help: Debug

.. cfg_cmd:: service https api graphql

help: GraphQL support

.. cfg_cmd:: service https api graphql authentication

help: GraphQL authentication

.. cfg_cmd:: service https api graphql authentication expiration

help: Token time to expire in seconds
3600


.. cfg_cmd:: service https api graphql authentication secret-length

help: Length of shared secret in bytes
32


.. cfg_cmd:: service https api graphql authentication type

help: Authentication type
key


.. cfg_cmd:: service https api graphql introspection

help: Schema introspection

.. cfg_cmd:: service https api keys

help: HTTP API keys

.. cfg_cmd:: service https api keys id <tag>

help: HTTP API id

.. cfg_cmd:: service https api keys id <tag> key

help: HTTP API plaintext key

.. cfg_cmd:: service https api strict

help: Enforce strict path checking

.. cfg_cmd:: service https certificates

help: TLS certificates

.. cfg_cmd:: service https certificates ca-certificate

help: Certificate Authority in PKI configuration

.. cfg_cmd:: service https certificates certificate

help: Certificate in PKI configuration

.. cfg_cmd:: service https certificates dh-params

help: Diffie Hellman parameters (server only)

.. cfg_cmd:: service https enable-http-redirect

help: Enable HTTP to HTTPS redirect

.. cfg_cmd:: service https listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service https port

help: Port number used by connection
443


.. cfg_cmd:: service https request-body-size-limit

help: Maximum request body size in megabytes
1


.. cfg_cmd:: service https tls-version

help: Specify available TLS version(s)
1.2 1.3


.. cfg_cmd:: service https vrf

help: VRF instance name

.. cfg_cmd:: service ids

help: Intrusion Detection System

.. cfg_cmd:: service ids ddos-protection

help: FastNetMon detection and protection parameters

.. cfg_cmd:: service ids ddos-protection alert-script

help: Path to fastnetmon alert script

.. cfg_cmd:: service ids ddos-protection ban-time

help: How long we should keep an IP in blocked state
1900


.. cfg_cmd:: service ids ddos-protection direction

help: Direction for processing traffic

.. cfg_cmd:: service ids ddos-protection excluded-network

help: Specify IPv4 and IPv6 networks which are going to be excluded from protection

.. cfg_cmd:: service ids ddos-protection listen-interface

help: Listen interface for mirroring traffic

.. cfg_cmd:: service ids ddos-protection mode

help: Traffic capture mode

.. cfg_cmd:: service ids ddos-protection network

help: Specify IPv4 and IPv6 networks which belong to you

.. cfg_cmd:: service ids ddos-protection sflow

help: Sflow settings

.. cfg_cmd:: service ids ddos-protection sflow listen-address

help: Local IPv4 addresses to listen on

.. cfg_cmd:: service ids ddos-protection sflow port

help: Port number used by connection
6343


.. cfg_cmd:: service ids ddos-protection threshold

help: Attack limits thresholds

.. cfg_cmd:: service ids ddos-protection threshold general

help: General threshold

.. cfg_cmd:: service ids ddos-protection threshold general fps

help: Flows per second

.. cfg_cmd:: service ids ddos-protection threshold general mbps

help: Megabits per second

.. cfg_cmd:: service ids ddos-protection threshold general pps

help: Packets per second

.. cfg_cmd:: service ids ddos-protection threshold icmp

help: ICMP threshold

.. cfg_cmd:: service ids ddos-protection threshold icmp fps

help: Flows per second

.. cfg_cmd:: service ids ddos-protection threshold icmp mbps

help: Megabits per second

.. cfg_cmd:: service ids ddos-protection threshold icmp pps

help: Packets per second

.. cfg_cmd:: service ids ddos-protection threshold tcp

help: TCP threshold

.. cfg_cmd:: service ids ddos-protection threshold tcp fps

help: Flows per second

.. cfg_cmd:: service ids ddos-protection threshold tcp mbps

help: Megabits per second

.. cfg_cmd:: service ids ddos-protection threshold tcp pps

help: Packets per second

.. cfg_cmd:: service ids ddos-protection threshold udp

help: UDP threshold

.. cfg_cmd:: service ids ddos-protection threshold udp fps

help: Flows per second

.. cfg_cmd:: service ids ddos-protection threshold udp mbps

help: Megabits per second

.. cfg_cmd:: service ids ddos-protection threshold udp pps

help: Packets per second

.. cfg_cmd:: service ipoe-server

help: Internet Protocol over Ethernet (IPoE) Server

.. cfg_cmd:: service ipoe-server authentication

help: Client authentication methods

.. cfg_cmd:: service ipoe-server authentication interface <tag>

help: Network interface for client MAC addresses

.. cfg_cmd:: service ipoe-server authentication interface <tag> mac <tag>

help: Media Access Control (MAC) address

.. cfg_cmd:: service ipoe-server authentication interface <tag> mac <tag> rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: service ipoe-server authentication interface <tag> mac <tag> rate-limit download

help: Download bandwidth limit in kbits/sec

.. cfg_cmd:: service ipoe-server authentication interface <tag> mac <tag> rate-limit upload

help: Upload bandwidth limit in kbits/sec

.. cfg_cmd:: service ipoe-server authentication interface <tag> mac <tag> vlan

help: VLAN monitor for automatic creation of VLAN interfaces

.. cfg_cmd:: service ipoe-server authentication mode

help: Authentication mode used by this server
local


.. cfg_cmd:: service ipoe-server authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: service ipoe-server authentication radius accounting-interim-interval

help: Interval in seconds to send accounting information

.. cfg_cmd:: service ipoe-server authentication radius acct-interim-jitter

help: Maximum jitter value in seconds to be applied to accounting information interval

.. cfg_cmd:: service ipoe-server authentication radius acct-timeout

help: Timeout for Interim-Update packets, terminate session afterwards
3


.. cfg_cmd:: service ipoe-server authentication radius dynamic-author

help: Dynamic Authorization Extension/Change of Authorization server

.. cfg_cmd:: service ipoe-server authentication radius dynamic-author key

help: Shared secret for Dynamic Authorization Extension server

.. cfg_cmd:: service ipoe-server authentication radius dynamic-author port

help: Port for Dynamic Authorization Extension server (DM/CoA)
1700


.. cfg_cmd:: service ipoe-server authentication radius dynamic-author server

help: IP address for Dynamic Authorization Extension server (DM/CoA)

.. cfg_cmd:: service ipoe-server authentication radius max-try

help: Number of tries to send Access-Request/Accounting-Request queries
3


.. cfg_cmd:: service ipoe-server authentication radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: service ipoe-server authentication radius nas-ip-address

help: NAS-IP-Address attribute sent to RADIUS

.. cfg_cmd:: service ipoe-server authentication radius preallocate-vif

help: Enable attribute NAS-Port-Id in Access-Request

.. cfg_cmd:: service ipoe-server authentication radius rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: service ipoe-server authentication radius rate-limit attribute

help: RADIUS attribute that contains rate information
Filter-Id


.. cfg_cmd:: service ipoe-server authentication radius rate-limit enable

help: Enable bandwidth shaping via RADIUS

.. cfg_cmd:: service ipoe-server authentication radius rate-limit multiplier

help: Shaper multiplier
1


.. cfg_cmd:: service ipoe-server authentication radius rate-limit vendor

help: Vendor dictionary

.. cfg_cmd:: service ipoe-server authentication radius server <tag>

help: No help available

.. cfg_cmd:: service ipoe-server authentication radius server <tag> acct-port

help: Accounting port
1813


.. cfg_cmd:: service ipoe-server authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: service ipoe-server authentication radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: service ipoe-server authentication radius server <tag> fail-time

help: Mark server unavailable for <n> seconds on failure
0


.. cfg_cmd:: service ipoe-server authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: service ipoe-server authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: service ipoe-server authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: service ipoe-server authentication radius timeout

help: Timeout in seconds to wait response from RADIUS server
3


.. cfg_cmd:: service ipoe-server client-ip-pool <tag>

help: Client IP pool

.. cfg_cmd:: service ipoe-server client-ip-pool <tag> next-pool

help: Next pool name

.. cfg_cmd:: service ipoe-server client-ip-pool <tag> range

help: Range of IP addresses

.. cfg_cmd:: service ipoe-server client-ipv6-pool <tag>

help: Pool of client IPv6 addresses

.. cfg_cmd:: service ipoe-server client-ipv6-pool <tag> delegate <tag>

help: Subnet used to delegate prefix through DHCPv6-PD (RFC3633)

.. cfg_cmd:: service ipoe-server client-ipv6-pool <tag> delegate <tag> delegation-prefix

help: Prefix length delegated to client

.. cfg_cmd:: service ipoe-server client-ipv6-pool <tag> prefix <tag>

help: Pool of addresses used to assign to clients

.. cfg_cmd:: service ipoe-server client-ipv6-pool <tag> prefix <tag> mask

help: Prefix length used for individual client
64


.. cfg_cmd:: service ipoe-server default-ipv6-pool

help: Default client IPv6 pool name

.. cfg_cmd:: service ipoe-server default-pool

help: Default client IP pool name

.. cfg_cmd:: service ipoe-server description

help: Description

.. cfg_cmd:: service ipoe-server extended-scripts

help: Extended script execution

.. cfg_cmd:: service ipoe-server extended-scripts on-change

help: Script to run when session interface changed by RADIUS CoA handling

.. cfg_cmd:: service ipoe-server extended-scripts on-down

help: Script to run when session interface going to terminate

.. cfg_cmd:: service ipoe-server extended-scripts on-pre-up

help: Script to run before session interface comes up

.. cfg_cmd:: service ipoe-server extended-scripts on-up

help: Script to run when session interface is completely configured and started

.. cfg_cmd:: service ipoe-server gateway-address

help: Gateway IP address

.. cfg_cmd:: service ipoe-server interface <tag>

help: Interface to listen dhcp or unclassified packets

.. cfg_cmd:: service ipoe-server interface <tag> client-subnet

help: Client address pool

.. cfg_cmd:: service ipoe-server interface <tag> external-dhcp

help: DHCP requests will be forwarded

.. cfg_cmd:: service ipoe-server interface <tag> external-dhcp dhcp-relay

help: DHCP Server the request will be redirected to.

.. cfg_cmd:: service ipoe-server interface <tag> external-dhcp giaddr

help: Relay Agent IPv4 Address

.. cfg_cmd:: service ipoe-server interface <tag> mode

help: Client connectivity mode
l2


.. cfg_cmd:: service ipoe-server interface <tag> network

help: Enables clients to share the same network or each client has its own vlan
shared


.. cfg_cmd:: service ipoe-server interface <tag> vlan

help: VLAN monitor for automatic creation of VLAN interfaces

.. cfg_cmd:: service ipoe-server limits

help: Limits the connection rate from a single source

.. cfg_cmd:: service ipoe-server limits burst

help: Burst count

.. cfg_cmd:: service ipoe-server limits connection-limit

help: Acceptable rate of connections (e.g. 1/min, 60/sec)

.. cfg_cmd:: service ipoe-server limits timeout

help: Timeout in seconds

.. cfg_cmd:: service ipoe-server max-concurrent-sessions

help: Maximum number of concurrent session start attempts

.. cfg_cmd:: service ipoe-server name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service ipoe-server shaper

help: Traffic shaper bandwidth parameters

.. cfg_cmd:: service ipoe-server shaper fwmark

help: Firewall mark value for traffic that excludes from shaping

.. cfg_cmd:: service ipoe-server snmp

help: Enable SNMP

.. cfg_cmd:: service ipoe-server snmp master-agent

help: Enable SNMP master agent mode

.. cfg_cmd:: service lldp

help: LLDP settings

.. cfg_cmd:: service lldp interface <tag>

help: Location data for interface

.. cfg_cmd:: service lldp interface <tag> disable

help: Disable instance

.. cfg_cmd:: service lldp interface <tag> location

help: LLDP-MED location data

.. cfg_cmd:: service lldp interface <tag> location coordinate-based

help: Coordinate based location

.. cfg_cmd:: service lldp interface <tag> location coordinate-based altitude

help: Altitude in meters
0


.. cfg_cmd:: service lldp interface <tag> location coordinate-based datum

help: Coordinate datum type
WGS84


.. cfg_cmd:: service lldp interface <tag> location coordinate-based latitude

help: Latitude

.. cfg_cmd:: service lldp interface <tag> location coordinate-based longitude

help: Longitude

.. cfg_cmd:: service lldp interface <tag> location elin

help: ECS ELIN (Emergency location identifier number)

.. cfg_cmd:: service lldp legacy-protocols

help: Legacy (vendor specific) protocols

.. cfg_cmd:: service lldp legacy-protocols cdp

help: Listen for CDP for Cisco routers/switches

.. cfg_cmd:: service lldp legacy-protocols edp

help: Listen for EDP for Extreme routers/switches

.. cfg_cmd:: service lldp legacy-protocols fdp

help: Listen for FDP for Foundry routers/switches

.. cfg_cmd:: service lldp legacy-protocols sonmp

help: Listen for SONMP for Nortel routers/switches

.. cfg_cmd:: service lldp management-address

help: Management IP Address

.. cfg_cmd:: service lldp snmp

help: Enable SNMP queries of the LLDP database

.. cfg_cmd:: service mdns

help: Multicast DNS (mDNS) parameters

.. cfg_cmd:: service mdns repeater

help: mDNS repeater configuration

.. cfg_cmd:: service mdns repeater allow-service

help: Allowed mDNS services to be repeated

.. cfg_cmd:: service mdns repeater browse-domain

help: mDNS browsing domains in addition to the default one

.. cfg_cmd:: service mdns repeater disable

help: Disable instance

.. cfg_cmd:: service mdns repeater interface

help: Interface to use

.. cfg_cmd:: service mdns repeater ip-version

help: IP address version to use
both


.. cfg_cmd:: service mdns repeater vrrp-disable

help: Disables mDNS repeater on VRRP interfaces not in MASTER state

.. cfg_cmd:: service monitoring

help: Monitoring services

.. cfg_cmd:: service monitoring telegraf

help: Telegraf metric collector

.. cfg_cmd:: service monitoring telegraf azure-data-explorer

help: Output plugin Azure Data Explorer

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication

help: Authentication parameters

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication client-id

help: Application client id

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication client-secret

help: Application client secret

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication tenant-id

help: Set tenant id

.. cfg_cmd:: service monitoring telegraf azure-data-explorer database

help: Remote database name

.. cfg_cmd:: service monitoring telegraf azure-data-explorer group-metrics

help: Type of metrics grouping when push to Azure Data Explorer
table-per-metric


.. cfg_cmd:: service monitoring telegraf azure-data-explorer table

help: Name of the single table [Only if set group-metrics single-table]

.. cfg_cmd:: service monitoring telegraf azure-data-explorer url

help: Remote URL

.. cfg_cmd:: service monitoring telegraf influxdb

help: Output plugin InfluxDB

.. cfg_cmd:: service monitoring telegraf influxdb authentication

help: Authentication parameters

.. cfg_cmd:: service monitoring telegraf influxdb authentication organization

help: Authentication organization for InfluxDB v2

.. cfg_cmd:: service monitoring telegraf influxdb authentication token

help: Authentication token for InfluxDB v2

.. cfg_cmd:: service monitoring telegraf influxdb bucket

help: Remote bucket
main


.. cfg_cmd:: service monitoring telegraf influxdb port

help: Port number used by connection
8086


.. cfg_cmd:: service monitoring telegraf influxdb url

help: Remote URL

.. cfg_cmd:: service monitoring telegraf prometheus-client

help: Output plugin Prometheus client

.. cfg_cmd:: service monitoring telegraf prometheus-client allow-from

help: Networks allowed to query this server

.. cfg_cmd:: service monitoring telegraf prometheus-client authentication

help: HTTP basic authentication parameters

.. cfg_cmd:: service monitoring telegraf prometheus-client authentication password

help: Authentication password

.. cfg_cmd:: service monitoring telegraf prometheus-client authentication username

help: Authentication username

.. cfg_cmd:: service monitoring telegraf prometheus-client listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service monitoring telegraf prometheus-client metric-version

help: Metric version control mapping from Telegraf to Prometheus format
2


.. cfg_cmd:: service monitoring telegraf prometheus-client port

help: Port number used by connection
9273


.. cfg_cmd:: service monitoring telegraf source

help: Source parameters for monitoring
all


.. cfg_cmd:: service monitoring telegraf splunk

help: Output plugin Splunk

.. cfg_cmd:: service monitoring telegraf splunk authentication

help: HTTP basic authentication parameters

.. cfg_cmd:: service monitoring telegraf splunk authentication insecure

help: Use TLS but skip host validation

.. cfg_cmd:: service monitoring telegraf splunk authentication token

help: Authorization token

.. cfg_cmd:: service monitoring telegraf splunk url

help: Remote URL

.. cfg_cmd:: service monitoring telegraf vrf

help: VRF instance name

.. cfg_cmd:: service monitoring zabbix-agent

help: Zabbix-agent settings

.. cfg_cmd:: service monitoring zabbix-agent directory

help: Folder containing individual Zabbix-agent configuration files

.. cfg_cmd:: service monitoring zabbix-agent host-name

help: Zabbix agent hostname

.. cfg_cmd:: service monitoring zabbix-agent limits

help: Limit settings

.. cfg_cmd:: service monitoring zabbix-agent limits buffer-flush-interval

help: Do not keep data longer than N seconds in buffer
5


.. cfg_cmd:: service monitoring zabbix-agent limits buffer-size

help: Maximum number of values in a memory buffer
100


.. cfg_cmd:: service monitoring zabbix-agent listen-address

help: Local IP addresses to listen on
0.0.0.0


.. cfg_cmd:: service monitoring zabbix-agent log

help: Log settings

.. cfg_cmd:: service monitoring zabbix-agent log debug-level

help: Debug level
warning


.. cfg_cmd:: service monitoring zabbix-agent log remote-commands

help: Enable logging of executed shell commands as warnings

.. cfg_cmd:: service monitoring zabbix-agent log size

help: Log file size in megabytes
0


.. cfg_cmd:: service monitoring zabbix-agent port

help: Port number used by connection
10050


.. cfg_cmd:: service monitoring zabbix-agent server

help: Remote server to connect to

.. cfg_cmd:: service monitoring zabbix-agent server-active <tag>

help: Remote server address to get active checks from

.. cfg_cmd:: service monitoring zabbix-agent server-active <tag> port

help: Port number used by connection

.. cfg_cmd:: service monitoring zabbix-agent timeout

help: Item processing timeout in seconds
3


.. cfg_cmd:: service ndp-proxy

help: Neighbor Discovery Protocol (NDP) Proxy

.. cfg_cmd:: service ndp-proxy interface <tag>

help: NDP proxy listener interface

.. cfg_cmd:: service ndp-proxy interface <tag> disable

help: Disable instance

.. cfg_cmd:: service ndp-proxy interface <tag> enable-router-bit

help: Enable router bit in Neighbor Advertisement messages

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag>

help: Prefix target addresses are matched against

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag> disable

help: Disable instance

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag> interface

help: Interface to forward Neighbor Solicitation message through. Required for "iface" mode

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag> mode

help: Specify the running mode of the rule
static


.. cfg_cmd:: service ndp-proxy interface <tag> timeout

help: Timeout for Neighbor Advertisement after Neighbor Solicitation message
500


.. cfg_cmd:: service ndp-proxy interface <tag> ttl

help: Proxy entry cache Time-To-Live
30000


.. cfg_cmd:: service ndp-proxy route-refresh

help: Refresh interval for IPv6 routes
30000


.. cfg_cmd:: service ntp

help: Network Time Protocol (NTP) configuration

.. cfg_cmd:: service ntp allow-client

help: Restrict to allowed IP client addresses

.. cfg_cmd:: service ntp allow-client address

help: Allowed IP client addresses

.. cfg_cmd:: service ntp interface

help: Interface to use

.. cfg_cmd:: service ntp leap-second

help: Leap second behavior
timezone


.. cfg_cmd:: service ntp listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service ntp server <tag>

help: Network Time Protocol (NTP) server

.. cfg_cmd:: service ntp server <tag> noselect

help: Marks the server as unused

.. cfg_cmd:: service ntp server <tag> nts

help: Enable Network Time Security (NTS) for the server

.. cfg_cmd:: service ntp server <tag> pool

help: Associate with a number of remote servers

.. cfg_cmd:: service ntp server <tag> prefer

help: Marks the server as preferred

.. cfg_cmd:: service ntp vrf

help: VRF instance name

.. cfg_cmd:: service pppoe-server

help: Point to Point over Ethernet (PPPoE) Server

.. cfg_cmd:: service pppoe-server access-concentrator

help: Access concentrator name
vyos-ac


.. cfg_cmd:: service pppoe-server authentication

help: Authentication for remote access PPPoE Server

.. cfg_cmd:: service pppoe-server authentication local-users

help: Local user authentication for PPPoE server

.. cfg_cmd:: service pppoe-server authentication local-users username <tag>

help: User name for authentication

.. cfg_cmd:: service pppoe-server authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: service pppoe-server authentication local-users username <tag> password

help: Password for authentication

.. cfg_cmd:: service pppoe-server authentication local-users username <tag> rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: service pppoe-server authentication local-users username <tag> rate-limit download

help: Download bandwidth limit in kbits/sec

.. cfg_cmd:: service pppoe-server authentication local-users username <tag> rate-limit upload

help: Upload bandwidth limit in kbits/sec

.. cfg_cmd:: service pppoe-server authentication local-users username <tag> static-ip

help: Static client IP address
*


.. cfg_cmd:: service pppoe-server authentication mode

help: Authentication mode used by this server
local


.. cfg_cmd:: service pppoe-server authentication protocols

help: Authentication protocol for remote access peer
pap chap mschap mschap-v2


.. cfg_cmd:: service pppoe-server authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: service pppoe-server authentication radius accounting-interim-interval

help: Interval in seconds to send accounting information

.. cfg_cmd:: service pppoe-server authentication radius acct-interim-jitter

help: Maximum jitter value in seconds to be applied to accounting information interval

.. cfg_cmd:: service pppoe-server authentication radius acct-timeout

help: Timeout for Interim-Update packets, terminate session afterwards
3


.. cfg_cmd:: service pppoe-server authentication radius called-sid-format

help: Format of Called-Station-Id attribute

.. cfg_cmd:: service pppoe-server authentication radius dynamic-author

help: Dynamic Authorization Extension/Change of Authorization server

.. cfg_cmd:: service pppoe-server authentication radius dynamic-author key

help: Shared secret for Dynamic Authorization Extension server

.. cfg_cmd:: service pppoe-server authentication radius dynamic-author port

help: Port for Dynamic Authorization Extension server (DM/CoA)
1700


.. cfg_cmd:: service pppoe-server authentication radius dynamic-author server

help: IP address for Dynamic Authorization Extension server (DM/CoA)

.. cfg_cmd:: service pppoe-server authentication radius max-try

help: Number of tries to send Access-Request/Accounting-Request queries
3


.. cfg_cmd:: service pppoe-server authentication radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: service pppoe-server authentication radius nas-ip-address

help: NAS-IP-Address attribute sent to RADIUS

.. cfg_cmd:: service pppoe-server authentication radius preallocate-vif

help: Enable attribute NAS-Port-Id in Access-Request

.. cfg_cmd:: service pppoe-server authentication radius rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: service pppoe-server authentication radius rate-limit attribute

help: RADIUS attribute that contains rate information
Filter-Id


.. cfg_cmd:: service pppoe-server authentication radius rate-limit enable

help: Enable bandwidth shaping via RADIUS

.. cfg_cmd:: service pppoe-server authentication radius rate-limit multiplier

help: Shaper multiplier
1


.. cfg_cmd:: service pppoe-server authentication radius rate-limit vendor

help: Vendor dictionary

.. cfg_cmd:: service pppoe-server authentication radius server <tag>

help: No help available

.. cfg_cmd:: service pppoe-server authentication radius server <tag> acct-port

help: Accounting port
1813


.. cfg_cmd:: service pppoe-server authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: service pppoe-server authentication radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: service pppoe-server authentication radius server <tag> fail-time

help: Mark server unavailable for <n> seconds on failure
0


.. cfg_cmd:: service pppoe-server authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: service pppoe-server authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: service pppoe-server authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: service pppoe-server authentication radius timeout

help: Timeout in seconds to wait response from RADIUS server
3


.. cfg_cmd:: service pppoe-server client-ip-pool <tag>

help: Client IP pool

.. cfg_cmd:: service pppoe-server client-ip-pool <tag> next-pool

help: Next pool name

.. cfg_cmd:: service pppoe-server client-ip-pool <tag> range

help: Range of IP addresses

.. cfg_cmd:: service pppoe-server client-ipv6-pool <tag>

help: Pool of client IPv6 addresses

.. cfg_cmd:: service pppoe-server client-ipv6-pool <tag> delegate <tag>

help: Subnet used to delegate prefix through DHCPv6-PD (RFC3633)

.. cfg_cmd:: service pppoe-server client-ipv6-pool <tag> delegate <tag> delegation-prefix

help: Prefix length delegated to client

.. cfg_cmd:: service pppoe-server client-ipv6-pool <tag> prefix <tag>

help: Pool of addresses used to assign to clients

.. cfg_cmd:: service pppoe-server client-ipv6-pool <tag> prefix <tag> mask

help: Prefix length used for individual client
64


.. cfg_cmd:: service pppoe-server default-ipv6-pool

help: Default client IPv6 pool name

.. cfg_cmd:: service pppoe-server default-pool

help: Default client IP pool name

.. cfg_cmd:: service pppoe-server description

help: Description

.. cfg_cmd:: service pppoe-server extended-scripts

help: Extended script execution

.. cfg_cmd:: service pppoe-server extended-scripts on-change

help: Script to run when session interface changed by RADIUS CoA handling

.. cfg_cmd:: service pppoe-server extended-scripts on-down

help: Script to run when session interface going to terminate

.. cfg_cmd:: service pppoe-server extended-scripts on-pre-up

help: Script to run before session interface comes up

.. cfg_cmd:: service pppoe-server extended-scripts on-up

help: Script to run when session interface is completely configured and started

.. cfg_cmd:: service pppoe-server gateway-address

help: Gateway IP address

.. cfg_cmd:: service pppoe-server interface <tag>

help: interface(s) to listen on

.. cfg_cmd:: service pppoe-server interface <tag> vlan

help: VLAN monitor for automatic creation of VLAN interfaces

.. cfg_cmd:: service pppoe-server limits

help: Limits the connection rate from a single source

.. cfg_cmd:: service pppoe-server limits burst

help: Burst count

.. cfg_cmd:: service pppoe-server limits connection-limit

help: Acceptable rate of connections (e.g. 1/min, 60/sec)

.. cfg_cmd:: service pppoe-server limits timeout

help: Timeout in seconds

.. cfg_cmd:: service pppoe-server max-concurrent-sessions

help: Maximum number of concurrent session start attempts

.. cfg_cmd:: service pppoe-server mtu

help: Maximum Transmission Unit (MTU)
1492


.. cfg_cmd:: service pppoe-server name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service pppoe-server pado-delay <tag>

help: PADO delays

.. cfg_cmd:: service pppoe-server pado-delay <tag> sessions

help: Number of sessions

.. cfg_cmd:: service pppoe-server ppp-options

help: Advanced protocol options

.. cfg_cmd:: service pppoe-server ppp-options disable-ccp

help: Disable Compression Control Protocol (CCP)

.. cfg_cmd:: service pppoe-server ppp-options interface-cache

help: PPP interface cache

.. cfg_cmd:: service pppoe-server ppp-options ipv4

help: IPv4 (IPCP) negotiation algorithm

.. cfg_cmd:: service pppoe-server ppp-options ipv6

help: IPv6 (IPCP6) negotiation algorithm
deny


.. cfg_cmd:: service pppoe-server ppp-options ipv6-accept-peer-interface-id

help: Accept peer interface identifier

.. cfg_cmd:: service pppoe-server ppp-options ipv6-interface-id

help: Fixed or random interface identifier for IPv6

.. cfg_cmd:: service pppoe-server ppp-options ipv6-peer-interface-id

help: Peer interface identifier for IPv6

.. cfg_cmd:: service pppoe-server ppp-options lcp-echo-failure

help: Maximum number of Echo-Requests may be sent without valid reply
3


.. cfg_cmd:: service pppoe-server ppp-options lcp-echo-interval

help: LCP echo-requests/sec
30


.. cfg_cmd:: service pppoe-server ppp-options lcp-echo-timeout

help: Timeout in seconds to wait for any peer activity. If this option specified it turns on adaptive lcp echo functionality and "lcp-echo-failure" is not used.
0


.. cfg_cmd:: service pppoe-server ppp-options min-mtu

help: Minimum acceptable MTU (68-65535)
1280


.. cfg_cmd:: service pppoe-server ppp-options mppe

help: Specifies mppe negotiation preferences
prefer


.. cfg_cmd:: service pppoe-server ppp-options mru

help: Preferred MRU (68-65535)

.. cfg_cmd:: service pppoe-server service-name

help: Service name

.. cfg_cmd:: service pppoe-server session-control

help: control sessions count
replace


.. cfg_cmd:: service pppoe-server shaper

help: Traffic shaper bandwidth parameters

.. cfg_cmd:: service pppoe-server shaper fwmark

help: Firewall mark value for traffic that excludes from shaping

.. cfg_cmd:: service pppoe-server snmp

help: Enable SNMP

.. cfg_cmd:: service pppoe-server snmp master-agent

help: Enable SNMP master agent mode

.. cfg_cmd:: service pppoe-server wins-server

help: Windows Internet Name Service (WINS) servers propagated to client

.. cfg_cmd:: service router-advert

help: IPv6 Router Advertisements (RAs) service

.. cfg_cmd:: service router-advert interface <tag>

help: Interface to send RA on

.. cfg_cmd:: service router-advert interface <tag> default-lifetime

help: Lifetime associated with the default router in units of seconds

.. cfg_cmd:: service router-advert interface <tag> default-preference

help: Preference associated with the default router,
medium


.. cfg_cmd:: service router-advert interface <tag> dnssl

help: DNS search list

.. cfg_cmd:: service router-advert interface <tag> hop-limit

help: Set Hop Count field of the IP header for outgoing packets
64


.. cfg_cmd:: service router-advert interface <tag> interval

help: Set interval between unsolicited multicast RAs

.. cfg_cmd:: service router-advert interface <tag> interval max

help: Maximum interval between unsolicited multicast RAs
600


.. cfg_cmd:: service router-advert interface <tag> interval min

help: Minimum interval between unsolicited multicast RAs

.. cfg_cmd:: service router-advert interface <tag> link-mtu

help: Link MTU value placed in RAs, exluded in RAs if unset

.. cfg_cmd:: service router-advert interface <tag> managed-flag

help: Hosts use the administered (stateful) protocol for address autoconfiguration in addition to any addresses autoconfigured using SLAAC

.. cfg_cmd:: service router-advert interface <tag> name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: service router-advert interface <tag> name-server-lifetime

help: Maximum duration how long the RDNSS entries are used

.. cfg_cmd:: service router-advert interface <tag> nat64prefix <tag>

help: NAT64 prefix included in the router advertisements

.. cfg_cmd:: service router-advert interface <tag> nat64prefix <tag> valid-lifetime

help: Time in seconds that the prefix will remain valid
65528


.. cfg_cmd:: service router-advert interface <tag> no-send-advert

help: Do not send router adverts

.. cfg_cmd:: service router-advert interface <tag> other-config-flag

help: Hosts use the administered (stateful) protocol for autoconfiguration of other (non-address) information

.. cfg_cmd:: service router-advert interface <tag> prefix <tag>

help: IPv6 prefix to be advertised in Router Advertisements (RAs)

.. cfg_cmd:: service router-advert interface <tag> prefix <tag> decrement-lifetime

help: Lifetime is decremented by the number of seconds since the last RA - use in conjunction with a DHCPv6-PD prefix

.. cfg_cmd:: service router-advert interface <tag> prefix <tag> deprecate-prefix

help: Upon shutdown, this option will deprecate the prefix by announcing it in the shutdown RA

.. cfg_cmd:: service router-advert interface <tag> prefix <tag> no-autonomous-flag

help: Prefix can not be used for stateless address auto-configuration

.. cfg_cmd:: service router-advert interface <tag> prefix <tag> no-on-link-flag

help: Prefix can not be used for on-link determination

.. cfg_cmd:: service router-advert interface <tag> prefix <tag> preferred-lifetime

help: Time in seconds that the prefix will remain preferred
14400


.. cfg_cmd:: service router-advert interface <tag> prefix <tag> valid-lifetime

help: Time in seconds that the prefix will remain valid
2592000


.. cfg_cmd:: service router-advert interface <tag> reachable-time

help: Time, in milliseconds, that a node assumes a neighbor is reachable after having received a reachability confirmation
0


.. cfg_cmd:: service router-advert interface <tag> retrans-timer

help: Time in milliseconds between retransmitted Neighbor Solicitation messages
0


.. cfg_cmd:: service router-advert interface <tag> route <tag>

help: IPv6 route to be advertised in Router Advertisements (RAs)

.. cfg_cmd:: service router-advert interface <tag> route <tag> no-remove-route

help: Do not announce this route with a zero second lifetime upon shutdown

.. cfg_cmd:: service router-advert interface <tag> route <tag> route-preference

help: Preference associated with the route,
medium


.. cfg_cmd:: service router-advert interface <tag> route <tag> valid-lifetime

help: Time in seconds that the route will remain valid
1800


.. cfg_cmd:: service router-advert interface <tag> source-address

help: Use IPv6 address as source address. Useful with VRRP.

.. cfg_cmd:: service salt-minion

help: Salt Minion

.. cfg_cmd:: service salt-minion hash

help: Hash used when discovering file on master server (default: sha256)
sha256


.. cfg_cmd:: service salt-minion id

help: Explicitly declare ID for this minion to use (default: hostname)

.. cfg_cmd:: service salt-minion interval

help: Interval in minutes between updates (default: 60)
60


.. cfg_cmd:: service salt-minion master

help: Hostname or IP address of the Salt master server

.. cfg_cmd:: service salt-minion master-key

help: URL with signature of master for auth reply verification

.. cfg_cmd:: service salt-minion source-interface

help: Interface used to establish connection

.. cfg_cmd:: service sla

help: Service level agreement (SLA)

.. cfg_cmd:: service sla owamp-server

help: One-way active measurement protocol (OWAMP) server

.. cfg_cmd:: service sla owamp-server port

help: Port number used by connection
861


.. cfg_cmd:: service sla twamp-server

help: Two-way active measurement protocol (TWAMP) server

.. cfg_cmd:: service sla twamp-server port

help: Port number used by connection
862


.. cfg_cmd:: service snmp

help: Simple Network Management Protocol (SNMP)

.. cfg_cmd:: service snmp community <tag>

help: Community name

.. cfg_cmd:: service snmp community <tag> authorization

help: Authorization type
ro


.. cfg_cmd:: service snmp community <tag> client

help: IP address of SNMP client allowed to contact system

.. cfg_cmd:: service snmp community <tag> network

help: Subnet of SNMP client(s) allowed to contact system
0.0.0.0/0 ::/0


.. cfg_cmd:: service snmp contact

help: Contact information

.. cfg_cmd:: service snmp description

help: Description

.. cfg_cmd:: service snmp listen-address <tag>

help: IP address to listen for incoming SNMP requests

.. cfg_cmd:: service snmp listen-address <tag> port

help: Port number used by connection
161


.. cfg_cmd:: service snmp location

help: Location information

.. cfg_cmd:: service snmp mib

help: Management information base (MIB)

.. cfg_cmd:: service snmp mib interface

help: Sets the interface name prefix to include in the IF-MIB data collection

.. cfg_cmd:: service snmp mib interface-max

help: Sets the maximum number of interfaces included in IF-MIB data collection

.. cfg_cmd:: service snmp oid-enable

help: Enable specific OIDs that by default are disable

.. cfg_cmd:: service snmp protocol

help: Protocol to be used (TCP/UDP)
udp


.. cfg_cmd:: service snmp script-extensions

help: SNMP script extensions

.. cfg_cmd:: service snmp script-extensions extension-name <tag>

help: Extension name

.. cfg_cmd:: service snmp script-extensions extension-name <tag> script

help: Script location and name

.. cfg_cmd:: service snmp smux-peer

help: Register a subtree for SMUX-based processing

.. cfg_cmd:: service snmp trap-source

help: SNMP trap source address

.. cfg_cmd:: service snmp trap-target <tag>

help: Address of trap target

.. cfg_cmd:: service snmp trap-target <tag> community

help: Community used when sending trap information

.. cfg_cmd:: service snmp trap-target <tag> port

help: Port number used by connection
162


.. cfg_cmd:: service snmp v3

help: Simple Network Management Protocol (SNMP) v3

.. cfg_cmd:: service snmp v3 engineid

help: Specifies the EngineID that uniquely identify an agent (e.g. 000000000000000000000002)

.. cfg_cmd:: service snmp v3 group <tag>

help: Specifies the group with name groupname

.. cfg_cmd:: service snmp v3 group <tag> mode

help: Define access permission
ro


.. cfg_cmd:: service snmp v3 group <tag> seclevel

help: Security levels
auth


.. cfg_cmd:: service snmp v3 group <tag> view

help: Defines the name of view

.. cfg_cmd:: service snmp v3 trap-target <tag>

help: Defines SNMP target for inform or traps for IP

.. cfg_cmd:: service snmp v3 trap-target <tag> auth

help: Defines the privacy

.. cfg_cmd:: service snmp v3 trap-target <tag> auth encrypted-password

help: Defines the encrypted key for authentication

.. cfg_cmd:: service snmp v3 trap-target <tag> auth plaintext-password

help: Defines the clear text key for authentication

.. cfg_cmd:: service snmp v3 trap-target <tag> auth type

help: Define used protocol
md5


.. cfg_cmd:: service snmp v3 trap-target <tag> port

help: Port number used by connection
162


.. cfg_cmd:: service snmp v3 trap-target <tag> privacy

help: Defines the privacy

.. cfg_cmd:: service snmp v3 trap-target <tag> privacy encrypted-password

help: Defines the encrypted key for privacy protocol

.. cfg_cmd:: service snmp v3 trap-target <tag> privacy plaintext-password

help: Defines the clear text key for privacy protocol

.. cfg_cmd:: service snmp v3 trap-target <tag> privacy type

help: Defines the protocol for privacy
des


.. cfg_cmd:: service snmp v3 trap-target <tag> protocol

help: Protocol to be used (TCP/UDP)
udp


.. cfg_cmd:: service snmp v3 trap-target <tag> type

help: Specifies the type of notification between inform and trap
inform


.. cfg_cmd:: service snmp v3 trap-target <tag> user

help: Defines username for authentication

.. cfg_cmd:: service snmp v3 user <tag>

help: Specifies the user with name username

.. cfg_cmd:: service snmp v3 user <tag> auth

help: Specifies the auth

.. cfg_cmd:: service snmp v3 user <tag> auth encrypted-password

help: Defines the encrypted key for authentication

.. cfg_cmd:: service snmp v3 user <tag> auth plaintext-password

help: Defines the clear text key for authentication

.. cfg_cmd:: service snmp v3 user <tag> auth type

help: Define used protocol
md5


.. cfg_cmd:: service snmp v3 user <tag> group

help: Specifies group for user name

.. cfg_cmd:: service snmp v3 user <tag> mode

help: Define access permission
ro


.. cfg_cmd:: service snmp v3 user <tag> privacy

help: Defines the privacy

.. cfg_cmd:: service snmp v3 user <tag> privacy encrypted-password

help: Defines the encrypted key for privacy protocol

.. cfg_cmd:: service snmp v3 user <tag> privacy plaintext-password

help: Defines the clear text key for privacy protocol

.. cfg_cmd:: service snmp v3 user <tag> privacy type

help: Defines the protocol for privacy
des


.. cfg_cmd:: service snmp v3 view <tag>

help: Specifies the view with name viewname

.. cfg_cmd:: service snmp v3 view <tag> oid <tag>

help: Specifies the oid

.. cfg_cmd:: service snmp v3 view <tag> oid <tag> exclude

help: Exclude is an optional argument

.. cfg_cmd:: service snmp v3 view <tag> oid <tag> mask

help: Defines a bit-mask that is indicating which subidentifiers of the associated subtree OID should be regarded as significant

.. cfg_cmd:: service snmp vrf

help: VRF instance name

.. cfg_cmd:: service ssh

help: Secure Shell (SSH)

.. cfg_cmd:: service ssh access-control

help: SSH user/group access controls

.. cfg_cmd:: service ssh access-control allow

help: Allow user/group SSH access

.. cfg_cmd:: service ssh access-control allow group

help: Allow members of a group to login

.. cfg_cmd:: service ssh access-control allow user

help: Allow specific users to login

.. cfg_cmd:: service ssh access-control deny

help: Deny user/group SSH access

.. cfg_cmd:: service ssh access-control deny group

help: Allow members of a group to login

.. cfg_cmd:: service ssh access-control deny user

help: Allow specific users to login

.. cfg_cmd:: service ssh ciphers

help: Allowed ciphers

.. cfg_cmd:: service ssh client-keepalive-interval

help: Enable transmission of keepalives from server to client

.. cfg_cmd:: service ssh disable-host-validation

help: Disable IP Address to Hostname lookup

.. cfg_cmd:: service ssh disable-password-authentication

help: Disable password-based authentication

.. cfg_cmd:: service ssh dynamic-protection

help: Allow dynamic protection

.. cfg_cmd:: service ssh dynamic-protection allow-from

help: Always allow inbound connections from these systems

.. cfg_cmd:: service ssh dynamic-protection block-time

help: Block source IP in seconds. Subsequent blocks increase by a factor of 1.5
120


.. cfg_cmd:: service ssh dynamic-protection detect-time

help: Remember source IP in seconds before reset their score
1800


.. cfg_cmd:: service ssh dynamic-protection threshold

help: Block source IP when their cumulative attack score exceeds threshold
30


.. cfg_cmd:: service ssh hostkey-algorithm

help: Allowed host key signature algorithms

.. cfg_cmd:: service ssh key-exchange

help: Allowed key exchange (KEX) algorithms

.. cfg_cmd:: service ssh listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service ssh loglevel

help: Log level
info


.. cfg_cmd:: service ssh mac

help: Allowed message authentication code (MAC) algorithms

.. cfg_cmd:: service ssh port

help: Port for SSH service
22


.. cfg_cmd:: service ssh rekey

help: SSH session rekey limit

.. cfg_cmd:: service ssh rekey data

help: Threshold data in megabytes

.. cfg_cmd:: service ssh rekey time

help: Threshold time in minutes

.. cfg_cmd:: service ssh vrf

help: VRF instance name

.. cfg_cmd:: service tftp-server

help: Trivial File Transfer Protocol (TFTP) server

.. cfg_cmd:: service tftp-server allow-upload

help: Allow TFTP file uploads

.. cfg_cmd:: service tftp-server directory

help: Folder containing files served by TFTP

.. cfg_cmd:: service tftp-server listen-address <tag>

help: Local IP addresses to listen on

.. cfg_cmd:: service tftp-server listen-address <tag> vrf

help: VRF instance name

.. cfg_cmd:: service tftp-server port

help: Port number used by connection
69


.. cfg_cmd:: service upnp

help: Universal Plug and Play (UPnP) service

.. cfg_cmd:: service upnp friendly-name

help: Name of this service

.. cfg_cmd:: service upnp listen

help: Local IP addresses for service to listen on

.. cfg_cmd:: service upnp nat-pmp

help: Enable NAT-PMP support

.. cfg_cmd:: service upnp pcp-lifetime

help: PCP-base lifetime Option

.. cfg_cmd:: service upnp pcp-lifetime max

help: Max lifetime time

.. cfg_cmd:: service upnp pcp-lifetime min

help: Min lifetime time

.. cfg_cmd:: service upnp presentation-url

help: Presentation Url

.. cfg_cmd:: service upnp rule <tag>

help: UPnP Rule

.. cfg_cmd:: service upnp rule <tag> action

help: Actions against the rule (REQUIRE)

.. cfg_cmd:: service upnp rule <tag> disable

help: Disable instance

.. cfg_cmd:: service upnp rule <tag> external-port-range

help: Port range (REQUIRE)

.. cfg_cmd:: service upnp rule <tag> internal-port-range

help: Port range (REQUIRE)

.. cfg_cmd:: service upnp rule <tag> ip

help: The IP to which this rule applies (REQUIRE)

.. cfg_cmd:: service upnp secure-mode

help: Enable Secure Mode

.. cfg_cmd:: service upnp stun

help: Enable STUN probe support (can be used with NAT 1:1 support for WAN interfaces)

.. cfg_cmd:: service upnp stun host

help: The STUN server address

.. cfg_cmd:: service upnp stun port

help: Port number used by connection

.. cfg_cmd:: service upnp wan-interface

help: WAN network interface

.. cfg_cmd:: service upnp wan-ip

help: WAN network IP

.. cfg_cmd:: service webproxy

help: Webproxy service settings

.. cfg_cmd:: service webproxy append-domain

help: Default domain name

.. cfg_cmd:: service webproxy authentication

help: Proxy Authentication Settings

.. cfg_cmd:: service webproxy authentication children

help: Number of authentication helper processes
5


.. cfg_cmd:: service webproxy authentication credentials-ttl

help: Authenticated session time to live in minutes
60


.. cfg_cmd:: service webproxy authentication ldap

help: LDAP authentication settings

.. cfg_cmd:: service webproxy authentication ldap base-dn

help: LDAP Base DN to search

.. cfg_cmd:: service webproxy authentication ldap bind-dn

help: LDAP DN used to bind to server

.. cfg_cmd:: service webproxy authentication ldap filter-expression

help: Filter expression to perform LDAP search with

.. cfg_cmd:: service webproxy authentication ldap password

help: LDAP password to bind with

.. cfg_cmd:: service webproxy authentication ldap persistent-connection

help: Use persistent LDAP connection

.. cfg_cmd:: service webproxy authentication ldap port

help: Port number used by connection
389


.. cfg_cmd:: service webproxy authentication ldap server

help: LDAP server to use

.. cfg_cmd:: service webproxy authentication ldap use-ssl

help: Use SSL/TLS for LDAP connection

.. cfg_cmd:: service webproxy authentication ldap username-attribute

help: LDAP username attribute

.. cfg_cmd:: service webproxy authentication ldap version

help: LDAP protocol version
3


.. cfg_cmd:: service webproxy authentication method

help: Authentication Method

.. cfg_cmd:: service webproxy authentication realm

help: Name of authentication realm (e.g. "My Company proxy server")

.. cfg_cmd:: service webproxy cache-peer <tag>

help: Specify other caches in a hierarchy

.. cfg_cmd:: service webproxy cache-peer <tag> address

help: Hostname or IP address of peer

.. cfg_cmd:: service webproxy cache-peer <tag> http-port

help: Default Proxy Port
3128


.. cfg_cmd:: service webproxy cache-peer <tag> icp-port

help: Cache peer ICP port
0


.. cfg_cmd:: service webproxy cache-peer <tag> options

help: Cache peer options
no-query default


.. cfg_cmd:: service webproxy cache-peer <tag> type

help: Squid peer type (default parent)
parent


.. cfg_cmd:: service webproxy cache-size

help: Disk cache size in MB
100


.. cfg_cmd:: service webproxy default-port

help: Default Proxy Port
3128


.. cfg_cmd:: service webproxy disable-access-log

help: Disable logging of HTTP accesses

.. cfg_cmd:: service webproxy domain-block

help: Domain name to block

.. cfg_cmd:: service webproxy domain-noncache

help: Domain name to access without caching

.. cfg_cmd:: service webproxy listen-address <tag>

help: IPv4 listen-address for WebProxy

.. cfg_cmd:: service webproxy listen-address <tag> disable-transparent

help: Disable transparent mode

.. cfg_cmd:: service webproxy listen-address <tag> port

help: Default Proxy Port

.. cfg_cmd:: service webproxy maximum-object-size

help: Maximum size of object to be stored in cache in kilobytes

.. cfg_cmd:: service webproxy mem-cache-size

help: Memory cache size in MB
20


.. cfg_cmd:: service webproxy minimum-object-size

help: Maximum size of object to be stored in cache in kilobytes

.. cfg_cmd:: service webproxy outgoing-address

help: Outgoing IP address for webproxy

.. cfg_cmd:: service webproxy reply-block-mime

help: MIME type to block

.. cfg_cmd:: service webproxy reply-body-max-size

help: Maximum reply body size in KB

.. cfg_cmd:: service webproxy safe-ports

help: Safe port ACL

.. cfg_cmd:: service webproxy ssl-safe-ports

help: SSL safe port

.. cfg_cmd:: service webproxy url-filtering

help: URL filtering settings

.. cfg_cmd:: service webproxy url-filtering disable

help: Disable instance

.. cfg_cmd:: service webproxy url-filtering squidguard

help: URL filtering via squidGuard redirector

.. cfg_cmd:: service webproxy url-filtering squidguard allow-category

help: Category to allow

.. cfg_cmd:: service webproxy url-filtering squidguard allow-ipaddr-url

help: Allow IP address URLs

.. cfg_cmd:: service webproxy url-filtering squidguard auto-update

help: Auto update settings

.. cfg_cmd:: service webproxy url-filtering squidguard auto-update update-hour

help: Hour of day for database update
0


.. cfg_cmd:: service webproxy url-filtering squidguard block-category

help: Category to block

.. cfg_cmd:: service webproxy url-filtering squidguard default-action

help: Default action (default: allow)

.. cfg_cmd:: service webproxy url-filtering squidguard enable-safe-search

help: Enable safe-mode search on popular search engines

.. cfg_cmd:: service webproxy url-filtering squidguard local-block

help: Local site to block

.. cfg_cmd:: service webproxy url-filtering squidguard local-block-keyword

help: Local keyword to block

.. cfg_cmd:: service webproxy url-filtering squidguard local-block-url

help: Local URL to block

.. cfg_cmd:: service webproxy url-filtering squidguard local-ok

help: Local site to allow

.. cfg_cmd:: service webproxy url-filtering squidguard local-ok-url

help: Local URL to allow

.. cfg_cmd:: service webproxy url-filtering squidguard log

help: Log block category

.. cfg_cmd:: service webproxy url-filtering squidguard redirect-url

help: Redirect URL for filtered websites
block.vyos.net


.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag>

help: URL filter rule for a source-group

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> allow-category

help: Category to allow

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> allow-ipaddr-url

help: Allow IP address URLs

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> block-category

help: Category to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> default-action

help: Default action (default: allow)

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> enable-safe-search

help: Enable safe-mode search on popular search engines

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-block

help: Local site to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-block-keyword

help: Local keyword to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-block-url

help: Local URL to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-ok

help: Local site to allow

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-ok-url

help: Local URL to allow

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> log

help: Log block category

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> redirect-url

help: Redirect URL for filtered websites

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> source-group

help: Source-group for this rule

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> time-period

help: Time-period for this rule

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag>

help: Source group name

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> address

help: Address for source-group

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> description

help: Description

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> domain

help: Domain for source-group

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> ldap-ip-search

help: LDAP search expression for an IP address list

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> ldap-user-search

help: LDAP search expression for a user group

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> user

help: List of user names

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag>

help: Time period name

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag> days <tag>

help: Time-period days

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag> days <tag> time

help: Time for time-period

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag> description

help: Description

