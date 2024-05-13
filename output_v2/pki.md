.. cfg_cmd:: pki

help: Public key infrastructure (PKI)

.. cfg_cmd:: pki ca <tag>

help: Certificate Authority

.. cfg_cmd:: pki ca <tag> certificate

help: Certificate in PEM format

.. cfg_cmd:: pki ca <tag> crl

help: Certificate revocation list in PEM format

.. cfg_cmd:: pki ca <tag> description

help: Description

.. cfg_cmd:: pki ca <tag> private

help: CA private key in PEM format

.. cfg_cmd:: pki ca <tag> private key

help: Private key in PEM format

.. cfg_cmd:: pki ca <tag> private password-protected

help: Private key portion is password protected

.. cfg_cmd:: pki ca <tag> revoke

help: Include certificate in parent CRL

.. cfg_cmd:: pki certificate <tag>

help: Certificate

.. cfg_cmd:: pki certificate <tag> acme

help: Automatic Certificate Management Environment (ACME) request

.. cfg_cmd:: pki certificate <tag> acme domain-name

help: Domain Name

.. cfg_cmd:: pki certificate <tag> acme email

help: Email address to associate with certificate

.. cfg_cmd:: pki certificate <tag> acme listen-address

help: Local IPv4 addresses to listen on

.. cfg_cmd:: pki certificate <tag> acme rsa-key-size

help: Size of the RSA key
2048


.. cfg_cmd:: pki certificate <tag> acme url

help: Remote URL
https://acme-v02.api.letsencrypt.org/directory


.. cfg_cmd:: pki certificate <tag> certificate

help: Certificate in PEM format

.. cfg_cmd:: pki certificate <tag> description

help: Description

.. cfg_cmd:: pki certificate <tag> private

help: Certificate private key

.. cfg_cmd:: pki certificate <tag> private key

help: Private key in PEM format

.. cfg_cmd:: pki certificate <tag> private password-protected

help: Private key portion is password protected

.. cfg_cmd:: pki certificate <tag> revoke

help: Include certificate in parent CRL

.. cfg_cmd:: pki dh <tag>

help: Diffie-Hellman parameters

.. cfg_cmd:: pki dh <tag> parameters

help: DH parameters in PEM format

.. cfg_cmd:: pki key-pair <tag>

help: Public and private keys

.. cfg_cmd:: pki key-pair <tag> private

help: Private key

.. cfg_cmd:: pki key-pair <tag> private key

help: Private key in PEM format

.. cfg_cmd:: pki key-pair <tag> private password-protected

help: Private key portion is password protected

.. cfg_cmd:: pki key-pair <tag> public

help: Public key

.. cfg_cmd:: pki key-pair <tag> public key

help: Public key in PEM format

.. cfg_cmd:: pki openssh <tag>

help: OpenSSH public and private keys

.. cfg_cmd:: pki openssh <tag> private

help: Private key

.. cfg_cmd:: pki openssh <tag> private key

help: Private key in PEM format

.. cfg_cmd:: pki openssh <tag> private password-protected

help: Private key portion is password protected

.. cfg_cmd:: pki openssh <tag> public

help: Public key

.. cfg_cmd:: pki openssh <tag> public key

help: Public key in PEM format

.. cfg_cmd:: pki openssh <tag> public type

help: SSH public key type

.. cfg_cmd:: pki openvpn

help: OpenVPN keys

.. cfg_cmd:: pki openvpn shared-secret <tag>

help: OpenVPN shared secret key

.. cfg_cmd:: pki openvpn shared-secret <tag> key

help: OpenVPN shared secret key data

.. cfg_cmd:: pki openvpn shared-secret <tag> version

help: OpenVPN shared secret key version

.. cfg_cmd:: pki x509

help: X509 Settings

.. cfg_cmd:: pki x509 default

help: X509 Default Values

.. cfg_cmd:: pki x509 default country

help: Default country
GB


.. cfg_cmd:: pki x509 default locality

help: Default locality
Some-City


.. cfg_cmd:: pki x509 default organization

help: Default organization
VyOS


.. cfg_cmd:: pki x509 default state

help: Default state
Some-State


