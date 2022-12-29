import os
from datetime import date

from pydantic import BaseSettings


class FacultySettings(BaseSettings):
    application: str = 'Faculty Management System'
    webmaster: str = 'jondoe@example.pl'
    created: date = '2022-12-29'


class LibrarySettings(BaseSettings):
    application: str = 'Library Management System'
    webmaster: str = 'jondoe@example.pl'
    created: date = '2022-12-29'


class StudentSettings(BaseSettings):
    application: str = 'Student Management System'
    webmaster: str = 'jondoe@example.pl'
    created: date = '2022-12-29'


class ServerSettings(BaseSettings):
    production_server: str
    prod_port: int
    development_server: str
    dev_port: int

    class Config:
        env_file = os.getcwd() + '/configuration/erp_settings.env'
