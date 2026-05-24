# Resume Extractor

## Project Overview

Resume Extractor is a full-stack web application built to analyze resumes and extract useful information automatically. It helps in evaluating resumes using an ATS (Applicant Tracking System) scoring system and provides structured insights from uploaded resumes.

The project is built using React for the frontend and Flask for the backend with REST API communication between both.

---

## Features

- Upload resume files (PDF, DOCX support depending on implementation)
- Extract important information from resumes
- ATS (Applicant Tracking System) score generation
- Simple and clean user interface
- REST API-based backend communication
- Scalable file handling system for uploads
- Modular backend structure for better maintenance

---

## System Architecture Flow

Below is the high-level architecture of the Resume Extractor system:

![System Architecture](./assets/resume-extractor-architecture.png)

## Tech Stack

### Frontend
- React.js
- JavaScript (ES6+)
- HTML5
- CSS3

### Backend
- Python
- Flask
- Flask REST APIs
- Flask-CORS
- PDF/Text processing libraries (if used in your project)

### Other
- File upload handling system
- Local storage for uploaded files
- REST API architecture

```bash

## Project Structure


Resume-Extractor/
│
├── frontend/ # React frontend
│ ├── src/
│ ├── components/
│ ├── pages/
│ └── App.js
│
├── backend/ # Flask backend
│ ├── app.py
│ ├── routes/
│ ├── utils/
│ └── requirements.txt
│
├── uploads/ # Uploaded resume files
│
├── models/ # Resume processing logic
│
└── README.md

```
---

## System Architecture Flow

1. User uploads resume from frontend.
2. React frontend sends file to Flask backend via REST API.
3. Backend receives and processes the resume file.
4. Text is extracted from the resume.
5. ATS scoring logic evaluates the resume.
6. Backend sends response back to frontend.
7. Frontend displays extracted data and score.

---

## Setup Instructions

### Clone Repository
```bash
git clone https://github.com/your-username/Resume-Extractor.git
cd Resume-Extractor
Setup Backend
cd backend
pip install -r requirements.txt
```
### Run backend server:
```bash
python app.py
```

### Backend will run on:
```bash
http://localhost:5000
```
### Setup Frontend
```bash
cd frontend
npm install
npm start
```
Frontend will run on:
```bash
http://localhost:3000
```
### API Endpoints

Upload Resume
```bash
POST /api/upload
```

Get Resume Analysis
```bash
GET /api/analyze/<file_id>
```
### Future Improvements
1. Improve ATS scoring using advanced NLP models
2. Add cloud storage (AWS / Firebase integration)
3. Add authentication system (Login/Register)
4. Support more resume formats like DOCX and TXT
5. Recruiter dashboard for better analysis
6. Deploy project on cloud (Render / AWS / Vercel)

### Learning Outcome

 While building this project, I learned -

Full-stack development using React and Flask
REST API design and integration
File upload and backend processing
Resume parsing and text extraction techniques
Structuring scalable backend systems
Connecting frontend and backend in real-time applications
