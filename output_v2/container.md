.. cfg_cmd:: container

help: Container applications

.. cfg_cmd:: container name <tag>

help: Container name

.. cfg_cmd:: container name <tag> allow-host-networks

help: Allow host networks in container

.. cfg_cmd:: container name <tag> arguments

help: The command's arguments for this container

.. cfg_cmd:: container name <tag> cap-add

help: Container capabilities/permissions

.. cfg_cmd:: container name <tag> command

help: Override the default CMD from the image

.. cfg_cmd:: container name <tag> description

help: Description

.. cfg_cmd:: container name <tag> device <tag>

help: Add a host device to the container

.. cfg_cmd:: container name <tag> device <tag> destination

help: Destination container device (Example: "/dev/x")

.. cfg_cmd:: container name <tag> device <tag> source

help: Source device (Example: "/dev/x")

.. cfg_cmd:: container name <tag> disable

help: Disable instance

.. cfg_cmd:: container name <tag> entrypoint

help: Override the default ENTRYPOINT from the image

.. cfg_cmd:: container name <tag> environment <tag>

help: Add custom environment variables

.. cfg_cmd:: container name <tag> environment <tag> value

help: Set environment option value

.. cfg_cmd:: container name <tag> gid

help: Group ID this container will run as

.. cfg_cmd:: container name <tag> host-name

help: Container host name

.. cfg_cmd:: container name <tag> image

help: Container image to use

.. cfg_cmd:: container name <tag> label <tag>

help: Add label variables

.. cfg_cmd:: container name <tag> label <tag> value

help: Set label option value

.. cfg_cmd:: container name <tag> memory

help: Memory (RAM) available to this container
512


.. cfg_cmd:: container name <tag> network <tag>

help: Attach user defined network to container

.. cfg_cmd:: container name <tag> network <tag> address

help: Assign static IP address to container

.. cfg_cmd:: container name <tag> port <tag>

help: Publish port to the container

.. cfg_cmd:: container name <tag> port <tag> destination

help: Destination container port

.. cfg_cmd:: container name <tag> port <tag> listen-address

help: Local IP addresses to listen on

.. cfg_cmd:: container name <tag> port <tag> protocol

help: Transport protocol used for port mapping
tcp


.. cfg_cmd:: container name <tag> port <tag> source

help: Source host port

.. cfg_cmd:: container name <tag> restart

help: Restart options for container
on-failure


.. cfg_cmd:: container name <tag> shared-memory

help: Shared memory available to this container
64


.. cfg_cmd:: container name <tag> uid

help: User ID this container will run as

.. cfg_cmd:: container name <tag> volume <tag>

help: Mount a volume into the container

.. cfg_cmd:: container name <tag> volume <tag> destination

help: Destination container directory

.. cfg_cmd:: container name <tag> volume <tag> mode

help: Volume access mode ro/rw
rw


.. cfg_cmd:: container name <tag> volume <tag> propagation

help: Volume bind propagation
rprivate


.. cfg_cmd:: container name <tag> volume <tag> source

help: Source host directory

.. cfg_cmd:: container network <tag>

help: Network name

.. cfg_cmd:: container network <tag> description

help: Description

.. cfg_cmd:: container network <tag> prefix

help: Prefix which allocated to that network

.. cfg_cmd:: container network <tag> vrf

help: VRF instance name

.. cfg_cmd:: container registry <tag>

help: Registry Name
docker.io quay.io


.. cfg_cmd:: container registry <tag> authentication

help: Authentication settings

.. cfg_cmd:: container registry <tag> authentication password

help: Password used for authentication

.. cfg_cmd:: container registry <tag> authentication username

help: Username used for authentication

.. cfg_cmd:: container registry <tag> disable

help: Disable instance

