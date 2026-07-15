"""
Emotion Detection Engine

Uses TF-IDF + Multinomial Naive Bayes
"""

import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from services.preprocessing import TextPreprocessor


class EmotionEngine:

    def __init__(self):

        self.processor = TextPreprocessor()
       
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        csv_path = os.path.join(BASE_DIR, "datasets", "emotions.csv")

        self.data = pd.read_csv(csv_path)


        self.texts = [
            self.processor.preprocess(text)
            for text in self.data["text"]
        ]

        self.labels = self.data["emotion"]

        self.vectorizer = TfidfVectorizer()

        X = self.vectorizer.fit_transform(self.texts)

        self.model = MultinomialNB()

        self.model.fit(X, self.labels)

    # -----------------------------
    # Predict Emotion
    # -----------------------------

    def predict(self, sentence):

        cleaned = self.processor.preprocess(sentence)

        vector = self.vectorizer.transform([cleaned])

        emotion = self.model.predict(vector)[0]

        probability = self.model.predict_proba(vector).max()

        return {
            "emotion": emotion,
            "confidence": round(float(probability), 2)
        }


# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":

    engine = EmotionEngine()

    while True:

        text = input("Message : ")

        if text.lower() == "exit":
            break

        result = engine.predict(text)

        print()

        print("Emotion :", result["emotion"])

        print("Confidence :", result["confidence"])

        print("-" * 40)