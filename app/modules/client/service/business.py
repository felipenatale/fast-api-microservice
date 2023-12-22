
from app.modules.client.repository.repository import get_clients, delete_client, add_client, get_client_in_db, update_client
from app.modules.client.model.client import Client, ClientSchema, UpdateSchema
from datetime import datetime

def get_clients_from_database():

    filter = [Client.deleted_at.is_(None)]
    clients = get_clients(filter)

    return clients

def delete_client_from_database(id):
    return delete_client(id)

def add_client_in_database(client: ClientSchema):
    db_client : Client = Client(
        name = client.name,
        document = client.document,
        address = client.address,
        created_at = datetime.strptime(client.created_at, '%d/%m/%Y')
    )

    return add_client(db_client)

def update_client_in_database(id, client: UpdateSchema):
    return update_client(id, client)


