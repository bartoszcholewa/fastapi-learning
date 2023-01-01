from dataclasses import field
from datetime import date
from typing import List, Optional

from bson import ObjectId
from constants import DEFAULT_DATE
from pydantic import validator
from pydantic.dataclasses import dataclass
from utils import string_to_date


class Config:
    arbitrary_types_allowed = True


@dataclass(config=Config)
class PurchaseHistory:
    purchase_id: Optional[int] = None
    shipping_address: Optional[str] = None
    email: Optional[str] = None
    date_purchased: Optional[date] = DEFAULT_DATE
    date_shipped: Optional[date] = DEFAULT_DATE
    date_payment: Optional[date] = DEFAULT_DATE

    @validator('date_purchased', pre=True)
    def date_purchased_datetime(cls, value: str):
        return string_to_date(value)

    @validator('date_shipped', pre=True)
    def date_shipped_datetime(cls, value: str):
        return string_to_date(value)

    @validator('date_payment', pre=True)
    def date_payment_datetime(cls, value: str):
        return string_to_date(value)


@dataclass(config=Config)
class PurchaseStatus:
    status_id: Optional[int] = None
    name: Optional[str] = None
    discount: Optional[float] = None
    date_membership: Optional[date] = DEFAULT_DATE

    @validator('date_membership', pre=True)
    def date_membership_datetime(cls, value: str):
        return string_to_date(value)


@dataclass(config=Config)
class Buyer:
    buyer_id: int
    user_id: int
    date_purchased: date
    purchase_history: List[PurchaseHistory] = field(default_factory=list)
    customer_status: Optional[PurchaseStatus] = field(default_factory=dict)
    _id: ObjectId = field(default=ObjectId())

    @validator('date_purchased', pre=True)
    def date_purchased_datetime(cls, value: str):
        return string_to_date(value)


@dataclass(config=Config)
class Login:
    id: int
    username: str
    password: str
