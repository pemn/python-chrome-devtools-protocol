'''
DO NOT EDIT THIS FILE

This file is generated from the CDP specification. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: DOMSnapshot
Experimental: True
'''

from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing

from . import dom
from . import dom_debugger
from . import page


@dataclass
class DOMNode:
    '''
    A Node in the DOM tree.
    '''
    #: `Node`'s nodeType.
    node_type: int

    #: `Node`'s nodeName.
    node_name: str

    #: `Node`'s nodeValue.
    node_value: str

    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.
    backend_node_id: 'dom.BackendNodeId'

    #: Only set for textarea elements, contains the text value.
    text_value: typing.Optional[str] = None

    #: Only set for input elements, contains the input's associated text value.
    input_value: typing.Optional[str] = None

    #: Only set for radio and checkbox input elements, indicates if the element has been checked
    input_checked: typing.Optional[bool] = None

    #: Only set for option elements, indicates if the element has been selected
    option_selected: typing.Optional[bool] = None

    #: The indexes of the node's child nodes in the `domNodes` array returned by `getSnapshot`, if
    #: any.
    child_node_indexes: typing.Optional[typing.List[int]] = None

    #: Attributes of an `Element` node.
    attributes: typing.Optional[typing.List['NameValue']] = None

    #: Indexes of pseudo elements associated with this node in the `domNodes` array returned by
    #: `getSnapshot`, if any.
    pseudo_element_indexes: typing.Optional[typing.List[int]] = None

    #: The index of the node's related layout tree node in the `layoutTreeNodes` array returned by
    #: `getSnapshot`, if any.
    layout_node_index: typing.Optional[int] = None

    #: Document URL that `Document` or `FrameOwner` node points to.
    document_url: typing.Optional[str] = None

    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.
    base_url: typing.Optional[str] = None

    #: Only set for documents, contains the document's content language.
    content_language: typing.Optional[str] = None

    #: Only set for documents, contains the document's character set encoding.
    document_encoding: typing.Optional[str] = None

    #: `DocumentType` node's publicId.
    public_id: typing.Optional[str] = None

    #: `DocumentType` node's systemId.
    system_id: typing.Optional[str] = None

    #: Frame ID for frame owner elements and also for the document node.
    frame_id: typing.Optional['page.FrameId'] = None

    #: The index of a frame owner element's content document in the `domNodes` array returned by
    #: `getSnapshot`, if any.
    content_document_index: typing.Optional[int] = None

    #: Type of a pseudo element node.
    pseudo_type: typing.Optional['dom.PseudoType'] = None

    #: Shadow root type.
    shadow_root_type: typing.Optional['dom.ShadowRootType'] = None

    #: Whether this DOM node responds to mouse clicks. This includes nodes that have had click
    #: event listeners attached via JavaScript as well as anchor tags that naturally navigate when
    #: clicked.
    is_clickable: typing.Optional[bool] = None

    #: Details of the node's event listeners, if any.
    event_listeners: typing.Optional[typing.List['dom_debugger.EventListener']] = None

    #: The selected url for nodes with a srcset attribute.
    current_source_url: typing.Optional[str] = None

    #: The url of the script (if any) that generates this node.
    origin_url: typing.Optional[str] = None

    #: Scroll offsets, set when this node is a Document.
    scroll_offset_x: typing.Optional[float] = None

    scroll_offset_y: typing.Optional[float] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['nodeType'] = self.node_type
        json['nodeName'] = self.node_name
        json['nodeValue'] = self.node_value
        json['backendNodeId'] = self.backend_node_id.to_json()
        if self.text_value is not None:
            json['textValue'] = self.text_value
        if self.input_value is not None:
            json['inputValue'] = self.input_value
        if self.input_checked is not None:
            json['inputChecked'] = self.input_checked
        if self.option_selected is not None:
            json['optionSelected'] = self.option_selected
        if self.child_node_indexes is not None:
            json['childNodeIndexes'] = [i for i in self.child_node_indexes]
        if self.attributes is not None:
            json['attributes'] = [i.to_json() for i in self.attributes]
        if self.pseudo_element_indexes is not None:
            json['pseudoElementIndexes'] = [i for i in self.pseudo_element_indexes]
        if self.layout_node_index is not None:
            json['layoutNodeIndex'] = self.layout_node_index
        if self.document_url is not None:
            json['documentURL'] = self.document_url
        if self.base_url is not None:
            json['baseURL'] = self.base_url
        if self.content_language is not None:
            json['contentLanguage'] = self.content_language
        if self.document_encoding is not None:
            json['documentEncoding'] = self.document_encoding
        if self.public_id is not None:
            json['publicId'] = self.public_id
        if self.system_id is not None:
            json['systemId'] = self.system_id
        if self.frame_id is not None:
            json['frameId'] = self.frame_id.to_json()
        if self.content_document_index is not None:
            json['contentDocumentIndex'] = self.content_document_index
        if self.pseudo_type is not None:
            json['pseudoType'] = self.pseudo_type.to_json()
        if self.shadow_root_type is not None:
            json['shadowRootType'] = self.shadow_root_type.to_json()
        if self.is_clickable is not None:
            json['isClickable'] = self.is_clickable
        if self.event_listeners is not None:
            json['eventListeners'] = [i.to_json() for i in self.event_listeners]
        if self.current_source_url is not None:
            json['currentSourceURL'] = self.current_source_url
        if self.origin_url is not None:
            json['originURL'] = self.origin_url
        if self.scroll_offset_x is not None:
            json['scrollOffsetX'] = self.scroll_offset_x
        if self.scroll_offset_y is not None:
            json['scrollOffsetY'] = self.scroll_offset_y
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'DOMNode':
        return cls(
            node_type=int(json['nodeType']),
            node_name=str(json['nodeName']),
            node_value=str(json['nodeValue']),
            backend_node_id=dom.BackendNodeId.from_json(json['backendNodeId']),
            text_value=str(json['textValue']) if 'textValue' in json else None,
            input_value=str(json['inputValue']) if 'inputValue' in json else None,
            input_checked=bool(json['inputChecked']) if 'inputChecked' in json else None,
            option_selected=bool(json['optionSelected']) if 'optionSelected' in json else None,
            child_node_indexes=[int(i) for i in json['childNodeIndexes']] if 'childNodeIndexes' in json else None,
            attributes=[NameValue.from_json(i) for i in json['attributes']] if 'attributes' in json else None,
            pseudo_element_indexes=[int(i) for i in json['pseudoElementIndexes']] if 'pseudoElementIndexes' in json else None,
            layout_node_index=int(json['layoutNodeIndex']) if 'layoutNodeIndex' in json else None,
            document_url=str(json['documentURL']) if 'documentURL' in json else None,
            base_url=str(json['baseURL']) if 'baseURL' in json else None,
            content_language=str(json['contentLanguage']) if 'contentLanguage' in json else None,
            document_encoding=str(json['documentEncoding']) if 'documentEncoding' in json else None,
            public_id=str(json['publicId']) if 'publicId' in json else None,
            system_id=str(json['systemId']) if 'systemId' in json else None,
            frame_id=page.FrameId.from_json(json['frameId']) if 'frameId' in json else None,
            content_document_index=int(json['contentDocumentIndex']) if 'contentDocumentIndex' in json else None,
            pseudo_type=dom.PseudoType.from_json(json['pseudoType']) if 'pseudoType' in json else None,
            shadow_root_type=dom.ShadowRootType.from_json(json['shadowRootType']) if 'shadowRootType' in json else None,
            is_clickable=bool(json['isClickable']) if 'isClickable' in json else None,
            event_listeners=[dom_debugger.EventListener.from_json(i) for i in json['eventListeners']] if 'eventListeners' in json else None,
            current_source_url=str(json['currentSourceURL']) if 'currentSourceURL' in json else None,
            origin_url=str(json['originURL']) if 'originURL' in json else None,
            scroll_offset_x=float(json['scrollOffsetX']) if 'scrollOffsetX' in json else None,
            scroll_offset_y=float(json['scrollOffsetY']) if 'scrollOffsetY' in json else None,
        )


