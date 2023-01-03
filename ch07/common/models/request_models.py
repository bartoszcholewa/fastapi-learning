from datetime import date
from typing import Optional

from pydantic import BaseModel


class AuctionsRequest(BaseModel):
    id: int
    name: str
    details: str
    type_id: int
    max_price: float
    min_price: float
    buyout_price: float
    created_date: date
    updated_date: date
    condition: str
    profile_id: int


class BidsRequest(BaseModel):
    id: int
    auction_id: int
    profile_id: int
    created_date: date
    updated_date: date
    price: float


class LoginRequest(BaseModel):
    username: str
    password: str


class ProfileRequest(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    membership_date: date
    member_type: str
    login_id: int
    status: int


class SignupRequest(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class TokenRequest(BaseModel):
    access_token: str
    token_type: str


class TokenDataRequest(BaseModel):
    username: Optional[str] = None
