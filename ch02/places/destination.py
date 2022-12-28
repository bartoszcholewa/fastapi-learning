from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/ch02/destinations/mostbooked")
def check_recommended_tour(resp: Response):
    resp.headers['X-Access-Tours'] = 'TryUs'
    resp.headers['X-Contact-Details'] = '1900888TOLL'
    resp.headers['Content-Language'] = 'en-US'
    ranked_desc_rates = sort_orders = sorted(tours.items(), key=lambda x: x[1].ratings, reverse=True)
    return ranked_desc_rates


@router.get("/ch02/destinations/details/{id}")
def check_tour_profile(id: UUID):
    tour_info_json = jsonable_encoder(tours[id])
    return JSONResponse(content=tour_info_json)


@router.get("/ch02/destinations/list/all")
def list_tour_destinations():
    tours_json = jsonable_encoder(tours)
    resp_headers = {
        'X-Access-Tours': 'Try Us',
        'X-Contact_details': '1-900-888-TOLL',
        'Set-Cookie': 'AppName=ITS; Max-Age=3600; Version=1'
    }
    return JSONResponse(content=tours_json, headers=resp_headers)
