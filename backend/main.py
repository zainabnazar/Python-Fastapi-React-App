from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class question(BaseModel):
    id:int
    text: str

DB: list[question]=[
    question(id=1, text="question 1"),
    question(id=2, text="question 2"),
    question(id=3, text="question 3"),
    question(id=4, text="question 4"),

]

@app.get("/api")
def read_root():
    return DB

