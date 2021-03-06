from fastapi.testclient import TestClient


from src.main import app

def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Battle snake noob"}


if __name__ == '__main__':
    client = TestClient(app)
    # test_read_main(client)
