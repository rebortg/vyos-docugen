.. cfg_cmd:: service ssh

help: Secure Shell (SSH)

.. cfg_cmd:: service ssh access-control

help: SSH user/group access controls

.. cfg_cmd:: service ssh access-control allow

help: Allow user/group SSH access

.. cfg_cmd:: service ssh access-control allow group

help: Allow members of a group to login

.. cfg_cmd:: service ssh access-control allow user

help: Allow specific users to login

.. cfg_cmd:: service ssh access-control deny

help: Deny user/group SSH access

.. cfg_cmd:: service ssh access-control deny group

help: Allow members of a group to login

.. cfg_cmd:: service ssh access-control deny user

help: Allow specific users to login

.. cfg_cmd:: service ssh ciphers

help: Allowed ciphers

.. cfg_cmd:: service ssh client-keepalive-interval

help: Enable transmission of keepalives from server to client

.. cfg_cmd:: service ssh disable-host-validation

help: Disable IP Address to Hostname lookup

.. cfg_cmd:: service ssh disable-password-authentication

help: Disable password-based authentication

.. cfg_cmd:: service ssh dynamic-protection

help: Allow dynamic protection

.. cfg_cmd:: service ssh dynamic-protection allow-from

help: Always allow inbound connections from these systems

.. cfg_cmd:: service ssh dynamic-protection block-time

help: Block source IP in seconds. Subsequent blocks increase by a factor of 1.5
120


.. cfg_cmd:: service ssh dynamic-protection detect-time

help: Remember source IP in seconds before reset their score
1800


.. cfg_cmd:: service ssh dynamic-protection threshold

help: Block source IP when their cumulative attack score exceeds threshold
30


.. cfg_cmd:: service ssh hostkey-algorithm

help: Allowed host key signature algorithms

.. cfg_cmd:: service ssh key-exchange

help: Allowed key exchange (KEX) algorithms

.. cfg_cmd:: service ssh listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service ssh loglevel

help: Log level
info


.. cfg_cmd:: service ssh mac

help: Allowed message authentication code (MAC) algorithms

.. cfg_cmd:: service ssh port

help: Port for SSH service
22


.. cfg_cmd:: service ssh rekey

help: SSH session rekey limit

.. cfg_cmd:: service ssh rekey data

help: Threshold data in megabytes

.. cfg_cmd:: service ssh rekey time

help: Threshold time in minutes

.. cfg_cmd:: service ssh vrf

help: VRF instance name

