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

