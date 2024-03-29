# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import users_pb2 as users__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/users.Users/GetUser',
                request_serializer=users__pb2.UserRequest.SerializeToString,
                response_deserializer=users__pb2.UserResponse.FromString,
                )
        self.GetUsers = channel.unary_unary(
                '/users.Users/GetUsers',
                request_serializer=users__pb2.UsersRequest.SerializeToString,
                response_deserializer=users__pb2.UsersResponse.FromString,
                )
        self.GetUsersAll = channel.unary_stream(
                '/users.Users/GetUsersAll',
                request_serializer=users__pb2.UsersRequestStream.SerializeToString,
                response_deserializer=users__pb2.UsersResponseStream.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsersAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=users__pb2.UserRequest.FromString,
                    response_serializer=users__pb2.UserResponse.SerializeToString,
            ),
            'GetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=users__pb2.UsersRequest.FromString,
                    response_serializer=users__pb2.UsersResponse.SerializeToString,
            ),
            'GetUsersAll': grpc.unary_stream_rpc_method_handler(
                    servicer.GetUsersAll,
                    request_deserializer=users__pb2.UsersRequestStream.FromString,
                    response_serializer=users__pb2.UsersResponseStream.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'users.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/GetUser',
            users__pb2.UserRequest.SerializeToString,
            users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/GetUsers',
            users__pb2.UsersRequest.SerializeToString,
            users__pb2.UsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsersAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/users.Users/GetUsersAll',
            users__pb2.UsersRequestStream.SerializeToString,
            users__pb2.UsersResponseStream.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
