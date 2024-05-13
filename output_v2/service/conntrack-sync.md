.. cfg_cmd:: service conntrack-sync

help: Connection tracking synchronization

.. cfg_cmd:: service conntrack-sync accept-protocol

help: Protocols for which local conntrack entries will be synced

.. cfg_cmd:: service conntrack-sync disable-external-cache

help: Directly injects the flow-states into the in-kernel Connection Tracking System of the backup firewall.

.. cfg_cmd:: service conntrack-sync disable-syslog

help: Disable connection logging via Syslog

.. cfg_cmd:: service conntrack-sync event-listen-queue-size

help: Queue size for local conntrack events
8


.. cfg_cmd:: service conntrack-sync expect-sync

help: Protocol for which expect entries need to be synchronized

.. cfg_cmd:: service conntrack-sync failover-mechanism

help: Failover mechanism to use for conntrack-sync

.. cfg_cmd:: service conntrack-sync failover-mechanism vrrp

help: VRRP as failover-mechanism to use for conntrack-sync

.. cfg_cmd:: service conntrack-sync failover-mechanism vrrp sync-group

help: VRRP sync group

.. cfg_cmd:: service conntrack-sync ignore-address

help: IP addresses for which local conntrack entries will not be synced

.. cfg_cmd:: service conntrack-sync interface <tag>

help: Interface to use for syncing conntrack entries

.. cfg_cmd:: service conntrack-sync interface <tag> peer

help: IP address of the peer to send the UDP conntrack info too. This disable multicast.

.. cfg_cmd:: service conntrack-sync interface <tag> port

help: Port number used by connection

.. cfg_cmd:: service conntrack-sync listen-address

help: Local IPv4 addresses to listen on

.. cfg_cmd:: service conntrack-sync mcast-group

help: Multicast group to use for syncing conntrack entries
225.0.0.50


.. cfg_cmd:: service conntrack-sync sync-queue-size

help: Queue size for syncing conntrack entries
1


