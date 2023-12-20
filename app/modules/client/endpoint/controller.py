from fastapi import APIRouter
from database.db_config import create_db_session
from sqlalchemy.sql import text
from app.modules.client.service.business import get_clients_from_database

router = APIRouter(prefix='/client', tags=['client'])

@router.get("/")
async def get_client():
    clients = get_clients_from_database()
    return clients