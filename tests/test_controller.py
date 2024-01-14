from fastapi.testclient import TestClient
from main import app

def test_should_add_client():
    client = TestClient(app) #arrange

    response = client.post(
        '/client/',
        json={"name": "testename", "document": "test document", "address": "teste address", "created_at": "23/11/2022"}
    ) #act

    assert response.status_code == 200 #assert
    assert response.json() == ["Operação realizada com sucesso!"] #asser

def test_should_get_client():
    client = TestClient(app)
    client.post(
        '/client/',
        json={"name": "testename", "document": "test document", "address": "teste address", "created_at": "23/11/2022"}
    ) #act
    response = client.get('/client/')

    assert response.status_code == 200