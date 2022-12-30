from typing import Any, Dict

from models.data.sqlalchemy_async_models import Attendance_Member
from sqlalchemy import delete, insert, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class AttendanceRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    async def insert_attendance(self, attendance: Attendance_Member) -> bool:
        try:
            sql = insert(Attendance_Member).values(
                id=attendance.id,
                member_id=attendance.member_id,
                timein=attendance.timein,
                timeout=attendance.timeout,
                date_log=attendance.date_log
            )
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
        except Exception as ex:
            print(ex)
            return False
        return True

    async def update_attendance(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            sql = update(Attendance_Member).where(Attendance_Member.id == id).values(**details)
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
        except Exception as ex:
            print(ex)
            return False
        return True

    async def delete_attendance(self, id: int) -> bool:
        try:
            sql = delete(Attendance_Member).where(Attendance_Member.id == id)
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
        except Exception as ex:
            print(ex)
            return False
        return True

    async def get_all_attendance(self):
        q = await self.sess.execute(select(Attendance_Member))
        return q.scalars().all()

    async def get_attendance(self, id: int):
        q = await self.sess.execute(select(Attendance_Member).where(Attendance_Member.member_id == id))
        return q.scalar()
