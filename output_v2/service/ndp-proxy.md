.. cfg_cmd:: service ndp-proxy

help: Neighbor Discovery Protocol (NDP) Proxy

.. cfg_cmd:: service ndp-proxy interface <tag>

help: NDP proxy listener interface

.. cfg_cmd:: service ndp-proxy interface <tag> disable

help: Disable instance

.. cfg_cmd:: service ndp-proxy interface <tag> enable-router-bit

help: Enable router bit in Neighbor Advertisement messages

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag>

help: Prefix target addresses are matched against

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag> disable

help: Disable instance

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag> interface

help: Interface to forward Neighbor Solicitation message through. Required for "iface" mode

.. cfg_cmd:: service ndp-proxy interface <tag> prefix <tag> mode

help: Specify the running mode of the rule
static


.. cfg_cmd:: service ndp-proxy interface <tag> timeout

help: Timeout for Neighbor Advertisement after Neighbor Solicitation message
500


.. cfg_cmd:: service ndp-proxy interface <tag> ttl

help: Proxy entry cache Time-To-Live
30000


.. cfg_cmd:: service ndp-proxy route-refresh

help: Refresh interval for IPv6 routes
30000


