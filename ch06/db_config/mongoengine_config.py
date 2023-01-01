from constants import DB_HOST, DB_NAME, DB_PORT
from mongoengine import connect


def create_db():
    global db
    db = connect(db=DB_NAME, host=DB_HOST, port=DB_PORT)


def disconnect_db():
    db.close()
