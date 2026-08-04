from fastapi import Request, HTTPException

ALLOWED_ROLES = {"Admin", "Editor", "Viewer"}

def require_roles(*allowed: str):
    async def dependency(request: Request):
        role = request.headers.get("X-Role")
        if role not in ALLOWED_ROLES or role not in allowed:
            raise HTTPException(status_code=403, detail="Forbidden: insufficient permissions")
        return role
    return dependency
