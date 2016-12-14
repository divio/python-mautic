# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from .api import API


class Files(API):
    _endpoint = 'files/images'

    def set_folder(self, folder='assets'):
        """
        Changes the file folder to look at

        :param folder: str [images, assets]
        :return: None
        """
        folder = folder.replace('/', '.')
        self._endpoint = 'files/{folder}'.format(folder=folder)

    def edit(self, obj_id, parameters=None, create_if_not_exists=False):
        return self.action_not_supported('edit')
