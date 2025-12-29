from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.parser_service import parse_resume
from app.services.scoring_service import score_resume_service

router = APIRouter()

@router.post("/resume/parse")
async def parse(file: UploadFile = File(...)):
    try:
        return await parse_resume(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/resume/score")
async def score(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        data = await parse_resume(file)
        score = score_resume_service(data["skills"], job_description)
        return {
            "skills": data["skills"],
            "score": score
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
