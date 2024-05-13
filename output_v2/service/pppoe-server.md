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

