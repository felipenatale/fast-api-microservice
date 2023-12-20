
from app.modules.client.repository.repository import get_clients
from app.modules.client.model.client import Client

def get_clients_from_database():

    filter = [Client.deleted_at.is_(None)]
    clients = get_clients(filter)

    return clients
