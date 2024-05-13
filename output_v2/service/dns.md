.. cfg_cmd:: service dns

help: Domain Name System (DNS) related services

.. cfg_cmd:: service dns dynamic

help: Dynamic DNS

.. cfg_cmd:: service dns dynamic interval

help: Interval in seconds to wait between Dynamic DNS updates
300


.. cfg_cmd:: service dns dynamic name <tag>

help: Dynamic DNS configuration

.. cfg_cmd:: service dns dynamic name <tag> address

help: Obtain IP address to send Dynamic DNS update for

.. cfg_cmd:: service dns dynamic name <tag> address interface

help: Interface to use

.. cfg_cmd:: service dns dynamic name <tag> address web

help: HTTP(S) web request to use

.. cfg_cmd:: service dns dynamic name <tag> address web skip

help: Pattern to skip from the HTTP(S) respose

.. cfg_cmd:: service dns dynamic name <tag> address web url

help: Remote URL

.. cfg_cmd:: service dns dynamic name <tag> description

help: Description

.. cfg_cmd:: service dns dynamic name <tag> expiry-time

help: Time in seconds for the hostname to be marked expired in cache

.. cfg_cmd:: service dns dynamic name <tag> host-name

help: Hostname to register with Dynamic DNS service

.. cfg_cmd:: service dns dynamic name <tag> ip-version

help: IP address version to use
ipv4


.. cfg_cmd:: service dns dynamic name <tag> key

help: File containing TSIG authentication key for RFC2136 nsupdate on remote DNS server

.. cfg_cmd:: service dns dynamic name <tag> password

help: Password used for authentication

.. cfg_cmd:: service dns dynamic name <tag> protocol

help: ddclient protocol used for Dynamic DNS service

.. cfg_cmd:: service dns dynamic name <tag> server

help: Remote Dynamic DNS server to send updates to

.. cfg_cmd:: service dns dynamic name <tag> ttl

help: Time-to-live (TTL)

.. cfg_cmd:: service dns dynamic name <tag> username

help: Username used for authentication

.. cfg_cmd:: service dns dynamic name <tag> wait-time

help: Time in seconds to wait between update attempts

.. cfg_cmd:: service dns dynamic name <tag> zone

help: DNS zone to be updated

.. cfg_cmd:: service dns dynamic vrf

help: VRF instance name

.. cfg_cmd:: service dns forwarding

help: DNS forwarding

.. cfg_cmd:: service dns forwarding allow-from

help: Networks allowed to query this server

.. cfg_cmd:: service dns forwarding authoritative-domain <tag>

help: Domain to host authoritative records for

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records

help: DNS zone records

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag>

help: A record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag> address

help: IPv4 address

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records a <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag>

help: AAAA record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag> address

help: IPv6 address

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records aaaa <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag>

help: CNAME record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag> target

help: Target DNS name

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records cname <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag>

help: MX record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> server <tag>

help: Mail server

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> server <tag> priority

help: Server priority
10


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records mx <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag>

help: NAPTR record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag>

help: NAPTR rule

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> lookup-a

help: A flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> lookup-srv

help: S flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> order

help: Rule order

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> preference

help: Rule preference
0


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> protocol-specific

help: P flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> regexp

help: Regular expression

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> replacement

help: Replacement DNS name

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> resolve-uri

help: U flag

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> rule <tag> service

help: Service type

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records naptr <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag>

help: NS record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag> target

help: Target DNS server authoritative for subdomain

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ns <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag>

help: PTR record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag> target

help: Target DNS name

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records ptr <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag>

help: SPF record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records spf <tag> value

help: Record contents

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag>

help: SRV record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag>

help: Service entry

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> hostname

help: Server hostname

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> port

help: Port number

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> priority

help: Entry priority
10


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> entry <tag> weight

help: Entry weight
0


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records srv <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag>

help: TXT record

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag> disable

help: Disable instance

.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag> ttl

help: Time-to-live (TTL)
300


.. cfg_cmd:: service dns forwarding authoritative-domain <tag> records txt <tag> value

help: Record contents

.. cfg_cmd:: service dns forwarding cache-size

help: DNS forwarding cache size
10000


.. cfg_cmd:: service dns forwarding dhcp

help: Interfaces whose DHCP client nameservers to forward requests to

.. cfg_cmd:: service dns forwarding dns64-prefix

help: Help to communicate between IPv6-only client and IPv4-only server

.. cfg_cmd:: service dns forwarding dnssec

help: DNSSEC mode
process-no-validate


.. cfg_cmd:: service dns forwarding domain <tag>

help: Domain to forward to a custom DNS server

.. cfg_cmd:: service dns forwarding domain <tag> addnta

help: Add NTA (negative trust anchor) for this domain (must be set if the domain does not support DNSSEC)

.. cfg_cmd:: service dns forwarding domain <tag> name-server <tag>

help: Domain Name Servers (DNS) addresses to forward queries to

.. cfg_cmd:: service dns forwarding domain <tag> name-server <tag> port

help: Port number used by connection
53


.. cfg_cmd:: service dns forwarding domain <tag> recursion-desired

help: Set the "recursion desired" bit in requests to the upstream nameserver

.. cfg_cmd:: service dns forwarding exclude-throttle-address

help: IP address or subnet

.. cfg_cmd:: service dns forwarding ignore-hosts-file

help: Do not use local /etc/hosts file in name resolution

.. cfg_cmd:: service dns forwarding listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service dns forwarding name-server <tag>

help: Domain Name Servers (DNS) addresses to forward queries to

.. cfg_cmd:: service dns forwarding name-server <tag> port

help: Port number used by connection
53


.. cfg_cmd:: service dns forwarding negative-ttl

help: Maximum amount of time negative entries are cached
3600


.. cfg_cmd:: service dns forwarding no-serve-rfc1918

help: Makes the server authoritatively not aware of RFC1918 addresses

.. cfg_cmd:: service dns forwarding options

help: DNS server options

.. cfg_cmd:: service dns forwarding options ecs-add-for

help: Client netmask for which EDNS Client Subnet will be added

.. cfg_cmd:: service dns forwarding options ecs-ipv4-bits

help: Number of bits of IPv4 address to pass for EDNS Client Subnet

.. cfg_cmd:: service dns forwarding options edns-subnet-allow-list

help: Netmask or domain that we should enable EDNS subnet for

.. cfg_cmd:: service dns forwarding port

help: Port number used by connection
53


.. cfg_cmd:: service dns forwarding serve-stale-extension

help: Number of times the expired TTL of a record is extended by 30 seconds when serving stale
0


.. cfg_cmd:: service dns forwarding source-address

help: Source IP address used to initiate connection
0.0.0.0 ::


.. cfg_cmd:: service dns forwarding system

help: Use system name servers

.. cfg_cmd:: service dns forwarding timeout

help: Number of milliseconds to wait for a remote authoritative server to respond
1500


