from typing import Any, Dict

from models.data.pony_models import Login, Profile_Members
from models.requests.members import ProfileMembersReq
from pony.orm import db_session, left_join


class MemberRepository:
    def insert_member(self, details: Dict[str, Any]) -> bool:
        try:
            with db_session:
                Profile_Members(**details)
        except Exception:
            return False
        return True

    def update_member(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            with db_session:
                profile = Profile_Members[id]
                profile.id = details["id"]
                profile.firstname = details["firstname"]
                profile.lastname = details["lastname"]
                profile.age = details["age"]
                profile.membership_type = details["membership_type"]
                profile.height = details["height"]
                profile.weight = details["weight"]
                profile.trainer_id = details["trainer_id"]
        except Exception:
            return False
        return True

    def delete_member(self, id: int) -> bool:
        try:
            with db_session:
                Profile_Members[id].delete()
        except Exception:
            return False
        return True

    def get_all_members(self):
        with db_session:
            members = Profile_Members.select()
            result = [ProfileMembersReq.from_orm(m) for m in members]
            return result

    def get_member(self, id: int):
        with db_session:
            login = Login.get(lambda x: x.id == id)
            member = Profile_Members.get(lambda m: m.id == login)
            result = ProfileMembersReq.from_orm(member)
            return result


class MemberGymClassRepository:
    def join_member_class(self):
        with db_session:
            generator_args = (m for m in Profile_Members for g in m.gclass)
            joins = left_join(generator_args)
            result = [ProfileMembersReq.from_orm(m) for m in joins]
            return result
