from secrets import compare_digest

from common.models.database_models import Login
from common.security.secure import verify_password
from fastapi.security import HTTPBasicCredentials


def authenticate(credentials: HTTPBasicCredentials, account: Login):
    try:
        is_username = compare_digest(credentials.username, account.username)
        is_password = compare_digest(credentials.password, account.password)
        verified_password = verify_password(credentials.password, account.passphrase)
        return (verified_password and is_username and is_password)
    except Exception as e:
        print(e)
        return False
