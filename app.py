from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_pdf_text
from utils.docx_reader import extract_docx_text
from utils.analyzer import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    job_description = request.form["job_description"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    resume.save(filepath)

    if resume.filename.endswith(".pdf"):
        resume_text = extract_pdf_text(filepath)

    elif resume.filename.endswith(".docx"):
        resume_text = extract_docx_text(filepath)

    else:
        return "Unsupported File"

    result = analyze_resume(resume_text, job_description)

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)