.. cfg_cmd:: service monitoring

help: Monitoring services

.. cfg_cmd:: service monitoring telegraf

help: Telegraf metric collector

.. cfg_cmd:: service monitoring telegraf azure-data-explorer

help: Output plugin Azure Data Explorer

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication

help: Authentication parameters

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication client-id

help: Application client id

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication client-secret

help: Application client secret

.. cfg_cmd:: service monitoring telegraf azure-data-explorer authentication tenant-id

help: Set tenant id

.. cfg_cmd:: service monitoring telegraf azure-data-explorer database

help: Remote database name

.. cfg_cmd:: service monitoring telegraf azure-data-explorer group-metrics

help: Type of metrics grouping when push to Azure Data Explorer
table-per-metric


.. cfg_cmd:: service monitoring telegraf azure-data-explorer table

help: Name of the single table [Only if set group-metrics single-table]

.. cfg_cmd:: service monitoring telegraf azure-data-explorer url

help: Remote URL

.. cfg_cmd:: service monitoring telegraf influxdb

help: Output plugin InfluxDB

.. cfg_cmd:: service monitoring telegraf influxdb authentication

help: Authentication parameters

.. cfg_cmd:: service monitoring telegraf influxdb authentication organization

help: Authentication organization for InfluxDB v2

.. cfg_cmd:: service monitoring telegraf influxdb authentication token

help: Authentication token for InfluxDB v2

.. cfg_cmd:: service monitoring telegraf influxdb bucket

help: Remote bucket
main


.. cfg_cmd:: service monitoring telegraf influxdb port

help: Port number used by connection
8086


.. cfg_cmd:: service monitoring telegraf influxdb url

help: Remote URL

.. cfg_cmd:: service monitoring telegraf prometheus-client

help: Output plugin Prometheus client

.. cfg_cmd:: service monitoring telegraf prometheus-client allow-from

help: Networks allowed to query this server

.. cfg_cmd:: service monitoring telegraf prometheus-client authentication

help: HTTP basic authentication parameters

.. cfg_cmd:: service monitoring telegraf prometheus-client authentication password

help: Authentication password

.. cfg_cmd:: service monitoring telegraf prometheus-client authentication username

help: Authentication username

.. cfg_cmd:: service monitoring telegraf prometheus-client listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: service monitoring telegraf prometheus-client metric-version

help: Metric version control mapping from Telegraf to Prometheus format
2


.. cfg_cmd:: service monitoring telegraf prometheus-client port

help: Port number used by connection
9273


.. cfg_cmd:: service monitoring telegraf source

help: Source parameters for monitoring
all


.. cfg_cmd:: service monitoring telegraf splunk

help: Output plugin Splunk

.. cfg_cmd:: service monitoring telegraf splunk authentication

help: HTTP basic authentication parameters

.. cfg_cmd:: service monitoring telegraf splunk authentication insecure

help: Use TLS but skip host validation

.. cfg_cmd:: service monitoring telegraf splunk authentication token

help: Authorization token

.. cfg_cmd:: service monitoring telegraf splunk url

help: Remote URL

.. cfg_cmd:: service monitoring telegraf vrf

help: VRF instance name

.. cfg_cmd:: service monitoring zabbix-agent

help: Zabbix-agent settings

.. cfg_cmd:: service monitoring zabbix-agent directory

help: Folder containing individual Zabbix-agent configuration files

.. cfg_cmd:: service monitoring zabbix-agent host-name

help: Zabbix agent hostname

.. cfg_cmd:: service monitoring zabbix-agent limits

help: Limit settings

.. cfg_cmd:: service monitoring zabbix-agent limits buffer-flush-interval

help: Do not keep data longer than N seconds in buffer
5


.. cfg_cmd:: service monitoring zabbix-agent limits buffer-size

help: Maximum number of values in a memory buffer
100


.. cfg_cmd:: service monitoring zabbix-agent listen-address

help: Local IP addresses to listen on
0.0.0.0


.. cfg_cmd:: service monitoring zabbix-agent log

help: Log settings

.. cfg_cmd:: service monitoring zabbix-agent log debug-level

help: Debug level
warning


.. cfg_cmd:: service monitoring zabbix-agent log remote-commands

help: Enable logging of executed shell commands as warnings

.. cfg_cmd:: service monitoring zabbix-agent log size

help: Log file size in megabytes
0


.. cfg_cmd:: service monitoring zabbix-agent port

help: Port number used by connection
10050


.. cfg_cmd:: service monitoring zabbix-agent server

help: Remote server to connect to

.. cfg_cmd:: service monitoring zabbix-agent server-active <tag>

help: Remote server address to get active checks from

.. cfg_cmd:: service monitoring zabbix-agent server-active <tag> port

help: Port number used by connection

.. cfg_cmd:: service monitoring zabbix-agent timeout

help: Item processing timeout in seconds
3


