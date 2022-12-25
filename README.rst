opensensemap-api
================

Python Client for interacting with the `openSenseMap <https://opensensemap.org/>`_
API.

This module is not official, developed, supported or endorsed by
`openSenseMap <https://opensensemap.org/>`_

Installation
------------

The module is available from the `Python Package Index <https://pypi.python.org/pypi>`_.

.. code:: bash

    $ pip3 install opensensemap-api

On a Fedora-based system or a CentOS/RHEL machine with EPEL.

.. code:: bash

    $ sudo dnf -y install python3-opensensemap-api

For Nix or NixOS users is a package available. Keep in mind that the lastest releases might only
be present in the ``unstable`` channel.

.. code:: bash

    $ nix-env -iA nixos.python3Packages.opensensemap-api

Usage
-----

The file ``example.py`` contains an example about how to use this module.

License
-------

``opensensemap-api`` is licensed under MIT, for more details check LICENSE.
