# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Emails(API):
    _endpoint = 'emails'

    def send(self, obj_id):
        """
        Send email to the assigned lists

        :param obj_id: int
        :return: dict|str
        """
        response = self._client.session.post(
            '{url}/{id}/send'.format(
                url=self.endpoint_url, id=obj_id
            )
        )
        return self.process_response(response)

    def send_to_contact(self, obj_id, contact_id):
        """
        Send email to a specific contact

        :param obj_id: int
        :param contact_id: int
        :return: dict|str
        """
        response = self._client.session.post(
            '{url}/{id}/send/contact/{contact_id}'.format(
                url=self.endpoint_url, id=obj_id, contact_id=contact_id
            )
        )
        return self.process_response(response)
