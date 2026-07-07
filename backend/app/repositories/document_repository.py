from sqlalchemy.orm import Session
from app.models.documents import Documents
from sqlalchemy import select


def save_document(db: Session, user_id:int,name: str, content: str, source: str):
    record = Documents(user_id=user_id,name=name, content=content, source=source)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_document(
    db: Session,
):
    return db.query(Documents).order_by(Documents.id.desc()).all()


def get_document_by_id(db: Session, document_id: int):
    return db.query(Documents).filter(Documents.id == document_id).first()


def delete_document(db: Session, document_id: int):
    record = db.query(Documents).filter(Documents.id == document_id).first()

    if record is None:
        return None

    db.delete(record)
    db.commit()
    return record


def update_document(
    db: Session, document_id: int, name: str, content: str, source: str
):
    record = db.query(Documents).filter(Documents.id == document_id).first()

    if record is None:
        return None

    record.name = name
    record.content = content
    record.source = source

    db.commit()
    db.refresh(record)
    return record


def get_document_by_sha256(db: Session, sha256: str) -> Documents | None:
    statement = select(Documents).where(Documents.sha256 == sha256)
    return db.scalar(statement)


def add_uploaded_document(
    db: Session,
    *,
    name: str,
    file_path: str,
    file_type: str,
    file_size: int,
    sha256: str,
) -> Documents:
    record = Documents(
        name=name,
        content=None,
        source="upload",
        file_path=file_path,
        file_type=file_type,
        file_size=file_size,
        sha256=sha256,
        status="pending",
        error_message=None,
    )
    db.add(record)
    db.flush()
    return record
