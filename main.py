from fastapi import FastAPI
from app.routes import healthcheck

app = FastAPI()

app.include_router(healthcheck.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}