# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Article.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rArticle.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"#\n\x07\x41\x64\x64ress\x12\n\n\x02IP\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\t\n\x07\x46\x61shion\"\n\n\x08Politics\"\x08\n\x06Sports\"\xb0\x01\n\rArticleFormat\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.ArticleFormat.Type\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12,\n\x08time_rec\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"-\n\x04Type\x12\x0b\n\x07\x46\x41SHION\x10\x00\x12\n\n\x06SPORTS\x10\x01\x12\x0c\n\x08POLITICS\x10\x02\"\xad\x01\n\x0e\x41rticleRequest\x12\x1b\n\x07\x66\x61shion\x18\x01 \x01(\x0b\x32\x08.FashionH\x00\x12\x1d\n\x08politics\x18\x02 \x01(\x0b\x32\t.PoliticsH\x00\x12\x19\n\x06sports\x18\x03 \x01(\x0b\x32\x07.SportsH\x00\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12,\n\x08time_rec\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\n\x04typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Article_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS._serialized_start=50
  _ADDRESS._serialized_end=85
  _FASHION._serialized_start=87
  _FASHION._serialized_end=96
  _POLITICS._serialized_start=98
  _POLITICS._serialized_end=108
  _SPORTS._serialized_start=110
  _SPORTS._serialized_end=118
  _ARTICLEFORMAT._serialized_start=121
  _ARTICLEFORMAT._serialized_end=297
  _ARTICLEFORMAT_TYPE._serialized_start=252
  _ARTICLEFORMAT_TYPE._serialized_end=297
  _ARTICLEREQUEST._serialized_start=300
  _ARTICLEREQUEST._serialized_end=473
# @@protoc_insertion_point(module_scope)
