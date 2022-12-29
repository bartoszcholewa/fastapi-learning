from uuid import uuid1

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ch02.login.user import approved_users
from ch02.places.destination import (Tour, TourBasicInfo, TourInput,
                                     TourLocation, tours, tours_basic_info,
                                     tours_locations)

router = APIRouter()


@router.post("/ch02/admin/destination/add")
def add_tour_destination(input: TourInput):
    try:
        tid = uuid1()
        tour = Tour(id=tid,
                    name=input.name,
                    city=input.city,
                    country=input.country,
                    type=input.type,
                    location=input.location,
                    amenities=input.amenities,
                    feedbacks=list(),
                    ratings=0.0,
                    visits=0,
                    isBooked=False)
        tour_basic_info = TourBasicInfo(id=tid,
                                        name=input.name,
                                        type=input.type,
                                        amenities=input.amenities,
                                        ratings=0.0)
        tour_location = TourLocation(id=tid,
                                     name=input.name,
                                     city=input.city,
                                     country=input.country,
                                     location=input.location)
        tours[tid] = tour
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        tour_json = jsonable_encoder(tour)
        return JSONResponse(content=tour_json, status_code=status.HTTP_201_CREATED)
    except Exception:
        return JSONResponse(content={"message": "invalid tour"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.put("/ch02/admin/destination/update", status_code=status.HTTP_202_ACCEPTED)
def update_tour_destination(tour: Tour):
    try:
        tid = tour.id
        tours[tid] = tour
        tour_basic_info = TourBasicInfo(id=tid,
                                        name=tour.name,
                                        type=tour.type,
                                        amenities=tour.amenities,
                                        ratings=tour.ratings)
        tour_location = TourLocation(id=tid,
                                     name=tour.name,
                                     city=tour.city,
                                     country=tour.country,
                                     location=tour.location)
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        return {"message": "tour updated"}
    except Exception:
        return {"message": "tour does not exist"}


@router.get("/ch02/admin/destination/list", status_code=200)
def list_all_tours():
    return tours


@router.get("/ch02/admin/tourist/list")
def list_all_tourists():
    return approved_users
