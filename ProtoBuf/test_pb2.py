# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\"\x17\n\x07TestMsg\x12\x0c\n\x04name\x18\x01 \x01(\tb\x06proto3'
)




_TESTMSG = _descriptor.Descriptor(
  name='TestMsg',
  full_name='TestMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='TestMsg.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=37,
)

DESCRIPTOR.message_types_by_name['TestMsg'] = _TESTMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMsg = _reflection.GeneratedProtocolMessageType('TestMsg', (_message.Message,), {
  'DESCRIPTOR' : _TESTMSG,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:TestMsg)
  })
_sym_db.RegisterMessage(TestMsg)


# @@protoc_insertion_point(module_scope)
