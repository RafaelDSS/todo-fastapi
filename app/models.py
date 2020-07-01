from .database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String)
    complete = Column(Boolean, default=False)
