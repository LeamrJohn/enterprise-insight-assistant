from pydantic import BaseModel, StringConstraints
from typing import Annotated
from datetime import datetime

NonBlankStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class DocumentCreate(BaseModel):
    name: str
    content: NonBlankStr
    source: str


class DocumentUpdate(BaseModel):
    name: str
    content: NonBlankStr
    source: str


class DocumentOut(BaseModel):
    id: int
    name: str
    content: str | None = None
    source: str
    file_type: str | None = None
    file_size: int | None = None
    sha256: str | None = None
    status: str = "completed"
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}
