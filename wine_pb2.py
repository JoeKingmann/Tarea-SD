# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wine.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nwine.proto\x12\x04wine\"\x1b\n\rTasterRequest\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\x0eTasterResponse\x12\x12\n\ntasterName\x18\x01 \x01(\t\x12\x11\n\tfromCache\x18\x02 \x01(\x08\x32J\n\nWineTaster\x12<\n\rGetTasterInfo\x12\x13.wine.TasterRequest\x1a\x14.wine.TasterResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wine_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TASTERREQUEST']._serialized_start=20
  _globals['_TASTERREQUEST']._serialized_end=47
  _globals['_TASTERRESPONSE']._serialized_start=49
  _globals['_TASTERRESPONSE']._serialized_end=104
  _globals['_WINETASTER']._serialized_start=106
  _globals['_WINETASTER']._serialized_end=180
# @@protoc_insertion_point(module_scope)