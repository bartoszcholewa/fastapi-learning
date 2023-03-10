from api import (buyer_pymongo, cart_beanie, login_mongoengine,
                 purchase_odmantic)
from fastapi import FastAPI

app = FastAPI()
app.include_router(login_mongoengine.router, prefix='/ch06')
app.include_router(buyer_pymongo.router, prefix='/ch06')
app.include_router(cart_beanie.router, prefix='/ch06')
app.include_router(purchase_odmantic.router, prefix='/ch06')
