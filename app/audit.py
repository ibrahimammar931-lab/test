"""
Audit logging middleware.
Records every successful POST, PUT, DELETE request in the audit_logs table.
"""
import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from . import crud
from .auth import _extract_actor_info
from .database import SessionLocal


class AuditLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        # Only log mutating requests that returned a 2xx status
        if request.method in ("POST", "PUT", "DELETE") and 200 <= response.status_code < 300:
            path = request.url.path.strip("/")
            parts = path.split("/")
            resource_type = parts[0] if parts else ""
            resource_id = None
            if len(parts) >= 2 and parts[1].isdigit():
                resource_id = int(parts[1])

            actor = _extract_actor_info(request)

            db = SessionLocal()
            try:
                audit_data = {
                    "method": request.method,
                    "path": path,
                    "resource_type": resource_type,
                    "resource_id": resource_id,
                    "actor": actor,
                }
                crud.create_audit_log(db, audit_data)
            except Exception:
                logging.warning("Failed to write audit log", exc_info=True)
            finally:
                db.close()

        return response
