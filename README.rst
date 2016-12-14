===============================
Mautic Python
===============================

Python wrapper for Mautic API based on `requests-oauthlib <https://github.com/requests/requests-oauthlib>`_

Installation
------------

Clone repo from GitHub_::

    $ git clone https://github.com/divio/python-mautic.git

Then install it by running::

    $ python setup.py install


Quickstart
----------
Put your Mautic API credentials in `apitester/oauth2_app.py`
Run Flask app to get OAuth2 token::

    $ python apitester/oauth2_app.py

This way you'll have `creds.json` in temporary directory. Now you can start using Mautic API:

.. code-block:: python

    >>> from python_mautic import MauticOauth2Client, Contacts
    >>> from python_mautic.utils import read_token_tempfile
    >>> token = read_token_tempfile()
    >>> mautic = MauticOauth2Client(base_url='<base URL>', client_id='<Mautic Public Key>', token=token)
    >>> contacts = Contacts(client=mautic)
    >>> print(contacts.get_list())
