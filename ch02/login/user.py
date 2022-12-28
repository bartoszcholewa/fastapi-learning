from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from ch02.background import audit_log_transaction

router = APIRouter()


class Tourist(BaseModel):
    id: UUID
    login: User
    date_signed: datetime
    booked: int
    tours: List[TourBasicInfo]


@router.post("/ch02/user/login/")
async def login(login: User, bg_task: BackgroundTasks):
    try:
        signup_json = jsonable_encoder(approved_users[login.id])
        bg_task.add_task(audit_log_transaction, touristId=str(login.id), message="login")
        return JSONResponse(content=signup_json, status_code=status.HTTP_200_OK)
    except:
        return JSONResponse(content={"message": "invalid operation"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/ch02/user/signup")
async def signup(signup: Signup):
    try:
        userid = uuid1()
        login = User(id=userid,
                     username=signup.username,
                     password=signup.password)
        tourist = Tourist(id=userid,
                          login=login,
                          date_signed=datetime.now(),
                          booked=0,
                          tours=list())
        tourist_json = jsonable_encoder(tourist)
        pending_users[userid] = tourist_json
        return JSONResponse(content=tourist_json, status_code=status.HTTP_201_CREATED)
    except:
        return JSONResponse(content={"message": "onvalid operation"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/ch02/user/login/{username}/{password}")
async def login(username: str, password: str, bg_task: BackgroundTasks):
    tourist_list = [
        tourist for tourist in approved_users.values()
        if tourist['login']['username'] == username and
           tourist['login']['password'] == password
    ]
    if len(tourist_list) == 0 or tourist_list is None:
        return JSONResponse(content={"message": "invalid operation"}, status_code=status.HTTP_403_FORBIDDEN)
    else:
        tourist = tourist_list[0]
        tour_json = jsonable_encoder(tourist)
        bg_task.add_task(audit_log_transaction, touristId=str(tourist['login']['id']), message="login")
        return JSONResponse(content=tour_json, status_code=status.HTTP_200_OK)
