from typing import Any, Dict

from models.data.sqlalchemy_models import (Attendance_Member, Profile_Members,
                                           Signup)
from sqlalchemy import desc
from sqlalchemy.orm import Session


class SignupRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_signup(self, signup: Signup) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except Exception as ex:
            print(ex)
            return False
        return True

    def update_signup(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Signup).filter(Signup.id == id).update(details)
            self.sess.commit()
        except Exception as ex:
            print(ex)
            return False
        return True

    def delete_signup(self, id: int) -> bool:
        try:
            self.sess.query(Signup).filter(Signup.id == id).delete()
            self.sess.commit()
        except Exception as ex:
            print(ex)
            return False
        return True

    def get_all_signup(self):
        return self.sess.query(Signup).all()

    def get_all_signup_where(self, username: str):
        return self.sess.query(Signup.username, Signup.password).filter(Signup.username == username).all()

    def get_all_signup_sorted_desc(self):
        return self.sess.query(Signup.username, Signup.password).order_by(desc(Signup.username)).all()

    def get_signup(self, id: int):
        return self.sess.query(Signup).filter(Signup.id == id).one_or_none()


class MemberAttendanceRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def join_member_attendance(self):
        return self.sess.query(Profile_Members, Attendance_Member).join(Attendance_Member).all()

    def outer_join_member(self):
        return self.sess.query(Profile_Members, Attendance_Member).outerjoin(Attendance_Member).all()
