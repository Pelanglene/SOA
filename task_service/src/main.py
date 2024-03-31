from concurrent import futures
import grpc

import protocols.task_service_pb2_grpc as task_service_pb2_grpc
import protocols.task_service_pb2 as task_service_pb2

from database import get_db_session
from crud import create_task, update_task, delete_task, get_task_by_id, list_tasks


class TaskService(task_service_pb2_grpc.TaskServiceServicer):
    def CreateTask(self, request, context):
        db_session = get_db_session()
        try:
            task = create_task(
                db=db_session,
                title=request.title,
                description=request.description,
                deadline=request.deadline.ToDatetime()
            )
            return task_service_pb2.TaskResponse(
                id=task.id,
                title=task.title,
                description=task.description,
                deadline=task.deadline.isoformat(),
                is_completed=task.is_completed
            )
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def UpdateTask(self, request, context):
        db_session = get_db_session()
        try:
            task = update_task(
                db=db_session,
                task_id=request.id,
                title=request.title,
                description=request.description,
                deadline=request.deadline.ToDatetime(),
                is_completed=request.is_completed
            )
            return task_service_pb2.TaskResponse(
                id=task.id,
                title=task.title,
                description=task.description,
                deadline=task.deadline.isoformat(),
                is_completed=task.is_completed
            )
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def DeleteTask(self, request, context):
        db_session = get_db_session()
        try:
            success = delete_task(
                db=db_session,
                task_id=request.id
            )
            return task_service_pb2.DeleteTaskResponse(success=success)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetTask(self, request, context):
        db_session = get_db_session()
        try:
            task = get_task_by_id(
                db=db_session,
                task_id=request.id
            )
            if task:
                return task_service_pb2.TaskResponse(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    deadline=task.deadline.isoformat(),
                    is_completed=task.is_completed
                )
            else:
                context.abort(grpc.StatusCode.NOT_FOUND, 'Task not found')
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListTasks(self, request, context):
        db_session = get_db_session()
        try:
            tasks = list_tasks(
                db=db_session,
                page=request.page,
                page_size=request.page_size
            )
            # Преобразование списка задач в формат ответа gRPC
            list_response = task_service_pb2.ListTasksResponse()
            for task in tasks:
                task_resp = task_service_pb2.TaskResponse(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    deadline=task.deadline.isoformat(),
                    is_completed=task.is_completed
                )
                list_response.tasks.append(task_resp)
            return list_response
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_service_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("amogus")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    print('bebra')
    serve()
