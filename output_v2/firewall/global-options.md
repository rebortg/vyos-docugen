.. cfg_cmd:: firewall global-options

help: Global Options

.. cfg_cmd:: firewall global-options all-ping

help: Policy for handling of all IPv4 ICMP echo requests
enable


.. cfg_cmd:: firewall global-options broadcast-ping

help: Policy for handling broadcast IPv4 ICMP echo and timestamp requests
disable


.. cfg_cmd:: firewall global-options ip-src-route

help: Policy for handling IPv4 packets with source route option
disable


.. cfg_cmd:: firewall global-options ipv6-receive-redirects

help: Policy for handling received ICMPv6 redirect messages
disable


.. cfg_cmd:: firewall global-options ipv6-source-validation

help: Policy for IPv6 source validation by reversed path, as specified in RFC3704
disable


.. cfg_cmd:: firewall global-options ipv6-src-route

help: Policy for handling IPv6 packets with routing extension header
disable


.. cfg_cmd:: firewall global-options log-martians

help: Policy for logging IPv4 packets with invalid addresses
enable


.. cfg_cmd:: firewall global-options receive-redirects

help: Policy for handling received IPv4 ICMP redirect messages
disable


.. cfg_cmd:: firewall global-options resolver-cache

help: Retains last successful value if domain resolution fails

.. cfg_cmd:: firewall global-options resolver-interval

help: Domain resolver update interval
300


.. cfg_cmd:: firewall global-options send-redirects

help: Policy for sending IPv4 ICMP redirect messages
enable


.. cfg_cmd:: firewall global-options source-validation

help: Policy for IPv4 source validation by reversed path, as specified in RFC3704
disable


.. cfg_cmd:: firewall global-options state-policy

help: Global firewall state-policy

.. cfg_cmd:: firewall global-options state-policy established

help: Global firewall policy for packets part of an established connection

.. cfg_cmd:: firewall global-options state-policy established action

help: Action for packets

.. cfg_cmd:: firewall global-options state-policy established log

help: Log packets hitting this rule

.. cfg_cmd:: firewall global-options state-policy established log-level

help: Set log-level. Log must be enable.

.. cfg_cmd:: firewall global-options state-policy invalid

help: Global firewall policy for packets part of an invalid connection

.. cfg_cmd:: firewall global-options state-policy invalid action

help: Action for packets

.. cfg_cmd:: firewall global-options state-policy invalid log

help: Log packets hitting this rule

.. cfg_cmd:: firewall global-options state-policy invalid log-level

help: Set log-level. Log must be enable.

.. cfg_cmd:: firewall global-options state-policy related

help: Global firewall policy for packets part of a related connection

.. cfg_cmd:: firewall global-options state-policy related action

help: Action for packets

.. cfg_cmd:: firewall global-options state-policy related log

help: Log packets hitting this rule

.. cfg_cmd:: firewall global-options state-policy related log-level

help: Set log-level. Log must be enable.

.. cfg_cmd:: firewall global-options syn-cookies

help: Policy for using TCP SYN cookies with IPv4
enable


.. cfg_cmd:: firewall global-options twa-hazards-protection

help: RFC1337 TCP TIME-WAIT assasination hazards protection
disable


