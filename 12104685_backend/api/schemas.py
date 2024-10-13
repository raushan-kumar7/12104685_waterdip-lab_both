from pydantic import BaseModel
from typing import List, Optional


class TaskBase(BaseModel):
    title: str
    is_completed: bool = False


class TaskCreate(BaseModel):
    title: str


class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True


class TaskList(BaseModel):
    tasks: List[Task]


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None


class BulkTaskCreate(BaseModel):
    tasks: List[TaskBase]

class TaskDelete(BaseModel):
    id: int

class BulkTaskDelete(BaseModel):
    tasks: List[TaskDelete]
