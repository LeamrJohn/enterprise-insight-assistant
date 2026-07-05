from pydantic import BaseModel


class DocumentCreate(BaseModel):
    name :str
    content:str
    source:str

class DocumentUpdate(BaseModel):
    name: str
    content: str
    source: str


class DocumentOut(BaseModel):
    id : int
    name :str
    content:str
    source:str
