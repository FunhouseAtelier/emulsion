# routes/api/demo/login/route.py

from fastapi import Request
import hashlib

# Demo constants
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "abc123"
DEMO_SALT = "s0m3_$@lt_v4lu3"

def verify_password_hash(password_hash: str) -> bool:
    expected_hash = hashlib.sha256((DEMO_PASSWORD + DEMO_SALT).encode()).hexdigest()
    return password_hash == expected_hash

async def demo_login(request: Request):
    form = await request.form()
    username = form.get("username", "").strip()
    password_hash = form.get("password_hash", "").strip()

    if username != DEMO_USERNAME or not verify_password_hash(password_hash):
        return {"status": "error", "message": "Invalid username or password."}

    return {"status": "success", "message": "Logged in as admin."}
