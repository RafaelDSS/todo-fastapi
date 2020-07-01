from pydantic import BaseModel
from typing import List, Optional


class TodoCreate(BaseModel):
    task_name: str
    complete: bool = False


class TodoList(TodoCreate):
    id: Optional[int] = None

    class Config:
        orm_mode = True
