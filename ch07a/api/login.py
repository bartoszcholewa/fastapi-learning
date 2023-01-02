from datetime import date
from typing import List

from db_config.sqlalchemy_connect import session_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasicCredentials
from models.data.sqlalchemy_models import Login, Signup
from models.request.signup import SignupRequest
from repository.signup import LoginRepository, SignupRepository
from security.secure import authenticate, get_password_hash, http_basic
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/signup/add')
def add_signup(request: SignupRequest, session: Session = Depends(session_db)):
    repository: SignupRepository = SignupRepository(session)
    signup = Signup(password=request.password, username=request.username, id=request.id)
    result = repository.insert_signup(signup)
    if result is True:
        return signup
    else:
        return JSONResponse(content={'message': 'create signup error'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/signup/list', response_model=List[SignupRequest])
def list_signup(credentials: HTTPBasicCredentials = Depends(http_basic), session: Session = Depends(session_db)):
    repository: SignupRepository = SignupRepository(session)
    result = repository.get_all_signup()
    return result


@router.get('/signup/approve')
def signup_approve(username: str, session: Session = Depends(session_db)):
    signup_repository: SignupRepository = SignupRepository(session)
    result: Signup = signup_repository.get_signup_username(username)
    if result is not None:
        passphrase = get_password_hash(result.password)
        login = Login(id=result.id, username=result.username, password=result.password, passphrase=passphrase,
                      approved_date=date.today())
        login_repository = LoginRepository(session)
        success = login_repository.insert_login(login)
        if success is True:
            return login
        else:
            return JSONResponse(content={'message': 'create login error'},
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JSONResponse(content={'message': f'{username} username is not valid'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/login')
def login(credentials: HTTPBasicCredentials = Depends(http_basic), session: Session = Depends(session_db)):
    login_repository: LoginRepository = LoginRepository(session)
    account = login_repository.get_all_login_username(credentials.username)
    if authenticate(credentials, account) and account is not None:
        return account
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
