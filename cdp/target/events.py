'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: target
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *


@dataclass
class AttachedToTarget:
    '''
    Issued when attached to target because of auto-attach or `attachToTarget` command.
    '''
    #: Issued when attached to target because of auto-attach or `attachToTarget` command.
    session_id: SessionID

    #: Issued when attached to target because of auto-attach or `attachToTarget` command.
    target_info: TargetInfo

    #: Issued when attached to target because of auto-attach or `attachToTarget` command.
    waiting_for_debugger: bool


@dataclass
class DetachedFromTarget:
    '''
    Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    issued multiple times per target if multiple sessions have been attached to it.
    '''
    #: Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    #: issued multiple times per target if multiple sessions have been attached to it.
    session_id: SessionID

    #: Issued when detached from target for any reason (including `detachFromTarget` command). Can be
    #: issued multiple times per target if multiple sessions have been attached to it.
    target_id: TargetID


@dataclass
class ReceivedMessageFromTarget:
    '''
    Notifies about a new protocol message received from the session (as reported in
    `attachedToTarget` event).
    '''
    #: Notifies about a new protocol message received from the session (as reported in
    #: `attachedToTarget` event).
    session_id: SessionID

    #: Notifies about a new protocol message received from the session (as reported in
    #: `attachedToTarget` event).
    message: str

    #: Notifies about a new protocol message received from the session (as reported in
    #: `attachedToTarget` event).
    target_id: TargetID


@dataclass
class TargetCreated:
    '''
    Issued when a possible inspection target is created.
    '''
    #: Issued when a possible inspection target is created.
    target_info: TargetInfo


@dataclass
class TargetDestroyed:
    '''
    Issued when a target is destroyed.
    '''
    #: Issued when a target is destroyed.
    target_id: TargetID


@dataclass
class TargetCrashed:
    '''
    Issued when a target has crashed.
    '''
    #: Issued when a target has crashed.
    target_id: TargetID

    #: Issued when a target has crashed.
    status: str

    #: Issued when a target has crashed.
    error_code: int


@dataclass
class TargetInfoChanged:
    '''
    Issued when some information about a target has changed. This only happens between
    `targetCreated` and `targetDestroyed`.
    '''
    #: Issued when some information about a target has changed. This only happens between
    #: `targetCreated` and `targetDestroyed`.
    target_info: TargetInfo

