from datetime import datetime, timedelta

from common.db_config.sqlalchemy_connect import session_db
from common.models.request_models import TokenDataRequest
from common.repository import LoginRepository
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from requests import Session

# openssl rand -hex 32
SECRET_KEY = 'a371b38ba3b93ab90b6f10f02cabb82e40a345d0aed5ba4f20e56519aa784714'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="ch07/login/token")


def create_access_token(data: dict, expires_after: timedelta):
    plain_text = data.copy()
    expire = datetime.utcnow() + expires_after
    plain_text.update({'exp': expire})
    encoded_jwt = jwt.encode(plain_text, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(session_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenDataRequest(username=username)
    except JWTError:
        raise credentials_exception

    login_repository = LoginRepository(session)
    user = login_repository.get_all_login_username(token_data.username)
    if user is None:
        raise credentials_exception
    return user
