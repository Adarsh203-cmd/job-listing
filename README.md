# Job Listing Application

The Job Listing Application is a full-stack web application that allows users to browse, filter, and manage job listings dynamically. It combines a robust Django-based backend with a ReactJS frontend to deliver a seamless user experience. The backend interacts with an external API to fetch job data and provides RESTful API endpoints, while the frontend renders the data dynamically with features like pagination and search filters.

## Features

### Backend
- Fetches job data from an external API using a Python script (`utils.py`).
- Provides RESTful API endpoints for managing job listings.
- Supports operations like GET, PUT, and dynamic filtering.

### Frontend
- Built using ReactJS for a dynamic and interactive user experience.
- Implements pagination for better data handling.
- Provides search and filter functionalities to refine job results.

---

## API Endpoints

The backend API endpoints can be tested using Postman or similar tools.

### Base URL: `http://127.0.0.1:8000/api/jobs/`

#### Example Endpoints:
- **GET**: Retrieve all job listings.
- **PUT**: Update a job listing.
  ```json
  {
      "title": "Django Developer",
      "company": "Temperstack",
      "location": "Reading, Berkshire",
      "posted_date": "2024-11-25",
      "updated_at": null,
      "details_url": "https://www.adzuna.co.uk/jobs/details/4950314317?utm_medium=api&utm_source=4332cdb8",
      "salary": "35000 - 35000",
      "job_type": "full_time",
      "is_remote": false,
      "employer_type": "permanent"
  }


# Setup and Installation
To set up and run this project on your local machine, follow these steps:

# 1. Backend Setup (Django)
Step 1: Clone the repository to your local machine:
```bash
 https://github.com/yourusername/joblisting.git
``` 
# Step 2: Navigate to the backend folder:
```bash
cd joblisting
```
# Step 3: Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
# Step 4: Run the Django development server:
```bash
python manage.py runserver
```
The backend will now be running at http://127.0.0.1:8000.
# 2. Frontend Setup (ReactJS)
Step 1: Navigate to the frontend folder:
```bash
cd job-frontend
```
# Step 2: Install the required dependencies using npm:
```bash
npm install
```
# Step 3: Run the React development server:
```bash
npm run dev
```
The frontend will now be running at http://localhost:3000.
## Technologies Used
### Backend:
-Django: For backend development and API creation.
-Django REST Framework: For building RESTful APIs.
-Python: The core language for backend logic.
-Postman: For testing API endpoints.
### Frontend:
-ReactJS: For building the user interface.
-JavaScript: For frontend development.
