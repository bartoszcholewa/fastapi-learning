from json import dumps, loads

from db_config.motor_config import (close_async_db, create_async_db,
                                    create_db_collections)
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.request.buyer_pymongo import BuyerReq
from repository.motor.buyer import BuyerRepository
from utils import json_serialize_date

router = APIRouter()

router.add_event_handler("startup", create_async_db)
router.add_event_handler("shutdown", close_async_db)


@router.post('buyer/async/add')
async def add_buyer(req: BuyerReq, db=Depends(create_db_collections)):
    buyer_dict = req.dict(exclude_unset=True)
    buyer_json = dumps(buyer_dict, default=json_serialize_date)
    repo: BuyerRepository = BuyerRepository(db['buyers'])

    result = await repo.insert_buyer(db['users'], loads(buyer_json))
    if result is True:
        return JSONResponse(content={'message': 'add buyer successful'},
                            status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={'message': 'add buyer unsuccessful'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
