from scraper import scrape_civil_service_jobs
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
from datetime import datetime

app = FastAPI()

# Allow frontend (Bolt) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to the Legal Job Finder API. Go to /jobs to see listings."}

# GET /jobs with optional filters
@app.get("/jobs")
def get_jobs(
    type: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    country: Optional[str] = Query(None),
    source: Optional[str] = Query(None),
    search: Optional[str] = Query(None)
):
    with open("jobs.json", "r") as f:
        jobs = json.load(f)

    filtered = []
    for job in jobs:
        if type and job["job_type"].lower() != type.lower():
            continue
        if city and job["location"]["city"].lower() != city.lower():
            continue
        if country and job["location"]["country"].lower() != country.lower():
            continue
        if source and job["source"].lower() != source.lower():
            continue
        if search and search.lower() not in (
            job["title"].lower()
            + job["company"].lower()
            + job["description"].lower()
        ):
            continue
        filtered.append(job)

    return filtered

@app.get("/scrape")
def scrape():
    return scrape_civil_service_jobs()

    with open("jobs.json", "w") as f:
        json.dump(sample_jobs, f, indent=4)
    return {"message": "Jobs updated"}
