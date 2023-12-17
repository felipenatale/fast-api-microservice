from fastapi.testclient import TestClient
from main import app

def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app) #arrange

    response = client.get('/') #act

    assert response.status_code == 200 #assert
    assert response.json() == {'message': 'Hello World'} #assert