def calculate_match_score(candidate, parsed_jd):
    score = 0

    candidate_skills = [s.lower() for s in candidate["skills"]]
    jd_skills = parsed_jd["skills"]

    role = candidate["current_role"].lower()

    # -------------------
    # 1. Skill Overlap (Highest Weight)
    # -------------------
    overlap = len(set(candidate_skills) & set(jd_skills))
    score += overlap * 20

    # -------------------
    # 2. Role Relevance
    # -------------------
    if "backend" in role:
        score += 20
    elif "full stack" in role:
        score += 14
    elif "devops" in role:
        score += 12
    elif "data engineer" in role:
        score += 8
    elif "frontend" in role:
        score += 4
    else:
        score += 0

    # -------------------
    # 3. Experience Match
    # -------------------
    required_exp = parsed_jd["experience"]
    candidate_exp = candidate["experience_years"]

    if required_exp > 0:
        diff = abs(candidate_exp - required_exp)

        if diff == 0:
            score += 20
        elif diff == 1:
            score += 16
        elif diff == 2:
            score += 12
        else:
            score += 6
    else:
        score += 10

    # -------------------
    # 4. Communication Bonus
    # -------------------
    score += candidate["communication_score"] * 0.08

    # -------------------
    # 5. GitHub Bonus
    # -------------------
    score += candidate["github_score"] * 0.05

    # -------------------
    # 6. Persona Bonus
    # -------------------
    persona = candidate["persona"].lower()

    if "actively exploring" in persona:
        score += 8
    elif "startup hungry" in persona:
        score += 6
    elif "passive but curious" in persona:
        score += 4
    elif "not looking" in persona:
        score -= 5

    # -------------------
    # Final Cap
    # -------------------
    return round(min(score, 100), 2)