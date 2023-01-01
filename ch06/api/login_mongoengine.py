from db_config.mongoengine_config import create_db, disconnect_db
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.request.login_pymongo import LoginReq
from repository.mongoengine.login import LoginRepository

router = APIRouter()

router.add_event_handler('startup', create_db)
router.add_event_handler('shutdown', disconnect_db)


@router.post('/login/add')
def create_login(req: LoginReq):
    login_dict = req.dict(exclude_unset=True)
    repo: LoginRepository = LoginRepository()
    result = repo.insert_login(login_dict)
    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'insert login unsuccessful'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
