from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ["IP", "port"]
    IP: str
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    port: int
    def __init__(self, IP: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ArticleFormat(_message.Message):
    __slots__ = ["author", "content", "time_rec", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FASHION: ArticleFormat.Type
    POLITICS: ArticleFormat.Type
    SPORTS: ArticleFormat.Type
    TIME_REC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    author: str
    content: str
    time_rec: _timestamp_pb2.Timestamp
    type: ArticleFormat.Type
    def __init__(self, type: _Optional[_Union[ArticleFormat.Type, str]] = ..., author: _Optional[str] = ..., time_rec: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., content: _Optional[str] = ...) -> None: ...

class ArticleRequest(_message.Message):
    __slots__ = ["author", "fashion", "politics", "sports", "time_rec"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    FASHION_FIELD_NUMBER: _ClassVar[int]
    POLITICS_FIELD_NUMBER: _ClassVar[int]
    SPORTS_FIELD_NUMBER: _ClassVar[int]
    TIME_REC_FIELD_NUMBER: _ClassVar[int]
    author: str
    fashion: Fashion
    politics: Politics
    sports: Sports
    time_rec: _timestamp_pb2.Timestamp
    def __init__(self, fashion: _Optional[_Union[Fashion, _Mapping]] = ..., politics: _Optional[_Union[Politics, _Mapping]] = ..., sports: _Optional[_Union[Sports, _Mapping]] = ..., author: _Optional[str] = ..., time_rec: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Fashion(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Politics(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Sports(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
