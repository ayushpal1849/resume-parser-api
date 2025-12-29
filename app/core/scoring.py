def calculate_score(skills, job_description):
    score = 0
    jd = job_description.lower()
    for skill in skills:
        if skill in jd:
            score += 5
    return min(score, 100)
