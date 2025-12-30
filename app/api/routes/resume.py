from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser_service import parse_resume
from app.services.scoring_service import score_resume_service
from app.models.response_schema import ResumeParseResponse, ResumeScoreResponse

router = APIRouter()

@router.post(
    "/resume/parse",
    response_model=ResumeParseResponse
)
async def parse(file: UploadFile = File(...)):
    return await parse_resume(file)


@router.post(
    "/resume/score",
    response_model=ResumeScoreResponse
)
async def score(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    data = await parse_resume(file)
    score = score_resume_service(data["skills"], job_description)

    return {
        "skills": data["skills"],
        "score": score
    }
