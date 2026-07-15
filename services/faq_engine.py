"""
faq_engine.py

AI Student Emotional Support System

Uses TF-IDF + Cosine Similarity
to find the most relevant answer
from the FAQ dataset.
"""

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from services.preprocessing import TextPreprocessor
import os
import pandas as pd


class FAQEngine:

    def __init__(self):

        self.processor = TextPreprocessor()

        # -----------------------------
        # Load FAQ Dataset
        # -----------------------------

       
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        csv_path = os.path.join(BASE_DIR, "datasets", "faq.csv")

        self.data = pd.read_csv(csv_path)

        # -----------------------------
        # Clean Questions
        # -----------------------------

        self.questions = [
            self.processor.preprocess(q)
            for q in self.data["question"]
        ]

        # -----------------------------
        # TF-IDF Model
        # -----------------------------

        self.vectorizer = TfidfVectorizer()

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    # ---------------------------------------
    # Find Best Answer
    # ---------------------------------------

    def get_answer(self, user_message):

        cleaned = self.processor.preprocess(user_message)

        user_vector = self.vectorizer.transform(
            [cleaned]
        )

        similarity = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        index = similarity.argmax()

        score = similarity[0][index]

        if score >= 0.30:

            return {
                "answer": self.data.iloc[index]["answer"],
                "score": round(float(score), 2)
            }

        return {
            "answer": (
                "I'm sorry, I couldn't understand your question.\n"
                "Could you explain it differently?"
            ),
            "score": round(float(score), 2)
        }


# ---------------------------------------
# Testing
# ---------------------------------------

if __name__ == "__main__":

    bot = FAQEngine()

    while True:

        question = input("You : ")

        if question.lower() == "exit":
            break

        result = bot.get_answer(question)

        print()

        print("Bot :", result["answer"])

        print("Similarity :", result["score"])

        print("-" * 40)