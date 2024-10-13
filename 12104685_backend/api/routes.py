from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import delete
from api import models
from api import schemas
from api.database import SessionLocal
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_root():
    return {"server": "Fast Api is Running"}

# Create a new Task
@router.post("/v1/tasks", status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return {"id": db_task.id}


# Get List of tasks
@router.get("/v1/tasks", response_model=schemas.TaskList)
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return {"tasks": tasks}


# Get a specific task by ID
@router.get("/v1/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(
            status_code=404, detail="There is no task at that id")
    return task


# Delete a specific task by given ID
@router.delete("/v1/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return None


# Update a specific task by given ID
@router.put("/v1/tasks/{task_id}", status_code=204)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(
            status_code=404, detail="There is no task at that id")
    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    return None


# Create a Bulk task at once
@router.post("/v1/tasks/bulk", status_code=201, response_model=dict)
def bulk_create_tasks(tasks: schemas.BulkTaskCreate, db: Session = Depends(get_db)):
    created_tasks = []
    try:
        for task in tasks.tasks:
            db_task = models.Task(title=task.title)
            db.add(db_task)
            db.commit()
            db.refresh(db_task)
        
            created_tasks.append({"id": db_task.id})
    except Exception as e:
        print(f"Error creating tasks: {e}")
        return {"error": "An error occurred while creating tasks."}, 500

    return {"tasks": created_tasks}


# Delete a Bulk task at once
@router.delete("/v1/tasks", status_code=204)
def bulk_delete_tasks(tasks: schemas.BulkTaskDelete, db: Session = Depends(get_db)):
    task_ids = [task.id for task in tasks.tasks]

    db.query(models.Task).filter(models.Task.id.in_(task_ids)).delete(synchronize_session=False)
    
    db.commit()

    return None
