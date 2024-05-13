.. cfg_cmd:: load-balancing wan

help: Configure Wide Area Network (WAN) load-balancing

.. cfg_cmd:: load-balancing wan disable-source-nat

help: Disable source NAT rules from being configured for WAN load balancing

.. cfg_cmd:: load-balancing wan enable-local-traffic

help: Enable WAN load balancing for locally sourced traffic

.. cfg_cmd:: load-balancing wan flush-connections

help: Flush connection tracking tables on connection state change

.. cfg_cmd:: load-balancing wan hook

help: Script to be executed on interface status change

.. cfg_cmd:: load-balancing wan interface-health <tag>

help: Interface name

.. cfg_cmd:: load-balancing wan interface-health <tag> failure-count

help: Failure count
1


.. cfg_cmd:: load-balancing wan interface-health <tag> nexthop

help: Outbound interface nexthop address. Can be 'DHCP or IPv4 address' [REQUIRED]

.. cfg_cmd:: load-balancing wan interface-health <tag> success-count

help: Success count
1


.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag>

help: Rule number

.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> resp-time

help: Ping response time (seconds)
5


.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> target

help: Health target address

.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> test-script

help: Path to user-defined script

.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> ttl-limit

help: TTL limit (hop count)
1


.. cfg_cmd:: load-balancing wan interface-health <tag> test <tag> type

help: WLB test type
ping


.. cfg_cmd:: load-balancing wan rule <tag>

help: Rule number (1-9999)

.. cfg_cmd:: load-balancing wan rule <tag> description

help: Description

.. cfg_cmd:: load-balancing wan rule <tag> destination

help: Destination

.. cfg_cmd:: load-balancing wan rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: load-balancing wan rule <tag> destination port

help: Port number

.. cfg_cmd:: load-balancing wan rule <tag> exclude

help: Exclude packets matching this rule from WAN load balance

.. cfg_cmd:: load-balancing wan rule <tag> failover

help: Enable failover for packets matching this rule from WAN load balance

.. cfg_cmd:: load-balancing wan rule <tag> inbound-interface

help: Inbound interface name (e.g., "eth0") [REQUIRED]

.. cfg_cmd:: load-balancing wan rule <tag> interface <tag>

help: Interface name [REQUIRED]

.. cfg_cmd:: load-balancing wan rule <tag> interface <tag> weight

help: Load-balance weight
1


.. cfg_cmd:: load-balancing wan rule <tag> limit

help: Enable packet limit for this rule

.. cfg_cmd:: load-balancing wan rule <tag> limit burst

help: Burst limit for matching packets
5


.. cfg_cmd:: load-balancing wan rule <tag> limit period

help: Time window for rate calculation
second


.. cfg_cmd:: load-balancing wan rule <tag> limit rate

help: Number of packets used for rate limit
5


.. cfg_cmd:: load-balancing wan rule <tag> limit threshold

help: Threshold behavior for limit
below


.. cfg_cmd:: load-balancing wan rule <tag> per-packet-balancing

help: Option to match traffic per-packet instead of the default, per-flow

.. cfg_cmd:: load-balancing wan rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")
all


.. cfg_cmd:: load-balancing wan rule <tag> source

help: Source information

.. cfg_cmd:: load-balancing wan rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: load-balancing wan rule <tag> source port

help: Port number

.. cfg_cmd:: load-balancing wan sticky-connections

help: Configure sticky connections

.. cfg_cmd:: load-balancing wan sticky-connections inbound

help: Enable sticky incoming WAN connections

