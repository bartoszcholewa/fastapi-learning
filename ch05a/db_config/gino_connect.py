from gino import Gino

DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_NAME = 'fastapi_ch05'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432

DB_URL = f'{DB_ENGINE}+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

db = Gino()
