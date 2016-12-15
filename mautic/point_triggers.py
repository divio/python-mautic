# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class PointTriggers(API):
    _endpoint = 'points/triggers'

    def delete_trigger_events(self, trigger_id, event_ids):
        """
        Remove events from a point trigger

        :param trigger_id: int
        :param event_ids: list|tuple
        :return: dict|str
        """

        response = self._client.session.delete(
            '{url}/{trigger_id}/events/delete'.format(
                url=self.endpoint_url, trigger_id=trigger_id
            ),
            params={'events': event_ids}
        )
        return self.process_response(response)
