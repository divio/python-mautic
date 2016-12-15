# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Points(API):
    _endpoint = 'points'

    def get_point_action_types(self):
        response = self._client.session.get(
            '{url}/actions/types'.format(url=self.endpoint_url)
        )
        return self.process_response(response)
