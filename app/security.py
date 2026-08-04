import os

from fastapi import HTTPException, Request, Depends


def require_api_key(request: Request):
    api_key = os.getenv("BOOKSTORE_API_KEY", "change-me")
    user_key = request.headers.get("X-API-Key")
    if user_key is None or user_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return user_key
