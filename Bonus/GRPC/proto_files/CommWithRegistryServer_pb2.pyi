import Article_pb2 as _Article_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServerListRequest(_message.Message):
    __slots__ = ["address", "name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    address: _Article_pb2.Address
    name: str
    def __init__(self, name: _Optional[str] = ..., address: _Optional[_Union[_Article_pb2.Address, _Mapping]] = ...) -> None: ...

class GetServerListResponse(_message.Message):
    __slots__ = ["address", "name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    address: _Article_pb2.Address
    name: str
    def __init__(self, name: _Optional[str] = ..., address: _Optional[_Union[_Article_pb2.Address, _Mapping]] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ["address", "name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    address: _Article_pb2.Address
    name: str
    def __init__(self, name: _Optional[str] = ..., address: _Optional[_Union[_Article_pb2.Address, _Mapping]] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
