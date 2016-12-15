# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Stats(API):
    _endpoint = 'stats'

    def get(self, table='', start=0, limit=0, order=None, where=None):
        """
        Get a list of stat items

        :param table: str database table name
        :param start: int
        :param limit: int
        :param order: list|tuple
        :param where: list|tuple
        :return:
        """
        parameters = {}

        args = ['start', 'limit', 'order', 'where']
        for arg in args:
            if arg in locals() and locals()[arg]:
                parameters[arg] = locals()[arg]

        response = self._client.session.get(
            '{url}/{table}'.format(
                url=self.endpoint_url, table=table
            ),
            params=parameters
        )
        return self.process_response(response)

    def delete(self, obj_id):
        return self.action_not_supported('delete')

    def get_list(
        self,
        search='',
        start=0,
        limit=0,
        order_by='',
        order_by_dir='ASC',
        published_only=False,
        minimal=False
    ):
        return self.action_not_supported('get_list')

    def create(self, parameters):
        return self.action_not_supported('create')

    def get_published_list(
        self, search='', start=0, limit=0, order_by='', order_by_dir='ASC'
    ):
        return self.action_not_supported('get_published_list')

    def edit(self, obj_id, parameters, create_if_not_exists=False):
        return self.action_not_supported('edit')
