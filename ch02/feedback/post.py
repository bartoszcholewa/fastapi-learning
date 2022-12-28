from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ch02.utility import check_post_owner

from ..handler_exceptions import PostFeedbackException, PostRatingException

router = APIRouter()


@router.get("/feedback/list")
async def show_tourist_post(touristId: UUID):
    tourist_posts = [
        assess for assess in feedback_tour.values()
        if assess.tourist_id == touristId
    ]
    tourist_posts_json = jsonable_encoder(tourist_posts)
    return JSONResponse(content=tourist_posts_json, status_code=200)


@router.post("/feedback/add")
def post_tourist_feedback(touristId: UUID, tid: UUID, post: Post, bg_task: BackgroundTask):
    if approved_users.get(touristId) is None and tours.get(tid) is None:
        raise PostFeedbackException(detail='tourist and tour details invalid', status_code=403)
    assessId = uuid1()
    assessment = Assessment(id=assessId, post=post, tour_id=tid, tourist_id=touristId)
    feedback_tour[assessId] = assessment
    tours[tid].ratings = (tours[tid].ratings + post.rating) / 2
    bg_task.add_task(log_post_transaction, str(touristId), message="post_tourist_feedback")
    assess_json = jsonable_encoder(assessment)
    return JSONResponse(content=assess_json, status_code=200)


@router.delete("/feedback/delete")
async def delete_tourist_feedback(assessId: UUID, touristId: UUID):
    if approved_users.get(touristId) is None and feedback_tour.get(assessId):
        raise PostFeedbackException(detail="tourist and tour details invalid", status_code=403)
    post_delete = [
        assess for assess in feedback_tour.values()
        if assess.id == assessId
    ]
    for assess in post_delete:
        is_owner = await check_post_owner(feedback_tour, assess.id, touristId)
        if is_owner:
            del feedback_tour[assess.id]
    return JSONResponse(content={"message": f"deleted posts for {touristId}"}, status_code=200)


@router.post("/feedback/update/rating")
def update_tour_rating(assessId: UUID, new_rating: StarRating):
    if feedback_tour.get(assessId) is None:
        raise PostRatingException(detail='tour assessment invalid', status_code=403)
    tid = feedback_tour[assessId].tour_id
    tours[tid].ratings = (tours[tid].ratings + new_rating) / 2
    tour_json = jsonable_encoder(tours[tid])
    return JSONResponse(content=tour_json, status_code=200)
