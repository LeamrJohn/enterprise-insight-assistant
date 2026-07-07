import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api import document as document_api

def test_unhandled_error_returns_safe_response(monkeypatch: pytest.MonkeyPatch):
    def raise_error(*args,**kwargs):
        raise RuntimeError("sensitive internal detail")
    monkeypatch.setattr(
        document_api,
        "update_document_service",
        raise_error,
    )

    with TestClient(app,raise_server_exceptions=False)as client:
        response = client.put("/documents/2",json={"name":"xx","content":"123","source":"11"})
    assert  response.status_code ==500
    assert  response.headers.get("X-Request-ID")
    assert  response.json() == {
        "code": "internal_error",
        "message": "internal server error",
        "details": [],
    }
    assert  "sensitive internal detail" not in response.text
