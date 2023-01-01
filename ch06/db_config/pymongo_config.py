from constants import DB_ENGINE, DB_HOST, DB_PORT
from pymongo import MongoClient

DB_URL = f'{DB_ENGINE}://{DB_HOST}:{DB_PORT}/'


def create_db_collections():
    client = MongoClient(DB_URL)
    try:
        db = client.fastapi_ch06
        buyers = db.buyer
        users = db.login
        yield {"users": users, "buyers": buyers}
    finally:
        client.close()
