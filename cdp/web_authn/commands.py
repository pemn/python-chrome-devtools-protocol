'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: web_authn
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *


class WebAuthn:
    @staticmethod
    def enable() -> None:
        '''
        Enable the WebAuthn domain and start intercepting credential storage and
        retrieval with a virtual authenticator.
        '''

        cmd_dict = {
            'method': 'WebAuthn.enable',
        }
        response = yield cmd_dict

    @staticmethod
    def disable() -> None:
        '''
        Disable the WebAuthn domain.
        '''

        cmd_dict = {
            'method': 'WebAuthn.disable',
        }
        response = yield cmd_dict

