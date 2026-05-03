from fastapi import FastAPI
from app.api.routes_auth import router as auth_router
from app.api.routes_users import router as users_router
# + routes_referentiels, routes_planning, etc.

app = FastAPI(title="School Timetable API")

app.include_router(auth_router)
app.include_router(users_router)
# app.include_router(...)