@dataclass
class InlineTextBox:
    '''
    Details of post layout rendered text positions. The exact layout should not be regarded as
    stable and may change between versions.
    '''
    #: The bounding box in document coordinates. Note that scroll offset of the document is ignored.
    bounding_box: 'dom.Rect'

    #: The starting index in characters, for this post layout textbox substring. Characters that
    #: would be represented as a surrogate pair in UTF-16 have length 2.
    start_character_index: int

    #: The number of characters in this post layout textbox substring. Characters that would be
    #: represented as a surrogate pair in UTF-16 have length 2.
    num_characters: int

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['boundingBox'] = self.bounding_box.to_json()
        json['startCharacterIndex'] = self.start_character_index
        json['numCharacters'] = self.num_characters
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'InlineTextBox':
        return cls(
            bounding_box=dom.Rect.from_json(json['boundingBox']),
            start_character_index=int(json['startCharacterIndex']),
            num_characters=int(json['numCharacters']),
        )


@dataclass
class LayoutTreeNode:
    '''
    Details of an element in the DOM tree with a LayoutObject.
    '''
    #: The index of the related DOM node in the `domNodes` array returned by `getSnapshot`.
    dom_node_index: int

    #: The bounding box in document coordinates. Note that scroll offset of the document is ignored.
    bounding_box: 'dom.Rect'

    #: Contents of the LayoutText, if any.
    layout_text: typing.Optional[str] = None

    #: The post-layout inline text nodes, if any.
    inline_text_nodes: typing.Optional[typing.List['InlineTextBox']] = None

    #: Index into the `computedStyles` array returned by `getSnapshot`.
    style_index: typing.Optional[int] = None

    #: Global paint order index, which is determined by the stacking order of the nodes. Nodes
    #: that are painted together will have the same index. Only provided if includePaintOrder in
    #: getSnapshot was true.
    paint_order: typing.Optional[int] = None

    #: Set to true to indicate the element begins a new stacking context.
    is_stacking_context: typing.Optional[bool] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['domNodeIndex'] = self.dom_node_index
        json['boundingBox'] = self.bounding_box.to_json()
        if self.layout_text is not None:
            json['layoutText'] = self.layout_text
        if self.inline_text_nodes is not None:
            json['inlineTextNodes'] = [i.to_json() for i in self.inline_text_nodes]
        if self.style_index is not None:
            json['styleIndex'] = self.style_index
        if self.paint_order is not None:
            json['paintOrder'] = self.paint_order
        if self.is_stacking_context is not None:
            json['isStackingContext'] = self.is_stacking_context
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'LayoutTreeNode':
        return cls(
            dom_node_index=int(json['domNodeIndex']),
            bounding_box=dom.Rect.from_json(json['boundingBox']),
            layout_text=str(json['layoutText']) if 'layoutText' in json else None,
            inline_text_nodes=[InlineTextBox.from_json(i) for i in json['inlineTextNodes']] if 'inlineTextNodes' in json else None,
            style_index=int(json['styleIndex']) if 'styleIndex' in json else None,
            paint_order=int(json['paintOrder']) if 'paintOrder' in json else None,
            is_stacking_context=bool(json['isStackingContext']) if 'isStackingContext' in json else None,
        )


