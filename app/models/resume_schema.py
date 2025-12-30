from pydantic import BaseModel

class ResumeParseRequest(BaseModel):
    """
    Request schema for resume scoring
    """
    job_description: str


class ResumeScoreRequest(BaseModel):
    """
    Request schema for resume scoring
    """
    job_description: str
