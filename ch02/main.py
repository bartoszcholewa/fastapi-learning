from datetime import datetime

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as GlobalStarletteHTTPException

from ch02.admin import manager
from ch02.feedback import post
from ch02.handler_exceptions import PostFeedbackException, PostRatingException
from ch02.login import user
from ch02.places import destination
from ch02.tourist import visit

app = FastAPI()

app.include_router(manager.router)
app.include_router(user.router)
app.include_router(destination.router)
app.include_router(visit.router)
app.include_router(post.router, prefix="/ch02/post")


@app.middleware("http")
async def log_transaction_filter(request: Request, call_next):
    start_time = datetime.now()
    method_name = request.method
    qp_map = request.query_params
    pp_map = request.path_params
    with open("request_log.txt", mode="a") as reqfile:
        content = f"method: {method_name}, query param: {qp_map}, path params: {pp_map} received at {start_time}"
        reqfile.write(content)
    response = await call_next(request)
    process_time = datetime.now() - start_time
    response.headers["X-Time-Elapsed"] = str(process_time)
    return response


@app.exception_handler(PostFeedbackException)
def feedback_exception_handler(req: Request, ex: PostFeedbackException):
    return JSONResponse(status_code=ex.status_code, content={"message": f"error: {ex.detail}"})


@app.exception_handler(PostRatingException)
def rating_exception_handler(req: Request, ex: PostRatingException):
    return JSONResponse(status_code=ex.status_code, content={"message": f"error: {ex.detail}"})


@app.exception_handler(GlobalStarletteHTTPException)
def global_exception_handler(req: Request, ex: str):
    return PlainTextResponse(f"Error message: {ex}", status_code=400)


@app.exception_handler(RequestValidationError)
def validationerror_exception_handler(req: Request, ex: str):
    return PlainTextResponse(f"Error message: {ex}", status_code=400)
