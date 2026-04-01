from flask import Flask, render_template, request
from model import predict_news

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        news = request.form["news"]
        prediction = predict_news(news)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)