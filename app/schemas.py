from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    status: str

class Task(TaskBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True  
