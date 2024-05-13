.. cfg_cmd:: protocols rpki

help: Resource Public Key Infrastructure (RPKI)

.. cfg_cmd:: protocols rpki cache <tag>

help: RPKI cache server address

.. cfg_cmd:: protocols rpki cache <tag> port

help: Port number used by connection

.. cfg_cmd:: protocols rpki cache <tag> preference

help: Preference of the cache server

.. cfg_cmd:: protocols rpki cache <tag> ssh

help: RPKI SSH connection settings

.. cfg_cmd:: protocols rpki cache <tag> ssh key

help: OpenSSH key in PKI configuration

.. cfg_cmd:: protocols rpki cache <tag> ssh username

help: Username used for authentication

.. cfg_cmd:: protocols rpki expire-interval

help: Interval to wait before expiring the cache
7200


.. cfg_cmd:: protocols rpki polling-period

help: Cache polling interval
300


.. cfg_cmd:: protocols rpki retry-interval

help: Retry interval to connect to the cache server
600


