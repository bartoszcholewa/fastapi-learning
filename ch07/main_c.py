from ch07c.api import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router, prefix="/ch07")


@app.get("/index")
def index():
    return {"content": "welcome"}
