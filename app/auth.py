"""
Placeholder authentication module.
TODO: Replace with real auth from tickets 6/7 once they are implemented.
Currently uses a hardcoded API-key-to-role mapping for demonstration.
"""
import logging

from fastapi import HTTPException, Request

# Hardcoded API keys with roles (never use in production).
# In a real implementation these would come from an environment variable or database.
_API_KEYS = {
    "admin-key": {"role": "admin"},
    "user-key": {"role": "user"},
}


def _extract_actor_info(request: Request) -> str:
    """
    Extract actor string from the X-API-Key header.
    Returns a string like 'key:admin-key role:admin' or 'anonymous'.
    """
    api_key = request.headers.get("X-API-Key")
    if not api_key:
        return "anonymous"
    info = _API_KEYS.get(api_key)
    if info:
        return f"key:{api_key} role:{info['role']}"
    # Unknown key – still log it but mark role as unknown
    logging.warning(f"Unknown API key used: {api_key}")
    return f"key:{api_key} role:unknown"


def get_current_actor(request: Request) -> str:
    """
    FastAPI dependency that returns the actor string for the current request.
    """
    return _extract_actor_info(request)


def require_admin(request: Request) -> str:
    """
    FastAPI dependency that raises 403 if the request does not belong to an admin.
    """
    actor = _extract_actor_info(request)
    if "role:admin" not in actor:
        raise HTTPException(status_code=403, detail="Admin access required")
    return actor
