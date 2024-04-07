from sqlalchemy.exc import SQLAlchemyError
from models import Task

def create_task(db, title, description, deadline):
    new_task = Task(title=title, description=description, deadline=deadline)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_task(db, task_id, title, description, deadline, is_completed):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        task.deadline = deadline
        task.is_completed = is_completed
        db.commit()
        db.refresh(task)
        return task
    else:
        raise ValueError("Task not found")

def delete_task(db, task_id):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    else:
        raise ValueError("Task not found")

def get_task_by_id(db, task_id):
    return db.query(Task).filter(Task.id == task_id).first()

def list_tasks(db, page, page_size):
    return db.query(Task).order_by(Task.created_at.desc()).offset(page * page_size).limit(page_size).all()