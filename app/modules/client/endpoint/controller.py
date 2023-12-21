from fastapi import APIRouter
from database.db_config import create_db_session
from sqlalchemy.sql import text
from sqlalchemy import Integer
from app.modules.client.service.business import get_clients_from_database, delete_client_from_database

router = APIRouter(prefix='/client', tags=['client'])

@router.get("/")
async def get_client():
    clients = get_clients_from_database()
    return clients

@router.delete("/{id}")
async def delete_client(id: int):
    clients = delete_client_from_database(id)
    return clients

    