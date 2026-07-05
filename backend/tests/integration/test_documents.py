from fastapi.testclient import TestClient


def test_document_lifecycle(
    client: TestClient,
) -> None:
    create_response = client.post(
        "/documents",
        json={
            "name": "pytest-document",
            "content": "Stored in the PostgreSQL test database.",
            "source": "pytest",
        },
    )

    assert create_response.status_code == 200
    created = create_response.json()
    document_id = created["id"]

    get_response = client.get(f"/documents/{document_id}")
    assert get_response.status_code == 200
    assert get_response.json() == created

    update_response = client.put(
        f"/documents/{document_id}",
        json={
            "name": "pytest-document-updated",
            "content": "Updated through the real repository.",
            "source": "pytest",
        },
    )
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "pytest-document-updated"

    delete_response = client.delete(f"/documents/{document_id}")
    assert delete_response.status_code == 200

    missing_response = client.get(f"/documents/{document_id}")
    assert missing_response.status_code == 404
    assert missing_response.headers["X-Request-ID"]
    assert missing_response.json() == {"detail": "document not found"}
