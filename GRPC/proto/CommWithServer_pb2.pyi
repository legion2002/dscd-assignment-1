import Article_pb2 as _Article_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetArticlesRequest(_message.Message):
    __slots__ = ["article", "uuid"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    article: _Article_pb2.ArticleRequest
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., article: _Optional[_Union[_Article_pb2.ArticleRequest, _Mapping]] = ...) -> None: ...

class GetArticlesResponse(_message.Message):
    __slots__ = ["article"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    article: _Article_pb2.ArticleFormat
    def __init__(self, article: _Optional[_Union[_Article_pb2.ArticleFormat, _Mapping]] = ...) -> None: ...

class JoinServerRequest(_message.Message):
    __slots__ = ["address", "name", "uuid"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    address: _Article_pb2.Address
    name: str
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[_Union[_Article_pb2.Address, _Mapping]] = ...) -> None: ...

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
    article: _Article_pb2.ArticleFormat
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., article: _Optional[_Union[_Article_pb2.ArticleFormat, _Mapping]] = ...) -> None: ...

class PublishArticlesResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
