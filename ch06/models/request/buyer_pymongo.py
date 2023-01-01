from datetime import date
from typing import Dict, List, Optional

from bson import ObjectId
from pydantic import BaseModel, validator
from utils import date_to_datetime


class PurchaseHistoryReq(BaseModel):
    """ Purchase history model for request data using PyMongo ODM"""

    purchase_id: int
    shipping_address: str
    email: str
    date_purchased: date
    date_shipped: date
    date_payment: date

    @validator('date_purchased')
    def date_purchased_datetime(cls, value: date):
        # Convert date to datetime class
        return date_to_datetime(value)

    @validator('date_shipped')
    def date_shipped_datetime(cls, value: date):
        # Convert date to datetime class
        return date_to_datetime(value)

    @validator('date_payment')
    def date_payment_datetime(cls, value: date):
        # Convert date to datetime class
        return date_to_datetime(value)

    class Config:
        # recognize the BSON data types
        arbitrary_types_allowed = False

        # convert the ObjectId property of the document
        # into a string during a query transaction
        json_encoders = {ObjectId: str}


class PurchaseStatusReq(BaseModel):
    status_id: int
    name: str
    discount: float
    date_membership: date

    @validator('date_membership')
    def date_membership_datetime(cls, value: date):
        # Convert date to datetime class
        return date_to_datetime(value)

    class Config:
        # recognize the BSON data types
        arbitrary_types_allowed = False

        # convert the ObjectId property of the document
        # into a string during a query transaction
        json_encoders = {ObjectId: str}


class BuyerReq(BaseModel):
    _id: ObjectId
    buyer_id: int
    user_id: int
    date_purchased: date
    purchase_history: List[Dict] = list()
    customer_status: Optional[Dict]

    @validator('date_purchased')
    def date_purchased_datetime(cls, value: date):
        return date_to_datetime(value)

    class Config:
        # recognize the BSON data types
        arbitrary_types_allowed = False

        # convert the ObjectId property of the document
        # into a string during a query transaction
        json_encoders = {ObjectId: str}
