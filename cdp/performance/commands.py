'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: performance
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *


class Performance:
    @staticmethod
    def disable() -> None:
        '''
        Disable collecting and reporting metrics.
        '''

        cmd_dict = {
            'method': 'Performance.disable',
        }
        response = yield cmd_dict

    @staticmethod
    def enable() -> None:
        '''
        Enable collecting and reporting metrics.
        '''

        cmd_dict = {
            'method': 'Performance.enable',
        }
        response = yield cmd_dict

    @staticmethod
    def set_time_domain(time_domain: str) -> None:
        '''
        Sets time domain to use for collecting and reporting duration metrics.
        Note that this must be called before enabling metrics collection. Calling
        this method while metrics collection is enabled returns an error.
        
        :param time_domain: Time domain
        '''

        cmd_dict = {
            'method': 'Performance.setTimeDomain',
            'params': {
                'timeDomain': time_domain,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def get_metrics() -> typing.List['Metric']:
        '''
        Retrieve current values of run-time metrics.
        :returns: Current values for run-time metrics.
        '''

        cmd_dict = {
            'method': 'Performance.getMetrics',
        }
        response = yield cmd_dict
        return [Metric.from_response(i) for i in response['metrics']]

