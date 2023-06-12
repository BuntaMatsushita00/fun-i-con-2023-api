from pydantic import BaseModel,Field
from typing import List



class Answer(BaseModel):
    name: str
    value: str

class Answers(BaseModel):
    answers: List[Answer] = Field(...,unique_items=True)
