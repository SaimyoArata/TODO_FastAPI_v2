from fastapi import FastAPI

from api.routers import task, done

app = FastAPI()
# ここでルーターを登録
app.include_router(task.router)
app.include_router(done.router)