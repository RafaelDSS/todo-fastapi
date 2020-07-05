from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.TodoList])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@app.post("/")
def create_task(task: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = models.Todo(**task.dict())
    db.add(todo)
    db.commit()
    return {"sucess": True}


@app.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == task_id).delete()

    if not todo:
        raise HTTPException(status_code=404, detail="The id does not exist")
    db.commit()
    return {"sucess": True}


@app.put("/{task_id}")
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
