from fastapi import FastAPI
from src.agents import branch_analyzer

app = FastAPI()


code = """
    if x > 5 :
        print("good")
"""


@app.post("/analyze")
async def analyze(code: str):
    result = await branch_analyzer(code)
    return result
