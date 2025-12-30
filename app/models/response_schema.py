from pydantic import BaseModel
from typing import List

class ResumeParseResponse(BaseModel):
    text_length: int
    skills: List[str]


class ResumeScoreResponse(BaseModel):
    skills: List[str]
    score: int
