# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import CommWithServer_pb2 as CommWithServer__pb2


class CommWithServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinServer = channel.unary_unary(
                '/CommWithServer/JoinServer',
                request_serializer=CommWithServer__pb2.JoinServerRequest.SerializeToString,
                response_deserializer=CommWithServer__pb2.JoinServerResponse.FromString,
                )
        self.LeaveServer = channel.unary_unary(
                '/CommWithServer/LeaveServer',
                request_serializer=CommWithServer__pb2.LeaveServerRequest.SerializeToString,
                response_deserializer=CommWithServer__pb2.LeaveServerResponse.FromString,
                )
        self.GetArticles = channel.unary_stream(
                '/CommWithServer/GetArticles',
                request_serializer=CommWithServer__pb2.GetArticlesRequest.SerializeToString,
                response_deserializer=CommWithServer__pb2.GetArticlesResponse.FromString,
                )
        self.PublishArticles = channel.unary_unary(
                '/CommWithServer/PublishArticles',
                request_serializer=CommWithServer__pb2.PublishArticlesRequest.SerializeToString,
                response_deserializer=CommWithServer__pb2.PublishArticlesResponse.FromString,
                )


class CommWithServerServicer(object):
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


def add_CommWithServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinServer': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinServer,
                    request_deserializer=CommWithServer__pb2.JoinServerRequest.FromString,
                    response_serializer=CommWithServer__pb2.JoinServerResponse.SerializeToString,
            ),
            'LeaveServer': grpc.unary_unary_rpc_method_handler(
                    servicer.LeaveServer,
                    request_deserializer=CommWithServer__pb2.LeaveServerRequest.FromString,
                    response_serializer=CommWithServer__pb2.LeaveServerResponse.SerializeToString,
            ),
            'GetArticles': grpc.unary_stream_rpc_method_handler(
                    servicer.GetArticles,
                    request_deserializer=CommWithServer__pb2.GetArticlesRequest.FromString,
                    response_serializer=CommWithServer__pb2.GetArticlesResponse.SerializeToString,
            ),
            'PublishArticles': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishArticles,
                    request_deserializer=CommWithServer__pb2.PublishArticlesRequest.FromString,
                    response_serializer=CommWithServer__pb2.PublishArticlesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommWithServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommWithServer(object):
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
        return grpc.experimental.unary_unary(request, target, '/CommWithServer/JoinServer',
            CommWithServer__pb2.JoinServerRequest.SerializeToString,
            CommWithServer__pb2.JoinServerResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/CommWithServer/LeaveServer',
            CommWithServer__pb2.LeaveServerRequest.SerializeToString,
            CommWithServer__pb2.LeaveServerResponse.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/CommWithServer/GetArticles',
            CommWithServer__pb2.GetArticlesRequest.SerializeToString,
            CommWithServer__pb2.GetArticlesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/CommWithServer/PublishArticles',
            CommWithServer__pb2.PublishArticlesRequest.SerializeToString,
            CommWithServer__pb2.PublishArticlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
