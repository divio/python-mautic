# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Notes(API):
    _endpoint = 'notes'
