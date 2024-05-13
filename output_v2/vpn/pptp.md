.. cfg_cmd:: vpn pptp

help: Point to Point Tunneling Protocol (PPTP) Virtual Private Network (VPN)

.. cfg_cmd:: vpn pptp remote-access

help: Remote access PPTP VPN

.. cfg_cmd:: vpn pptp remote-access authentication

help: Authentication for remote access PPTP VPN

.. cfg_cmd:: vpn pptp remote-access authentication local-users

help: Local user authentication for PPPoE server

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag>

help: User name for authentication

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> disable

help: Disable instance

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> password

help: Password for authentication

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> rate-limit download

help: Download bandwidth limit in kbits/sec

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> rate-limit upload

help: Upload bandwidth limit in kbits/sec

.. cfg_cmd:: vpn pptp remote-access authentication local-users username <tag> static-ip

help: Static client IP address
*


.. cfg_cmd:: vpn pptp remote-access authentication mode

help: Authentication mode used by this server
local


.. cfg_cmd:: vpn pptp remote-access authentication protocols

help: Authentication protocol for remote access peer
pap chap mschap mschap-v2


.. cfg_cmd:: vpn pptp remote-access authentication radius

help: RADIUS based user authentication

.. cfg_cmd:: vpn pptp remote-access authentication radius accounting-interim-interval

help: Interval in seconds to send accounting information

.. cfg_cmd:: vpn pptp remote-access authentication radius acct-interim-jitter

help: Maximum jitter value in seconds to be applied to accounting information interval

.. cfg_cmd:: vpn pptp remote-access authentication radius acct-timeout

help: Timeout for Interim-Update packets, terminate session afterwards
3


.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author

help: Dynamic Authorization Extension/Change of Authorization server

.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author key

help: Shared secret for Dynamic Authorization Extension server

.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author port

help: Port for Dynamic Authorization Extension server (DM/CoA)
1700


.. cfg_cmd:: vpn pptp remote-access authentication radius dynamic-author server

help: IP address for Dynamic Authorization Extension server (DM/CoA)

.. cfg_cmd:: vpn pptp remote-access authentication radius max-try

help: Number of tries to send Access-Request/Accounting-Request queries
3


.. cfg_cmd:: vpn pptp remote-access authentication radius nas-identifier

help: NAS-Identifier attribute sent to RADIUS

.. cfg_cmd:: vpn pptp remote-access authentication radius nas-ip-address

help: NAS-IP-Address attribute sent to RADIUS

.. cfg_cmd:: vpn pptp remote-access authentication radius preallocate-vif

help: Enable attribute NAS-Port-Id in Access-Request

.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit

help: Upload/Download speed limits

.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit attribute

help: RADIUS attribute that contains rate information
Filter-Id


.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit enable

help: Enable bandwidth shaping via RADIUS

.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit multiplier

help: Shaper multiplier
1


.. cfg_cmd:: vpn pptp remote-access authentication radius rate-limit vendor

help: Vendor dictionary

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag>

help: No help available

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> acct-port

help: Accounting port
1813


.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> disable

help: Disable instance

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> disable-accounting

help: Disable accounting

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> fail-time

help: Mark server unavailable for <n> seconds on failure
0


.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> key

help: Shared secret key

.. cfg_cmd:: vpn pptp remote-access authentication radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: vpn pptp remote-access authentication radius source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: vpn pptp remote-access authentication radius timeout

help: Timeout in seconds to wait response from RADIUS server
3


.. cfg_cmd:: vpn pptp remote-access client-ip-pool <tag>

help: Client IP pool

.. cfg_cmd:: vpn pptp remote-access client-ip-pool <tag> next-pool

help: Next pool name

.. cfg_cmd:: vpn pptp remote-access client-ip-pool <tag> range

help: Range of IP addresses

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag>

help: Pool of client IPv6 addresses

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> delegate <tag>

help: Subnet used to delegate prefix through DHCPv6-PD (RFC3633)

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> delegate <tag> delegation-prefix

help: Prefix length delegated to client

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> prefix <tag>

