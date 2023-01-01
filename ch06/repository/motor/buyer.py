from typing import Any, Dict


class BuyerRepository:
    def __init__(self, buyers):
        self.buyers = buyers

    async def insert_buyer(self, users, details: Dict[str, Any]) -> bool:
        try:
            user = await users.find_one({'_id': details['user_id']})
            if user is None:
                return False
            else:
                await self.buyers.insert_one(details)

        except Exception:
            return False
        return True
