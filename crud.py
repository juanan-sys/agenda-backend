from models import TaskV2
from database import SessionLocal

def create_task_v2(task):
    db = SessionLocal()
    new_task = TaskV2(
        title=task.title,
        date=task.date,
        hour=task.hour,
        priority=task.priority,
        notify=task.notify
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    return new_task

def get_tasks_v2_by_date(date):
    db = SessionLocal()
    tasks = db.query(TaskV2).filter(TaskV2.date == date).all()
    db.close()
    return tasks

def update_task_v2(task_id, task):
    db = SessionLocal()
    db_task = db.query(TaskV2).filter(TaskV2.id == task_id).first()
    if not db_task:
        return None

    for field, value in task.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

def delete_task_v2(task_id):
    db = SessionLocal()
    db_task = db.query(TaskV2).filter(TaskV2.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    db.close()