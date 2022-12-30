from api import admin
from fastapi import FastAPI

app = FastAPI()
app.include_router(admin.router, prefix='/ch05')
