def extract_skills(text):

    skills_db = [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Artificial Intelligence",
        "Pandas",
        "NumPy",
        "Scikit-Learn",
        "TensorFlow",
        "PyTorch",
        "Keras",
        "NLP",
        "Computer Vision",
        "Streamlit",
        "Flask",
        "FastAPI",
        "Django",
        "Git",
        "GitHub",
        "Power BI",
        "Tableau",
        "Excel",
        "AWS",
        "Azure",
        "GCP",
        "Docker",
        "Kubernetes",
        "Linux",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "FAISS",
        "LangChain",
        "RAG",
        "LLM",
        "OpenAI",
        "Gemini"
    ]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_skills, jd_skills):

    matched = []
    missing = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(jd_skills) == 0:
        score = 0

    else:
        score = round(
            (len(matched) / len(jd_skills)) * 100,
            2
        )

    return score, matched, missing