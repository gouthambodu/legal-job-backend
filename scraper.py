import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

def scrape_civil_service_jobs():
    url = "https://www.civilservicejobs.service.gov.uk/csr/index.cgi"
    params = {
        "SID": "Y3NycF9odG1sPTEyMzQ1Njc4OTAmam9ibGlzdF92aWV3X3ZhYz0xNTM4NDU3JmpvYmxpc3RfY3Vyc29yX2NvbGxhcHNlPXRydWU=",
        "jcode": "",
        "sort": "posting",
        "order": "desc",
        "search_distance": "10",
        "postcode": "",
        "working_pattern": "",
        "location": "",
        "job_type": "",
        "keyword": "legal",  # You can change this to paralegal, trainee, etc.
        "page": "1"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    job_cards = soup.select("div.job-result")

    for i, job in enumerate(job_cards):
        title_tag = job.select_one("h3.job-title a")
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = "https://www.civilservicejobs.service.gov.uk" + title_tag["href"]

        dept = job.select_one("div.job-department").get_text(strip=True) if job.select_one("div.job-department") else "Civil Service"
        location = job.select_one("div.job-location").get_text(strip=True) if job.select_one("div.job-location") else "UK"
        salary = job.select_one("div.job-salary").get_text(strip=True) if job.select_one("div.job-salary") else "N/A"

        jobs.append({
            "id": i + 1,
            "title": title,
            "company": dept,
            "location": {
                "country": "UK",
                "city": location.split(",")[0]
            },
            "salary": salary,
            "posting_date": str(datetime.now().date()),
            "description": f"{title} at {dept}",
            "source": "CivilServiceJobs",
            "job_type": "Legal",
            "url": link
        })

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=4)

    return {"message": f"{len(jobs)} Civil Service jobs saved"}
