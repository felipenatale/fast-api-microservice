from fastapi import FastAPI
from app.routes import healthcheck
from app.modules.client.endpoint import controller

app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(controller.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}