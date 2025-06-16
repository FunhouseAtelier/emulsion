# server/api/api.py

from fastapi import APIRouter, Request
from routes.api.demo.weather.route import get_weather_data
from routes.api.demo.movie.route import get_movie_data
from routes.api.demo.login.route import demo_login

router = APIRouter(prefix="/api/demo")

@router.get("/weather")
async def weather(request: Request):
    return await get_weather_data(request)

@router.get("/movie")
async def movie(request: Request):
    return await get_movie_data(request)

@router.post("/login")
async def login(request: Request):
    return await demo_login(request)
