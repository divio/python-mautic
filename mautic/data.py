# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Data(API):
    _endpoint = 'data'

    def get(self, data_type, options=None):
        """
        Get a single item
        :param data_type: str
        :param options: dict
        :return: dict|str
        """
        if options is None:
            options = {}
        response = self._client.session.get(
            '{url}/{type}'.format(
                url=self.endpoint_url, type=data_type
            ),
            params=options
        )
        return self.process_response(response)