@dataclass
class ComputedStyle:
    '''
    A subset of the full ComputedStyle as defined by the request whitelist.
    '''
    #: Name/value pairs of computed style properties.
    properties: typing.List['NameValue']

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['properties'] = [i.to_json() for i in self.properties]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'ComputedStyle':
        return cls(
            properties=[NameValue.from_json(i) for i in json['properties']],
        )


@dataclass
class NameValue:
    '''
    A name/value pair.
    '''
    #: Attribute/property name.
    name: str

    #: Attribute/property value.
    value: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        json['value'] = self.value
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'NameValue':
        return cls(
            name=str(json['name']),
            value=str(json['value']),
        )


class StringIndex(int):
    '''
    Index of the string in the strings table.
    '''
    def to_json(self) -> int:
        return self

    @classmethod
    def from_json(cls, json: int) -> 'StringIndex':
        return cls(json)

    def __repr__(self):
        return 'StringIndex({})'.format(super().__repr__())


class ArrayOfStrings(list):
    '''
    Index of the string in the strings table.
    '''
    def to_json(self) -> typing.List['StringIndex']:
        return self

    @classmethod
    def from_json(cls, json: typing.List['StringIndex']) -> 'ArrayOfStrings':
        return cls(json)

    def __repr__(self):
        return 'ArrayOfStrings({})'.format(super().__repr__())


