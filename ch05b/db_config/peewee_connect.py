from contextvars import ContextVar

from peewee import PostgresqlDatabase, _ConnectionState

DB_ENGINE = 'postgresql'
DB_HOST = 'localhost'
DB_NAME = 'fastapi_ch05'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_PORT = 5432

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        self._state.get()[key] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = PostgresqlDatabase(
    DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

db._state = PeeweeConnectionState()
