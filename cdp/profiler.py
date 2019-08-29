'''
DO NOT EDIT THIS FILE

This file is generated from the CDP specification. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: Profiler
Experimental: False
'''

from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing

from . import debugger
from . import runtime


@dataclass
class ProfileNode:
    '''
    Profile node. Holds callsite information, execution statistics and child nodes.
    '''
    #: Unique id of the node.
    id: int

    #: Function location.
    call_frame: 'runtime.CallFrame'

    #: Number of samples where this node was on top of the call stack.
    hit_count: typing.Optional[int] = None

    #: Child node ids.
    children: typing.Optional[typing.List[int]] = None

    #: The reason of being not optimized. The function may be deoptimized or marked as don't
    #: optimize.
    deopt_reason: typing.Optional[str] = None

    #: An array of source position ticks.
    position_ticks: typing.Optional[typing.List['PositionTickInfo']] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['id'] = self.id
        json['callFrame'] = self.call_frame.to_json()
        if self.hit_count is not None:
            json['hitCount'] = self.hit_count
        if self.children is not None:
            json['children'] = [i for i in self.children]
        if self.deopt_reason is not None:
            json['deoptReason'] = self.deopt_reason
        if self.position_ticks is not None:
            json['positionTicks'] = [i.to_json() for i in self.position_ticks]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ProfileNode':
        return cls(
            id=int(json['id']),
            call_frame=runtime.CallFrame.from_json(json['callFrame']),
            hit_count=int(json['hitCount']) if 'hitCount' in json else None,
            children=[int(i) for i in json['children']] if 'children' in json else None,
            deopt_reason=str(json['deoptReason']) if 'deoptReason' in json else None,
            position_ticks=[PositionTickInfo.from_json(i) for i in json['positionTicks']] if 'positionTicks' in json else None,
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
    samples: typing.Optional[typing.List[int]] = None

    #: Time intervals between adjacent samples in microseconds. The first delta is relative to the
    #: profile startTime.
    time_deltas: typing.Optional[typing.List[int]] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['nodes'] = [i.to_json() for i in self.nodes]
        json['startTime'] = self.start_time
        json['endTime'] = self.end_time
        if self.samples is not None:
            json['samples'] = [i for i in self.samples]
        if self.time_deltas is not None:
            json['timeDeltas'] = [i for i in self.time_deltas]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'Profile':
        return cls(
            nodes=[ProfileNode.from_json(i) for i in json['nodes']],
            start_time=float(json['startTime']),
            end_time=float(json['endTime']),
            samples=[int(i) for i in json['samples']] if 'samples' in json else None,
            time_deltas=[int(i) for i in json['timeDeltas']] if 'timeDeltas' in json else None,
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

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['line'] = self.line
        json['ticks'] = self.ticks
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'PositionTickInfo':
        return cls(
            line=int(json['line']),
            ticks=int(json['ticks']),
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

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['startOffset'] = self.start_offset
        json['endOffset'] = self.end_offset
        json['count'] = self.count
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'CoverageRange':
        return cls(
            start_offset=int(json['startOffset']),
            end_offset=int(json['endOffset']),
            count=int(json['count']),
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

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['functionName'] = self.function_name
        json['ranges'] = [i.to_json() for i in self.ranges]
        json['isBlockCoverage'] = self.is_block_coverage
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'FunctionCoverage':
        return cls(
            function_name=str(json['functionName']),
            ranges=[CoverageRange.from_json(i) for i in json['ranges']],
            is_block_coverage=bool(json['isBlockCoverage']),
        )


@dataclass
class ScriptCoverage:
    '''
    Coverage data for a JavaScript script.
    '''
    #: JavaScript script id.
    script_id: 'runtime.ScriptId'

    #: JavaScript script name or url.
    url: str

    #: Functions contained in the script that has coverage data.
    functions: typing.List['FunctionCoverage']

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['scriptId'] = self.script_id.to_json()
        json['url'] = self.url
        json['functions'] = [i.to_json() for i in self.functions]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ScriptCoverage':
        return cls(
            script_id=runtime.ScriptId.from_json(json['scriptId']),
            url=str(json['url']),
            functions=[FunctionCoverage.from_json(i) for i in json['functions']],
        )


@dataclass
class TypeObject:
    '''
    Describes a type collected during runtime.
    '''
    #: Name of a type collected with type profiling.
    name: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'TypeObject':
        return cls(
            name=str(json['name']),
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

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['offset'] = self.offset
        json['types'] = [i.to_json() for i in self.types]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'TypeProfileEntry':
        return cls(
            offset=int(json['offset']),
            types=[TypeObject.from_json(i) for i in json['types']],
        )


@dataclass
class ScriptTypeProfile:
    '''
    Type profile data collected during runtime for a JavaScript script.
    '''
    #: JavaScript script id.
    script_id: 'runtime.ScriptId'

    #: JavaScript script name or url.
    url: str

    #: Type profile entries for parameters and return values of the functions in the script.
    entries: typing.List['TypeProfileEntry']

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['scriptId'] = self.script_id.to_json()
        json['url'] = self.url
        json['entries'] = [i.to_json() for i in self.entries]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ScriptTypeProfile':
        return cls(
            script_id=runtime.ScriptId.from_json(json['scriptId']),
            url=str(json['url']),
            entries=[TypeProfileEntry.from_json(i) for i in json['entries']],
        )


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:

    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.disable',
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:

    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.enable',
    }
    json = yield cmd_dict


def get_best_effort_coverage() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.List['ScriptCoverage']]:
    '''
    Collect coverage data for the current isolate. The coverage data may be incomplete due to
    garbage collection.

    :returns: Coverage data for the current isolate.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.getBestEffortCoverage',
    }
    json = yield cmd_dict
    return [ScriptCoverage.from_json(i) for i in json['result']]


def set_sampling_interval(
        interval: int
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

    :param interval: New sampling interval in microseconds.
    '''
    params: T_JSON_DICT = dict()
    params['interval'] = interval
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.setSamplingInterval',
        'params': params,
    }
    json = yield cmd_dict


def start() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:

    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.start',
    }
    json = yield cmd_dict


def start_precise_coverage(
        call_count: typing.Optional[bool] = None,
        detailed: typing.Optional[bool] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
    coverage may be incomplete. Enabling prevents running optimized code and resets execution
    counters.

    :param call_count: Collect accurate call counts beyond simple 'covered' or 'not covered'.
    :param detailed: Collect block-based coverage.
    '''
    params: T_JSON_DICT = dict()
    if call_count is not None:
        params['callCount'] = call_count
    if detailed is not None:
        params['detailed'] = detailed
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.startPreciseCoverage',
        'params': params,
    }
    json = yield cmd_dict


def start_type_profile() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enable type profile.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.startTypeProfile',
    }
    json = yield cmd_dict


def stop() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,'Profile']:
    '''


    :returns: Recorded profile.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.stop',
    }
    json = yield cmd_dict
    return Profile.from_json(json['profile'])


def stop_precise_coverage() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disable precise code coverage. Disabling releases unnecessary execution count records and allows
    executing optimized code.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.stopPreciseCoverage',
    }
    json = yield cmd_dict


