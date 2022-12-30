from pony.orm import Database

DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_NAME = 'fastapi_ch05'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432

db = Database("postgres", host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
