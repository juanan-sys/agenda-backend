from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routers import tasks_v2

app = FastAPI(title="Agenda Personal")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego puedes restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(tasks_v2.router)