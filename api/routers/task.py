from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()

# 表示
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="１つ目のTODOタスク")]

# 追加
@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

# 説明変更
@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

# 削除
@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return