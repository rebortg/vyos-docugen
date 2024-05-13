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

