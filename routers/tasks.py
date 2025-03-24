from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskCreate, TaskResponse
from utils import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Task).filter(Task.owner_id == user.id).all()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = Task(**task.dict(), owner_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    existing_task = db.query(Task).filter(Task.id == id, Task.owner_id == user.id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task.title = task.title
    existing_task.description = task.description
    db.commit()
    db.refresh(existing_task)
    
    return existing_task

@router.delete("/{id}")
def delete_task(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    existing_task = db.query(Task).filter(Task.id == id, Task.owner_id == user.id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(existing_task)
    db.commit()
    return {"message": "Task deleted successfully"}
