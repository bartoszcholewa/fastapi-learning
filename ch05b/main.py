from api import attendance
from fastapi import FastAPI

app = FastAPI()
app.include_router(attendance.router, prefix='/ch05')
