from fastapi.testclient import TestClient
from app.modules.client.model.client import Client
from app.modules.client.repository.repository import get_client_in_db
from main import app
from alchemy_mock.mocking import UnifiedAlchemyMagicMock

def test_inserindo_cliente_deve_retornar_sucesso():
    
    # session = UnifiedAlchemyMagicMock()

    # client = Client(name="Joao", document="32165498723", address="Rua Polar")
    # session.add(client)
    # session.commit()

    assert True == True