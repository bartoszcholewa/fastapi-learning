from db_config.sqlalchemy_async_connect import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, Time
from sqlalchemy.orm import relationship


class Attendance_Member(Base):
    __tablename__ = "attendance_member"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('profile_members.id'), unique=False, index=False)
    timeout = Column(Time, unique=False, index=False)
    timein = Column(Time, unique=False, index=False)
    date_log = Column(Date, unique=False, index=False)

    members = relationship('Profile_Members', back_populates="attendance")
