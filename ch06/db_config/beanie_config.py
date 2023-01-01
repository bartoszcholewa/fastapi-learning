from beanie import init_beanie
from constants import DB_ENGINE, DB_HOST, DB_NAME, DB_PORT
from models.data.beanie import Cart, Order, Receipt
from motor.motor_asyncio import AsyncIOMotorClient


async def db_connect():
    global client
    client = AsyncIOMotorClient(f'{DB_ENGINE}://{DB_HOST}:{DB_PORT}/{DB_NAME}')
    await init_beanie(client.fastapi_ch06, document_models=[Cart, Order, Receipt])


async def db_disconnect():
    client.close()
