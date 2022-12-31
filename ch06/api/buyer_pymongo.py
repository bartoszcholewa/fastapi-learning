from json import dumps, loads

from db_config.pymongo_config import create_db_collections
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.request.buyer_pymongo import BuyerReq
from repository.pymongo.buyer import BuyerRepository
from utils import json_serialize_date, json_serialize_oid

router = APIRouter()


@router.post('/buyer/add')
def add_buyer(request: BuyerReq, db=Depends(create_db_collections)):
    buyer_dict = request.dict(exclude_unset=True)
    buyer_json = dumps(buyer_dict, default=json_serialize_date)

    repo: BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.insert_buyer(db["users"], loads(buyer_json))

    if result is True:
        return JSONResponse(content={"message": "add buyer successful"},
                            status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"message": "add buyer unsuccessful"},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/buyer/list/all")
def list_all_buyer(db=Depends(create_db_collections)):
    repo: BuyerRepository = BuyerRepository(db["buyers"])
    buyers = repo.get_all_buyer()
    return loads(dumps(buyers, default=json_serialize_oid))
