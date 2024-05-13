.. cfg_cmd:: protocols pim

help: Protocol Independent Multicast (PIM) and IGMP

.. cfg_cmd:: protocols pim ecmp

help: Enable PIM ECMP

.. cfg_cmd:: protocols pim ecmp rebalance

help: Enable PIM ECMP Rebalance

.. cfg_cmd:: protocols pim igmp

help: Internet Group Management Protocol (IGMP) options

.. cfg_cmd:: protocols pim igmp watermark-warning

help: Configure group limit for watermark warning

.. cfg_cmd:: protocols pim interface <tag>

help: PIM interface

.. cfg_cmd:: protocols pim interface <tag> bfd

help: Enable Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: protocols pim interface <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols pim interface <tag> dr-priority

help: Designated router election priority

.. cfg_cmd:: protocols pim interface <tag> hello

help: Hello Interval

.. cfg_cmd:: protocols pim interface <tag> igmp

help: Internet Group Management Protocol (IGMP) options

.. cfg_cmd:: protocols pim interface <tag> igmp disable

help: Disable instance

.. cfg_cmd:: protocols pim interface <tag> igmp join <tag>

help: IGMP join multicast group

.. cfg_cmd:: protocols pim interface <tag> igmp join <tag> source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: protocols pim interface <tag> igmp query-interval

help: IGMP host query interval

.. cfg_cmd:: protocols pim interface <tag> igmp query-max-response-time

help: IGMP max query response time

.. cfg_cmd:: protocols pim interface <tag> igmp version

help: Interface IGMP version
3


.. cfg_cmd:: protocols pim interface <tag> no-bsm

help: Do not process bootstrap messages

.. cfg_cmd:: protocols pim interface <tag> no-unicast-bsm

help: Do not process unicast bootstrap messages

.. cfg_cmd:: protocols pim interface <tag> passive

help: Disable sending and receiving PIM control packets on the interface

.. cfg_cmd:: protocols pim interface <tag> source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: protocols pim join-prune-interval

help: Join prune send interval
60


.. cfg_cmd:: protocols pim keep-alive-timer

help: Keep alive Timer

.. cfg_cmd:: protocols pim no-v6-secondary

help: Disable IPv6 secondary address in hello packets

.. cfg_cmd:: protocols pim packets

help: Packets to process at once
3


.. cfg_cmd:: protocols pim register-accept-list

help: Only accept registers from a specific source prefix list

.. cfg_cmd:: protocols pim register-accept-list prefix-list

help: Prefix-list to use

.. cfg_cmd:: protocols pim register-suppress-time

help: Register suppress timer

.. cfg_cmd:: protocols pim rp

help: Rendezvous Point

.. cfg_cmd:: protocols pim rp address <tag>

help: Rendezvous Point address

.. cfg_cmd:: protocols pim rp address <tag> group

help: Group Address range

.. cfg_cmd:: protocols pim rp keep-alive-timer

help: Keep alive Timer

.. cfg_cmd:: protocols pim spt-switchover

help: Shortest-path tree (SPT) switchover

.. cfg_cmd:: protocols pim spt-switchover infinity-and-beyond

help: Never switch to SPT Tree

.. cfg_cmd:: protocols pim spt-switchover infinity-and-beyond prefix-list

help: Prefix-list to use

.. cfg_cmd:: protocols pim ssm

help: Source-Specific Multicast

.. cfg_cmd:: protocols pim ssm prefix-list

help: Prefix-list to use

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

