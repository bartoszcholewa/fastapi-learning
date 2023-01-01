from typing import Any, Dict


class LoginRepository:

    def __init__(self, logins):
        self.logins = logins

    def insert_login(self, details: Dict[str, Any]) -> bool:
        try:
            self.logins.insert_one(details)
        except Exception as ex:
            print(ex)
            return False
        return True
