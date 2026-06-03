from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=list[schemas.TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.post("/", response_model=schemas.TaskOut, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/{id_task}", response_model=schemas.TaskOut)
def read_task(id_task: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, id_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{id_task}", response_model=schemas.TaskOut)
def update_task(id_task: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task(db, id_task, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{id_task}", response_model=schemas.TaskOut)
def delete_task(id_task: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, id_task)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted
