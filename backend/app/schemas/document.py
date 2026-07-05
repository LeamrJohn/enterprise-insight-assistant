from pydantic import BaseModel, StringConstraints
from typing import Annotated

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
    content: str | None
    source: str
