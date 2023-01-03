from fastapi.security import HTTPBasic, HTTPDigest
from passlib.context import CryptContext

http_basic = HTTPBasic()
http_digest = HTTPDigest()

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def get_password_hash(password: str):
    return crypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return crypt_context.verify(plain_password, hashed_password)
