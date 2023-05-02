from sqlalchemy import Column, Integer, String
from database import Base
from typing import List
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import ARRAY


class Questions(Base):
    __tablename__ = "questionss"
    id = Column(Integer, primary_key=True, index=True)
    questionText = Column(String)
    # questionAnswers = Column(ARRAY(String))
    correct = Column(String)
   