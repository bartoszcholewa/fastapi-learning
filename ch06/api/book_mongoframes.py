from json import dumps, loads

from db_config.mongoframes_config import create_db_client, disconnect_db_client
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.request.category_mongoframes import BookReq
from repository.mongoframes.book import BookRepository
from utils import json_serial

router = APIRouter()

router.add_event_handler("startup", create_db_client)
router.add_event_handler("shutdown", disconnect_db_client)


@router.post("/book/create")
def create_book(req: BookReq):
    book_dict = req.dict(exclude_unset=True)
    book_json = dumps(book_dict, default=json_serial)
    repo: BookRepository = BookRepository()
    result = repo.insert_book(loads(book_json))
    if result is True:
        return req
    else:
        return JSONResponse(content={"message": "insert book unsuccessful"}, status_code=500)
