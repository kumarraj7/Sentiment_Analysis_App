from transformers import pipeline

print("🚀 Loading RoBERTa...")

bert_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)


def predict_sentiment(text):
    try:
        result = bert_model(text[:512])[0]

        print("Raw Output:", result)

        label = result['label'].lower()  

        if "positive" in label:
            return "positive"
        elif "neutral" in label:
            return "neutral"
        else:
            return "negative"

    except Exception as e:
        print("Error:", e)
        return "neutral"