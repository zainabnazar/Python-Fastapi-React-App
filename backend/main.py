from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class question(BaseModel):
    id:int
    questionText: str
    questionAnswers: List[str]
    correct:str



DB: list[question]=[
    question(id=1, questionText="What is the capital of France?",questionAnswers=["Paris","London","Russia"],correct="Paris"),
    question(id=2, questionText="How many planets in the solar system?",questionAnswers=["10","13","16"],correct="13"),
    question(id=3, questionText="Which country launched the world's largest carbon market on February 1, 2021?",questionAnswers=["China","USA","Germany"],correct="USA"),
    question(id=4, questionText="In March 2021, which company announced that it would start producing COVID-19 vaccines for its rival, Johnson & Johnson?",questionAnswers=["Pfizer","Moderna","AstraZeneca"],correct="Pfizer"),
]

@app.get("/api")
def read_root():
    return DB

