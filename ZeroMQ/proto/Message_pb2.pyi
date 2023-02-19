from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    __slots__ = ["author", "time_rec", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ANYTHING: ArticleRequest.Type
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    FASHION: ArticleRequest.Type
    POLITICS: ArticleRequest.Type
    SPORTS: ArticleRequest.Type
    TIME_REC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    author: str
    time_rec: _timestamp_pb2.Timestamp
    type: ArticleRequest.Type
    def __init__(self, type: _Optional[_Union[ArticleRequest.Type, str]] = ..., author: _Optional[str] = ..., time_rec: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetArticlesRequest(_message.Message):
    __slots__ = ["article", "uuid"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    article: ArticleRequest
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., article: _Optional[_Union[ArticleRequest, _Mapping]] = ...) -> None: ...

class GetArticlesResponse(_message.Message):
    __slots__ = ["article"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    article: _containers.RepeatedCompositeFieldContainer[ArticleFormat]
    def __init__(self, article: _Optional[_Iterable[_Union[ArticleFormat, _Mapping]]] = ...) -> None: ...

class GetServerListRequest(_message.Message):
    __slots__ = ["address", "name", "typeOfRequest"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPEOFREQUEST_FIELD_NUMBER: _ClassVar[int]
    address: Address
    name: str
    typeOfRequest: str
    def __init__(self, typeOfRequest: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class GetServerListResponse(_message.Message):
    __slots__ = ["serverDetails"]
    SERVERDETAILS_FIELD_NUMBER: _ClassVar[int]
    serverDetails: _containers.RepeatedCompositeFieldContainer[ServerAddress]
    def __init__(self, serverDetails: _Optional[_Iterable[_Union[ServerAddress, _Mapping]]] = ...) -> None: ...

class JoinServerRequest(_message.Message):
    __slots__ = ["address", "name", "uuid"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    address: Address
    name: str
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class JoinServerResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class LeaveServerRequest(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class LeaveServerResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class PublishArticlesRequest(_message.Message):
    __slots__ = ["article", "uuid"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    article: ArticleFormat
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., article: _Optional[_Union[ArticleFormat, _Mapping]] = ...) -> None: ...

class PublishArticlesResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ["address", "name", "typeOfRequest"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPEOFREQUEST_FIELD_NUMBER: _ClassVar[int]
    address: Address
    name: str
    typeOfRequest: str
    def __init__(self, typeOfRequest: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ServerAddress(_message.Message):
    __slots__ = ["address", "name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    address: Address
    name: str
    def __init__(self, name: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class StandardFormat(_message.Message):
    __slots__ = ["getArticles", "join", "leave", "publish", "typeOfRequest"]
    GETARTICLES_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    LEAVE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    TYPEOFREQUEST_FIELD_NUMBER: _ClassVar[int]
    getArticles: GetArticlesRequest
    join: JoinServerRequest
    leave: LeaveServerRequest
    publish: PublishArticlesRequest
    typeOfRequest: str
    def __init__(self, typeOfRequest: _Optional[str] = ..., join: _Optional[_Union[JoinServerRequest, _Mapping]] = ..., leave: _Optional[_Union[LeaveServerRequest, _Mapping]] = ..., getArticles: _Optional[_Union[GetArticlesRequest, _Mapping]] = ..., publish: _Optional[_Union[PublishArticlesRequest, _Mapping]] = ...) -> None: ...
