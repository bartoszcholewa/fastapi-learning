from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_NAME = 'fastapi_ch05'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432

DB_URL = f'{DB_ENGINE}+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DB_URL, future=True, echo=True)

AsyncSessionFactory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()
