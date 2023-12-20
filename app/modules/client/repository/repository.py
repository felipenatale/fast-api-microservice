from app.modules.client.model.client import Client
from database.db_config import session_scope

def get_clients(filter):
    client_dict = []
    
    try:
        with session_scope() as session:
        
            clients = session.query(Client).filter(*filter).all()

            for client in clients:
                client_dict.append({"Id": client.id, "Name": client.name, "Address": client.address, "document": client.document})

            return client_dict

    except Exception as error:
        print (error)
        return {}
