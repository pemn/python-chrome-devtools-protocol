'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: headless_experimental
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *


@dataclass
class NeedsBeginFramesChanged:
    '''
    Issued when the target starts or stops needing BeginFrames.
    '''
    #: Issued when the target starts or stops needing BeginFrames.
    needs_begin_frames: bool

