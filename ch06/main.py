from api import buyer_pymongo, login_mongoengine
from fastapi import FastAPI

app = FastAPI()
app.include_router(login_mongoengine.router, prefix='/ch06')
app.include_router(buyer_pymongo.router, prefix='/ch06')
