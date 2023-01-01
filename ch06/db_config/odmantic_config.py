from constants import DB_ENGINE, DB_HOST, DB_NAME, DB_PORT
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


def create_db_connection():
    global client_od
    client_od = AsyncIOMotorClient(f'{DB_ENGINE}://{DB_HOST}:{DB_PORT}')


def create_db_engine():
    engine = AIOEngine(client=client_od, database=DB_NAME)
    return engine


def close_db_connection():
    client_od.close()