@dataclass
class RareStringData:
    '''
    Data that is only present on rare nodes.
    '''
    index: typing.List[int]

    value: typing.List['StringIndex']

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['index'] = [i for i in self.index]
        json['value'] = [i.to_json() for i in self.value]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'RareStringData':
        return cls(
            index=[int(i) for i in json['index']],
            value=[StringIndex.from_json(i) for i in json['value']],
        )


@dataclass
class RareBooleanData:
    index: typing.List[int]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['index'] = [i for i in self.index]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'RareBooleanData':
        return cls(
            index=[int(i) for i in json['index']],
        )


@dataclass
class RareIntegerData:
    index: typing.List[int]

    value: typing.List[int]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['index'] = [i for i in self.index]
        json['value'] = [i for i in self.value]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'RareIntegerData':
        return cls(
            index=[int(i) for i in json['index']],
            value=[int(i) for i in json['value']],
        )


class Rectangle(list):
    def to_json(self) -> typing.List[float]:
        return self

    @classmethod
    def from_json(cls, json: typing.List[float]) -> 'Rectangle':
        return cls(json)

    def __repr__(self):
        return 'Rectangle({})'.format(super().__repr__())


@dataclass
class DocumentSnapshot:
    '''
    Document snapshot.
    '''
    #: Document URL that `Document` or `FrameOwner` node points to.
    document_url: 'StringIndex'

    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.
    base_url: 'StringIndex'

    #: Contains the document's content language.
    content_language: 'StringIndex'

    #: Contains the document's character set encoding.
    encoding_name: 'StringIndex'

    #: `DocumentType` node's publicId.
    public_id: 'StringIndex'

    #: `DocumentType` node's systemId.
    system_id: 'StringIndex'

    #: Frame ID for frame owner elements and also for the document node.
    frame_id: 'StringIndex'

    #: A table with dom nodes.
    nodes: 'NodeTreeSnapshot'

    #: The nodes in the layout tree.
    layout: 'LayoutTreeSnapshot'

    #: The post-layout inline text nodes.
    text_boxes: 'TextBoxSnapshot'

    #: Horizontal scroll offset.
    scroll_offset_x: typing.Optional[float] = None

    #: Vertical scroll offset.
    scroll_offset_y: typing.Optional[float] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['documentURL'] = self.document_url.to_json()
        json['baseURL'] = self.base_url.to_json()
        json['contentLanguage'] = self.content_language.to_json()
        json['encodingName'] = self.encoding_name.to_json()
        json['publicId'] = self.public_id.to_json()
        json['systemId'] = self.system_id.to_json()
        json['frameId'] = self.frame_id.to_json()
        json['nodes'] = self.nodes.to_json()
        json['layout'] = self.layout.to_json()
        json['textBoxes'] = self.text_boxes.to_json()
        if self.scroll_offset_x is not None:
            json['scrollOffsetX'] = self.scroll_offset_x
        if self.scroll_offset_y is not None:
            json['scrollOffsetY'] = self.scroll_offset_y
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'DocumentSnapshot':
        return cls(
            document_url=StringIndex.from_json(json['documentURL']),
            base_url=StringIndex.from_json(json['baseURL']),
            content_language=StringIndex.from_json(json['contentLanguage']),
            encoding_name=StringIndex.from_json(json['encodingName']),
            public_id=StringIndex.from_json(json['publicId']),
            system_id=StringIndex.from_json(json['systemId']),
            frame_id=StringIndex.from_json(json['frameId']),
            nodes=NodeTreeSnapshot.from_json(json['nodes']),
            layout=LayoutTreeSnapshot.from_json(json['layout']),
            text_boxes=TextBoxSnapshot.from_json(json['textBoxes']),
            scroll_offset_x=float(json['scrollOffsetX']) if 'scrollOffsetX' in json else None,
            scroll_offset_y=float(json['scrollOffsetY']) if 'scrollOffsetY' in json else None,
        )


