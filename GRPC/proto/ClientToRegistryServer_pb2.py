# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ClientToRegistryServer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Article_pb2 as Article__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x43lientToRegistryServer.proto\x1a\rArticle.proto\"F\n\x14GetServerListRequest\x12\x13\n\x04name\x18\x01 \x01(\x0b\x32\x05.Name\x12\x19\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x08.Address\"G\n\x15GetServerListResponse\x12\x13\n\x04name\x18\x01 \x01(\x0b\x32\x05.Name\x12\x19\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x08.Address2\\\n\x16\x43lientToRegistryServer\x12\x42\n\rGetServerList\x12\x15.GetServerListRequest\x1a\x16.GetServerListResponse\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ClientToRegistryServer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETSERVERLISTREQUEST._serialized_start=47
  _GETSERVERLISTREQUEST._serialized_end=117
  _GETSERVERLISTRESPONSE._serialized_start=119
  _GETSERVERLISTRESPONSE._serialized_end=190
  _CLIENTTOREGISTRYSERVER._serialized_start=192
  _CLIENTTOREGISTRYSERVER._serialized_end=284
# @@protoc_insertion_point(module_scope)
