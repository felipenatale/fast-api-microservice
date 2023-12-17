from fastapi import APIRouter

router = APIRouter(prefix='/healthcheck', tags=['token'])

@router.get("/")
async def healthcheck():
    return "healthy"