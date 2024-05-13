.. cfg_cmd:: system login

help: System User Login Configuration

.. cfg_cmd:: system login banner

help: System login banners

.. cfg_cmd:: system login banner post-login

help: A system banner after the user logs in 

.. cfg_cmd:: system login banner pre-login

help: A system banner before the user logs in

.. cfg_cmd:: system login max-login-session

help: Maximum number of all login sessions

.. cfg_cmd:: system login radius

help: RADIUS based user authentication

.. cfg_cmd:: system login radius security-mode

help: Security mode for RADIUS authentication
optional


.. cfg_cmd:: system login radius server <tag>

help: No help available

.. cfg_cmd:: system login radius server <tag> disable

help: Disable instance

.. cfg_cmd:: system login radius server <tag> key

help: Shared secret key

.. cfg_cmd:: system login radius server <tag> port

help: Port number used by connection
1812


.. cfg_cmd:: system login radius server <tag> priority

help: Server priority
255


.. cfg_cmd:: system login radius server <tag> timeout

help: Session timeout
2


.. cfg_cmd:: system login radius source-address

help: Source IP address used to initiate connection

.. cfg_cmd:: system login radius vrf

help: VRF instance name

.. cfg_cmd:: system login tacacs

help: TACACS+ based user authentication

.. cfg_cmd:: system login tacacs security-mode

help: Security mode for TACACS+ authentication
optional


.. cfg_cmd:: system login tacacs server <tag>

help: TACACS+ server configuration

.. cfg_cmd:: system login tacacs server <tag> disable

help: Disable instance

.. cfg_cmd:: system login tacacs server <tag> key

help: Shared secret key

.. cfg_cmd:: system login tacacs server <tag> port

help: Port number used by connection
49


.. cfg_cmd:: system login tacacs source-address

help: IPv4 source address used to initiate connection

.. cfg_cmd:: system login tacacs timeout

help: Session timeout
2


.. cfg_cmd:: system login tacacs vrf

help: VRF instance name

.. cfg_cmd:: system login timeout

help: Session timeout

.. cfg_cmd:: system login user <tag>

help: Local user account information

.. cfg_cmd:: system login user <tag> authentication

help: Authentication settings

.. cfg_cmd:: system login user <tag> authentication encrypted-password

help: Encrypted password
!


.. cfg_cmd:: system login user <tag> authentication otp

help: One-Time-Pad (two-factor) authentication parameters

.. cfg_cmd:: system login user <tag> authentication otp key

help: Key/secret the token algorithm (see RFC4226)

.. cfg_cmd:: system login user <tag> authentication otp rate-limit

help: Limit number of logins (rate-limit) per rate-time
3


.. cfg_cmd:: system login user <tag> authentication otp rate-time

help: Limit number of logins (rate-limit) per rate-time
30


.. cfg_cmd:: system login user <tag> authentication otp window-size

help: Set window of concurrently valid codes
3


.. cfg_cmd:: system login user <tag> authentication plaintext-password

help: Plaintext password used for encryption

.. cfg_cmd:: system login user <tag> authentication public-keys <tag>

help: Remote access public keys

.. cfg_cmd:: system login user <tag> authentication public-keys <tag> key

help: Public key value (Base64 encoded)

.. cfg_cmd:: system login user <tag> authentication public-keys <tag> options

help: Optional public key options

.. cfg_cmd:: system login user <tag> authentication public-keys <tag> type

help: SSH public key type

.. cfg_cmd:: system login user <tag> disable

help: Disable instance

.. cfg_cmd:: system login user <tag> full-name

help: Full name of the user (use quotes for names with spaces)

.. cfg_cmd:: system login user <tag> home-directory

help: Home directory

