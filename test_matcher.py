from modules.matcher import extract_skills

job_description = """
We are hiring an AI Engineer.

Required Skills:
Python
SQL
Machine Learning
AWS
Docker
Git
"""

skills = extract_skills(job_description)

print(skills)