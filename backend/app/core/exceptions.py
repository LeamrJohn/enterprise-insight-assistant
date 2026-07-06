from uuid import uuid4
from fastapi import Request
from fastapi.responses import JSONResponse


class DocumentUploadError(Exception):
    pass


class EmptyDocumentError(DocumentUploadError):
    pass


class UnsupportedDocumentTypeError(DocumentUploadError):
    pass


class DocumentTooLargeError(DocumentUploadError):
    pass


class InvalidDocumentNameError(DocumentUploadError):
    pass


class DuplicateDocumentError(DocumentUploadError):
    pass


async def unhandled_exception_handler(
    request: Request,
    _exc: Exception,
) -> JSONResponse:
    request_id = getattr(
        request.state,
        "request_id",
        uuid4().hex,
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "internal server error"},
        headers={"X-Request-ID": request_id},
    )
