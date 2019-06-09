'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: profiler
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from ..runtime import types as runtime



@dataclass
class ProfileNode:
    '''
    Profile node. Holds callsite information, execution statistics and child nodes.
    '''
    #: Unique id of the node.
    id: int

    #: Function location.
    call_frame: runtime.CallFrame

    #: Number of samples where this node was on top of the call stack.
    hit_count: int

    #: Child node ids.
    children: typing.List

    #: The reason of being not optimized. The function may be deoptimized or marked as don't
    #: optimize.
    deopt_reason: str

    #: An array of source position ticks.
    position_ticks: typing.List['PositionTickInfo']

    @classmethod
    def from_response(cls, response):
        return cls(
            id=int(response.get('id')),
            call_frame=runtime.CallFrame.from_response(response.get('callFrame')),
            hit_count=int(response.get('hitCount')),
            children=[int(i) for i in response.get('children')],
            deopt_reason=str(response.get('deoptReason')),
            position_ticks=[PositionTickInfo.from_response(i) for i in response.get('positionTicks')],
        )


@dataclass
class Profile:
    '''
    Profile.
    '''
    #: The list of profile nodes. First item is the root node.
    nodes: typing.List['ProfileNode']

    #: Profiling start timestamp in microseconds.
    start_time: float

    #: Profiling end timestamp in microseconds.
    end_time: float

    #: Ids of samples top nodes.
    samples: typing.List

    #: Time intervals between adjacent samples in microseconds. The first delta is relative to the
    #: profile startTime.
    time_deltas: typing.List

    @classmethod
    def from_response(cls, response):
        return cls(
            nodes=[ProfileNode.from_response(i) for i in response.get('nodes')],
            start_time=float(response.get('startTime')),
            end_time=float(response.get('endTime')),
            samples=[int(i) for i in response.get('samples')],
            time_deltas=[int(i) for i in response.get('timeDeltas')],
        )


@dataclass
class PositionTickInfo:
    '''
    Specifies a number of samples attributed to a certain source position.
    '''
    #: Source line number (1-based).
    line: int

    #: Number of samples attributed to the source line.
    ticks: int

    @classmethod
    def from_response(cls, response):
        return cls(
            line=int(response.get('line')),
            ticks=int(response.get('ticks')),
        )


@dataclass
class CoverageRange:
    '''
    Coverage data for a source range.
    '''
    #: JavaScript script source offset for the range start.
    start_offset: int

    #: JavaScript script source offset for the range end.
    end_offset: int

    #: Collected execution count of the source range.
    count: int

    @classmethod
    def from_response(cls, response):
        return cls(
            start_offset=int(response.get('startOffset')),
            end_offset=int(response.get('endOffset')),
            count=int(response.get('count')),
        )


@dataclass
class FunctionCoverage:
    '''
    Coverage data for a JavaScript function.
    '''
    #: JavaScript function name.
    function_name: str

    #: Source ranges inside the function with coverage data.
    ranges: typing.List['CoverageRange']

    #: Whether coverage data for this function has block granularity.
    is_block_coverage: bool

    @classmethod
    def from_response(cls, response):
        return cls(
            function_name=str(response.get('functionName')),
            ranges=[CoverageRange.from_response(i) for i in response.get('ranges')],
            is_block_coverage=bool(response.get('isBlockCoverage')),
        )


@dataclass
class ScriptCoverage:
    '''
    Coverage data for a JavaScript script.
    '''
    #: JavaScript script id.
    script_id: runtime.ScriptId

    #: JavaScript script name or url.
    url: str

    #: Functions contained in the script that has coverage data.
    functions: typing.List['FunctionCoverage']

    @classmethod
    def from_response(cls, response):
        return cls(
            script_id=runtime.ScriptId.from_response(response.get('scriptId')),
            url=str(response.get('url')),
            functions=[FunctionCoverage.from_response(i) for i in response.get('functions')],
        )


@dataclass
class TypeObject:
    '''
    Describes a type collected during runtime.
    '''
    #: Name of a type collected with type profiling.
    name: str

    @classmethod
    def from_response(cls, response):
        return cls(
            name=str(response.get('name')),
        )


@dataclass
class TypeProfileEntry:
    '''
    Source offset and types for a parameter or return value.
    '''
    #: Source offset of the parameter or end of function for return values.
    offset: int

    #: The types for this parameter or return value.
    types: typing.List['TypeObject']

    @classmethod
    def from_response(cls, response):
        return cls(
            offset=int(response.get('offset')),
            types=[TypeObject.from_response(i) for i in response.get('types')],
        )


@dataclass
class ScriptTypeProfile:
    '''
    Type profile data collected during runtime for a JavaScript script.
    '''
    #: JavaScript script id.
    script_id: runtime.ScriptId

    #: JavaScript script name or url.
    url: str

    #: Type profile entries for parameters and return values of the functions in the script.
    entries: typing.List['TypeProfileEntry']

    @classmethod
    def from_response(cls, response):
        return cls(
            script_id=runtime.ScriptId.from_response(response.get('scriptId')),
            url=str(response.get('url')),
            entries=[TypeProfileEntry.from_response(i) for i in response.get('entries')],
        )

