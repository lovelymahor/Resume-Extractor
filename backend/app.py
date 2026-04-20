from flask import Flask, request, jsonify
from flask_cors import CORS
from pdfminer.high_level import extract_text as pdfminer_extract
from pdf2image import convert_from_bytes
import pytesseract

app = Flask(__name__)
CORS(app)

# ✅ Tesseract path (IMPORTANT)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ---------------------------
# PDF TEXT EXTRACTION (PDF + OCR)
# ---------------------------
def extract_text(file):
    file.seek(0)

    # 1. Try PDF text extraction
    try:
        text = pdfminer_extract(file)
        if text and text.strip():
            return text
    except Exception as e:
        print("PDFMiner Error:", e)

    # 2. OCR fallback
    try:
        file.seek(0)
        images = convert_from_bytes(file.read())

        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)

        return text

    except Exception as e:
        print("OCR ERROR:", e)
        return ""


# ---------------------------
# RESUME VALIDATION
# ---------------------------
def is_resume(text):
    text_lower = text.lower()
    keywords = ["project", "skills", "experience", "education", "intern", "github", "linkedin"]
    matches = sum(1 for k in keywords if k in text_lower)
    return matches >= 2


# ---------------------------
# ATS SCORING ENGINE
# ---------------------------
def analyze_resume_text(text):
    score = 0
    feedback = []
    career_scores = {
        "Frontend Developer": 0,
        "Backend Developer": 0,
        "Data Analyst": 0
    }

    text_lower = text.lower()

    # Skills (30)
    skills = ["python", "java", "c++", "javascript", "react", "node", "sql", "html", "css"]
    skill_hits = sum(1 for s in skills if s in text_lower)
    score += min(skill_hits * 4, 30)

    if skill_hits < 2:
        feedback.append("Add more technical skills")

    # Projects (25)
    project_count = text_lower.count("project")
    if project_count:
        score += min(10 + project_count * 5, 25)
    else:
        feedback.append("Add detailed project section")

    # Experience (20)
    if "intern" in text_lower or "experience" in text_lower:
        score += 20
    else:
        score += 5
        feedback.append("Add internship or experience")

    # Education (10)
    if any(x in text_lower for x in ["b.sc", "bsc", "btech", "university", "college"]):
        score += 10
    else:
        feedback.append("Add education details")

    # Links (10)
    if "github" in text_lower:
        score += 5
    else:
        feedback.append("Add GitHub profile")

    if "linkedin" in text_lower:
        score += 5
    else:
        feedback.append("Add LinkedIn profile")

    # Structure (5)
    if len(text) > 1200:
        score += 5
    else:
        feedback.append("Improve resume structure and detail")

    score = min(score, 100)

    # Career scoring
    if "react" in text_lower:
        career_scores["Frontend Developer"] += 4
    if "javascript" in text_lower:
        career_scores["Frontend Developer"] += 3
    if "html" in text_lower:
        career_scores["Frontend Developer"] += 2
    if "css" in text_lower:
        career_scores["Frontend Developer"] += 2

    if "node" in text_lower:
        career_scores["Backend Developer"] += 4
    if "express" in text_lower:
        career_scores["Backend Developer"] += 3
    if "api" in text_lower:
        career_scores["Backend Developer"] += 2
    if "python" in text_lower:
        career_scores["Backend Developer"] += 2

    if "sql" in text_lower:
        career_scores["Data Analyst"] += 4
    if "pandas" in text_lower:
        career_scores["Data Analyst"] += 3
    if "numpy" in text_lower:
        career_scores["Data Analyst"] += 2
    if "python" in text_lower:
        career_scores["Data Analyst"] += 2

    best_score = max(career_scores.values())

    career = [
        role for role, val in career_scores.items()
        if val == best_score and best_score > 0
    ]

    if not career:
        career = ["General IT / Entry-Level Software Role"]

    return score, feedback, career


# ---------------------------
# API ROUTE
# ---------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    text = extract_text(file)

    print("EXTRACTED TEXT:", repr(text[:500]))

    if not text.strip():
        return jsonify({
            "score": 0,
            "feedback": ["Could not read PDF (OCR/PDF issue)"],
            "career": ["Not detected"]
        })

    if not is_resume(text):
        return jsonify({
            "score": 0,
            "feedback": ["This file does not look like a resume"],
            "career": ["Not applicable"]
        })

    score, feedback, career = analyze_resume_text(text)

    return jsonify({
        "score": score,
        "feedback": feedback,
        "career": career
    })


# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)