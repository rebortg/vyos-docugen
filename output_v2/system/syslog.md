.. cfg_cmd:: system syslog

help: System logging

.. cfg_cmd:: system syslog console

help: logging to serial console

.. cfg_cmd:: system syslog console facility <tag>

help: Facility for logging

.. cfg_cmd:: system syslog console facility <tag> level

help: Logging level
err


.. cfg_cmd:: system syslog file <tag>

help: Logging to a file

.. cfg_cmd:: system syslog file <tag> archive

help: Log file size and rotation characteristics

.. cfg_cmd:: system syslog file <tag> archive file

help: Number of saved files
5


.. cfg_cmd:: system syslog file <tag> archive size

help: Size of log files in kbytes
256


.. cfg_cmd:: system syslog file <tag> facility <tag>

help: Facility for logging

.. cfg_cmd:: system syslog file <tag> facility <tag> level

help: Logging level
err


.. cfg_cmd:: system syslog global

help: Logging to system standard location

.. cfg_cmd:: system syslog global facility <tag>

help: Facility for logging

.. cfg_cmd:: system syslog global facility <tag> level

help: Logging level
err


.. cfg_cmd:: system syslog global marker

help: mark messages sent to syslog

.. cfg_cmd:: system syslog global marker interval

help: time interval how often a mark message is being sent in seconds
1200


.. cfg_cmd:: system syslog global preserve-fqdn

help: uses FQDN for logging

.. cfg_cmd:: system syslog host <tag>

help: Logging to remote host

.. cfg_cmd:: system syslog host <tag> facility <tag>

help: Facility for logging

.. cfg_cmd:: system syslog host <tag> facility <tag> level

help: Logging level
err


.. cfg_cmd:: system syslog host <tag> format

help: Logging format

.. cfg_cmd:: system syslog host <tag> format octet-counted

help: Allows for the transmission of all characters inside a syslog message

.. cfg_cmd:: system syslog host <tag> port

help: Port number used by connection
514


.. cfg_cmd:: system syslog host <tag> protocol

help: Protocol to be used (TCP/UDP)
udp


.. cfg_cmd:: system syslog user <tag>

help: Logging to specific terminal of given user

.. cfg_cmd:: system syslog user <tag> facility <tag>

help: Facility for logging

.. cfg_cmd:: system syslog user <tag> facility <tag> level

help: Logging level
err


.. cfg_cmd:: system syslog vrf

help: VRF instance name

