# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Stages(API):
    _endpoint = 'stages'

    def add_contact(self, obj_id, contact_id):
        """
        Add a contact to the stage

        :param obj_id: int Stage ID
        :param contact_id: int Contact ID
        :return: dict|str
        """
        response = self._client.session.post(
            '{url}/{id}/contact/add/{contact_id}'.format(
                url=self.endpoint_url, id=obj_id, contact_id=contact_id
            )
        )
        return self.process_response(response)

    def remove_contact(self, obj_id, contact_id):
        """
        Remove a contact from the stage

        :param obj_id: int Stage ID
        :param contact_id: int Contact ID
        :return: dict|str
        """
        response = self._client.session.post(
            '{url}/{id}/contact/remove/{contact_id}'.format(
                url=self.endpoint_url, id=obj_id, contact_id=contact_id
            )
        )
        return self.process_response(response)
