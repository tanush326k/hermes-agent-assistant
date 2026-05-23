from fastapi import APIRouter
from app.agent.executor import run_agent
from app.agent.memory import get_memory

router = APIRouter()

@router.get("/")
def home():
    return {"message": "🔥 Hermes Agent is running"}

@router.post("/run")
def run(task: str):
    return run_agent(task)

@router.get("/memory")
def memory():
    return get_memory()