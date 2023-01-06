from datetime import datetime, timedelta
from typing import Optional

from ch07e.request_models import TokenData
from common.db_config.sqlalchemy_connect import session_db
from common.models.database_models import Login
from common.repository import LoginRepository
from fastapi import Depends, HTTPException, Security, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.requests import Request
from fastapi.security import OAuth2, SecurityScopes
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from sqlalchemy.orm import Session

SECRET_KEY = 'a371b38ba3b93ab90b6f10f02cabb82e40a345d0aed5ba4f20e56519aa784714'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class OAuth2PasswordBearerScopes(OAuth2):
    def __init__(
            self,
            tokenUrl: str,
            scheme_name: str = None,
            scopes: dict = None,
            auto_error: bool = True
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={'tokenUrl': tokenUrl, 'scopes': scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        header_authorization: str = request.headers.get("Authorization")
        header_scheme, header_param = get_authorization_scheme_param(header_authorization)
        if header_scheme.lower() == 'bearer':
            authorization = True
            scheme = header_scheme
            param = header_param
        else:
            scheme = ''
            authorization = False

        if not authorization or scheme.lower() != 'bearer':
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Not authenticated'
                )
            else:
                return None
        return param


oauth2_scheme = OAuth2PasswordBearerScopes(
    tokenUrl="/ch07/login/token",
    scopes={"admin_read": "admin role that has read only role",
            "admin_write": "admin role that has write only role",
            "bidder_read": "customer role that has read only role",
            "bidder_write": "customer role that has write only role",
            "auction_read": "buyer role that has read only role",
            "auction_write": "buyer role that has write only role",
            "user": "valid user of the application",
            "guest": "visitor of the site"},
)


def create_access_token(data: dict, expires_after: timedelta):
    plain_text = data.copy()
    expire = datetime.utcnow() + expires_after
    plain_text.update({'exp': expire})
    encoded_jwt = jwt.encode(plain_text, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme),
                     sess: Session = Depends(session_db)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except JWTError:
        raise credentials_exception
    loginrepo = LoginRepository(sess)
    user = loginrepo.get_all_login_username(token_data.username)

    if user is None:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    print(user)
    return user


def get_current_valid_user(current_user: Login = Security(get_current_user, scopes=["user"])):
    if current_user is None:
        raise HTTPException(status_code=400, detail="Invalid user")
    return current_user
