from utils.ats_score import calculate_ats_score
import re

SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "flask",
    "django",
    "react",
    "node.js",
    "git",
    "github",
    "docker",
    "aws",
    "mongodb",
    "mysql",
    "machine learning",
    "data analysis"
]


def analyze_resume(resume_text, job_description):

    resume = resume_text.lower()
    jd = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in SKILLS:

        if skill in jd:

            if skill in resume:
                matched_skills.append(skill.title())
            else:
                missing_skills.append(skill.title())

    score = calculate_ats_score(
        matched_skills,
        missing_skills
    )

    strengths = []

    if len(matched_skills) >= 5:
        strengths.append("Strong Technical Skills")

    if "project" in resume:
        strengths.append("Good Project Experience")

    if "intern" in resume or "internship" in resume:
        strengths.append("Has Internship Experience")

    if "certification" in resume or "certificate" in resume:
        strengths.append("Has Certifications")

    if len(strengths) == 0:
        strengths.append("Resume contains relevant information.")

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strengths": strengths
    }