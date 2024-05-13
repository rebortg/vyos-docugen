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

