# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/helloworld.Greeter/SayHello',
                request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )
        self.ListFeatures = channel.unary_stream(
                '/helloworld.Greeter/ListFeatures',
                request_serializer=helloworld__pb2.Rectangle.SerializeToString,
                response_deserializer=helloworld__pb2.Feature.FromString,
                )
        self.RecordRoute = channel.stream_unary(
                '/helloworld.Greeter/RecordRoute',
                request_serializer=helloworld__pb2.Point.SerializeToString,
                response_deserializer=helloworld__pb2.RouteSummary.FromString,
                )
        self.RouteChat = channel.stream_stream(
                '/helloworld.Greeter/RouteChat',
                request_serializer=helloworld__pb2.RouteNote.SerializeToString,
                response_deserializer=helloworld__pb2.RouteNote.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFeatures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordRoute(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteChat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=helloworld__pb2.HelloRequest.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
            'ListFeatures': grpc.unary_stream_rpc_method_handler(
                    servicer.ListFeatures,
                    request_deserializer=helloworld__pb2.Rectangle.FromString,
                    response_serializer=helloworld__pb2.Feature.SerializeToString,
            ),
            'RecordRoute': grpc.stream_unary_rpc_method_handler(
                    servicer.RecordRoute,
                    request_deserializer=helloworld__pb2.Point.FromString,
                    response_serializer=helloworld__pb2.RouteSummary.SerializeToString,
            ),
            'RouteChat': grpc.stream_stream_rpc_method_handler(
                    servicer.RouteChat,
                    request_deserializer=helloworld__pb2.RouteNote.FromString,
                    response_serializer=helloworld__pb2.RouteNote.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/SayHello',
            helloworld__pb2.HelloRequest.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld.Greeter/ListFeatures',
            helloworld__pb2.Rectangle.SerializeToString,
            helloworld__pb2.Feature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordRoute(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/helloworld.Greeter/RecordRoute',
            helloworld__pb2.Point.SerializeToString,
            helloworld__pb2.RouteSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteChat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/helloworld.Greeter/RouteChat',
            helloworld__pb2.RouteNote.SerializeToString,
            helloworld__pb2.RouteNote.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)