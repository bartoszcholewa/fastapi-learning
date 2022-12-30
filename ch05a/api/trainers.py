from cqrs.commands import ProfileTrainerCommand
from cqrs.trainers.command.create_handlers import AddTrainerCommandHandler
from db_config.gino_connect import DB_URL, db
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.requests.trainers import ProfileTrainersReq
from repository.gino.trainers import TrainerRepository


async def sess_db():
    await db.set_bind(DB_URL)


router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/trainer/add")
async def add_trainer(req: ProfileTrainersReq):
    handler = AddTrainerCommandHandler()
    mem_profile = dict()
    mem_profile["id"] = req.id
    mem_profile["firstname"] = req.firstname
    mem_profile["lastname"] = req.lastname
    mem_profile["age"] = req.age
    mem_profile["position"] = req.position
    mem_profile["tenure"] = req.tenure
    mem_profile["shift"] = req.shift
    command = ProfileTrainerCommand()
    command.details = mem_profile
    result = await handler.handle(command)
    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'create trainer profile problem encountered'}, status_code=500)


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
