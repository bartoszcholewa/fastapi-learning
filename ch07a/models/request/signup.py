from pydantic import BaseModel


class SignupRequest(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True
