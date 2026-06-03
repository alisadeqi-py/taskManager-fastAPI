from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed_is: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    at_created: datetime

    class Config:
        from_attributes = True