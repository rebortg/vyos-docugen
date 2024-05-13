.. cfg_cmd:: protocols rip

help: Routing Information Protocol (RIP) parameters

.. cfg_cmd:: protocols rip default-distance

help: Administrative distance

.. cfg_cmd:: protocols rip default-information

help: Control distribution of default route

.. cfg_cmd:: protocols rip default-information originate

help: Distribute a default route

.. cfg_cmd:: protocols rip default-metric

help: Metric of redistributed routes

.. cfg_cmd:: protocols rip distribute-list

help: Filter networks in routing updates

.. cfg_cmd:: protocols rip distribute-list access-list

help: Access-list

.. cfg_cmd:: protocols rip distribute-list access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols rip distribute-list access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols rip distribute-list interface <tag>

help: Apply filtering to an interface

.. cfg_cmd:: protocols rip distribute-list interface <tag> access-list

help: Access-list

.. cfg_cmd:: protocols rip distribute-list interface <tag> access-list in

help: Access list to apply to input packets

.. cfg_cmd:: protocols rip distribute-list interface <tag> access-list out

help: Access list to apply to output packets

.. cfg_cmd:: protocols rip distribute-list interface <tag> prefix-list

help: Prefix-list

.. cfg_cmd:: protocols rip distribute-list interface <tag> prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols rip distribute-list interface <tag> prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols rip distribute-list prefix-list

help: Prefix-list

.. cfg_cmd:: protocols rip distribute-list prefix-list in

help: Prefix-list to apply to input packets

.. cfg_cmd:: protocols rip distribute-list prefix-list out

help: Prefix-list to apply to output packets

.. cfg_cmd:: protocols rip interface <tag>

help: No help available

.. cfg_cmd:: protocols rip interface <tag> authentication

help: Authentication

.. cfg_cmd:: protocols rip interface <tag> authentication md5 <tag>

help: MD5 key id

.. cfg_cmd:: protocols rip interface <tag> authentication md5 <tag> password

help: Authentication password

.. cfg_cmd:: protocols rip interface <tag> authentication plaintext-password

help: Plain text password

.. cfg_cmd:: protocols rip interface <tag> receive

help: Advertisement reception

.. cfg_cmd:: protocols rip interface <tag> receive version

help: Limit RIP protocol version

.. cfg_cmd:: protocols rip interface <tag> send

help: Advertisement transmission

.. cfg_cmd:: protocols rip interface <tag> send version

help: Limit RIP protocol version

.. cfg_cmd:: protocols rip interface <tag> split-horizon

help: Split horizon parameters

.. cfg_cmd:: protocols rip interface <tag> split-horizon disable

help: Disable instance

.. cfg_cmd:: protocols rip interface <tag> split-horizon poison-reverse

help: Disable split horizon on specified interface

.. cfg_cmd:: protocols rip neighbor

help: Neighbor router

.. cfg_cmd:: protocols rip network

help: RIP network

.. cfg_cmd:: protocols rip network-distance <tag>

help: Source network

.. cfg_cmd:: protocols rip network-distance <tag> access-list

help: Access list

.. cfg_cmd:: protocols rip network-distance <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols rip passive-interface

help: Suppress routing updates on an interface

.. cfg_cmd:: protocols rip redistribute

help: Redistribute information from another routing protocol

.. cfg_cmd:: protocols rip redistribute babel

help: Redistribute Babel routes

.. cfg_cmd:: protocols rip redistribute babel metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute babel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip redistribute bgp

help: Redistribute BGP routes

.. cfg_cmd:: protocols rip redistribute bgp metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute bgp route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip redistribute connected

help: Redistribute connected routes

.. cfg_cmd:: protocols rip redistribute connected metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute connected route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip redistribute isis

help: Redistribute IS-IS routes

.. cfg_cmd:: protocols rip redistribute isis metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute isis route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip redistribute kernel

help: Redistribute kernel routes

.. cfg_cmd:: protocols rip redistribute kernel metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute kernel route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip redistribute ospf

help: Redistribute OSPF routes

.. cfg_cmd:: protocols rip redistribute ospf metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute ospf route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip redistribute static

help: Redistribute static routes

.. cfg_cmd:: protocols rip redistribute static metric

help: Metric for redistributed routes

.. cfg_cmd:: protocols rip redistribute static route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip route

help: RIP static route

.. cfg_cmd:: protocols rip route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols rip timers

help: RIPng timer values

.. cfg_cmd:: protocols rip timers garbage-collection

help: Garbage collection timer
120


.. cfg_cmd:: protocols rip timers timeout

help: Routing information timeout timer
180


.. cfg_cmd:: protocols rip timers update

help: Routing table update timer
30


.. cfg_cmd:: protocols rip version

help: Limit RIP protocol version

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


