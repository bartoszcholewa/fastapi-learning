from models.data.sqlalchemy_models import Login, Profile_Members
from sqlalchemy.orm import Session


class LoginMemberRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def join_login_members(self):
        return self.sess.query(Login, Profile_Members).filter(Login.id == Profile_Members.id).all()