@dataclass
class NodeTreeSnapshot:
    '''
    Table containing nodes.
    '''
    #: Parent node index.
    parent_index: typing.Optional[typing.List[int]] = None

    #: `Node`'s nodeType.
    node_type: typing.Optional[typing.List[int]] = None

    #: `Node`'s nodeName.
    node_name: typing.Optional[typing.List['StringIndex']] = None

    #: `Node`'s nodeValue.
    node_value: typing.Optional[typing.List['StringIndex']] = None

    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.
    backend_node_id: typing.Optional[typing.List['dom.BackendNodeId']] = None

    #: Attributes of an `Element` node. Flatten name, value pairs.
    attributes: typing.Optional[typing.List['ArrayOfStrings']] = None

    #: Only set for textarea elements, contains the text value.
    text_value: typing.Optional['RareStringData'] = None

    #: Only set for input elements, contains the input's associated text value.
    input_value: typing.Optional['RareStringData'] = None

    #: Only set for radio and checkbox input elements, indicates if the element has been checked
    input_checked: typing.Optional['RareBooleanData'] = None

    #: Only set for option elements, indicates if the element has been selected
    option_selected: typing.Optional['RareBooleanData'] = None

    #: The index of the document in the list of the snapshot documents.
    content_document_index: typing.Optional['RareIntegerData'] = None

    #: Type of a pseudo element node.
    pseudo_type: typing.Optional['RareStringData'] = None

    #: Whether this DOM node responds to mouse clicks. This includes nodes that have had click
    #: event listeners attached via JavaScript as well as anchor tags that naturally navigate when
    #: clicked.
    is_clickable: typing.Optional['RareBooleanData'] = None

    #: The selected url for nodes with a srcset attribute.
    current_source_url: typing.Optional['RareStringData'] = None

    #: The url of the script (if any) that generates this node.
    origin_url: typing.Optional['RareStringData'] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        if self.parent_index is not None:
            json['parentIndex'] = [i for i in self.parent_index]
        if self.node_type is not None:
            json['nodeType'] = [i for i in self.node_type]
        if self.node_name is not None:
            json['nodeName'] = [i.to_json() for i in self.node_name]
        if self.node_value is not None:
            json['nodeValue'] = [i.to_json() for i in self.node_value]
        if self.backend_node_id is not None:
            json['backendNodeId'] = [i.to_json() for i in self.backend_node_id]
        if self.attributes is not None:
            json['attributes'] = [i.to_json() for i in self.attributes]
        if self.text_value is not None:
            json['textValue'] = self.text_value.to_json()
        if self.input_value is not None:
            json['inputValue'] = self.input_value.to_json()
        if self.input_checked is not None:
            json['inputChecked'] = self.input_checked.to_json()
        if self.option_selected is not None:
            json['optionSelected'] = self.option_selected.to_json()
        if self.content_document_index is not None:
            json['contentDocumentIndex'] = self.content_document_index.to_json()
        if self.pseudo_type is not None:
            json['pseudoType'] = self.pseudo_type.to_json()
        if self.is_clickable is not None:
            json['isClickable'] = self.is_clickable.to_json()
        if self.current_source_url is not None:
            json['currentSourceURL'] = self.current_source_url.to_json()
        if self.origin_url is not None:
            json['originURL'] = self.origin_url.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'NodeTreeSnapshot':
        return cls(
            parent_index=[int(i) for i in json['parentIndex']] if 'parentIndex' in json else None,
            node_type=[int(i) for i in json['nodeType']] if 'nodeType' in json else None,
            node_name=[StringIndex.from_json(i) for i in json['nodeName']] if 'nodeName' in json else None,
            node_value=[StringIndex.from_json(i) for i in json['nodeValue']] if 'nodeValue' in json else None,
            backend_node_id=[dom.BackendNodeId.from_json(i) for i in json['backendNodeId']] if 'backendNodeId' in json else None,
            attributes=[ArrayOfStrings.from_json(i) for i in json['attributes']] if 'attributes' in json else None,
            text_value=RareStringData.from_json(json['textValue']) if 'textValue' in json else None,
            input_value=RareStringData.from_json(json['inputValue']) if 'inputValue' in json else None,
            input_checked=RareBooleanData.from_json(json['inputChecked']) if 'inputChecked' in json else None,
            option_selected=RareBooleanData.from_json(json['optionSelected']) if 'optionSelected' in json else None,
            content_document_index=RareIntegerData.from_json(json['contentDocumentIndex']) if 'contentDocumentIndex' in json else None,
            pseudo_type=RareStringData.from_json(json['pseudoType']) if 'pseudoType' in json else None,
            is_clickable=RareBooleanData.from_json(json['isClickable']) if 'isClickable' in json else None,
            current_source_url=RareStringData.from_json(json['currentSourceURL']) if 'currentSourceURL' in json else None,
            origin_url=RareStringData.from_json(json['originURL']) if 'originURL' in json else None,
        )


