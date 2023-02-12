import Article_pb2 as _Article_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FAIL: Status
SUCCESS: Status

class GetArticlesRequest(_message.Message):
    __slots__ = ["ArticleResquest", "uuid"]
    ARTICLERESQUEST_FIELD_NUMBER: _ClassVar[int]
    ArticleResquest: _Article_pb2.Article
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., ArticleResquest: _Optional[_Union[_Article_pb2.Article, _Mapping]] = ...) -> None: ...

class GetArticlesResponse(_message.Message):
    __slots__ = ["Article"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    Article: _Article_pb2.Article
    def __init__(self, Article: _Optional[_Union[_Article_pb2.Article, _Mapping]] = ...) -> None: ...

class JoinServerRequest(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class JoinServerResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, str]] = ...) -> None: ...

class LeaveServerRequest(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class LeaveServerResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, str]] = ...) -> None: ...

class PublishArticlesRequest(_message.Message):
    __slots__ = ["Article", "uuid"]
    ARTICLE_FIELD_NUMBER: _ClassVar[int]
    Article: _Article_pb2.Article
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., Article: _Optional[_Union[_Article_pb2.Article, _Mapping]] = ...) -> None: ...

class PublishArticlesResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
