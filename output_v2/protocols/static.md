.. cfg_cmd:: protocols static

help: Static Routing

.. cfg_cmd:: protocols static arp

help: Static ARP translation

.. cfg_cmd:: protocols static arp interface <tag>

help: Interface configuration

.. cfg_cmd:: protocols static arp interface <tag> address <tag>

help: IP address for static ARP entry

.. cfg_cmd:: protocols static arp interface <tag> address <tag> description

help: Description

.. cfg_cmd:: protocols static arp interface <tag> address <tag> mac

help: Media Access Control (MAC) address

.. cfg_cmd:: protocols static multicast

help: Multicast static route

.. cfg_cmd:: protocols static multicast interface-route <tag>

help: Multicast interface based route

.. cfg_cmd:: protocols static multicast interface-route <tag> next-hop-interface <tag>

help: Next-hop interface

.. cfg_cmd:: protocols static multicast interface-route <tag> next-hop-interface <tag> distance

help: Distance value for this route

.. cfg_cmd:: protocols static multicast route <tag>

help: Configure static unicast route into MRIB for multicast RPF lookup

.. cfg_cmd:: protocols static multicast route <tag> next-hop <tag>

help: Nexthop IPv4 address

.. cfg_cmd:: protocols static multicast route <tag> next-hop <tag> distance

help: Distance value for this route

.. cfg_cmd:: protocols static neighbor-proxy

help: Neighbor proxy parameters

.. cfg_cmd:: protocols static neighbor-proxy arp <tag>

help: IP address for selective ARP proxy

.. cfg_cmd:: protocols static neighbor-proxy arp <tag> interface

help: Interface to use

.. cfg_cmd:: protocols static neighbor-proxy nd <tag>

help: IPv6 address for selective NDP proxy

.. cfg_cmd:: protocols static neighbor-proxy nd <tag> interface

help: Interface to use

.. cfg_cmd:: protocols static route <tag>

help: Static IPv4 route

.. cfg_cmd:: protocols static route <tag> blackhole

help: Silently discard pkts when matched

.. cfg_cmd:: protocols static route <tag> blackhole distance

help: Distance for this route

.. cfg_cmd:: protocols static route <tag> blackhole tag

help: Tag value for this route

.. cfg_cmd:: protocols static route <tag> description

help: Description

.. cfg_cmd:: protocols static route <tag> dhcp-interface

help: DHCP interface supplying next-hop IP address

.. cfg_cmd:: protocols static route <tag> interface <tag>

help: Next-hop IPv4 router interface

.. cfg_cmd:: protocols static route <tag> interface <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static route <tag> interface <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static route <tag> interface <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static route <tag> next-hop <tag>

help: Next-hop IPv4 router address

.. cfg_cmd:: protocols static route <tag> next-hop <tag> bfd

help: BFD monitoring

.. cfg_cmd:: protocols static route <tag> next-hop <tag> bfd multi-hop

help: Use BFD multi hop session

.. cfg_cmd:: protocols static route <tag> next-hop <tag> bfd multi-hop source <tag>

help: Use source for BFD session

.. cfg_cmd:: protocols static route <tag> next-hop <tag> bfd multi-hop source <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static route <tag> next-hop <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static route <tag> next-hop <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static route <tag> next-hop <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static route <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: protocols static route <tag> next-hop <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static route <tag> reject

help: Emit an ICMP unreachable when matched

.. cfg_cmd:: protocols static route <tag> reject distance

help: Distance for this route

.. cfg_cmd:: protocols static route <tag> reject tag

help: Tag value for this route

.. cfg_cmd:: protocols static route-map

help: Specify route-map name to use

.. cfg_cmd:: protocols static route6 <tag>

help: Static IPv6 route

.. cfg_cmd:: protocols static route6 <tag> blackhole

help: Silently discard pkts when matched

.. cfg_cmd:: protocols static route6 <tag> blackhole distance

help: Distance for this route

.. cfg_cmd:: protocols static route6 <tag> blackhole tag

help: Tag value for this route

.. cfg_cmd:: protocols static route6 <tag> description

help: Description

