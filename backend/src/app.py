from fastapi import FastAPI
from src.controller import router

app = FastAPI()


code = """
    if x > 5 :
        print("good")
"""

app.include_router(router=router)
