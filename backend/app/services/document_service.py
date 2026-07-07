from sqlalchemy.orm import Session

from app.repositories.document_repository import (
    get_document,
    save_document,
    get_document_by_id,
    delete_document,
    update_document,
)


def save_document_service(db: Session, user_id:int,name: str, content: str, source: str) -> dict:
    record = save_document(
        db=db,
        user_id = user_id,
        name=name,
        content=content,
        source=source,
    )
    return {
        "id": record.id,
        "name": record.name,
        "content": record.content,
        "source": record.source,
    }


def get_document_service(db: Session, user_id: int) -> list[dict]:
    documents = get_document(db, user_id=user_id)
    result = []
    for document in documents:
        result.append(
            {
                "id": document.id,
                "name": document.name,
                "content": document.content,
                "source": document.source,
            }
        )
    return result


def get_document_by_id_service(db: Session, document_id: int,user_id:int):
    record = get_document_by_id(db, document_id,user_id=user_id)

    if record is None:
        return None

    return {
        "id": record.id,
        "name": record.name,
        "content": record.content,
        "source": record.source,
    }


def delete_document_service(db: Session, document_id: int, user_id: int):
    record = delete_document(db, document_id, user_id=user_id)

    if record is None:
        return None
    return {
        "id": record.id,
        "name": record.name,
        "content": record.content,
        "source": record.source,
    }


def update_document_service(
    db: Session,
    document_id: int,
    user_id: int,
    name: str,
    content: str,
    source: str,
):
    record = update_document(
        db=db,
        document_id=document_id,
        user_id=user_id,
        name=name,
        content=content,
        source=source,
    )

    if record is None:
        return None

    return {
        "id": record.id,
        "name": record.name,
        "content": record.content,
        "source": record.source,
    }
