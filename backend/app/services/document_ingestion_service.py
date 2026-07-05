from typing import BinaryIO
from sqlalchemy.orm import Session
from app.core.settings import Settings
from app.core.exceptions import DuplicateDocumentError
from app.models.documents import Documents
from app.repositories.document_repository import (
    add_uploaded_document,
    get_document_by_sha256,
)
from app.services.file_storage_service import save_document_file
from sqlalchemy.exc import IntegrityError


def upload_document_service(
    db: Session,
    *,
    file_stream: BinaryIO,
    original_name: str | None,
    settings: Settings,
) -> Documents:
    stored_file = save_document_file(
        file_stream=file_stream, original_name=original_name, settings=settings
    )
    try:
        existing_document = get_document_by_sha256(db, stored_file.sha256)
        if existing_document is not None:
            raise DuplicateDocumentError(
                f"Document with SHA256 {stored_file.sha256} already exists."
            )

        record = add_uploaded_document(
            db=db,
            name=stored_file.original_name,
            file_path=stored_file.relative_path,
            sha256=stored_file.sha256,
            file_size=stored_file.size_bytes,
            file_type=stored_file.extension,
        )
        db.commit()
        db.refresh(record)
        return record
    except IntegrityError as exc:
        db.rollback()
        stored_file.absolute_path.unlink(missing_ok=True)
        raise DuplicateDocumentError(
            f"Document with SHA256 {stored_file.sha256} already exists."
        ) from exc
    except Exception:
        db.rollback()
        stored_file.absolute_path.unlink(missing_ok=True)
        raise
