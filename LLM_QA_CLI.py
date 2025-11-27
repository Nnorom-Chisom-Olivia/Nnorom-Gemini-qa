import google.generativeai as genai
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

def preprocess_text(text):
    """Lowercase, remove punctuation, and tokenize."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return " ".join(tokens)

def ask_gemini(question):
    """Send question to Gemini LLM."""
    if not question or question.strip() == "":
        return "Error: Question cannot be empty."

    model = genai.GenerativeModel("gemini-2.5-flash")

    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {e}"

def main():
    print("\n=== AI Question Answering CLI ===\n")
    while True:
        q = input("Enter your question (or 'exit'): ").strip()

        if q.lower() == "exit":
            break

        if q == "":
            print("Please enter a valid question.\n")
            continue

        processed = preprocess_text(q)
        print("\nProcessed Question:", processed)

        answer = ask_gemini(q)
        print("\nAI Answer:\n", answer, "\n")

if __name__ == "__main__":
    main()
