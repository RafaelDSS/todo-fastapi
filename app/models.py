from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String)
    complete = Column(Boolean, default=False)
