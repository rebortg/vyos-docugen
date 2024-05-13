.. cfg_cmd:: protocols ripng

help: Routing Information Protocol (RIPng) parameters

.. cfg_cmd:: protocols ripng aggregate-address

help: Aggregate RIPng route announcement

.. cfg_cmd:: protocols ripng default-information

help: Control distribution of default route

.. cfg_cmd:: protocols ripng default-information originate

help: Distribute a default route

.. cfg_cmd:: protocols ripng default-metric

help: Metric of redistributed routes

.. cfg_cmd:: protocols ripng distribute-list

help: Filter networks in routing updates

.. cfg_cmd:: protocols ripng distribute-list access-list

help: Access-list

.. cfg_cmd:: protocols ripng distribute-list access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols ripng distribute-list access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols ripng distribute-list interface <tag>

help: Apply filtering to an interface

.. cfg_cmd:: protocols ripng distribute-list interface <tag> access-list

help: Access-list

.. cfg_cmd:: protocols ripng distribute-list interface <tag> access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols ripng distribute-list interface <tag> access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols ripng distribute-list interface <tag> prefix-list

help: Prefix-list

.. cfg_cmd:: protocols ripng distribute-list interface <tag> prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols ripng distribute-list interface <tag> prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols ripng distribute-list prefix-list

help: Prefix-list

.. cfg_cmd:: protocols ripng distribute-list prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols ripng distribute-list prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols ripng interface <tag>

help: Interface name

.. cfg_cmd:: protocols ripng interface <tag> split-horizon

help: Split horizon parameters

.. cfg_cmd:: protocols ripng interface <tag> split-horizon disable

help: Disable instance

.. cfg_cmd:: protocols ripng interface <tag> split-horizon poison-reverse

help: Disable split horizon on specified interface

.. cfg_cmd:: protocols ripng network

help: RIPng network

.. cfg_cmd:: protocols ripng passive-interface

help: Passive interface

.. cfg_cmd:: protocols ripng redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: protocols ripng redistribute babel

help: Redistribute Babel routes

.. cfg_cmd:: protocols ripng redistribute babel metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols ripng redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng redistribute bgp

help: Redistribute BGP routes

.. cfg_cmd:: protocols ripng redistribute bgp metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols ripng redistribute bgp route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng redistribute connected

help: Redistribute connected routes

.. cfg_cmd:: protocols ripng redistribute connected metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols ripng redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng redistribute kernel

help: Redistribute kernel routes

.. cfg_cmd:: protocols ripng redistribute kernel metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols ripng redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng redistribute ospfv3

help: Redistribute OSPFv3 routes

.. cfg_cmd:: protocols ripng redistribute ospfv3 metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols ripng redistribute ospfv3 route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng redistribute static

help: Redistribute static routes

.. cfg_cmd:: protocols ripng redistribute static metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols ripng redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng route

help: RIPng static route

.. cfg_cmd:: protocols ripng route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols ripng timers

help: RIPng timer values

.. cfg_cmd:: protocols ripng timers garbage-collection

help: Garbage collection timer
120


.. cfg_cmd:: protocols ripng timers timeout

help: Routing information timeout timer
180


.. cfg_cmd:: protocols ripng timers update

help: Routing table update timer
30


