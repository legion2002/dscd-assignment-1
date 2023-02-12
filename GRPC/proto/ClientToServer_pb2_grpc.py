# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ClientToServer_pb2 as ClientToServer__pb2


class ClientToServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinServer = channel.unary_unary(
                '/grpc_protos.ClientToServer/JoinServer',
                request_serializer=ClientToServer__pb2.JoinServerRequest.SerializeToString,
                response_deserializer=ClientToServer__pb2.JoinServerResponse.FromString,
                )
        self.LeaveServer = channel.unary_unary(
                '/grpc_protos.ClientToServer/LeaveServer',
                request_serializer=ClientToServer__pb2.LeaveServerRequest.SerializeToString,
                response_deserializer=ClientToServer__pb2.LeaveServerResponse.FromString,
                )
        self.GetArticles = channel.unary_stream(
                '/grpc_protos.ClientToServer/GetArticles',
                request_serializer=ClientToServer__pb2.GetArticlesRequest.SerializeToString,
                response_deserializer=ClientToServer__pb2.GetArticlesResponse.FromString,
                )
        self.PublishArticles = channel.unary_unary(
                '/grpc_protos.ClientToServer/PublishArticles',
                request_serializer=ClientToServer__pb2.PublishArticlesRequest.SerializeToString,
                response_deserializer=ClientToServer__pb2.PublishArticlesResponse.FromString,
                )


class ClientToServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LeaveServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetArticles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishArticles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientToServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinServer': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinServer,
                    request_deserializer=ClientToServer__pb2.JoinServerRequest.FromString,
                    response_serializer=ClientToServer__pb2.JoinServerResponse.SerializeToString,
            ),
            'LeaveServer': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveServer,
                    request_deserializer=ClientToServer__pb2.LeaveServerRequest.FromString,
                    response_serializer=ClientToServer__pb2.LeaveServerResponse.SerializeToString,
            ),
            'GetArticles': grpc.unary_stream_rpc_method_handler(
                    servicer.GetArticles,
                    request_deserializer=ClientToServer__pb2.GetArticlesRequest.FromString,
                    response_serializer=ClientToServer__pb2.GetArticlesResponse.SerializeToString,
            ),
            'PublishArticles': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishArticles,
                    request_deserializer=ClientToServer__pb2.PublishArticlesRequest.FromString,
                    response_serializer=ClientToServer__pb2.PublishArticlesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_protos.ClientToServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientToServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_protos.ClientToServer/JoinServer',
            ClientToServer__pb2.JoinServerRequest.SerializeToString,
            ClientToServer__pb2.JoinServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LeaveServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_protos.ClientToServer/LeaveServer',
            ClientToServer__pb2.LeaveServerRequest.SerializeToString,
            ClientToServer__pb2.LeaveServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetArticles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc_protos.ClientToServer/GetArticles',
            ClientToServer__pb2.GetArticlesRequest.SerializeToString,
            ClientToServer__pb2.GetArticlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishArticles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_protos.ClientToServer/PublishArticles',
            ClientToServer__pb2.PublishArticlesRequest.SerializeToString,
            ClientToServer__pb2.PublishArticlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)