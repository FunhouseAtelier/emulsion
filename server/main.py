# server/main.py

# import os
# from app.routes import base, api, demo
# from app.utils.middleware import configure_middleware
# from app.utils.templates import templates
# from dotenv import load_dotenv
# from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from pathlib import Path
# from app.utils.templates import render

# # Load environment mode
# load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
# ENV_MODE = os.getenv("ENV_MODE", "production")
# print(f"🔧 Running in {ENV_MODE.upper()} mode")

from fastapi import FastAPI
from server.api.router import router as api_router
from server.api.demo.router import router as api_demo_router
from server.utils.envars import ENV_MODE

print(f"🔧 Running in {ENV_MODE.upper()} mode")

app = FastAPI()

app.include_router(api_router)
app.include_router(api_demo_router)

# # Create app
# app = FastAPI()

# # Apply all middleware
# configure_middleware(app, ENV_MODE)

# # Serve static files
# app.mount("/static", StaticFiles(directory="app/static", html=False), name="static")

# # Include routers
# app.include_router(base.router) # type: ignore[arg-type]
# app.include_router(api.router) # type: ignore[arg-type]
# # app.include_router(demo.router) # type: ignore[arg-type]

# # Catch-all route for unmatched paths
# @app.get("/{full_path:path}", response_class=HTMLResponse)
# async def catch_all(full_path: str, request: Request):
#     if full_path.startswith("api/") or full_path.startswith("static/"):
#         raise HTTPException(status_code=404)
#     return render("errors/not-found.jinja", request)