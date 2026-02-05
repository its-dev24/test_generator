from fastapi import APIRouter
from src.agents import branch_analyzer

router = APIRouter()


@router.get("/analyze")
async def analyze(code: str):
    result = await branch_analyzer(code)
    return result