.. cfg_cmd:: protocols static route6 <tag> interface <tag>

help: IPv6 gateway interface name

.. cfg_cmd:: protocols static route6 <tag> interface <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static route6 <tag> interface <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static route6 <tag> interface <tag> segments

help: SRv6 segments

.. cfg_cmd:: protocols static route6 <tag> interface <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag>

help: IPv6 gateway address

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> bfd

help: BFD monitoring

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> bfd multi-hop

help: Use BFD multi hop session

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> bfd multi-hop source <tag>

help: Use source for BFD session

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> bfd multi-hop source <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> segments

help: SRv6 segments

.. cfg_cmd:: protocols static route6 <tag> next-hop <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static route6 <tag> reject

help: Emit an ICMP unreachable when matched

.. cfg_cmd:: protocols static route6 <tag> reject distance

help: Distance for this route

.. cfg_cmd:: protocols static route6 <tag> reject tag

help: Tag value for this route

.. cfg_cmd:: protocols static table <tag>

help: Policy route table number

.. cfg_cmd:: protocols static table <tag> description

help: Description

.. cfg_cmd:: protocols static table <tag> route <tag>

help: Static IPv4 route

.. cfg_cmd:: protocols static table <tag> route <tag> blackhole

help: Silently discard pkts when matched

.. cfg_cmd:: protocols static table <tag> route <tag> blackhole distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route <tag> blackhole tag

help: Tag value for this route

.. cfg_cmd:: protocols static table <tag> route <tag> description

help: Description

.. cfg_cmd:: protocols static table <tag> route <tag> dhcp-interface

help: DHCP interface supplying next-hop IP address

.. cfg_cmd:: protocols static table <tag> route <tag> interface <tag>

help: Next-hop IPv4 router interface

.. cfg_cmd:: protocols static table <tag> route <tag> interface <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static table <tag> route <tag> interface <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route <tag> interface <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag>

help: Next-hop IPv4 router address

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> bfd

help: BFD monitoring

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> bfd multi-hop

help: Use BFD multi hop session

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> bfd multi-hop source <tag>

help: Use source for BFD session

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> bfd multi-hop source <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: protocols static table <tag> route <tag> next-hop <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static table <tag> route <tag> reject

help: Emit an ICMP unreachable when matched

.. cfg_cmd:: protocols static table <tag> route <tag> reject distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route <tag> reject tag

help: Tag value for this route

.. cfg_cmd:: protocols static table <tag> route6 <tag>

help: Static IPv6 route

.. cfg_cmd:: protocols static table <tag> route6 <tag> blackhole

help: Silently discard pkts when matched

.. cfg_cmd:: protocols static table <tag> route6 <tag> blackhole distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route6 <tag> blackhole tag

help: Tag value for this route

.. cfg_cmd:: protocols static table <tag> route6 <tag> description

help: Description

.. cfg_cmd:: protocols static table <tag> route6 <tag> interface <tag>

help: IPv6 gateway interface name

.. cfg_cmd:: protocols static table <tag> route6 <tag> interface <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static table <tag> route6 <tag> interface <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route6 <tag> interface <tag> segments

help: SRv6 segments

.. cfg_cmd:: protocols static table <tag> route6 <tag> interface <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag>

help: IPv6 gateway address

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> bfd

help: BFD monitoring

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> bfd multi-hop

help: Use BFD multi hop session

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> bfd multi-hop source <tag>

help: Use source for BFD session

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> bfd multi-hop source <tag> profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> bfd profile

help: Use settings from BFD profile

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> disable

help: Disable instance

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> interface

help: Gateway interface name

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> segments

help: SRv6 segments

.. cfg_cmd:: protocols static table <tag> route6 <tag> next-hop <tag> vrf

help: VRF to leak route

.. cfg_cmd:: protocols static table <tag> route6 <tag> reject

help: Emit an ICMP unreachable when matched

.. cfg_cmd:: protocols static table <tag> route6 <tag> reject distance

help: Distance for this route

.. cfg_cmd:: protocols static table <tag> route6 <tag> reject tag

help: Tag value for this route

