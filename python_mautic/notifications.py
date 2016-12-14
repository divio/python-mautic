# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Notifications(API):
    _endpoint = 'notifications'
