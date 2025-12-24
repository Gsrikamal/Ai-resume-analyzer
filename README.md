# AI Resume Analyzer & Job Recommendation System

This project is a Flask-based web application that analyzes resumes and compares them with job descriptions using Natural Language Processing (NLP) and a pre-trained BERT model.

## Technologies Used
- Python
- Flask
- NLP
- BERT (Sentence Transformers)
- HTML
- CSS

## Features
- Upload resume in PDF format
- Paste job description
- Generate resume–job match score using cosine similarity

## How to Run the Project
1. Clone the repository
2. Create virtual environment  
   python -m venv venv
3. Activate virtual environment  
   venv\Scripts\activate
4. Install dependencies  
   pip install -r requirements.txt
5. Run application  
   python app.py
6. Open browser and go to  
   http://127.0.0.1:5000/

## Use Case
Helps job seekers understand how well their resume matches a specific job role.

## Note
This project uses a pre-trained BERT model. No custom model training is performed.
