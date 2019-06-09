'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: io
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *
from ..runtime import types as runtime



class IO:
    @staticmethod
    def close(handle: StreamHandle) -> None:
        '''
        Close the stream, discard any temporary backing storage.
        
        :param handle: Handle of the stream to close.
        '''

        cmd_dict = {
            'method': 'IO.close',
            'params': {
                'handle': handle,
            }
        }
        response = yield cmd_dict

    @staticmethod
    def read(handle: StreamHandle, offset: int, size: int) -> dict:
        '''
        Read a chunk of the stream
        
        :param handle: Handle of the stream to read.
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset
        following the last read). Some types of streams may only support sequential reads.
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :returns: a dict with the following keys:
            * base64Encoded: Set if the data is base64-encoded
            * data: Data that were read.
            * eof: Set if the end-of-file condition occured while reading.
        '''

        cmd_dict = {
            'method': 'IO.read',
            'params': {
                'handle': handle,
                'offset': offset,
                'size': size,
            }
        }
        response = yield cmd_dict
        return {
                'base64Encoded': bool.from_response(response['base64Encoded']),
                'data': str.from_response(response['data']),
                'eof': bool.from_response(response['eof']),
            }

    @staticmethod
    def resolve_blob(object_id: runtime.RemoteObjectId) -> str:
        '''
        Return UUID of Blob object specified by a remote object id.
        
        :param object_id: Object id of a Blob object wrapper.
        :returns: UUID of the specified Blob.
        '''

        cmd_dict = {
            'method': 'IO.resolveBlob',
            'params': {
                'objectId': object_id,
            }
        }
        response = yield cmd_dict
        return str.from_response(response['uuid'])

