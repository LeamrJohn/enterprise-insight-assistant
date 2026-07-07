from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.document import DocumentCreate, DocumentOut, DocumentUpdate
from app.services.document_service import (
    get_document_by_id_service,
    get_document_service,
    save_document_service,
    delete_document_service,
    update_document_service,
)
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/documents", response_model=list[DocumentOut])
def get_document(db: Session = Depends(get_db)):
    return get_document_service(db)


@router.post("/documents", response_model=DocumentOut)
def create_document(
    request_model: DocumentCreate,
    current_user :User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return save_document_service(
        db=db,
        user_id = current_user.id,
        name=request_model.name,
        content=request_model.content,
        source=request_model.source,
    )


@router.get("/documents/{document_id}", response_model=DocumentOut)
def get_document_by_id(document_id: int, db: Session = Depends(get_db)):
    record = get_document_by_id_service(db, document_id)
    if record is None:
        raise HTTPException(status_code=404, detail="document not found")
    return record


@router.delete("/documents/{document_id}", response_model=DocumentOut)
def delete_document_by_id(document_id: int, db: Session = Depends(get_db)):
    record = delete_document_service(db, document_id)

    if record is None:
        raise HTTPException(status_code=404, detail="document not found")

    return record


@router.put("/documents/{document_id}", response_model=DocumentOut)
def update_document_by_id(
    document_id: int,
    request_model: DocumentUpdate,
    db: Session = Depends(get_db),
):
    record = update_document_service(
        db=db,
        document_id=document_id,
        name=request_model.name,
        content=request_model.content,
        source=request_model.source,
    )

    if record is None:
        raise HTTPException(status_code=404, detail="document not found")

    return record
