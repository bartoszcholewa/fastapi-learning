from db_config.sqlalchemy_async_connect import AsyncSessionFactory
from fastapi import APIRouter
from models.data.sqlalchemy_async_models import Attendance_Member
from models.requests.attendance import AttendanceMemberReq
from repository.aslalchemy.attendance import AttendanceRepository

router = APIRouter()


@router.post('/attendance/add')
async def add_attendance(req: AttendanceMemberReq):
    async with AsyncSessionFactory() as sess:
        async with sess.begin():
            repo = AttendanceRepository(sess)
            attendance = Attendance_Member(
                id=req.id,
                member_id=req.member_id,
                timein=req.timein,
                timeout=req.timeout,
                date_log=req.date_log
            )
            return await repo.insert_attendance(attendance)


@router.patch('/attendance/update')
async def update_attendance(id: int, req: AttendanceMemberReq):
    async with AsyncSessionFactory() as sess:
        async with sess.begin():
            repo = AttendanceRepository(sess)
            attendance_dict = req.dict(exclude_unset=True)
            return await repo.update_attendance(id, attendance_dict)


@router.delete('/attendance/delete/{id}')
async def delete_attendance(id: int):
    async with AsyncSessionFactory() as sess:
        async with sess.begin():
            repo = AttendanceRepository(sess)
            return await repo.delete_attendance(id)


@router.get('/attendance/list')
async def list_attendance():
    async with AsyncSessionFactory() as sess:
        async with sess.begin():
            repo = AttendanceRepository(sess)
            return await repo.get_all_attendance()
