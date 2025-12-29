from app.utils.file_handler import save_file, delete_file
from app.core.ocr import extract_text
from app.core.nlp import extract_skills

async def parse_resume(file):
    path = save_file(file)
    try:
        text = extract_text(path)
    finally:
        delete_file(path)

    skills = extract_skills(text)
    return {
        "text_length": len(text),
        "skills": skills
    }
