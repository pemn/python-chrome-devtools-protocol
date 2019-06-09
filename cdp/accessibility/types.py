'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: accessibility
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from ..dom import types as dom


class AXNodeId(str):
    '''
    Unique accessibility node identifier.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'AXNodeId({})'.format(str.__repr__(self))



class AXValueType:
    '''
    Enum of possible property types.
    '''
    BOOLEAN = "boolean"
    TRISTATE = "tristate"
    BOOLEAN_OR_UNDEFINED = "booleanOrUndefined"
    IDREF = "idref"
    IDREF_LIST = "idrefList"
    INTEGER = "integer"
    NODE = "node"
    NODE_LIST = "nodeList"
    NUMBER = "number"
    STRING = "string"
    COMPUTED_STRING = "computedString"
    TOKEN = "token"
    TOKEN_LIST = "tokenList"
    DOM_RELATION = "domRelation"
    ROLE = "role"
    INTERNAL_ROLE = "internalRole"
    VALUE_UNDEFINED = "valueUndefined"


class AXValueSourceType:
    '''
    Enum of possible property sources.
    '''
    ATTRIBUTE = "attribute"
    IMPLICIT = "implicit"
    STYLE = "style"
    CONTENTS = "contents"
    PLACEHOLDER = "placeholder"
    RELATED_ELEMENT = "relatedElement"


class AXValueNativeSourceType:
    '''
    Enum of possible native property sources (as a subtype of a particular AXValueSourceType).
    '''
    FIGCAPTION = "figcaption"
    LABEL = "label"
    LABELFOR = "labelfor"
    LABELWRAPPED = "labelwrapped"
    LEGEND = "legend"
    TABLECAPTION = "tablecaption"
    TITLE = "title"
    OTHER = "other"


class AXPropertyName:
    '''
    Values of AXProperty name:
    - from 'busy' to 'roledescription': states which apply to every AX node
    - from 'live' to 'root': attributes which apply to nodes in live regions
    - from 'autocomplete' to 'valuetext': attributes which apply to widgets
    - from 'checked' to 'selected': states which apply to widgets
    - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
    '''
    BUSY = "busy"
    DISABLED = "disabled"
    EDITABLE = "editable"
    FOCUSABLE = "focusable"
    FOCUSED = "focused"
    HIDDEN = "hidden"
    HIDDEN_ROOT = "hiddenRoot"
    INVALID = "invalid"
    KEYSHORTCUTS = "keyshortcuts"
    SETTABLE = "settable"
    ROLEDESCRIPTION = "roledescription"
    LIVE = "live"
    ATOMIC = "atomic"
    RELEVANT = "relevant"
    ROOT = "root"
    AUTOCOMPLETE = "autocomplete"
    HAS_POPUP = "hasPopup"
    LEVEL = "level"
    MULTISELECTABLE = "multiselectable"
    ORIENTATION = "orientation"
    MULTILINE = "multiline"
    READONLY = "readonly"
    REQUIRED = "required"
    VALUEMIN = "valuemin"
    VALUEMAX = "valuemax"
    VALUETEXT = "valuetext"
    CHECKED = "checked"
    EXPANDED = "expanded"
    MODAL = "modal"
    PRESSED = "pressed"
    SELECTED = "selected"
    ACTIVEDESCENDANT = "activedescendant"
    CONTROLS = "controls"
    DESCRIBEDBY = "describedby"
    DETAILS = "details"
    ERRORMESSAGE = "errormessage"
    FLOWTO = "flowto"
    LABELLEDBY = "labelledby"
    OWNS = "owns"


@dataclass
class AXRelatedNode:
    #: The BackendNodeId of the related DOM node.
    backend_dom_node_id: dom.BackendNodeId

    #: The IDRef value provided, if any.
    idref: str

    #: The text alternative of this node in the current context.
    text: str

    @classmethod
    def from_response(cls, response):
        return cls(
            backend_dom_node_id=dom.BackendNodeId.from_response(response.get('backendDOMNodeId')),
            idref=str(response.get('idref')),
            text=str(response.get('text')),
        )


@dataclass
class AXValue:
    '''
    A single computed AX property.
    '''
    #: The type of this value.
    type_: AXValueType

    #: The computed value of this property.
    value: typing.Any

    #: One or more related nodes, if applicable.
    related_nodes: typing.List['AXRelatedNode']

    #: The sources which contributed to the computation of this property.
    sources: typing.List['AXValueSource']

    @classmethod
    def from_response(cls, response):
        return cls(
            type_=AXValueType.from_response(response.get('type')),
            value=typing.Any(response.get('value')),
            related_nodes=[AXRelatedNode.from_response(i) for i in response.get('relatedNodes')],
            sources=[AXValueSource.from_response(i) for i in response.get('sources')],
        )


@dataclass
class AXNode:
    '''
    A node in the accessibility tree.
    '''
    #: Unique identifier for this node.
    node_id: AXNodeId

    #: Whether this node is ignored for accessibility
    ignored: bool

    #: Collection of reasons why this node is hidden.
    ignored_reasons: typing.List['AXProperty']

    #: This `Node`'s role, whether explicit or implicit.
    role: AXValue

    #: The accessible name for this `Node`.
    name: AXValue

    #: The accessible description for this `Node`.
    description: AXValue

    #: The value for this `Node`.
    value: AXValue

    #: All other properties
    properties: typing.List['AXProperty']

    #: IDs for each of this node's child nodes.
    child_ids: typing.List['AXNodeId']

    #: The backend ID for the associated DOM node, if any.
    backend_dom_node_id: dom.BackendNodeId

    @classmethod
    def from_response(cls, response):
        return cls(
            node_id=AXNodeId.from_response(response.get('nodeId')),
            ignored=bool(response.get('ignored')),
            ignored_reasons=[AXProperty.from_response(i) for i in response.get('ignoredReasons')],
            role=AXValue.from_response(response.get('role')),
            name=AXValue.from_response(response.get('name')),
            description=AXValue.from_response(response.get('description')),
            value=AXValue.from_response(response.get('value')),
            properties=[AXProperty.from_response(i) for i in response.get('properties')],
            child_ids=[AXNodeId.from_response(i) for i in response.get('childIds')],
            backend_dom_node_id=dom.BackendNodeId.from_response(response.get('backendDOMNodeId')),
        )


@dataclass
class AXValueSource:
    '''
    A single source for a computed AX property.
    '''
    #: What type of source this is.
    type_: AXValueSourceType

    #: The value of this property source.
    value: AXValue

    #: The name of the relevant attribute, if any.
    attribute: str

    #: The value of the relevant attribute, if any.
    attribute_value: AXValue

    #: Whether this source is superseded by a higher priority source.
    superseded: bool

    #: The native markup source for this value, e.g. a <label> element.
    native_source: AXValueNativeSourceType

    #: The value, such as a node or node list, of the native source.
    native_source_value: AXValue

    #: Whether the value for this property is invalid.
    invalid: bool

    #: Reason for the value being invalid, if it is.
    invalid_reason: str

    @classmethod
    def from_response(cls, response):
        return cls(
            type_=AXValueSourceType.from_response(response.get('type')),
            value=AXValue.from_response(response.get('value')),
            attribute=str(response.get('attribute')),
            attribute_value=AXValue.from_response(response.get('attributeValue')),
            superseded=bool(response.get('superseded')),
            native_source=AXValueNativeSourceType.from_response(response.get('nativeSource')),
            native_source_value=AXValue.from_response(response.get('nativeSourceValue')),
            invalid=bool(response.get('invalid')),
            invalid_reason=str(response.get('invalidReason')),
        )


@dataclass
class AXProperty:
    #: The name of this property.
    name: AXPropertyName

    #: The value of this property.
    value: AXValue

    @classmethod
    def from_response(cls, response):
        return cls(
            name=AXPropertyName.from_response(response.get('name')),
            value=AXValue.from_response(response.get('value')),
        )

