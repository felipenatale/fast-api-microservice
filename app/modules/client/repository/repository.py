from app.modules.client.model.client import Client, ClientSchema, UpdateSchema
from database.db_config import session_scope

def get_clients(filter):
    client_dict = []
    
    try:
        with session_scope() as session:
        
            clients = get_client_in_db(session, filter)

            for client in clients:
                client_dict.append({"Id": client.id, "Name": client.name, "Address": client.address, "document": client.document})

            return client_dict

    except Exception as error:
        print (error)
        return {}

def get_client_in_db(session, filter):
    return session.query(Client).filter(*filter).all()

def get_one_client_in_db(session, filter):
    return session.query(Client).filter(*filter).first()

def delete_client(id):
    try:
        with session_scope() as session:
        
            filter = [Client.id == id]
            clients = get_client_in_db(session, filter)

            for client in clients:
                session.delete(client)
                
            return {"Operação realizada com sucesso!"}

    except Exception as error:
        print (error)
        return {"Erro na operação."}

def add_client(client: Client):
    try:
        with session_scope() as session:
        
            session.add(client)
                
            return {"Operação realizada com sucesso!"}

    except Exception as error:
        print (error)
        return {"Erro na operação."}

def update_client(id: int, client: UpdateSchema):
    try:
        with session_scope() as session:
        
            filter = [Client.id == id]
            client_db = get_one_client_in_db(session, filter)

            client_db.address = client.address
                
            return {"Operação realizada com sucesso!"}

    except Exception as error:
        print (error)
        return {"Erro na operação."}