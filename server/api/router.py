# server/api/api.py

from fastapi import APIRouter, Request
from routes.api.version.route import get_version_data

router = APIRouter(prefix="/api")

@router.get("/version")
async def version():
    return get_version_data()
