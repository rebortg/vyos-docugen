.. cfg_cmd:: protocols pim6

help: Protocol Independent Multicast for IPv6 (PIMv6) and MLD

.. cfg_cmd:: protocols pim6 interface <tag>

help: PIMv6 interface

.. cfg_cmd:: protocols pim6 interface <tag> dr-priority

help: Designated router election priority

.. cfg_cmd:: protocols pim6 interface <tag> hello

help: Hello Interval

.. cfg_cmd:: protocols pim6 interface <tag> mld

help: Multicast Listener Discovery (MLD)

.. cfg_cmd:: protocols pim6 interface <tag> mld disable

help: Disable instance

.. cfg_cmd:: protocols pim6 interface <tag> mld interval

help: Query interval

.. cfg_cmd:: protocols pim6 interface <tag> mld join <tag>

help: MLD join multicast group

.. cfg_cmd:: protocols pim6 interface <tag> mld join <tag> source

help: Source address

.. cfg_cmd:: protocols pim6 interface <tag> mld last-member-query-count

help: Last member query count

.. cfg_cmd:: protocols pim6 interface <tag> mld last-member-query-interval

help: Last member query interval

.. cfg_cmd:: protocols pim6 interface <tag> mld max-response-time

help: Max query response time

.. cfg_cmd:: protocols pim6 interface <tag> mld version

help: MLD version
2


.. cfg_cmd:: protocols pim6 interface <tag> no-bsm

help: Do not process bootstrap messages

.. cfg_cmd:: protocols pim6 interface <tag> no-unicast-bsm

help: Do not process unicast bootstrap messages

.. cfg_cmd:: protocols pim6 interface <tag> passive

help: Disable sending and receiving PIM control packets on the interface

.. cfg_cmd:: protocols pim6 join-prune-interval

help: Join prune send interval
60


.. cfg_cmd:: protocols pim6 keep-alive-timer

help: Keep alive Timer

.. cfg_cmd:: protocols pim6 packets

help: Packets to process at once
3


.. cfg_cmd:: protocols pim6 register-suppress-time

help: Register suppress timer

.. cfg_cmd:: protocols pim6 rp

help: Rendezvous Point

.. cfg_cmd:: protocols pim6 rp address <tag>

help: Rendezvous Point address

.. cfg_cmd:: protocols pim6 rp address <tag> group

help: Group Address range

.. cfg_cmd:: protocols pim6 rp address <tag> prefix-list6

help: Prefix-list to use

.. cfg_cmd:: protocols pim6 rp keep-alive-timer

help: Keep alive Timer

