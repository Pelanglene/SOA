from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import os
from flask_migrate import Migrate

from .test import aboba

import grpc
from .task_service_pb2_grpc import *
from .task_service_pb2 import *

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birthdate = db.Column(db.Date)
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))


GRPC_CHANNEL = grpc.insecure_channel(os.environ.get("GRPC_SERVER_URI"))
GRPC_TASK_SERVICE_STUB = TaskServiceStub(GRPC_CHANNEL)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        print("token:", token)

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print("data:", data)
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        
        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/api/tasks/create', methods=['POST'])
@token_required
def create_grpc_task(current_user):
    data = request.get_json()
    response = GRPC_TASK_SERVICE_STUB.CreateTask(
        CreateTaskRequest(
            title=data['title'], 
            description=data['description']
        )
    )
    return jsonify({
        'id': response.id,
        'title': response.title,
        'description': response.description
    }), 201


@app.route('/api/tasks/update/<int:task_id>', methods=['PUT'])
@token_required
def update_grpc_task(current_user, task_id):
    data = request.get_json()
    response = GRPC_TASK_SERVICE_STUB.UpdateTask(
        UpdateTaskRequest(
            id=task_id,
            title=data['title'], 
            description=data['description'],
            is_completed=data['is_completed']
        )
    )
    return jsonify({
        'id': response.id,
        'title': response.title,
        'description': response.description,
        'is_completed': response.is_completed
    }), 200


@app.route('/api/tasks/delete/<int:task_id>', methods=['DELETE'])
@token_required
def delete_grpc_task(current_user, task_id):
    response = GRPC_TASK_SERVICE_STUB.DeleteTask(
        DeleteTaskRequest(id=task_id)
    )
    return jsonify({'success': response.success}), 200


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
@token_required
def get_grpc_task(current_user, task_id):
    response = GRPC_TASK_SERVICE_STUB.GetTask(
        GetTaskRequest(id=task_id)
    )
    return jsonify({
        'id': response.id,
        'title': response.title,
        'description': response.description,
        'is_completed': response.is_completed
    }), 200


@app.route('/api/tasks/', methods=['GET'])
@token_required
def list_grpc_tasks(current_user):
    page = request.args.get('page', 0, type=int)
    page_size = request.args.get('page_size', 10, type=int)
    response = GRPC_TASK_SERVICE_STUB.ListTasks(
        ListTasksRequest(page=page, page_size=page_size)
    )
    tasks = [{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'is_completed': task.is_completed
    } for task in response.tasks]
    return jsonify(tasks), 200

@app.route('/api/users/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256', salt_length=16)

    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/users/auth', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return jsonify({'message': 'User not found!'}), 404

    if check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        print("token:", token)
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Wrong credentials'}), 401

@app.route('/api/users/me', methods=['PUT'])
@token_required
def update_user(current_user):
    data = request.get_json()
    
    current_user.first_name = data.get('first_name', current_user.first_name)
    current_user.last_name = data.get('last_name', current_user.last_name)
    current_user.birthdate = data.get('birthdate', current_user.birthdate)
    current_user.email = data.get('email', current_user.email)
    current_user.phone_number = data.get('phone_number', current_user.phone_number)
    
    db.session.commit()
    
    return jsonify({'message': 'User data updated successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
