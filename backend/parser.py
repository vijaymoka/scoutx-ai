def parse_jd(jd_text):
    text = jd_text.lower()

    skills_master = [
        "python", "node.js", "react", "aws", "docker",
        "mongodb", "postgresql", "kubernetes",
        "fastapi", "java", "sql", "typescript"
    ]

    found_skills = [skill for skill in skills_master if skill in text]

    experience = 0

    for i in range(1, 16):
        if f"{i} year" in text or f"{i}+ years" in text:
            experience = i

    return {
        "skills": found_skills,
        "experience": experience
    }