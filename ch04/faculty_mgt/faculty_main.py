from faculty_mgt.controller import admin, assignments, books
from fastapi import FastAPI

faculty_app = FastAPI()

faculty_app.include_router(admin.router)
faculty_app.include_router(assignments.router)
faculty_app.include_router(books.router)
