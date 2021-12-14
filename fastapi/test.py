"""
http://127.0.0.1:8000/save_score?id=1&score=2.5
uvicorn test:app --reload
"""
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/save_score")
async def save_score(id, score):
    test = {"message2": "Hello World"}
    print(f"{id} {score}")
    return test

