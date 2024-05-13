.. cfg_cmd:: service dhcp-relay

help: Host Configuration Protocol (DHCP) relay agent

.. cfg_cmd:: service dhcp-relay disable

help: Disable instance

.. cfg_cmd:: service dhcp-relay interface

help: Interface to use

.. cfg_cmd:: service dhcp-relay listen-interface

help: Interface for DHCP Relay Agent to listen for requests

.. cfg_cmd:: service dhcp-relay relay-options

help: Relay options

.. cfg_cmd:: service dhcp-relay relay-options hop-count

help: Policy to discard packets that have reached specified hop-count
10


.. cfg_cmd:: service dhcp-relay relay-options max-size

help: Maximum packet size to send to a DHCPv4/BOOTP server
576


.. cfg_cmd:: service dhcp-relay relay-options relay-agents-packets

help: Policy to handle incoming DHCPv4 packets which already contain relay agent options
forward


.. cfg_cmd:: service dhcp-relay server

help: DHCP server address

.. cfg_cmd:: service dhcp-relay upstream-interface

help: Interface for DHCP Relay Agent forward requests out

