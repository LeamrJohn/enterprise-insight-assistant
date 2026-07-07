import pytest
from fastapi.testclient import TestClient

from app.api import document as document_api
from app.main import app


def test_unhandled_exception_returns_safe_500(monkeypatch: pytest.MonkeyPatch):
    def raise_runtime_error(_db):
        raise RuntimeError("sensitive internal detail")

    monkeypatch.setattr(
        document_api,
        "get_document_service",
        raise_runtime_error,
    )

    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get("/documents")

    assert response.status_code == 500
    assert response.headers.get("X-Request-ID")
    assert response.json() == {
        "code": "internal_error",
        "message": "internal server error",
        "details": [],
    }
    assert "sensitive internal detail" not in response.text


def test_unhandled_exception_preserves_incoming_request_id(
    monkeypatch: pytest.MonkeyPatch,
):
    def raise_runtime_error(_db):
        raise RuntimeError("sensitive internal detail")

    monkeypatch.setattr(
        document_api,
        "get_document_service",
        raise_runtime_error,
    )
    request_id = "test-request-id"

    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get("/documents", headers={"X-Request-ID": request_id})

    assert response.status_code == 500
    assert response.headers["X-Request-ID"] == request_id
