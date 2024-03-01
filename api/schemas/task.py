from typing import Optional # OptionalはNoneを許容する型

# BasemodelはFastAPIのスキーマモデルクラス
# Fieldは属性の詳細を指定するためのクラス
from pydantic import BaseModel, Field 


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ") # descriptionはOpenAPIドキュメントに表示される説明
    
    class Config:
        orm_mode = True