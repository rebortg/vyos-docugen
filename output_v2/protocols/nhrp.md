.. cfg_cmd:: protocols nhrp

help: Next Hop Resolution Protocol (NHRP) parameters

.. cfg_cmd:: protocols nhrp tunnel <tag>

help: Tunnel for NHRP

.. cfg_cmd:: protocols nhrp tunnel <tag> cisco-authentication

help: Pass phrase for cisco authentication

.. cfg_cmd:: protocols nhrp tunnel <tag> dynamic-map <tag>

help: Set an HUB tunnel address

.. cfg_cmd:: protocols nhrp tunnel <tag> dynamic-map <tag> nbma-domain-name

help: Set HUB fqdn (nbma-address - fqdn)

.. cfg_cmd:: protocols nhrp tunnel <tag> holding-time

help: Holding time in seconds

.. cfg_cmd:: protocols nhrp tunnel <tag> map <tag>

help: Set an HUB tunnel address

.. cfg_cmd:: protocols nhrp tunnel <tag> map <tag> cisco

help: If the statically mapped peer is running Cisco IOS, specify this

.. cfg_cmd:: protocols nhrp tunnel <tag> map <tag> nbma-address

help: Set HUB address (nbma-address - external hub address or fqdn)

.. cfg_cmd:: protocols nhrp tunnel <tag> map <tag> register

help: Specifies that Registration Request should be sent to this peer on startup

.. cfg_cmd:: protocols nhrp tunnel <tag> multicast

help: Set multicast for NHRP

.. cfg_cmd:: protocols nhrp tunnel <tag> non-caching

help: This can be used to reduce memory consumption on big NBMA subnets

.. cfg_cmd:: protocols nhrp tunnel <tag> redirect

help: Enable sending of Cisco style NHRP Traffic Indication packets

.. cfg_cmd:: protocols nhrp tunnel <tag> shortcut

help: Enable creation of shortcut routes. A received NHRP Traffic Indication will trigger the resolution and establishment of a shortcut route

.. cfg_cmd:: protocols nhrp tunnel <tag> shortcut-destination

help: This instructs opennhrp to reply with authorative answers on NHRP Resolution Requests destined to addresses in this interface

.. cfg_cmd:: protocols nhrp tunnel <tag> shortcut-target <tag>

help: Defines an off-NBMA network prefix for which the GRE interface will act as a gateway

.. cfg_cmd:: protocols nhrp tunnel <tag> shortcut-target <tag> holding-time

help: Holding time in seconds

