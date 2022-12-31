from bson import ObjectId
from pydantic import BaseModel


class LoginReq(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        # recognize the BSON data types
        arbitrary_types_allowed = False

        # convert the ObjectId property of the document
        # into a string during a query transaction
        json_encoders = {ObjectId: str}
