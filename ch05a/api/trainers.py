from db_config.gino_connect import DB_URL, db
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.requests.trainers import ProfileTrainersReq
from repository.gino.trainers import TrainerRepository


async def sess_db():
    await db.set_bind(DB_URL)


router = APIRouter(dependencies=[Depends(sess_db)])


@router.patch('/trainer/update')
async def update_trainer(id: int, req: ProfileTrainersReq):
    mem_profile_dict = req.dict(exclude_unset=True)
    repo = TrainerRepository()
    result = await repo.update_trainer(id, mem_profile_dict)
    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'update trainer profile problem encountered'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/trainer/list')
async def list_trainers():
    repo = TrainerRepository()
    return await repo.get_all_members()
