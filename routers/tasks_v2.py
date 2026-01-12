from fastapi import APIRouter, HTTPException
from backend.schemas import TaskV2, TaskV2Base, TaskV2Update
from backend import crud

router = APIRouter(prefix="/tasks_v2", tags=["Tasks V2"])

@router.get("/{date}")
def get_tasks(date: str):
    return crud.get_tasks_v2_by_date(date)

@router.post("/")
def create(task: TaskV2Base):
    return crud.create_task_v2(task)

@router.put("/{task_id}")
def update(task_id: int, task: TaskV2Update):
    updated = crud.update_task_v2(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return updated

@router.delete("/{task_id}")
def delete(task_id: int):
    crud.delete_task_v2(task_id)
    return {"message": "Tarea eliminada"}