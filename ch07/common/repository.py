from typing import Any, Dict

from common.models.database_models import (Auctions, Bids, Login, Profile,
                                           Signup)
from sqlalchemy import desc
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session: Session):
        self.session: Session = session


class AuctionsRepository(BaseRepository):

    def insert_auction(self, auc: Auctions) -> bool:
        try:
            self.session.add(auc)
            self.session.commit()
        except Exception:
            return False
        return True

    def update_auction(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.session.query(Auctions).filter(Auctions.id == id).update(details)
            self.session.commit()

        except Exception:
            return False
        return True

    def delete_auction(self, id: int) -> bool:
        try:
            self.session.query(Auctions).filter(Auctions.id == id).delete()
            self.session.commit()

        except Exception:
            return False
        return True

    def get_all_auctions(self):
        return self.session.query(Auctions).all()

    def get_auctions_profile_id(self, profile_id: int):
        return self.session.query(Auctions).filter(Auctions.profile_id == profile_id).all()

    def get_auction(self, id: int):
        return self.session.query(Auctions).filter(Auctions.id == id).one_or_none()


class BidsRepository(BaseRepository):

    def insert_bid(self, bid: Bids) -> bool:
        try:
            self.session.add(bid)
            self.session.commit()
        except Exception:
            return False
        return True

    def update_bid(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.session.query(Bids).filter(Bids.id == id).update(details)
            self.session.commit()

        except Exception:
            return False
        return True

    def delete_bid(self, id: int) -> bool:
        try:
            self.session.query(Bids).filter(Bids.id == id).delete()
            self.session.commit()

        except Exception:
            return False
        return True

    def get_all_bids(self):
        return self.session.query(Bids).all()

    def get_bids_auction_id(self, auction_id: int):
        return self.session.query(Bids).filter(Bids.auction_id == auction_id).all()

    def get_bid(self, id: int):
        return self.session.query(Bids).filter(Bids.id == id).one_or_none()


class LoginRepository:
    def __init__(self, sess: Session):
        self.session: Session = sess

    def insert_login(self, login: Login) -> bool:
        try:
            self.session.add(login)
            self.session.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def update_login(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.session.query(Login).filter(Login.id == id).update(details)
            self.session.commit()

        except Exception:
            return False
        return True

    def delete_login(self, id: int) -> bool:
        try:
            self.session.query(Login).filter(Login.id == id).delete()
            self.session.commit()
        except Exception:
            return False
        return True

    def get_all_login(self):
        return self.session.query(Login).all()

    def get_all_login_username(self, username: str):
        return self.session.query(Login).filter(Login.username == username).one_or_none()

    def get_all_login_sorted_desc(self):
        return self.session.query(Login.username, Login.password).order_by(desc(Login.username)).all()

    def get_login(self, id: int):
        return self.session.query(Login).filter(Login.id == id).one_or_none()


class ProfileRepository(BaseRepository):

    def insert_profile(self, profile: Profile) -> bool:
        try:
            self.session.add(profile)
            self.session.commit()
        except Exception:
            return False
        return True

    def update_profile(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.session.query(Profile).filter(Profile.id == id).update(details)
            self.session.commit()

        except Exception:
            return False
        return True

    def delete_profile(self, id: int) -> bool:
        try:
            self.session.query(Profile).filter(Profile.id == id).delete()
            self.session.commit()

        except Exception:
            return False
        return True

    def get_all_profile(self):
        return self.session.query(Profile).all()

    def get_profile_login_id(self, login_id: int):
        return self.session.query(Profile).filter(Profile.login_id == login_id).one_or_none()

    def get_profile(self, id: int):
        return self.session.query(Profile).filter(Profile.id == id).one_or_none()


class SignupRepository(BaseRepository):

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

        except Exception:
            return False
        return True

    def delete_signup(self, id: int) -> bool:
        try:
            self.session.query(Signup).filter(Signup.id == id).delete()
            self.session.commit()

        except Exception:
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
