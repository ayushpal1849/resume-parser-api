from app.core.nlp import extract_skills

def score_resume_service(resume_skills: list[str], job_description: str) -> float:
    """
    Calculates a match score (0-100) by comparing skills extracted from the resume
    against skills extracted from the Job Description.
    """
    # Extract skills from the Job Description using the same NLP logic
    jd_skills = extract_skills(job_description)
    
    # Avoid division by zero if no skills are found in JD
    if not jd_skills:
        return 0.0

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)
    
    matches = resume_set.intersection(jd_set)
    
    # Calculate score based on coverage of JD skills
    score = (len(matches) / len(jd_set)) * 100
    
    return round(score, 2)