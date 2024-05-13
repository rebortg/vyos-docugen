.. cfg_cmd:: policy route6 <tag>

help: Policy route rule set name for IPv6

.. cfg_cmd:: policy route6 <tag> default-log

help: Log packets hitting default-action

.. cfg_cmd:: policy route6 <tag> description

help: Description

.. cfg_cmd:: policy route6 <tag> interface

help: Interface to use

.. cfg_cmd:: policy route6 <tag> rule <tag>

help: Policy rule number

.. cfg_cmd:: policy route6 <tag> rule <tag> action

help: Rule action

.. cfg_cmd:: policy route6 <tag> rule <tag> connection-mark

help: Connection mark

.. cfg_cmd:: policy route6 <tag> rule <tag> description

help: Description

.. cfg_cmd:: policy route6 <tag> rule <tag> destination

help: Destination parameters

.. cfg_cmd:: policy route6 <tag> rule <tag> destination address

help: IP address, subnet, or range

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group

help: Group

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group address-group

help: Group of addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group domain-group

help: Group of domains

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group mac-group

help: Group of MAC addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group network-group

help: Group of networks

.. cfg_cmd:: policy route6 <tag> rule <tag> destination group port-group

help: Group of ports

.. cfg_cmd:: policy route6 <tag> rule <tag> destination port

help: Port

.. cfg_cmd:: policy route6 <tag> rule <tag> disable

help: Disable instance

.. cfg_cmd:: policy route6 <tag> rule <tag> dscp

help: DSCP value

.. cfg_cmd:: policy route6 <tag> rule <tag> dscp-exclude

help: DSCP value not to match

.. cfg_cmd:: policy route6 <tag> rule <tag> fragment

help: IP fragment match

.. cfg_cmd:: policy route6 <tag> rule <tag> fragment match-frag

help: Second and further fragments of fragmented packets

.. cfg_cmd:: policy route6 <tag> rule <tag> fragment match-non-frag

help: Head fragments or unfragmented packets

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit

help: Hop limit

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit eq

help: Match on equal value

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit gt

help: Match on greater then value

.. cfg_cmd:: policy route6 <tag> rule <tag> hop-limit lt

help: Match on less then value

.. cfg_cmd:: policy route6 <tag> rule <tag> icmpv6

help: ICMPv6 type and code information

.. cfg_cmd:: policy route6 <tag> rule <tag> icmpv6 type

help: ICMP type-name

.. cfg_cmd:: policy route6 <tag> rule <tag> ipsec

help: Inbound IPsec packets

.. cfg_cmd:: policy route6 <tag> rule <tag> ipsec match-ipsec

help: Inbound IPsec packets

.. cfg_cmd:: policy route6 <tag> rule <tag> ipsec match-none

help: Inbound non-IPsec packets

.. cfg_cmd:: policy route6 <tag> rule <tag> limit

help: Rate limit using a token bucket filter

.. cfg_cmd:: policy route6 <tag> rule <tag> limit burst

help: Maximum number of packets to allow in excess of rate

.. cfg_cmd:: policy route6 <tag> rule <tag> limit rate

help: Maximum average matching rate

.. cfg_cmd:: policy route6 <tag> rule <tag> log

help: Log packets hitting this rule

.. cfg_cmd:: policy route6 <tag> rule <tag> mark

help: Firewall mark

.. cfg_cmd:: policy route6 <tag> rule <tag> packet-length

help: Payload size in bytes, including header and data to match

.. cfg_cmd:: policy route6 <tag> rule <tag> packet-length-exclude

help: Payload size in bytes, including header and data not to match

.. cfg_cmd:: policy route6 <tag> rule <tag> packet-type

help: Packet type

.. cfg_cmd:: policy route6 <tag> rule <tag> protocol

help: Protocol to match (protocol name, number, or "all")
all


.. cfg_cmd:: policy route6 <tag> rule <tag> recent

help: Parameters for matching recently seen sources

.. cfg_cmd:: policy route6 <tag> rule <tag> recent count

help: Source addresses seen more than N times

.. cfg_cmd:: policy route6 <tag> rule <tag> recent time

help: Source addresses seen in the last N seconds

.. cfg_cmd:: policy route6 <tag> rule <tag> set

help: Packet modifications

.. cfg_cmd:: policy route6 <tag> rule <tag> set connection-mark

help: Connection marking

.. cfg_cmd:: policy route6 <tag> rule <tag> set dscp

help: Packet Differentiated Services Codepoint (DSCP)

.. cfg_cmd:: policy route6 <tag> rule <tag> set mark

help: Packet marking

.. cfg_cmd:: policy route6 <tag> rule <tag> set table

help: Routing table to forward packet with

.. cfg_cmd:: policy route6 <tag> rule <tag> set tcp-mss

help: TCP Maximum Segment Size

.. cfg_cmd:: policy route6 <tag> rule <tag> source

help: Source parameters

.. cfg_cmd:: policy route6 <tag> rule <tag> source address

help: IP address, subnet, or range

.. cfg_cmd:: policy route6 <tag> rule <tag> source group

help: Group

.. cfg_cmd:: policy route6 <tag> rule <tag> source group address-group

help: Group of addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> source group domain-group

help: Group of domains

.. cfg_cmd:: policy route6 <tag> rule <tag> source group mac-group

help: Group of MAC addresses

.. cfg_cmd:: policy route6 <tag> rule <tag> source group network-group

help: Group of networks

.. cfg_cmd:: policy route6 <tag> rule <tag> source group port-group

help: Group of ports

.. cfg_cmd:: policy route6 <tag> rule <tag> source mac-address

help: MAC address

.. cfg_cmd:: policy route6 <tag> rule <tag> source port

help: Port

.. cfg_cmd:: policy route6 <tag> rule <tag> state

help: Session state

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp

help: TCP options to match

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags

help: TCP flags to match

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags ack

help: Acknowledge flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags cwr

help: Congestion Window Reduced flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags ecn

help: Explicit Congestion Notification flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags fin

help: Finish flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not

help: Match flags not set

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not ack

help: Acknowledge flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not cwr

help: Congestion Window Reduced flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not ecn

help: Explicit Congestion Notification flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not fin

help: Finish flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not psh

help: Push flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not rst

help: Reset flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not syn

help: Synchronise flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags not urg

help: Urgent flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags psh

help: Push flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags rst

help: Reset flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags syn

help: Synchronise flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp flags urg

help: Urgent flag

.. cfg_cmd:: policy route6 <tag> rule <tag> tcp mss

help: Maximum segment size (MSS)

.. cfg_cmd:: policy route6 <tag> rule <tag> time

help: Time to match rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time monthdays

help: Monthdays to match rule on

.. cfg_cmd:: policy route6 <tag> rule <tag> time startdate

help: Date to start matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time starttime

help: Time of day to start matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time stopdate

help: Date to stop matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time stoptime

help: Time of day to stop matching rule

.. cfg_cmd:: policy route6 <tag> rule <tag> time utc

help: Interpret times for startdate, stopdate, starttime and stoptime to be UTC

.. cfg_cmd:: policy route6 <tag> rule <tag> time weekdays

help: Weekdays to match rule on

