from datetime import date, time

from pydantic import BaseModel


class AttendanceMemberReq(BaseModel):
    id: int
    member_id: int
    timeout: time
    timein: time
    date_log: date