def stop_type_profile() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disable type profile. Disabling releases type profile data collected so far.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.stopTypeProfile',
    }
    json = yield cmd_dict


def take_precise_coverage() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.List['ScriptCoverage']]:
    '''
    Collect coverage data for the current isolate, and resets execution counters. Precise code
    coverage needs to have started.

    :returns: Coverage data for the current isolate.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.takePreciseCoverage',
    }
    json = yield cmd_dict
    return [ScriptCoverage.from_json(i) for i in json['result']]


def take_type_profile() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.List['ScriptTypeProfile']]:
    '''
    Collect type profile.

    :returns: Type profile for all scripts since startTypeProfile() was turned on.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Profiler.takeTypeProfile',
    }
    json = yield cmd_dict
    return [ScriptTypeProfile.from_json(i) for i in json['result']]


@event_class('Profiler.consoleProfileFinished')
@dataclass
class ConsoleProfileFinished:
    id: str
    #: Location of console.profileEnd().

    location: 'debugger.Location'
    profile: 'Profile'
    #: Profile title passed as an argument to console.profile().

    title: typing.Optional[str]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ConsoleProfileFinished':
        return cls(
            id=str(json['id']),
            location=debugger.Location.from_json(json['location']),
            profile=Profile.from_json(json['profile']),
            title=str(json['title']) if 'title' in json else None
        )


@event_class('Profiler.consoleProfileStarted')
@dataclass
class ConsoleProfileStarted:
    '''
    Sent when new profile recording is started using console.profile() call.
    '''
    id: str
    #: Location of console.profile().

    location: 'debugger.Location'
    #: Profile title passed as an argument to console.profile().

    title: typing.Optional[str]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ConsoleProfileStarted':
        return cls(
            id=str(json['id']),
            location=debugger.Location.from_json(json['location']),
            title=str(json['title']) if 'title' in json else None
        )
