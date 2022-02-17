from fastapi import FastAPI
from Routes.route_user import user_route
import uvicorn


api = FastAPI()
api.include_router(user_route)
