import requests
from datetime import datetime
from jobs.models import Job

# Adzuna API credentials
API_URL = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
APP_ID = "4332cdb8"  # Replace with your actual app ID
APP_KEY = "2bf864a4db54f6e7684c335457b10612"  # Replace with your actual app key

def fetch_and_save_jobs():
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50,  # Adjust as needed
        "content-type": "application/json"
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        for job in data.get("results", []):
            # Extract required fields
            title = job.get("title", "")
            company = job.get("company", {}).get("display_name", "Unknown Company")
            location = job.get("location", {}).get("display_name", "Unknown Location")
            posted_date = datetime.strptime(job["created"], "%Y-%m-%dT%H:%M:%SZ").date()
            details_url = job.get("redirect_url", "")
            salary = f"{job.get('salary_min', 0)} - {job.get('salary_max', 0)}"
            job_type = job.get("contract_time", "")
            is_remote = "remote" in location.lower()
            employer_type = job.get("contract_type", "")

            # Save to the database
            job_obj, created = Job.objects.get_or_create(
                title=title,
                company=company,
                defaults={
                    "location": location,
                    "posted_date": posted_date,
                    "details_url": details_url,
                    "salary": salary,
                    "job_type": job_type,
                    "is_remote": is_remote,
                    "employer_type": employer_type,
                },
            )

            if created:
                print(f"Saved new job: {title} at {company}")
            else:
                print(f"Job already exists: {title} at {company}")
    else:
        print(f"Failed to fetch data: {response.status_code}")
