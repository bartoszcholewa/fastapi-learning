from json import dumps, loads

from db_config.pymongo_config import create_db_collections
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.request.login_pymongo import LoginReq
from repository.pymongo.login import LoginRepository
from utils import json_serialize_date

router = APIRouter()


@router.post('/login/add')
def add_login(request: LoginReq, db=Depends(create_db_collections)):
    login_dict = request.dict(exclude_unset=True)
    login_json = dumps(login_dict, default=json_serialize_date)

    repo: LoginRepository = LoginRepository(db["users"])
    result = repo.insert_login(loads(login_json))

    if result is True:
        return JSONResponse(content={"message": "add user successful"},
                            status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"message": "add user unsuccessful"},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
