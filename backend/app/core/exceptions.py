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
