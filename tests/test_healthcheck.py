from fastapi.testclient import TestClient
from main import app

def test_healthcheck_deve_retornar_200_e_healthy():
    client = TestClient(app) #arrange

    response = client.get('/healthcheck/') #act

    assert response.status_code == 200 #assert
    assert response.json() == 'healthy' #assert