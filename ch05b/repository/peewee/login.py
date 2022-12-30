from datetime import date
from typing import Any, Dict

from models.data.peewee_models import (Gym_Class, Login, Profile_Members,
                                       Profile_Trainers)
from peewee import JOIN


class LoginRepository:

    def insert_login(self, id: int, user: str, passwd: str, approved: date, type: int) -> bool:
        try:
            Login.create(id=id, username=user, password=passwd, date_approved=approved, user_type=type)
        except Exception as ex:
            print(ex)
            return False
        return True

    def update_login(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            query = Login.update(**details).where(Login.id == id)
            query.execute()
        except Exception as ex:
            print(ex)
            return False
        return True

    def delete_login(self, id: int) -> bool:
        try:
            Login.delete_by_id(id)
        except Exception as ex:
            print(ex)
            return False
        return True

    def get_all_login(self):
        return list(Login.select())

    def get_login(self, id: int):
        return Login.get(Login.id == id)


class LoginTrainersRepository:

    def join_login_trainers(self):
        return list(Profile_Trainers.select(Profile_Trainers, Login).join(Login))


class MemberGymClassesRepository:
    def outer_join_member_gym(self):
        return list(Profile_Members.select(Profile_Members, Gym_Class).join(Gym_Class, join_type=JOIN.LEFT_OUTER))
