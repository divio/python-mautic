# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Forms(API):
    _endpoint = 'forms'

    def delete_fields(self, form_id, field_ids):
        """
        Remove fields from a form

        :param form_id: int
        :param field_ids: list|tuple
        :return: dict|str
        """

        response = self._client.session.delete(
            '{url}/{form_id}/fields/delete'.format(
                url=self.endpoint_url, form_id=form_id
            ),
            params={'fields': field_ids}
        )
        return self.process_response(response)

    def delete_actions(self, form_id, action_ids):
        """
        Remove actions from a form

        :param form_id: int
        :param action_ids: list|tuple
        :return: dict|str
        """

        response = self._client.session.delete(
            '{url}/{form_id}/actions/delete'.format(
                url=self.endpoint_url, form_id=form_id
            ),
            params={'actions': action_ids}
        )
        return self.process_response(response)
