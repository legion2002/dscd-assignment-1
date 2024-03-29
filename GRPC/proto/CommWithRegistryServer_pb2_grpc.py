# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import CommWithRegistryServer_pb2 as CommWithRegistryServer__pb2


class CommWithRegistryServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServerList = channel.unary_stream(
                '/CommWithRegistryServer/GetServerList',
                request_serializer=CommWithRegistryServer__pb2.GetServerListRequest.SerializeToString,
                response_deserializer=CommWithRegistryServer__pb2.GetServerListResponse.FromString,
                )
        self.Register = channel.unary_unary(
                '/CommWithRegistryServer/Register',
                request_serializer=CommWithRegistryServer__pb2.RegisterRequest.SerializeToString,
                response_deserializer=CommWithRegistryServer__pb2.RegisterResponse.FromString,
                )


class CommWithRegistryServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServerList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommWithRegistryServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServerList': grpc.unary_stream_rpc_method_handler(
                    servicer.GetServerList,
                    request_deserializer=CommWithRegistryServer__pb2.GetServerListRequest.FromString,
                    response_serializer=CommWithRegistryServer__pb2.GetServerListResponse.SerializeToString,
            ),
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=CommWithRegistryServer__pb2.RegisterRequest.FromString,
                    response_serializer=CommWithRegistryServer__pb2.RegisterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommWithRegistryServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommWithRegistryServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServerList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/CommWithRegistryServer/GetServerList',
            CommWithRegistryServer__pb2.GetServerListRequest.SerializeToString,
            CommWithRegistryServer__pb2.GetServerListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommWithRegistryServer/Register',
            CommWithRegistryServer__pb2.RegisterRequest.SerializeToString,
            CommWithRegistryServer__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
