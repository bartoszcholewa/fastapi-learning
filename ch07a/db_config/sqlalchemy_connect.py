from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_NAME = 'fastapi_ch07'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432

DB_URL = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def session_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
