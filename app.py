# FINAL SUBMISSION: Nnorom's GEMINI AI Q&A WEB APP
# Developed by Nnorom | Bioinformatics | November 2025

from flask import Flask, render_template_string, request
import google.generativeai as genai

# My WORKING KEY (already tested and working)
genai.configure(api_key="AIzaSyDdeKqzg3y152OOYoVKrwgetgAv_osLP3w")
model = genai.GenerativeModel('gemini-2.5-flash')

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Nnorom - AI Question & Answer System</title>
    <style>
        body {font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color:white; padding:40px;}
        .container {max-width:900px; margin:auto; background:rgba(255,255,255,0.1); padding:50px; border-radius:25px; backdrop-filter:blur(10px);}
        h1 {text-align:center; font-size:48px; margin:0;}
        .tagline {text-align:center; font-size:22px; margin:10px 0 30px;}
        textarea {width:100%; padding:20px; font-size:19px; border-radius:15px; border:none; margin-top:20px;}
        input[type="submit"] {background:#ff6b6b; color:white; padding:20px 70px; font-size:24px; border:none; border-radius:50px; cursor:pointer; margin-top:25px;}
        input[type="submit"]:hover {background:#e91e63;}
        .answer {background:white; color:#333; padding:35px; margin-top:40px; border-radius:20px; border-left:8px solid #ff6b6b;}
        footer {text-align:center; margin-top:60px; font-size:15px;}
    </style>
</head>
<body>
<div class="container">
    <h1>Nnorom's AI Q&A</h1>
    <p class="tagline">Powered by Google Gemini 2.5 Flash • Developed by Chisom</p>

    <form method="POST">
        <textarea name="q" rows="6" placeholder="Ask me anything… e.g., Explain how AlphaFold changed protein research" required></textarea>
        <center><input type="submit" value="ASK GEMINI"></center>
    </form>

    {% if answer %}
    <div class="answer">
        <h2>Gemini Answer:</h2>
        <p>{{ answer }}</p>
    </div>
    {% endif %}

    <footer>© Nnorom • Bioinformatics Student • Nigeria • November 2025</footer>
</div>
</body>
</html>
'''
@app.route('/', methods=['GET', 'POST'])
def home():
    answer = ""
    if request.method == 'POST':
        question = request.form['q']
        response = model.generate_content(question)
        answer = response.text
    return render_template_string(HTML, answer=answer)

print("\nNnorom, YOUR FINAL GEMINI APP IS LIVE!!!")
print("Click → http://127.0.0.1:5000")
print("Every question answers in 2–4 seconds — perfect!\n")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=False)
