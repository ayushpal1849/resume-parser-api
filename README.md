# 📄 AI Resume Parser & Scoring API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
![Stars](https://img.shields.io/github/stars/ayushpal1849/resume-parser-api?style=social)


**AI Resume Parser API** is a powerful asynchronous REST API built with **FastAPI** that leverages **OCR (Tesseract)**, **NLP (spaCy)**, and scoring mechanisms to parse resume files (PDF/Image) and extract structured information like skills — even scoring candidates based on job descriptions.

This project is designed for **HR Tech platforms, ATS systems, and AI-driven recruitment tools**.
---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)

---

## � Features

- **📄 Multi-Format Support**: Seamlessly extracts text from **PDF** resumes using `pypdf` and **Image**-based resumes (JPG, PNG) using **Tesseract OCR**.
- **🧠 NLP Skill Extraction**: Utilizes **Spacy** to intelligently identify potential skills (Nouns/Proper Nouns) from the extracted text.
- **📊 Resume Scoring**: Calculates a relevance **score (0-100) against job descriptions** by comparing extracted skills against a provided Job Description.
- **⚡ High Performance**: Built on **FastAPI** for high-speed, **asynchronous** request processing.
- 📄 Auto-generated API documentation (Swagger / ReDoc).

---


## 🧩 Tech Stack

*   **Framework**: FastAPI, Uvicorn
*   **OCR & Image Processing**: PyTesseract, OpenCV (`cv2`), pypdf
*   **Natural Language Processing**: Spacy (`en_core_web_sm`)
*   **Utilities**: Pydantic, Python-Multipart


| Technology | Purpose |
|-----------|---------|
| Python | Core language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| Tesseract OCR | Image text extraction |
| spaCy | NLP processing |
| Pydantic | Data validation |
| OpenCV / PIL | Image processing |

---


## 📂 Project Structure

```bash
resume-parser-api/
│
├── app/
│   ├── api/              # API routes
│   ├── core/             # Business logic
│   ├── services/         # Resume parsing & scoring services
│   ├── utils/            # OCR & helper utilities
│   ├── models/           # Pydantic schemas
│   └── main.py           # App entry point
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.10 - 3.12** (Recommended)
2. **Tesseract OCR Engine**:
   - **Windows**: Download Installer and add the installation path to your System Environment Variables.
   - **Linux**: `sudo apt-get install tesseract-ocr`
   - **macOS**: `brew install tesseract`

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayushpal1849/resume-parser-api.git
   cd resume-parser-api
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Spacy Model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 🏃‍♂️ Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive API docs (Swagger UI) at:
**http://127.0.0.1:8000/docs**

### Key Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | Check API status |
| `POST` | `/api/resume/parse` | Upload a resume (PDF/Image) to extract skills |
| `POST` | `/api/resume/score` | Upload a resume and Job Description to get a match score |

## 🧪 Example Requests

### ▶️ Parse Resume

```bash
curl -X POST "http://localhost:8000/api/resume/parse" \
-F "resume=@resume.pdf"
```

### ▶️ Score Resume Against Job Description

```bash
curl -X POST "http://localhost:8000/api/resume/score" \
-F "resume=@resume.pdf" \
-F "job_description=@jd.txt"
```

## 📤 Sample Response

```json
{
  "candidate_name": "John Doe",
  "skills": ["Python", "FastAPI", "Machine Learning"],
  "experience_years": 2,
  "resume_score": 82
}
```

## 📌 Use Cases

* Applicant Tracking Systems (ATS)

* Resume screening automation

* AI-driven recruitment platforms

* HR analytics tools

* Resume evaluation & ranking systems

<!-- ## 🔒 Error Handling

* Consistent JSON-based error responses

* Validation via Pydantic schemas

* Graceful handling of invalid file formats -->

## 👤 Author

**Ayush Pal**
Python Developer | Backend & AI Engineer

**🔗 GitHub:** https://github.com/ayushpal1849

**🔗 LinkedIn:** https://www.linkedin.com/in/ayush-pal-ap223/