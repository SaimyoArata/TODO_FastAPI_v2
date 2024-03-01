from fastapi import APIRouter

router = APIRouter()

# 完了フラグを立てる
@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
    return

# 完了フラグを外す
@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
    return