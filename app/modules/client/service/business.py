
from app.modules.client.repository.repository import get_clients, delete_client
from app.modules.client.model.client import Client

def get_clients_from_database():

    filter = [Client.deleted_at.is_(None)]
    clients = get_clients(filter)

    return clients

def delete_client_from_database(id):
    return delete_client(id)