.. cfg_cmd:: service snmp

help: Simple Network Management Protocol (SNMP)

.. cfg_cmd:: service snmp community <tag>

help: Community name

.. cfg_cmd:: service snmp community <tag> authorization

help: Authorization type
ro


.. cfg_cmd:: service snmp community <tag> client

help: IP address of SNMP client allowed to contact system

.. cfg_cmd:: service snmp community <tag> network

help: Subnet of SNMP client(s) allowed to contact system
0.0.0.0/0 ::/0


.. cfg_cmd:: service snmp contact

help: Contact information

.. cfg_cmd:: service snmp description

help: Description

.. cfg_cmd:: service snmp listen-address <tag>

help: IP address to listen for incoming SNMP requests

.. cfg_cmd:: service snmp listen-address <tag> port

help: Port number used by connection
161


.. cfg_cmd:: service snmp location

help: Location information

.. cfg_cmd:: service snmp mib

help: Management information base (MIB)

.. cfg_cmd:: service snmp mib interface

help: Sets the interface name prefix to include in the IF-MIB data collection

.. cfg_cmd:: service snmp mib interface-max

help: Sets the maximum number of interfaces included in IF-MIB data collection

.. cfg_cmd:: service snmp oid-enable

help: Enable specific OIDs that by default are disable

.. cfg_cmd:: service snmp protocol

help: Protocol to be used (TCP/UDP)
udp


.. cfg_cmd:: service snmp script-extensions

help: SNMP script extensions

.. cfg_cmd:: service snmp script-extensions extension-name <tag>

help: Extension name

.. cfg_cmd:: service snmp script-extensions extension-name <tag> script

help: Script location and name

.. cfg_cmd:: service snmp smux-peer

help: Register a subtree for SMUX-based processing

.. cfg_cmd:: service snmp trap-source

help: SNMP trap source address

.. cfg_cmd:: service snmp trap-target <tag>

help: Address of trap target

.. cfg_cmd:: service snmp trap-target <tag> community

help: Community used when sending trap information

.. cfg_cmd:: service snmp trap-target <tag> port

help: Port number used by connection
162


.. cfg_cmd:: service snmp v3

help: Simple Network Management Protocol (SNMP) v3

.. cfg_cmd:: service snmp v3 engineid

help: Specifies the EngineID that uniquely identify an agent (e.g. 000000000000000000000002)

.. cfg_cmd:: service snmp v3 group <tag>

help: Specifies the group with name groupname

.. cfg_cmd:: service snmp v3 group <tag> mode

help: Define access permission
ro


.. cfg_cmd:: service snmp v3 group <tag> seclevel

help: Security levels
auth


.. cfg_cmd:: service snmp v3 group <tag> view

help: Defines the name of view

.. cfg_cmd:: service snmp v3 trap-target <tag>

help: Defines SNMP target for inform or traps for IP

.. cfg_cmd:: service snmp v3 trap-target <tag> auth

help: Defines the privacy

.. cfg_cmd:: service snmp v3 trap-target <tag> auth encrypted-password

help: Defines the encrypted key for authentication

.. cfg_cmd:: service snmp v3 trap-target <tag> auth plaintext-password

help: Defines the clear text key for authentication

.. cfg_cmd:: service snmp v3 trap-target <tag> auth type

help: Define used protocol
md5


.. cfg_cmd:: service snmp v3 trap-target <tag> port

help: Port number used by connection
162


.. cfg_cmd:: service snmp v3 trap-target <tag> privacy

help: Defines the privacy

.. cfg_cmd:: service snmp v3 trap-target <tag> privacy encrypted-password

help: Defines the encrypted key for privacy protocol

.. cfg_cmd:: service snmp v3 trap-target <tag> privacy plaintext-password

help: Defines the clear text key for privacy protocol

.. cfg_cmd:: service snmp v3 trap-target <tag> privacy type

help: Defines the protocol for privacy
des


.. cfg_cmd:: service snmp v3 trap-target <tag> protocol

help: Protocol to be used (TCP/UDP)
udp


.. cfg_cmd:: service snmp v3 trap-target <tag> type

help: Specifies the type of notification between inform and trap
inform


.. cfg_cmd:: service snmp v3 trap-target <tag> user

help: Defines username for authentication

.. cfg_cmd:: service snmp v3 user <tag>

help: Specifies the user with name username

.. cfg_cmd:: service snmp v3 user <tag> auth

help: Specifies the auth

.. cfg_cmd:: service snmp v3 user <tag> auth encrypted-password

help: Defines the encrypted key for authentication

.. cfg_cmd:: service snmp v3 user <tag> auth plaintext-password

help: Defines the clear text key for authentication

.. cfg_cmd:: service snmp v3 user <tag> auth type

help: Define used protocol
md5


.. cfg_cmd:: service snmp v3 user <tag> group

help: Specifies group for user name

.. cfg_cmd:: service snmp v3 user <tag> mode

help: Define access permission
ro


.. cfg_cmd:: service snmp v3 user <tag> privacy

help: Defines the privacy

.. cfg_cmd:: service snmp v3 user <tag> privacy encrypted-password

help: Defines the encrypted key for privacy protocol

.. cfg_cmd:: service snmp v3 user <tag> privacy plaintext-password

help: Defines the clear text key for privacy protocol

.. cfg_cmd:: service snmp v3 user <tag> privacy type

help: Defines the protocol for privacy
des


.. cfg_cmd:: service snmp v3 view <tag>

help: Specifies the view with name viewname

.. cfg_cmd:: service snmp v3 view <tag> oid <tag>

help: Specifies the oid

.. cfg_cmd:: service snmp v3 view <tag> oid <tag> exclude

help: Exclude is an optional argument

.. cfg_cmd:: service snmp v3 view <tag> oid <tag> mask

help: Defines a bit-mask that is indicating which subidentifiers of the associated subtree OID should be regarded as significant

.. cfg_cmd:: service snmp vrf

help: VRF instance name