help: Pool of addresses used to assign to clients

.. cfg_cmd:: vpn pptp remote-access client-ipv6-pool <tag> prefix <tag> mask

help: Prefix length used for individual client
64


.. cfg_cmd:: vpn pptp remote-access default-ipv6-pool

help: Default client IPv6 pool name

.. cfg_cmd:: vpn pptp remote-access default-pool

help: Default client IP pool name

.. cfg_cmd:: vpn pptp remote-access description

help: Description

.. cfg_cmd:: vpn pptp remote-access extended-scripts

help: Extended script execution

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-change

help: Script to run when session interface changed by RADIUS CoA handling

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-down

help: Script to run when session interface going to terminate

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-pre-up

help: Script to run before session interface comes up

.. cfg_cmd:: vpn pptp remote-access extended-scripts on-up

help: Script to run when session interface is completely configured and started

.. cfg_cmd:: vpn pptp remote-access gateway-address

help: Gateway IP address

.. cfg_cmd:: vpn pptp remote-access limits

help: Limits the connection rate from a single source

.. cfg_cmd:: vpn pptp remote-access limits burst

help: Burst count

.. cfg_cmd:: vpn pptp remote-access limits connection-limit

help: Acceptable rate of connections (e.g. 1/min, 60/sec)

.. cfg_cmd:: vpn pptp remote-access limits timeout

help: Timeout in seconds

.. cfg_cmd:: vpn pptp remote-access max-concurrent-sessions

help: Maximum number of concurrent session start attempts

.. cfg_cmd:: vpn pptp remote-access mtu

help: Maximum Transmission Unit (MTU)
1436


.. cfg_cmd:: vpn pptp remote-access name-server

help: Domain Name Servers (DNS) addresses

.. cfg_cmd:: vpn pptp remote-access outside-address

help: External IP address to which VPN clients will connect

.. cfg_cmd:: vpn pptp remote-access ppp-options

help: Advanced protocol options

.. cfg_cmd:: vpn pptp remote-access ppp-options disable-ccp

help: Disable Compression Control Protocol (CCP)

.. cfg_cmd:: vpn pptp remote-access ppp-options interface-cache

help: PPP interface cache

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv4

help: IPv4 (IPCP) negotiation algorithm

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6

help: IPv6 (IPCP6) negotiation algorithm
deny


.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6-accept-peer-interface-id

help: Accept peer interface identifier

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6-interface-id

help: Fixed or random interface identifier for IPv6

.. cfg_cmd:: vpn pptp remote-access ppp-options ipv6-peer-interface-id

help: Peer interface identifier for IPv6

.. cfg_cmd:: vpn pptp remote-access ppp-options lcp-echo-failure

help: Maximum number of Echo-Requests may be sent without valid reply
3


.. cfg_cmd:: vpn pptp remote-access ppp-options lcp-echo-interval

help: LCP echo-requests/sec
30


.. cfg_cmd:: vpn pptp remote-access ppp-options lcp-echo-timeout

help: Timeout in seconds to wait for any peer activity. If this option specified it turns on adaptive lcp echo functionality and "lcp-echo-failure" is not used.
0


.. cfg_cmd:: vpn pptp remote-access ppp-options min-mtu

help: Minimum acceptable MTU (68-65535)

.. cfg_cmd:: vpn pptp remote-access ppp-options mppe

help: Specifies mppe negotiation preferences
prefer


.. cfg_cmd:: vpn pptp remote-access ppp-options mru

help: Preferred MRU (68-65535)

.. cfg_cmd:: vpn pptp remote-access shaper

help: Traffic shaper bandwidth parameters

.. cfg_cmd:: vpn pptp remote-access shaper fwmark

help: Firewall mark value for traffic that excludes from shaping

.. cfg_cmd:: vpn pptp remote-access snmp

help: Enable SNMP

.. cfg_cmd:: vpn pptp remote-access snmp master-agent

help: Enable SNMP master agent mode

.. cfg_cmd:: vpn pptp remote-access wins-server

help: Windows Internet Name Service (WINS) servers propagated to client

