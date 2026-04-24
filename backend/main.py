from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import JDInput
from parser import parse_jd
from scorer import calculate_match_score
import json

app = FastAPI(title="ScoutX AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "running"}


@app.post("/analyze-jd")
def analyze_jd(data: JDInput):
    return parse_jd(data.job_description)


def get_interest_score(persona):
    p = persona.lower()

    if "actively exploring" in p:
        return 92
    elif "burned out" in p:
        return 90
    elif "startup hungry" in p:
        return 84
    elif "passive but curious" in p:
        return 72
    elif "remote only" in p:
        return 65
    elif "higher salary" in p:
        return 68
    elif "leadership seeking" in p:
        return 74
    elif "not looking" in p:
        return 35

    return 60


def get_reply(persona):
    p = persona.lower()

    if "actively exploring" in p:
        return (
            "Sounds interesting. Happy to discuss the opportunity.",
            "Warm Lead 🔥"
        )

    elif "burned out" in p:
        return (
            "Open to switching soon if the role has strong growth.",
            "Warm Lead 🔥"
        )

    elif "startup hungry" in p:
        return (
            "Interested if there is ownership and fast growth.",
            "Interested 🚀"
        )

    elif "passive but curious" in p:
        return (
            "Not actively looking, but open to hearing details.",
            "Passive 👀"
        )

    elif "not looking" in p:
        return (
            "Happy where I am currently. Maybe later.",
            "Cold ❄️"
        )

    return (
        "Please share more details.",
        "Neutral"
    )


@app.post("/match-candidates")
def match_candidates(data: JDInput):
    parsed = parse_jd(data.job_description)

    with open("../dataset/candidates.json", "r", encoding="utf-8") as f:
        candidates = json.load(f)

    results = []

    for candidate in candidates:
        match_score = calculate_match_score(candidate, parsed)
        interest_score = get_interest_score(candidate["persona"])

        final_score = round(
            (match_score * 0.7) + (interest_score * 0.3), 2
        )

        reply_text, status = get_reply(candidate["persona"])

        outreach = (
            f"Hi {candidate['name'].split()[0]}, "
            f"your experience as a {candidate['current_role']} "
            f"stood out. Open to discussing this role?"
        )

        candidate_skills = [s.lower() for s in candidate["skills"]]
        overlap = list(set(candidate_skills) & set(parsed["skills"]))

        reasons = []

        if overlap:
            reasons.append("Skill match: " + ", ".join(overlap[:3]))

        if candidate["experience_years"] >= parsed["experience"] and parsed["experience"] > 0:
            reasons.append(
                f"{candidate['experience_years']} years relevant experience"
            )

        reasons.append(f"Persona: {candidate['persona']}")

        if final_score >= 85:
            priority = "Hot Lead"
        elif final_score >= 70:
            priority = "Strong Fit"
        elif final_score >= 55:
            priority = "Consider"
        else:
            priority = "Low Priority"

        results.append({
            "name": candidate["name"],
            "role": candidate["current_role"],
            "location": candidate["location"],
            "match_score": match_score,
            "interest_score": interest_score,
            "final_score": final_score,
            "priority": priority,
            "persona": candidate["persona"],
            "why_matched": reasons,
            "outreach_message": outreach,
            "candidate_reply": reply_text,
            "engagement_status": status
        })

    ranked = sorted(results, key=lambda x: x["final_score"], reverse=True)

    return {
        "parsed_jd": parsed,
        "total_candidates_scanned": len(candidates),
        "shortlist": ranked[:10]
    }