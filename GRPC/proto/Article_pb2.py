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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rArticle.proto\x12\x0bgrpc_protos\x1a\x1fgoogle/protobuf/timestamp.proto\"#\n\x07\x41\x64\x64ress\x12\n\n\x02IP\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t\"\t\n\x07\x46\x61shion\"\n\n\x08Politics\"\x08\n\x06Sports\"\xdb\x01\n\x07\x41rticle\x12\'\n\x07\x66\x61shion\x18\x01 \x01(\x0b\x32\x14.grpc_protos.FashionH\x00\x12)\n\x08politics\x18\x02 \x01(\x0b\x32\x15.grpc_protos.PoliticsH\x00\x12%\n\x06sports\x18\x03 \x01(\x0b\x32\x13.grpc_protos.SportsH\x00\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12,\n\x08time_rec\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\tB\x06\n\x04type\"\xd2\x01\n\x0f\x41rticleResquest\x12\'\n\x07\x66\x61shion\x18\x01 \x01(\x0b\x32\x14.grpc_protos.FashionH\x00\x12)\n\x08politics\x18\x02 \x01(\x0b\x32\x15.grpc_protos.PoliticsH\x00\x12%\n\x06sports\x18\x03 \x01(\x0b\x32\x13.grpc_protos.SportsH\x00\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12,\n\x08time_rec\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x06\n\x04typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Article_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS._serialized_start=63
  _ADDRESS._serialized_end=98
  _NAME._serialized_start=100
  _NAME._serialized_end=120
  _FASHION._serialized_start=122
  _FASHION._serialized_end=131
  _POLITICS._serialized_start=133
  _POLITICS._serialized_end=143
  _SPORTS._serialized_start=145
  _SPORTS._serialized_end=153
  _ARTICLE._serialized_start=156
  _ARTICLE._serialized_end=375
  _ARTICLERESQUEST._serialized_start=378
  _ARTICLERESQUEST._serialized_end=588
# @@protoc_insertion_point(module_scope)