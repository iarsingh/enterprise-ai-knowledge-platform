from fastapi.testclient import TestClient
from entknow.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'Where does customer data stay?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "policy"
    miss = client.post("/ask", json={"question": 'sports'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
