# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Reports(API):
    _endpoint = 'reports'

    def create(self, parameters):
        return self.action_not_supported('create')

    def edit(self, obj_id, parameters, create_if_not_exists=False):
        return self.action_not_supported('edit')

    def delete(self, obj_id):
        return self.action_not_supported('delete')
