# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from .task_service_pb2 import *


class TaskServiceStub(object):
    """The task service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTask = channel.unary_unary(
                '/task_service.TaskService/CreateTask',
                request_serializer=CreateTaskRequest.SerializeToString,
                response_deserializer=TaskResponse.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/task_service.TaskService/UpdateTask',
                request_serializer=UpdateTaskRequest.SerializeToString,
                response_deserializer=TaskResponse.FromString,
                )
        self.DeleteTask = channel.unary_unary(
                '/task_service.TaskService/DeleteTask',
                request_serializer=TaskIdRequest.SerializeToString,
                response_deserializer=DeleteTaskResponse.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/task_service.TaskService/GetTask',
                request_serializer=TaskIdRequest.SerializeToString,
                response_deserializer=TaskResponse.FromString,
                )
        self.ListTasks = channel.unary_unary(
                '/task_service.TaskService/ListTasks',
                request_serializer=ListTasksRequest.SerializeToString,
                response_deserializer=ListTasksResponse.FromString,
                )


class TaskServiceServicer(object):
    """The task service definition.
    """

    def CreateTask(self, request, context):
        """Creates a new task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Updates an existing task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Deletes a task.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Gets a task by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """Lists tasks with pagination.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=CreateTaskRequest.FromString,
                    response_serializer=TaskResponse.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=UpdateTaskRequest.FromString,
                    response_serializer=TaskResponse.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=TaskIdRequest.FromString,
                    response_serializer=DeleteTaskResponse.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=TaskIdRequest.FromString,
                    response_serializer=TaskResponse.SerializeToString,
            ),
            'ListTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTasks,
                    request_deserializer=ListTasksRequest.FromString,
                    response_serializer=ListTasksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'task_service.TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """The task service definition.
    """

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task_service.TaskService/CreateTask',
            task__service__pb2.CreateTaskRequest.SerializeToString,
            task__service__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task_service.TaskService/UpdateTask',
            task__service__pb2.UpdateTaskRequest.SerializeToString,
            task__service__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task_service.TaskService/DeleteTask',
            task__service__pb2.TaskIdRequest.SerializeToString,
            task__service__pb2.DeleteTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task_service.TaskService/GetTask',
            task__service__pb2.TaskIdRequest.SerializeToString,
            task__service__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task_service.TaskService/ListTasks',
            task__service__pb2.ListTasksRequest.SerializeToString,
            task__service__pb2.ListTasksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)