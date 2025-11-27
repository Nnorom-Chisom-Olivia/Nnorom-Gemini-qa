from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import os
import re

app = Flask(__name__)

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def preprocess_text(text):
    """Clean and normalize input text."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def ask_gemini(question):
    """Fetch Gemini response."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(question)
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    llm_answer = ""
    processed = ""

    if request.method == "POST":
        question = request.form["question"]
        processed = preprocess_text(question)
        llm_answer = ask_gemini(question)

    return render_template("index.html", processed=processed, llm_answer=llm_answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
