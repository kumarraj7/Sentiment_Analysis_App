from flask import Flask, render_template, request
from model import predict_sentiment

app = Flask(__name__)

print("✅ BERT Model Ready!")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("text", "")

        if user_input.strip():
            prediction = predict_sentiment(user_input)

            print("Input:", user_input)
            print("Prediction:", prediction)

    return render_template("index.html",
                           prediction=prediction,
                           text=user_input)


if __name__ == "__main__":
    app.run(debug=True)