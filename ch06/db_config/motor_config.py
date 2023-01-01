from constants import DB_HOST, DB_PORT
from motor.motor_asyncio import AsyncIOMotorClient


def create_async_db():
    global client
    client = AsyncIOMotorClient(f"{DB_HOST}:{DB_PORT}")


def create_db_collections():
    db = client.fastapi_ch06
    buyers = db['buyer']
    users = db['login']
    return {'users': users, 'buyers': buyers}


def close_async_db():
    client.close()
