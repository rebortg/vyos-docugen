.. cfg_cmd:: service webproxy

help: Webproxy service settings

.. cfg_cmd:: service webproxy append-domain

help: Default domain name

.. cfg_cmd:: service webproxy authentication

help: Proxy Authentication Settings

.. cfg_cmd:: service webproxy authentication children

help: Number of authentication helper processes
5


.. cfg_cmd:: service webproxy authentication credentials-ttl

help: Authenticated session time to live in minutes
60


.. cfg_cmd:: service webproxy authentication ldap

help: LDAP authentication settings

.. cfg_cmd:: service webproxy authentication ldap base-dn

help: LDAP Base DN to search

.. cfg_cmd:: service webproxy authentication ldap bind-dn

help: LDAP DN used to bind to server

.. cfg_cmd:: service webproxy authentication ldap filter-expression

help: Filter expression to perform LDAP search with

.. cfg_cmd:: service webproxy authentication ldap password

help: LDAP password to bind with

.. cfg_cmd:: service webproxy authentication ldap persistent-connection

help: Use persistent LDAP connection

.. cfg_cmd:: service webproxy authentication ldap port

help: Port number used by connection
389


.. cfg_cmd:: service webproxy authentication ldap server

help: LDAP server to use

.. cfg_cmd:: service webproxy authentication ldap use-ssl

help: Use SSL/TLS for LDAP connection

.. cfg_cmd:: service webproxy authentication ldap username-attribute

help: LDAP username attribute

.. cfg_cmd:: service webproxy authentication ldap version

help: LDAP protocol version
3


.. cfg_cmd:: service webproxy authentication method

help: Authentication Method

.. cfg_cmd:: service webproxy authentication realm

help: Name of authentication realm (e.g. "My Company proxy server")

.. cfg_cmd:: service webproxy cache-peer <tag>

help: Specify other caches in a hierarchy

.. cfg_cmd:: service webproxy cache-peer <tag> address

help: Hostname or IP address of peer

.. cfg_cmd:: service webproxy cache-peer <tag> http-port

help: Default Proxy Port
3128


.. cfg_cmd:: service webproxy cache-peer <tag> icp-port

help: Cache peer ICP port
0


.. cfg_cmd:: service webproxy cache-peer <tag> options

help: Cache peer options
no-query default


.. cfg_cmd:: service webproxy cache-peer <tag> type

help: Squid peer type (default parent)
parent


.. cfg_cmd:: service webproxy cache-size

help: Disk cache size in MB
100


.. cfg_cmd:: service webproxy default-port

help: Default Proxy Port
3128


.. cfg_cmd:: service webproxy disable-access-log

help: Disable logging of HTTP accesses

.. cfg_cmd:: service webproxy domain-block

help: Domain name to block

.. cfg_cmd:: service webproxy domain-noncache

help: Domain name to access without caching

.. cfg_cmd:: service webproxy listen-address <tag>

help: IPv4 listen-address for WebProxy

.. cfg_cmd:: service webproxy listen-address <tag> disable-transparent

help: Disable transparent mode

.. cfg_cmd:: service webproxy listen-address <tag> port

help: Default Proxy Port

.. cfg_cmd:: service webproxy maximum-object-size

help: Maximum size of object to be stored in cache in kilobytes

.. cfg_cmd:: service webproxy mem-cache-size

help: Memory cache size in MB
20


.. cfg_cmd:: service webproxy minimum-object-size

help: Maximum size of object to be stored in cache in kilobytes

.. cfg_cmd:: service webproxy outgoing-address

help: Outgoing IP address for webproxy

.. cfg_cmd:: service webproxy reply-block-mime

help: MIME type to block

.. cfg_cmd:: service webproxy reply-body-max-size

help: Maximum reply body size in KB

.. cfg_cmd:: service webproxy safe-ports

help: Safe port ACL

.. cfg_cmd:: service webproxy ssl-safe-ports

help: SSL safe port

.. cfg_cmd:: service webproxy url-filtering

help: URL filtering settings

.. cfg_cmd:: service webproxy url-filtering disable

help: Disable instance

.. cfg_cmd:: service webproxy url-filtering squidguard

help: URL filtering via squidGuard redirector

.. cfg_cmd:: service webproxy url-filtering squidguard allow-category

help: Category to allow

.. cfg_cmd:: service webproxy url-filtering squidguard allow-ipaddr-url

help: Allow IP address URLs

.. cfg_cmd:: service webproxy url-filtering squidguard auto-update

help: Auto update settings

.. cfg_cmd:: service webproxy url-filtering squidguard auto-update update-hour

help: Hour of day for database update
0


.. cfg_cmd:: service webproxy url-filtering squidguard block-category

help: Category to block

.. cfg_cmd:: service webproxy url-filtering squidguard default-action

help: Default action (default: allow)

.. cfg_cmd:: service webproxy url-filtering squidguard enable-safe-search

help: Enable safe-mode search on popular search engines

.. cfg_cmd:: service webproxy url-filtering squidguard local-block

help: Local site to block

.. cfg_cmd:: service webproxy url-filtering squidguard local-block-keyword

help: Local keyword to block

.. cfg_cmd:: service webproxy url-filtering squidguard local-block-url

help: Local URL to block

.. cfg_cmd:: service webproxy url-filtering squidguard local-ok

help: Local site to allow

.. cfg_cmd:: service webproxy url-filtering squidguard local-ok-url

help: Local URL to allow

.. cfg_cmd:: service webproxy url-filtering squidguard log

help: Log block category

.. cfg_cmd:: service webproxy url-filtering squidguard redirect-url

help: Redirect URL for filtered websites
block.vyos.net


.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag>

help: URL filter rule for a source-group

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> allow-category

help: Category to allow

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> allow-ipaddr-url

help: Allow IP address URLs

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> block-category

help: Category to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> default-action

help: Default action (default: allow)

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> enable-safe-search

help: Enable safe-mode search on popular search engines

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-block

help: Local site to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-block-keyword

help: Local keyword to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-block-url

help: Local URL to block

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-ok

help: Local site to allow

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> local-ok-url

help: Local URL to allow

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> log

help: Log block category

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> redirect-url

help: Redirect URL for filtered websites

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> source-group

help: Source-group for this rule

.. cfg_cmd:: service webproxy url-filtering squidguard rule <tag> time-period

help: Time-period for this rule

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag>

help: Source group name

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> address

help: Address for source-group

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> description

help: Description

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> domain

help: Domain for source-group

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> ldap-ip-search

help: LDAP search expression for an IP address list

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> ldap-user-search

help: LDAP search expression for a user group

.. cfg_cmd:: service webproxy url-filtering squidguard source-group <tag> user

help: List of user names

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag>

help: Time period name

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag> days <tag>

help: Time-period days

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag> days <tag> time

help: Time for time-period

.. cfg_cmd:: service webproxy url-filtering squidguard time-period <tag> description

help: Description

