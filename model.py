import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])
data = data.sample(frac=1, random_state=42)

data["content"] = data["title"] + " " + data["text"]
data = data[["content", "label"]]

x_train, x_test, y_train, y_test = train_test_split(
    data["content"], data["label"], test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer(stop_words="english")
x_train = vectorizer.fit_transform(x_train)

model = LogisticRegression()
model.fit(x_train, y_train)

def predict_news(news):
    transformed = vectorizer.transform([news])
    prediction = model.predict(transformed)

    return "🟢 Real News" if prediction[0] == 1 else "🔴 Fake News"