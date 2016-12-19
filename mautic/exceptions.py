# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


class MauticException(Exception):
    """
    Base class for Mautic exceptions.
    """
    code = 500
    default_message = 'Mautic error occurred.'

    def __init__(self, message=None):
        if message is not None:
            self.message = message
        else:
            self.message = self.default_message

    def __repr__(self):
        return '{} {}'.format(
            type(self).__name__,
            self.message,
        )

    def __str__(self):
        return self.__repr__()


class ActionNotSupportedException(MauticException):
    """
    Exception representing an unsupported action
    """

    default_message = 'Action is not supported at this time.'


class ContextNotFoundException(MauticException):
    """
    Exception representing a requested API context which was not found
    """

    default_message = 'Context not found.'


class IncorrectParametersReturnedException(MauticException):
    """
    Exception representing an incorrect parameter set for an OAuth token request
    """

    default_message = 'Incorrect parameters returned.'


class UnexpectedResponseFormatException(MauticException):
    """
    Exception representing an unexpected HTTP response
    """

    default_message = 'The response returned is in an unexpected format.'
