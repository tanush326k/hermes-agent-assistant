from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Hermes Agent (Upgraded)")

app.include_router(router)