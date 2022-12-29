from datetime import datetime
from typing import List
from uuid import UUID, uuid1

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ch02.login.user import approved_users
from ch02.places.destination import TourBasicInfo, tours

router = APIRouter()

tour_preferences = set()


class Visit(BaseModel):
    id: UUID
    destination: List[TourBasicInfo]
    last_tour: datetime


class Booking(BaseModel):
    id: UUID
    destination: TourBasicInfo
    booking_date: datetime
    tourist_id: UUID


@router.get("/ch02/tourist/tour/booked")
def show_booked_tours(touristId: UUID):
    if approved_users.get(touristId) is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="details are missing",
                            headers={"X-InputError": "missing tourist ID"})
    return approved_users[touristId].tours


@router.post("/ch02/tourist/tour/booking/add")
def create_booking(tour: TourBasicInfo, touristId: UUID):
    if approved_users.get(touristId) is None:
        raise HTTPException(status_code=500, detail="details are missing")
    booking = Booking(id=uuid1(),
                      destination=tour,
                      booking_date=datetime.now(),
                      tourist_id=touristId)
    approved_users[touristId].tours.append(tour)
    approved_users[touristId].booked += 1
    tours[tour.id].isBooked = True
    tours[tour.id].visits += 1
    return booking