@dataclass
class LayoutTreeSnapshot:
    '''
    Table of details of an element in the DOM tree with a LayoutObject.
    '''
    #: Index of the corresponding node in the `NodeTreeSnapshot` array returned by `captureSnapshot`.
    node_index: typing.List[int]

    #: Array of indexes specifying computed style strings, filtered according to the `computedStyles` parameter passed to `captureSnapshot`.
    styles: typing.List['ArrayOfStrings']

    #: The absolute position bounding box.
    bounds: typing.List['Rectangle']

    #: Contents of the LayoutText, if any.
    text: typing.List['StringIndex']

    #: Stacking context information.
    stacking_contexts: 'RareBooleanData'

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['nodeIndex'] = [i for i in self.node_index]
        json['styles'] = [i.to_json() for i in self.styles]
        json['bounds'] = [i.to_json() for i in self.bounds]
        json['text'] = [i.to_json() for i in self.text]
        json['stackingContexts'] = self.stacking_contexts.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'LayoutTreeSnapshot':
        return cls(
            node_index=[int(i) for i in json['nodeIndex']],
            styles=[ArrayOfStrings.from_json(i) for i in json['styles']],
            bounds=[Rectangle.from_json(i) for i in json['bounds']],
            text=[StringIndex.from_json(i) for i in json['text']],
            stacking_contexts=RareBooleanData.from_json(json['stackingContexts']),
        )


