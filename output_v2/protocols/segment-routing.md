.. cfg_cmd:: protocols segment-routing

help: Segment Routing

.. cfg_cmd:: protocols segment-routing interface <tag>

help: Interface specific Segment Routing options

.. cfg_cmd:: protocols segment-routing interface <tag> srv6

help: Accept SR-enabled IPv6 packets on this interface

.. cfg_cmd:: protocols segment-routing interface <tag> srv6 hmac

help: Define HMAC policy for ingress SR-enabled packets on this interface
accept


.. cfg_cmd:: protocols segment-routing srv6

help: Segment-Routing SRv6 configuration

.. cfg_cmd:: protocols segment-routing srv6 locator <tag>

help: Segment Routing SRv6 locator

.. cfg_cmd:: protocols segment-routing srv6 locator <tag> behavior-usid

help: Set SRv6 behavior uSID

.. cfg_cmd:: protocols segment-routing srv6 locator <tag> block-len

help: Configure SRv6 locator block length in bits
40


.. cfg_cmd:: protocols segment-routing srv6 locator <tag> func-bits

help: Configure SRv6 locator function length in bits
16


.. cfg_cmd:: protocols segment-routing srv6 locator <tag> node-len

help: Configure SRv6 locator node length in bits
24


.. cfg_cmd:: protocols segment-routing srv6 locator <tag> prefix

help: SRv6 locator prefix

