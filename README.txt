🚀 Sentiment Analysis Web App (Flask + RoBERTa)

This project is a Sentiment Analysis Web Application built using Flask and a pre-trained RoBERTa model from the 🤗 Hugging Face Transformers library.

It allows users to enter text and instantly get sentiment predictions:
👉 Positive | Neutral | Negative

🏗️ Tech Stack
Backend: Flask
Model: Transformers
Language: Python
ML Model:
cardiffnlp/twitter-roberta-base-sentiment-latest
____________________________________________________
# Sentiment Analysis App

## Run Instructions

1. Install dependencies:
pip install flask transformers scikit-learn pandas torch

2. Place datasets in root folder:
- e_consultation_sentiment_dataset.csv

3. Run:
python app.py

4. Open browser:
http://127.0.0.1:5000
