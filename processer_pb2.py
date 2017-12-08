# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: processer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='processer.proto',
  package='nlp',
  syntax='proto3',
  serialized_pb=_b('\n\x0fprocesser.proto\x12\x03nlp\"4\n\x0cInputRequest\x12\r\n\x05input\x18\x01 \x01(\t\x12\x15\n\routputs_count\x18\x02 \x01(\x05\"/\n\rReloadRequest\x12\x0c\n\x04\x63mds\x18\x01 \x03(\t\x12\x10\n\x08\x66ilepath\x18\x02 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eOutputResponse\x12\x0f\n\x07results\x18\x01 \x03(\t2m\n\tProcesser\x12\x31\n\x05Input\x12\x11.nlp.InputRequest\x1a\x13.nlp.OutputResponse\"\x00\x12-\n\x06Reload\x12\x12.nlp.ReloadRequest\x1a\r.nlp.Response\"\x00\x62\x06proto3')
)




_INPUTREQUEST = _descriptor.Descriptor(
  name='InputRequest',
  full_name='nlp.InputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='nlp.InputRequest.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs_count', full_name='nlp.InputRequest.outputs_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=76,
)


_RELOADREQUEST = _descriptor.Descriptor(
  name='ReloadRequest',
  full_name='nlp.ReloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmds', full_name='nlp.ReloadRequest.cmds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filepath', full_name='nlp.ReloadRequest.filepath', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=125,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='nlp.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='nlp.Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=154,
)


_OUTPUTRESPONSE = _descriptor.Descriptor(
  name='OutputResponse',
  full_name='nlp.OutputResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='nlp.OutputResponse.results', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=189,
)

DESCRIPTOR.message_types_by_name['InputRequest'] = _INPUTREQUEST
DESCRIPTOR.message_types_by_name['ReloadRequest'] = _RELOADREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['OutputResponse'] = _OUTPUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputRequest = _reflection.GeneratedProtocolMessageType('InputRequest', (_message.Message,), dict(
  DESCRIPTOR = _INPUTREQUEST,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:nlp.InputRequest)
  ))
_sym_db.RegisterMessage(InputRequest)

ReloadRequest = _reflection.GeneratedProtocolMessageType('ReloadRequest', (_message.Message,), dict(
  DESCRIPTOR = _RELOADREQUEST,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:nlp.ReloadRequest)
  ))
_sym_db.RegisterMessage(ReloadRequest)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:nlp.Response)
  ))
_sym_db.RegisterMessage(Response)

OutputResponse = _reflection.GeneratedProtocolMessageType('OutputResponse', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTRESPONSE,
  __module__ = 'processer_pb2'
  # @@protoc_insertion_point(class_scope:nlp.OutputResponse)
  ))
_sym_db.RegisterMessage(OutputResponse)



_PROCESSER = _descriptor.ServiceDescriptor(
  name='Processer',
  full_name='nlp.Processer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=191,
  serialized_end=300,
  methods=[
  _descriptor.MethodDescriptor(
    name='Input',
    full_name='nlp.Processer.Input',
    index=0,
    containing_service=None,
    input_type=_INPUTREQUEST,
    output_type=_OUTPUTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Reload',
    full_name='nlp.Processer.Reload',
    index=1,
    containing_service=None,
    input_type=_RELOADREQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROCESSER)

DESCRIPTOR.services_by_name['Processer'] = _PROCESSER

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class ProcesserStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Input = channel.unary_unary(
          '/nlp.Processer/Input',
          request_serializer=InputRequest.SerializeToString,
          response_deserializer=OutputResponse.FromString,
          )
      self.Reload = channel.unary_unary(
          '/nlp.Processer/Reload',
          request_serializer=ReloadRequest.SerializeToString,
          response_deserializer=Response.FromString,
          )


  class ProcesserServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Input(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Reload(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_ProcesserServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Input': grpc.unary_unary_rpc_method_handler(
            servicer.Input,
            request_deserializer=InputRequest.FromString,
            response_serializer=OutputResponse.SerializeToString,
        ),
        'Reload': grpc.unary_unary_rpc_method_handler(
            servicer.Reload,
            request_deserializer=ReloadRequest.FromString,
            response_serializer=Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'nlp.Processer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaProcesserServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Input(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Reload(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaProcesserStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Input(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Input.future = None
    def Reload(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Reload.future = None


  def beta_create_Processer_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('nlp.Processer', 'Input'): InputRequest.FromString,
      ('nlp.Processer', 'Reload'): ReloadRequest.FromString,
    }
    response_serializers = {
      ('nlp.Processer', 'Input'): OutputResponse.SerializeToString,
      ('nlp.Processer', 'Reload'): Response.SerializeToString,
    }
    method_implementations = {
      ('nlp.Processer', 'Input'): face_utilities.unary_unary_inline(servicer.Input),
      ('nlp.Processer', 'Reload'): face_utilities.unary_unary_inline(servicer.Reload),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Processer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('nlp.Processer', 'Input'): InputRequest.SerializeToString,
      ('nlp.Processer', 'Reload'): ReloadRequest.SerializeToString,
    }
    response_deserializers = {
      ('nlp.Processer', 'Input'): OutputResponse.FromString,
      ('nlp.Processer', 'Reload'): Response.FromString,
    }
    cardinalities = {
      'Input': cardinality.Cardinality.UNARY_UNARY,
      'Reload': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'nlp.Processer', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
