# ScoutX AI 🚀

AI-Powered Talent Scouting & Engagement Agent

ScoutX AI helps recruiters move from Job Description to ranked shortlist in minutes.

Instead of manually screening resumes, sourcing profiles, and chasing candidate interest, ScoutX uses AI-driven scoring to identify the best-fit candidates and estimate their likelihood of engaging.

---

# 🌟 Problem Statement

Recruiters spend hours:

- Parsing job descriptions manually
- Searching through candidate databases
- Comparing profiles one by one
- Following up with low-response candidates
- Losing time on unqualified leads

ScoutX AI solves this by automating the entire first layer of hiring intelligence.

---

# 💡 What ScoutX AI Does

Input a Job Description.

ScoutX AI automatically:

✅ Parses required skills, experience, and role signals  
✅ Scans candidate dataset  
✅ Calculates Match Score  
✅ Simulates candidate intent / engagement likelihood  
✅ Calculates Interest Score  
✅ Generates personalized outreach messages  
✅ Simulates candidate responses  
✅ Produces ranked shortlist instantly

---
# ScoutX AI Architecture

                ┌──────────────────────┐
                │   Recruiter Inputs   │
                │  Job Description JD  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Next.js Frontend   │
                │   Vercel Hosted UI   │
                └──────────┬───────────┘
                           │ REST API
                           ▼
                ┌──────────────────────┐
                │   FastAPI Backend    │
                │   Render Hosted API  │
                └──────────┬───────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐  ┌────────────────┐  ┌────────────────────┐
│ JD Parser     │  │ Match Engine   │  │ Interest Engine    │
│ Skills        │  │ Skill overlap  │  │ Persona signals    │
│ Experience    │  │ Experience fit │  │ Intent scoring     │
│ Role signals  │  │ Role relevance │  │ Reply simulation   │
└──────┬────────┘  └──────┬─────────┘  └──────────┬─────────┘
       │                  │                       │
       └────────────┬─────┴──────────────┬────────┘
                    ▼                    ▼
             ┌──────────────────────────────────┐
             │      Ranking & Prioritization    │
             │ Final Score = 70% Match         │
             │             + 30% Interest      │
             └──────────────┬──────────────────┘
                            ▼
             ┌──────────────────────────────────┐
             │ Ranked Shortlist Output          │
             │ Hot Lead / Strong Fit / Consider │
             │ Outreach Msg + Candidate Reply   │
             └──────────────────────────────────┘

Data Source:
JSON Candidate Dataset (20+ profiles)

# 🏆 Core Output

Each candidate receives:

- **Match Score** → How well profile matches JD  
- **Interest Score** → Predicted willingness to engage  
- **Final Score** → Weighted ranking score  
- **Priority Tag** → Hot Lead / Strong Fit / Consider  
- **AI Outreach Message**  
- **Simulated Candidate Reply**

---

# ⚙️ Tech Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Vercel Deployment

## Backend

- FastAPI
- Python

## Hosting

- Render (Backend API)
- Vercel (Frontend)

---

# 🧠 Scoring Logic

## Match Score (70%)

Calculated using:

- Skill overlap with JD
- Relevant years of experience
- Role relevance
- Startup / growth fit signals

## Interest Score (30%)

Behavioral intent model based on candidate persona:

Examples:

- Actively Exploring → High
- Burned Out / Ready to Move → High
- Passive but Curious → Medium
- Not Looking → Low

## Final Score

Final Score =

0.7 × Match Score + 0.3 × Interest Score

---

# 📊 Example Use Case

## Input JD

Hiring Senior Backend Engineer:

- Node.js
- AWS
- MongoDB
- 5+ years experience
- Bangalore / Hybrid

## Output

1. Rahul Sharma — Final Score 97.6 (Hot Lead)  
2. Siddharth Jain — Final Score 96.7 (Hot Lead)  
3. Sneha Reddy — Final Score 83.9 (Strong Fit)

---

# 🔥 Why ScoutX AI Is Valuable

Recruiters save hours of manual sourcing.

Instead of reviewing 100 profiles manually:

ScoutX instantly surfaces top 10 ranked candidates ready for outreach.

---

# 🚀 Live Demo

Frontend App:

(Paste Vercel URL here)

Backend API:

https://scoutx-ai.onrender.com

---

# 📂 Repositories

Main Repo:

https://github.com/vijaymoka/scoutx-ai

Frontend Repo:

https://github.com/vijaymoka/scoutx-frontend

---

# 📹 Demo Video

(Add Loom / YouTube link here)

---

# 🏗 Future Roadmap

- LinkedIn / Naukri integrations
- Real candidate outreach via Email / WhatsApp
- LLM-powered resume understanding
- ATS integrations
- Live recruiter dashboard
- Feedback learning loop

---

# 👤 Built For Catalyst Hackathon

By Vijay Krishna Moka

---