from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine
from app.models import models
from app.routers.routes import router

app = FastAPI(title="AI Agent Backend")

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Backend do Agente de IA rodando!"}