@dataclass
class TextBoxSnapshot:
    '''
    Table of details of the post layout rendered text positions. The exact layout should not be regarded as
    stable and may change between versions.
    '''
    #: Index of the layout tree node that owns this box collection.
    layout_index: typing.List[int]

    #: The absolute position bounding box.
    bounds: typing.List['Rectangle']

    #: The starting index in characters, for this post layout textbox substring. Characters that
    #: would be represented as a surrogate pair in UTF-16 have length 2.
    start: typing.List[int]

    #: The number of characters in this post layout textbox substring. Characters that would be
    #: represented as a surrogate pair in UTF-16 have length 2.
    length: typing.List[int]

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['layoutIndex'] = [i for i in self.layout_index]
        json['bounds'] = [i.to_json() for i in self.bounds]
        json['start'] = [i for i in self.start]
        json['length'] = [i for i in self.length]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> 'TextBoxSnapshot':
        return cls(
            layout_index=[int(i) for i in json['layoutIndex']],
            bounds=[Rectangle.from_json(i) for i in json['bounds']],
            start=[int(i) for i in json['start']],
            length=[int(i) for i in json['length']],
        )


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disables DOM snapshot agent for the given page.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'DOMSnapshot.disable',
    }
    json = yield cmd_dict


def enable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enables DOM snapshot agent for the given page.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'DOMSnapshot.enable',
    }
    json = yield cmd_dict


def get_snapshot(
        computed_style_whitelist: typing.List[str],
        include_event_listeners: typing.Optional[bool] = None,
        include_paint_order: typing.Optional[bool] = None,
        include_user_agent_shadow_tree: typing.Optional[bool] = None
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.Tuple[typing.List['DOMNode'], typing.List['LayoutTreeNode'], typing.List['ComputedStyle']]]:
    '''
    Returns a document snapshot, including the full DOM tree of the root node (including iframes,
    template contents, and imported documents) in a flattened array, as well as layout and
    white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
    flattened.

    :param computed_style_whitelist: Whitelist of computed styles to return.
    :param include_event_listeners: Whether or not to retrieve details of DOM listeners (default false).
    :param include_paint_order: Whether to determine and include the paint order index of LayoutTreeNodes (default false).
    :param include_user_agent_shadow_tree: Whether to include UA shadow tree in the snapshot (default false).
    :returns: a tuple with the following items:
        0. domNodes: The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
        1. layoutTreeNodes: The nodes in the layout tree.
        2. computedStyles: Whitelisted ComputedStyle properties for each node in the layout tree.
    '''
    params: T_JSON_DICT = dict()
    params['computedStyleWhitelist'] = [i for i in computed_style_whitelist]
    if include_event_listeners is not None:
        params['includeEventListeners'] = include_event_listeners
    if include_paint_order is not None:
        params['includePaintOrder'] = include_paint_order
    if include_user_agent_shadow_tree is not None:
        params['includeUserAgentShadowTree'] = include_user_agent_shadow_tree
    cmd_dict: T_JSON_DICT = {
        'method': 'DOMSnapshot.getSnapshot',
        'params': params,
    }
    json = yield cmd_dict
    return (
        [DOMNode.from_json(i) for i in json['domNodes']],
        [LayoutTreeNode.from_json(i) for i in json['layoutTreeNodes']],
        [ComputedStyle.from_json(i) for i in json['computedStyles']]
    )


def capture_snapshot(
        computed_styles: typing.List[str]
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.Tuple[typing.List['DocumentSnapshot'], typing.List[str]]]:
    '''
    Returns a document snapshot, including the full DOM tree of the root node (including iframes,
    template contents, and imported documents) in a flattened array, as well as layout and
    white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
    flattened.

    :param computed_styles: Whitelist of computed styles to return.
    :returns: a tuple with the following items:
        0. documents: The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
        1. strings: Shared string table that all string properties refer to with indexes.
    '''
    params: T_JSON_DICT = dict()
    params['computedStyles'] = [i for i in computed_styles]
    cmd_dict: T_JSON_DICT = {
        'method': 'DOMSnapshot.captureSnapshot',
        'params': params,
    }
    json = yield cmd_dict
    return (
        [DocumentSnapshot.from_json(i) for i in json['documents']],
        [str(i) for i in json['strings']]
    )
