.. cfg_cmd:: protocols bfd

help: Bidirectional Forwarding Detection (BFD)

.. cfg_cmd:: protocols bfd peer <tag>

help: Configures BFD peer to listen and talk to

.. cfg_cmd:: protocols bfd peer <tag> echo-mode

help: Enables the echo transmission mode

.. cfg_cmd:: protocols bfd peer <tag> interval

help: Configure timer intervals

.. cfg_cmd:: protocols bfd peer <tag> interval echo-interval

help: Echo receive transmission interval

.. cfg_cmd:: protocols bfd peer <tag> interval multiplier

help: Multiplier to determine packet loss
3


.. cfg_cmd:: protocols bfd peer <tag> interval receive

help: Minimum interval of receiving control packets
300


.. cfg_cmd:: protocols bfd peer <tag> interval transmit

help: Minimum interval of transmitting control packets
300


.. cfg_cmd:: protocols bfd peer <tag> minimum-ttl

help: Expect packets with at least this TTL

.. cfg_cmd:: protocols bfd peer <tag> multihop

help: Allow this BFD peer to not be directly connected

.. cfg_cmd:: protocols bfd peer <tag> passive

help: Do not attempt to start sessions

.. cfg_cmd:: protocols bfd peer <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols bfd peer <tag> shutdown

help: Disable this peer

.. cfg_cmd:: protocols bfd peer <tag> source

help: Bind listener to specified interface/address, mandatory for IPv6

.. cfg_cmd:: protocols bfd peer <tag> source address

help: Local address to bind our peer listener to

.. cfg_cmd:: protocols bfd peer <tag> source interface

help: Interface to use

.. cfg_cmd:: protocols bfd peer <tag> vrf

help: VRF instance name

.. cfg_cmd:: protocols bfd profile <tag>

help: Configure BFD profile used by individual peer

.. cfg_cmd:: protocols bfd profile <tag> echo-mode

help: Enables the echo transmission mode

.. cfg_cmd:: protocols bfd profile <tag> interval

help: Configure timer intervals

.. cfg_cmd:: protocols bfd profile <tag> interval echo-interval

help: Echo receive transmission interval

.. cfg_cmd:: protocols bfd profile <tag> interval multiplier

help: Multiplier to determine packet loss
3


.. cfg_cmd:: protocols bfd profile <tag> interval receive

help: Minimum interval of receiving control packets
300


.. cfg_cmd:: protocols bfd profile <tag> interval transmit

help: Minimum interval of transmitting control packets
300


.. cfg_cmd:: protocols bfd profile <tag> minimum-ttl

help: Expect packets with at least this TTL

.. cfg_cmd:: protocols bfd profile <tag> passive

help: Do not attempt to start sessions

.. cfg_cmd:: protocols bfd profile <tag> shutdown

help: Disable this peer

