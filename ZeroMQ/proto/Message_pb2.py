# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rMessage.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"#\n\x07\x41\x64\x64ress\x12\n\n\x02IP\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\xd1\x01\n\x0eStandardFormat\x12\x15\n\rtypeOfRequest\x18\x01 \x01(\t\x12\"\n\x04join\x18\x02 \x01(\x0b\x32\x12.JoinServerRequestH\x00\x12$\n\x05leave\x18\x03 \x01(\x0b\x32\x13.LeaveServerRequestH\x00\x12*\n\x0bgetArticles\x18\x04 \x01(\x0b\x32\x13.GetArticlesRequestH\x00\x12*\n\x07publish\x18\x05 \x01(\x0b\x32\x17.PublishArticlesRequestH\x00\x42\x06\n\x04\x64\x61ta\"8\n\rServerAddress\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x08.Address\"\xb0\x01\n\rArticleFormat\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.ArticleFormat.Type\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12,\n\x08time_rec\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"-\n\x04Type\x12\x0b\n\x07\x46\x41SHION\x10\x00\x12\n\n\x06SPORTS\x10\x01\x12\x0c\n\x08POLITICS\x10\x02\"\xaf\x01\n\x0e\x41rticleRequest\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.ArticleRequest.Type\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12,\n\x08time_rec\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\";\n\x04Type\x12\x0b\n\x07\x46\x41SHION\x10\x00\x12\n\n\x06SPORTS\x10\x01\x12\x0c\n\x08POLITICS\x10\x02\x12\x0c\n\x08\x41NYTHING\x10\x03\"V\n\x14GetServerListRequest\x12\x15\n\rtypeOfRequest\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x08.Address\">\n\x15GetServerListResponse\x12%\n\rserverDetails\x18\x01 \x03(\x0b\x32\x0e.ServerAddress\"Q\n\x0fRegisterRequest\x12\x15\n\rtypeOfRequest\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x08.Address\"\"\n\x10RegisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"a\n\x11JoinServerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x08.Address\x12\x15\n\rtypeOfRequest\x18\x04 \x01(\t\"9\n\x12LeaveServerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x15\n\rtypeOfRequest\x18\x02 \x01(\t\"[\n\x12GetArticlesRequest\x12\x15\n\rtypeOfRequest\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12 \n\x07\x61rticle\x18\x03 \x01(\x0b\x32\x0f.ArticleRequest\"^\n\x16PublishArticlesRequest\x12\x15\n\rtypeOfRequest\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x1f\n\x07\x61rticle\x18\x03 \x01(\x0b\x32\x0e.ArticleFormat\"$\n\x12JoinServerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"%\n\x13LeaveServerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"6\n\x13GetArticlesResponse\x12\x1f\n\x07\x61rticle\x18\x01 \x03(\x0b\x32\x0e.ArticleFormat\")\n\x17PublishArticlesResponse\x12\x0e\n\x06status\x18\x01 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS._serialized_start=50
  _ADDRESS._serialized_end=85
  _STANDARDFORMAT._serialized_start=88
  _STANDARDFORMAT._serialized_end=297
  _SERVERADDRESS._serialized_start=299
  _SERVERADDRESS._serialized_end=355
  _ARTICLEFORMAT._serialized_start=358
  _ARTICLEFORMAT._serialized_end=534
  _ARTICLEFORMAT_TYPE._serialized_start=489
  _ARTICLEFORMAT_TYPE._serialized_end=534
  _ARTICLEREQUEST._serialized_start=537
  _ARTICLEREQUEST._serialized_end=712
  _ARTICLEREQUEST_TYPE._serialized_start=653
  _ARTICLEREQUEST_TYPE._serialized_end=712
  _GETSERVERLISTREQUEST._serialized_start=714
  _GETSERVERLISTREQUEST._serialized_end=800
  _GETSERVERLISTRESPONSE._serialized_start=802
  _GETSERVERLISTRESPONSE._serialized_end=864
  _REGISTERREQUEST._serialized_start=866
  _REGISTERREQUEST._serialized_end=947
  _REGISTERRESPONSE._serialized_start=949
  _REGISTERRESPONSE._serialized_end=983
  _JOINSERVERREQUEST._serialized_start=985
  _JOINSERVERREQUEST._serialized_end=1082
  _LEAVESERVERREQUEST._serialized_start=1084
  _LEAVESERVERREQUEST._serialized_end=1141
  _GETARTICLESREQUEST._serialized_start=1143
  _GETARTICLESREQUEST._serialized_end=1234
  _PUBLISHARTICLESREQUEST._serialized_start=1236
  _PUBLISHARTICLESREQUEST._serialized_end=1330
  _JOINSERVERRESPONSE._serialized_start=1332
  _JOINSERVERRESPONSE._serialized_end=1368
  _LEAVESERVERRESPONSE._serialized_start=1370
  _LEAVESERVERRESPONSE._serialized_end=1407
  _GETARTICLESRESPONSE._serialized_start=1409
  _GETARTICLESRESPONSE._serialized_end=1463
  _PUBLISHARTICLESRESPONSE._serialized_start=1465
  _PUBLISHARTICLESRESPONSE._serialized_end=1506
# @@protoc_insertion_point(module_scope)
