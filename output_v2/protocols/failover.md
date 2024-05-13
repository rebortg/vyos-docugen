.. cfg_cmd:: protocols failover

help: Failover Routing

.. cfg_cmd:: protocols failover route <tag>

help: Failover IPv4 route

.. cfg_cmd:: protocols failover route <tag> next-hop <tag>

help: Next-hop IPv4 router address

.. cfg_cmd:: protocols failover route <tag> next-hop <tag> check

help: Check target options

.. cfg_cmd:: protocols failover route <tag> next-hop <tag> check policy

help: Policy for check targets
any-available


.. cfg_cmd:: protocols failover route <tag> next-hop <tag> check port

help: Port number used by connection

.. cfg_cmd:: protocols failover route <tag> next-hop <tag> check target

help: Check target address

.. cfg_cmd:: protocols failover route <tag> next-hop <tag> check timeout

help: Timeout between checks
10


.. cfg_cmd:: protocols failover route <tag> next-hop <tag> check type

help: Check type
icmp


.. cfg_cmd:: protocols failover route <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: protocols failover route <tag> next-hop <tag> metric

help: Route metric for this gateway
1


