"""
Admin-only endpoint for viewing audit logs.
"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..auth import require_admin
from ..database import get_db

router = APIRouter(prefix="/audit-logs", tags=["audit"])


@router.get("/", response_model=list[schemas.AuditLogOut])
def get_audit_logs(
    request: Request,
    db: Session = Depends(get_db),
    admin: str = Depends(require_admin),
):
    """Retrieve all audit logs (admin only)."""
    return crud.get_audit_logs(db)
