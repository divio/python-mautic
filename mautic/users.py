# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Users(API):
    _endpoint = 'users'

    def get_self(self):
        """
        Get your (API) user

        :return: dict|str
        """
        response = self._client.session.get(
            '{url}/self'.format(url=self.endpoint_url)
        )
        return self.process_response(response)

    def check_permission(self, obj_id, permissions):
        """
        Get list of permissions for a user

        :param obj_id: int
        :param permissions: str|list|tuple
        :return: dict|str
        """
        response = self._client.session.post(
            '{url}/{id}/permissioncheck'.format(
                url=self.endpoint_url, id=obj_id
            ),
            data={'permissions': permissions}
        )
        return self.process_response(response)
