from db_config.sqlalchemy_connect import Base
from sqlalchemy import Column, Date, Integer, String


class Signup(Base):
    __tablename__ = 'signup'

    id = Column(Integer, primary_key=True, index=True)
    username = Column('username', String, unique=False, index=False)
    password = Column('password', String, unique=False, index=False)


class Login(Base):
    __tablename__ = 'login'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=False)
    password = Column(String, unique=False, index=False)
    passphrase = Column(String, unique=False, index=False)
    approved_date = Column(Date, unique=False, index=False)
