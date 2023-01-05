from datetime import timedelta
from typing import List

from ch07d.secure import (ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token,
                          get_current_user)
from common.db_config.sqlalchemy_connect import session_db
from common.models.database_models import Login
from common.models.request_models import SignupRequest
from common.repository import LoginRepository, SignupRepository
from common.security.secure import authenticate
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/login/token')
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(session_db)):
    username = form_data.username
    password = form_data.password
    login_repository = LoginRepository(session)
    account = login_repository.get_all_login_username(username)
    if authenticate(username, password, account):
        access_token = create_access_token(
            data={'sub': username},
            expires_after=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {'access_token': access_token, 'token_type': 'bearer'}

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect username or password'
        )


@router.get("/signup/list", response_model=List[SignupRequest])
def list_signup(current_user: Login = Depends(get_current_user), sess: Session = Depends(session_db)):
    repo: SignupRepository = SignupRepository(sess)
    result = repo.get_all_signup()
    return result
