from common.db_config.sqlalchemy_connect import session_db
from common.repository import LoginRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/ch07/login/token')


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(session_db)):
    print('hello33')
    login_repository = LoginRepository(session)
    user = login_repository.get_all_login_username(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    return user
