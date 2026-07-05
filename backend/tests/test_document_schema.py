from app.schemas.document import DocumentOut


def test_document_out_allows_none_content():

    document_out = DocumentOut(
        id=1,
        name="pending.pdf",
        content=None,
        source="upload",
    )
    assert document_out.content is None
