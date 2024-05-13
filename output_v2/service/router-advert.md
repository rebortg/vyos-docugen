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

