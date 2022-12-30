from typing import List

from db_config.sqlalchemy_connect import SessionFactory
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.data.sqlalchemy_models import Signup
from models.requests.signup import SignupReq
from repository.sqlalchemy.signup import SignupRepository
from sqlalchemy.orm import Session

router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post('/signup/add')
def add_signup(req: SignupReq, sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    signup = Signup(password=req.password, username=req.username, id=req.id)
    result = repo.insert_signup(signup)
    if result is True:
        return signup
    else:
        return JSONResponse(content={"message": "create signup problem encountered"},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/signup/list', response_model=List[SignupReq])
def list_signup(sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    result = repo.get_all_signup()
    return result


@router.get('/signup/list/{id}', response_model=SignupReq)
def get_signup(id: int, sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    result = repo.get_signup(id)
    return result
