from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf, get_similarity_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files['resume']
    job_desc = request.form['job_desc']

    resume_text = extract_text_from_pdf(resume)
    score = get_similarity_score(resume_text, job_desc)

    return render_template('result.html', score=round(score * 100, 2))

if __name__ == '__main__':
    app.run(debug=True)
