from json import dumps, loads

from db_config.beanie_config import db_connect, db_disconnect
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.request.order_beanie import CartReq
from repository.beanie.cart import CartRepository
from utils import json_serial

router = APIRouter()

router.add_event_handler("startup", db_connect)
router.add_event_handler("shutdown", db_disconnect)


@router.post("/cart/add/item")
async def add_cart_item(req: CartReq):
    cart_dict = req.dict(exclude_unset=True)
    cart_json = dumps(cart_dict, default=json_serial)
    repo: CartRepository = CartRepository()
    result = await repo.add_item(loads(cart_json))
    if result is True:
        return req
    else:
        return JSONResponse(content={"message": "insert cart unsuccessful"}, status_code=500)
