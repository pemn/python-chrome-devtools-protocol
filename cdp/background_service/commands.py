'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: background_service
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *


class BackgroundService:
    @staticmethod
    def start_observing(service: ServiceName) -> None:
        '''
        Enables event updates for the service.
        
        :param service: 
        '''

        cmd_dict = {
            'method': 'BackgroundService.startObserving',
            'params': {
                'service': service,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def stop_observing(service: ServiceName) -> None:
        '''
        Disables event updates for the service.
        
        :param service: 
        '''

        cmd_dict = {
            'method': 'BackgroundService.stopObserving',
            'params': {
                'service': service,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def set_recording(should_record: bool, service: ServiceName) -> None:
        '''
        Set the recording state for the service.
        
        :param should_record: 
        :param service: 
        '''

        cmd_dict = {
            'method': 'BackgroundService.setRecording',
            'params': {
                'shouldRecord': should_record,
                'service': service,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def clear_events(service: ServiceName) -> None:
        '''
        Clears all stored data for the service.
        
        :param service: 
        '''

        cmd_dict = {
            'method': 'BackgroundService.clearEvents',
            'params': {
                'service': service,
            }
        }
        response = yield cmd_dict

