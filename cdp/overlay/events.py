'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: overlay
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..dom import types as dom
from ..page import types as page



@dataclass
class InspectNodeRequested:
    '''
    Fired when the node should be inspected. This happens after call to `setInspectMode` or when
    user manually inspects an element.
    '''
    #: Fired when the node should be inspected. This happens after call to `setInspectMode` or when
    #: user manually inspects an element.
    backend_node_id: dom.BackendNodeId


@dataclass
class NodeHighlightRequested:
    '''
    Fired when the node should be highlighted. This happens after call to `setInspectMode`.
    '''
    #: Fired when the node should be highlighted. This happens after call to `setInspectMode`.
    node_id: dom.NodeId


@dataclass
class ScreenshotRequested:
    '''
    Fired when user asks to capture screenshot of some area on the page.
    '''
    #: Fired when user asks to capture screenshot of some area on the page.
    viewport: page.Viewport


@dataclass
class InspectModeCanceled:
    '''
    Fired when user cancels the inspect mode.
    '''
    pass

