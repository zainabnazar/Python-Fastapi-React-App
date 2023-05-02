from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import ARRAY

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class question(BaseModel):
    # we don't need the unique id anymore because the database model will create it for us
   # id:int
    questionText: str
    questionAnswers: List[str]
    correct:str
 


DB: list[question]=[
    question(id=1, questionText="What is the capital of France???",questionAnswers=["Paris","London","Russia"],correct="Paris"),
    question(id=2, questionText="How many planets in the solar system?",questionAnswers=["10","13","16"],correct="13"),
    question(id=3, questionText="Which country launched the world's largest carbon market on February 1, 2021?",questionAnswers=["China","USA","Germany"],correct="USA"),
    question(id=4, questionText="In March 2021, which company announced that it would start producing COVID-19 vaccines for its rival, Johnson & Johnson?",questionAnswers=["Pfizer","Moderna","AstraZeneca"],correct="Pfizer"),
]

# @app.on_event("startup")
# def startup_db():
#     db = SessionLocal()
#     num_questions = db.query(models.Questions).count()
#     all_questions = db.query(models.Questions).all()
#     if num_questions==0:
#         questions = [
#             {'questionText':'What is the capital of France???','correct':'Paris'},
#             {'questionText':"How many planets in the solar system?",'correct':"13"},
#         ]
#         for question in questions:
#             db.add(models.Questions(**question))
#        # db.query(models.Questions).delete()
#         db.commit()
#     else: 
#         print(f"{num_questions} questions already in DB")


@app.get("/api")
def read_root(db: Session= Depends(get_db)):
    #Before we return the hardcoded data, now we want to retunr the database data
    return DB
#    print(db.query(models.Questions).all())
#    return db.query(models.Questions).all()


