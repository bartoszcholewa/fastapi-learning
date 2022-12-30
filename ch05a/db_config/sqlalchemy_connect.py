from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Prepare engine communication url
DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_NAME = 'fastapi_ch05'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432

# Create proper database connection URL
DB_URL = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Create connection engine based on URL
engine = create_engine(DB_URL)

# Initialize the session factory
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Map model classes to database tables
Base = declarative_base()
