from typing import Any, Dict

from models.data.gino_models import (Gym_Class, Profile_Members,
                                     Profile_Trainers)


class TrainerRepository:
    async def insert_trainer(self, details: Dict[str, Any]) -> bool:
        try:
            await Profile_Trainers.create(**details)
        except Exception as ex:
            print(ex)
            return False
        return True

    async def update_trainer(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            trainer = await Profile_Trainers.get(id)
            await trainer.update(**details).apply()
        except Exception as ex:
            print(ex)
            return False
        return True

    async def delete_trainer(self, id: int) -> bool:
        try:
            trainer = await Profile_Trainers.get(id)
            await trainer.delete()
        except Exception as ex:
            print(ex)
            return False
        return True

    async def get_all_members(self):
        return await Profile_Trainers.query.gino.all()

    async def get_member(self, id: int):
        return await Profile_Trainers.get(id)


class GymClassRepository:
    async def join_classes_trainer(self):
        query = Gym_Class.join(Profile_Trainers).select()
        result = await query.gino.load(Gym_Class.distinct(Gym_Class.id).load(parent=Profile_Trainers)).all()
        return result

    async def join_member_classes(self):
        query = Gym_Class.join(Profile_Trainers).select()
        result = await query.gino.load(Profile_Members.distinct(Profile_Members.id).load(add_child=Gym_Class)).all()
        return result
