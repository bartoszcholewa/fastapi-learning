from constants import DB_ENGINE, DB_HOST, DB_NAME, DB_PORT
from mongoframes import Frame
from pymongo import MongoClient


def create_db_client():
    Frame._client = MongoClient(f'{DB_ENGINE}://{DB_HOST}:{DB_PORT}/{DB_NAME}')


def disconnect_db_client():
    Frame._client.close()
