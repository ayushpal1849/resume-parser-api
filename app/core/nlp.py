import spacy
from spacy.language import Language

# Load the Spacy model
nlp = spacy.load("en_core_web_sm")

# Extensive list of skills (Tech + Soft Skills)
# You can expand this list or load it from a JSON file for production use
SKILLS_DB = [
    # Programming Languages
    "Python", "Java", "C++", "C#", "JavaScript", "TypeScript", "Ruby", "Go", "Swift", "Kotlin", "PHP", "Rust", "SQL",
    # Web & Frameworks
    "HTML", "CSS", "React", "Angular", "Vue.js", "Node.js", "Django", "Flask", "FastAPI", "Spring Boot", "ASP.NET", "jQuery", "Bootstrap", "Tailwind",
    # Data Science & AI
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "TensorFlow", "PyTorch", "Scikit-Learn", "Pandas", "NumPy", "OpenCV", "Keras", "Matplotlib", "Seaborn",
    # Databases
    "PostgreSQL", "MySQL", "MongoDB", "Redis", "Oracle", "Firebase", "Cassandra", "DynamoDB",
    # DevOps & Cloud
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Jenkins", "Git", "GitHub", "GitLab", "CI/CD", "Terraform", "Ansible", "Linux", "Bash",
    # Soft Skills
    "Communication", "Teamwork", "Problem Solving", "Leadership", "Time Management", "Critical Thinking", "Adaptability", "Creativity", "Conflict Resolution",
    # Tools & Methodologies
    "JIRA", "Trello", "Slack", "Excel", "Power BI", "Tableau", "Agile", "Scrum", "Kanban", "Waterfall", "REST API", "GraphQL", "SOAP"
]

# Add EntityRuler to the pipeline for phrase matching
# This allows us to match multi-token skills like "Machine Learning" automatically
if "entity_ruler" not in nlp.pipe_names:
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    
    patterns = []
    for skill in SKILLS_DB:
        # Create a pattern for case-insensitive matching
        # nlp.make_doc(skill) ensures multi-word skills are tokenized correctly for the pattern
        pattern_tokens = [{"LOWER": token.text.lower()} for token in nlp.make_doc(skill)]
        patterns.append({"label": "SKILL", "pattern": pattern_tokens})
    
    ruler.add_patterns(patterns)

def extract_skills(text: str) -> list[str]:
    """
    Extracts skills from the text using Spacy EntityRuler.
    Filters only entities labeled as 'SKILL'.
    """
    # Remove newlines to ensure sentence structure is somewhat preserved
    doc = nlp(text.replace("\n", " "))
    
    unique_skills = set()
    
    # Extract entities labeled as SKILL by our EntityRuler
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            unique_skills.add(ent.text.title()) # Normalize to Title Case
            
    return list(unique_skills)