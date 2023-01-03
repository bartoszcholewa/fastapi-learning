from ch07b.security.secure import authenticate
from common.db_config.sqlalchemy_connect import session_db
from common.models.database_models import Signup
from common.models.request_models import SignupRequest
from common.repository import SignupRepository
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/signup/add', dependencies=[Depends(authenticate)])
def signup_add(request: SignupRequest, session: Session = Depends(session_db)):
    repository: SignupRepository = SignupRepository(session)
    signup = Signup(password=request.password, username=request.username, id=request.id)
    result = repository.insert_signup(signup)
    if result is True:
        return result
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
