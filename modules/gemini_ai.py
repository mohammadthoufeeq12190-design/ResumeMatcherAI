def generate_feedback(resume_text, match_score, missing_skills):

    return f"""
AI Resume Review

Strengths:
- Strong Python skills
- Good Machine Learning knowledge
- Practical AI projects

Missing Skills:
{', '.join(missing_skills)}

Suggestions:
- Learn AWS
- Learn Docker
- Add more AI projects

Hiring Recommendation:
Resume Match Score: {match_score}%

Suitable for entry-level AI Engineer roles.
"""