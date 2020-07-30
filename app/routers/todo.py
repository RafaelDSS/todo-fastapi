from fastapi import APIRouter
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.TodoList])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@router.get("/{task_id}", response_model=schemas.TodoList)
def list_task(task_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == task_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="The id does not exist")
    return todo


@router.post("/")
def create_task(task: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = models.Todo(**task.dict())
    db.add(todo)
    db.commit()
    return {"sucess": True}


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == task_id).delete()

    if not todo:
        raise HTTPException(status_code=404, detail="The id does not exist")
    db.commit()
    return {"sucess": True}


@router.put("/{task_id}")
def edit_task(task_id: int, task: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = (
        db.query(models.Todo)
        .filter(models.Todo.id == task_id)
        .update(values=task.dict())
    )

    if not todo:
        raise HTTPException(status_code=404, detail="The id does not exist")
    db.commit()
    return {"sucess": True}
