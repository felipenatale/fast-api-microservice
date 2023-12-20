from fastapi import APIRouter
from database.db_config import create_db_session
from sqlalchemy.sql import text
import time

router = APIRouter(prefix='/healthcheck', tags=['healthcheck'])

@router.get("/")
async def healthcheck():
    return "healthy"

@router.get("/database")
def check_database_health():
    try:                
        start_time = time.time()
        session_db = create_db_session()
        session_db.execute(text('SELECT 1'))
        end_time = time.time()
        
        elapsed_time = end_time - start_time        

        return {"status":"healthy", "time": elapsed_time}
    except Exception as err:
        return 'error', 500