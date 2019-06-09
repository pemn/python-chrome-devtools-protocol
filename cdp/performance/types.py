'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: performance
Experimental: False
'''

from dataclasses import dataclass, field
import typing



@dataclass
class Metric:
    '''
    Run-time execution metric.
    '''
    #: Metric name.
    name: str

    #: Metric value.
    value: float

    @classmethod
    def from_response(cls, response):
        return cls(
            name=str(response.get('name')),
            value=float(response.get('value')),
        )

