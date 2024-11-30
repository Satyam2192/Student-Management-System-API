# Student Management System API

## Overview
This is a FastAPI-based Student Management System with MongoDB backend.
- LIVE: https://student-management-system-api-ocpb.onrender.com
- Postman: https://documenter.getpostman.com/view/31555061/2sAYBYeVA3

## Setup

1. Clone the repository
```bash
git clone https://github.com/Satyam2192/Student-Management-System-API.git
cd student_management
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up MongoDB URI
- Create a `.env` file in the project root
- Add your MongoDB connection string:
```
MONGO_URI=mongodb://localhost:27017
```

## Running the Application
```bash
uvicorn main:app --reload
```

## Docker Deployment
```bash
docker build -t student-management-api .
docker run -p 8000:8000 -e MONGO_URI=mongodb://localhost:27017
```

## API Endpoints
- `POST /students`: Create a new student
- `GET /students`: List students with optional filters
- `GET /students/{id}`: Fetch a specific student
- `PATCH /students/{id}`: Update student information
- `DELETE /students/{id}`: Delete a student
