from secrets import compare_digest

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.data.sqlalchemy_models import Login
from passlib.context import CryptContext

http_basic = HTTPBasic()

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def get_password_hash(password: str):
    return crypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(credentials: HTTPBasicCredentials, account: Login):
    try:
        is_username = compare_digest(credentials.username, account.username)
        is_password = compare_digest(credentials.password, account.password)
        verified_password = verify_password(credentials.password, account.passphrase)
        return (verified_password and is_username and is_password)
    except Exception as e:
        print(e)
        return False
