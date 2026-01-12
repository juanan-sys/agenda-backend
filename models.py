from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean
from backend.database import Base

class TaskV2(Base):
    __tablename__ = "tasks_v2"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(String, nullable=False)  # formato YYYY-MM-DD
    hour = Column(String, nullable=True)   # formato HH:MM
    priority = Column(Integer, default=2)  # 1=baja, 2=media, 3=alta
    completed = Column(Boolean, default=False)
    notify = Column(Boolean, default=False)

