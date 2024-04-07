FROM python:3.8

RUN pip install grpcio-tools

# compile proto
WORKDIR /app

COPY protocols/tasks.proto ./tasks.proto

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. tasks.proto

COPY ./task_service/src/* .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
