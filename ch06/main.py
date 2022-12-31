from api import buyer_pymongo, login_pymongo
from fastapi import FastAPI

app = FastAPI()
app.include_router(login_pymongo.router, prefix='/ch06')
app.include_router(buyer_pymongo.router, prefix='/ch06')
