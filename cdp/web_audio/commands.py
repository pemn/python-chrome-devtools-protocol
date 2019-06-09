'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: web_audio
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *


class WebAudio:
    @staticmethod
    def enable() -> None:
        '''
        Enables the WebAudio domain and starts sending context lifetime events.
        '''

        cmd_dict = {
            'method': 'WebAudio.enable',
        }
        response = yield cmd_dict

    @staticmethod
    def disable() -> None:
        '''
        Disables the WebAudio domain.
        '''

        cmd_dict = {
            'method': 'WebAudio.disable',
        }
        response = yield cmd_dict

    @staticmethod
    def get_realtime_data(context_id: ContextId) -> ContextRealtimeData:
        '''
        Fetch the realtime data from the registered contexts.
        
        :param context_id: 
        :returns: 
        '''

        cmd_dict = {
            'method': 'WebAudio.getRealtimeData',
            'params': {
                'contextId': context_id,
            }
        }
        response = yield cmd_dict
        return ContextRealtimeData.from_response(response['realtimeData'])

