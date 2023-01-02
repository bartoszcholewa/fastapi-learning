from typing import Any, Dict

from models.data.sqlalchemy_models import Login, Signup
from sqlalchemy import desc
from sqlalchemy.orm import Session


class SignupRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def insert_signup(self, signup: Signup) -> bool:
        try:
            self.session.add(signup)
            self.session.commit()
            print(signup.id)
        except Exception as ex:
            print(ex)
            return False
        return True

    def update_signup(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.session.query(Signup).filter(Signup.id == id).update(details)
            self.session.commit()
        except Exception as ex:
            print(ex)
            return False
        return True

    def delete_signup(self, id: int) -> bool:
        try:
            self.session.query(Signup).filter(Signup.id == id).delete()
            self.session.commit()
        except Exception as ex:
            print(ex)
            return False
        return True

    def get_all_signup(self):
        return self.session.query(Signup).all()

    def get_signup_username(self, username: str):
        return self.session.query(Signup).filter(Signup.username == username).one_or_none()

    def get_all_signup_sorted_desc(self):
        return self.session.query(Signup.username, Signup.password).order_by(desc(Signup.username)).all()

    def get_signup(self, id: int):
        return self.session.query(Signup).filter(Signup.id == id).one_or_none()


class LoginRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def insert_login(self, login: Login) -> bool:
        try:
            self.session.add(login)
            self.session.commit()
        except Exception as ex:
            print(ex)
            return False
        return True

    def get_all_login_username(self, username: str):
        return self.session.query(Login).filter(Login.username == username).one_or_none()
