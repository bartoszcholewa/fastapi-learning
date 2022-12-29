from fastapi import FastAPI
from student_mgt.controller import admin, assignments, books, reservations

student_app = FastAPI()

student_app.include_router(reservations.router)
student_app.include_router(admin.router)
student_app.include_router(assignments.router)
student_app.include_router(books.router)
