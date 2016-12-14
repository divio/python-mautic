# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import os
from tempfile import gettempdir

tmp = os.path.join(gettempdir(), 'mautic_creds.json')


def read_token_tempfile():
    """
    Example of function for getting stored token
    :return: token dict
    """
    with open(tmp, 'r') as f:
        return json.loads(f.read())


def update_token_tempfile(token):
    """
    Example of function for token update
    """
    with open(tmp, 'w') as f:
        f.write(json.dumps(token, indent=4))
