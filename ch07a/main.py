from api import login
from fastapi import FastAPI

app = FastAPI()

app.include_router(login.router, prefix='/ch07')


@app.get('/')
def index():
    return {'content': 'welcome'}
