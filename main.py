from fastapi import FastAPI
from pydantic import BaseModel
from database import session
from models import Task
app=FastAPI()

class Tasks(BaseModel):
    id: int
    task:str
    owner: str



@app.get("/tasks")
def Get_tasks():
    tasks=session.query(Task).all()
    return tasks

@app.post("/tasks")
def Post_tasks(new_task:Tasks):
    add_task=Task(id=new_task.id,task=new_task.task,owner=new_task.owner)
    session.add(add_task)
    session.commit()
    return add_task

@app.delete("/tasks/{id}")
def delete_tasks(id:int):
    task_to_delete=session.query(Task).filter_by(id=id).first()
    session.delete(task_to_delete)
    session.commit()
    return task_to_delete