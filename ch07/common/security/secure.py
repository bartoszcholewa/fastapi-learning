from common.models.database_models import Login
from fastapi.security import HTTPBasic, HTTPDigest
from passlib.context import CryptContext

http_basic = HTTPBasic()
http_digest = HTTPDigest()

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def get_password_hash(password: str):
    return crypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(username, password, account: Login):
    try:
        password_check = verify_password(password, account.passphrase)
        return password_check
    except Exception as ex:
        print(ex)
        return False
