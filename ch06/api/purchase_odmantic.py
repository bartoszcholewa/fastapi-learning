from json import dumps, loads

from db_config.odmantic_config import (close_db_connection,
                                       create_db_connection, create_db_engine)
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request.purchase_odmantic import PurchaseReq
from repository.odmantic.purchase import PurchaseRepository
from utils import json_serial

router = APIRouter()

router.add_event_handler("startup", create_db_connection)
router.add_event_handler("shutdown", close_db_connection)


@router.post("/purchase/add")
async def add_purchase(req: PurchaseReq, engine=Depends(create_db_engine)):
    purchase_dict = req.dict(exclude_unset=True)
    purchase_json = dumps(purchase_dict, default=json_serial)
    repo: PurchaseRepository = PurchaseRepository(engine)
    result = await repo.insert_purchase(loads(purchase_json))
    if result is True:
        return req
    else:
        return JSONResponse(content={"message": "insert purchase unsuccessful"}, status_code=500)
