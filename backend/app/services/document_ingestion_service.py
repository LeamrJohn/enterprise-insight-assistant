from pathlib import Path
from app.repositories.chunk_repository import add_chunk
from app.utils.document_chunk import chunk_file
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
    user_id: int,
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
            user_id=user_id,
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


def process_document_chunks(
    db: Session,
    document: Documents,
    settings:  Settings,
) -> Documents:
    assert document.file_path is not None
    absolute_path = settings.storage_dir / document.file_path
    chunk_texts = chunk_file(absolute_path)

    document.status = "processing"
    db.flush()

    for i, text in enumerate(chunk_texts):
        add_chunk(
            db=db,
            document_id=document.id,
            chunk_index=i,
            content=text,
            token_count=len(text.split()),
        )
    document.status = "completed"
    document.content = "\n\n".join(chunk_texts)
    db.commit()
    db.refresh(document)
    return document
