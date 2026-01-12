from pydantic import BaseModel

class TaskV2Base(BaseModel):
    title: str
    date: str
    hour: str | None = None
    priority: int = 2
    notify: bool = False

class TaskV2(TaskV2Base):
    id: int
    completed: bool = False

    class Config:
        orm_mode = True

class TaskV2Update(BaseModel):
    title: str | None = None
    hour: str | None = None
    priority: int | None = None
    completed: bool | None = None
    notify: bool | None = None
