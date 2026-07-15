"""
recommendation_engine.py

Provides personalized wellness recommendations
based on detected emotion and risk level.
"""

import random
import pandas as pd
import os

class RecommendationEngine:

    def __init__(self):

               
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        csv_path = os.path.join(BASE_DIR, "datasets", "recommendations.csv")

        self.data = pd.read_csv(csv_path)


    # ----------------------------------

    def get_recommendations(
        self,
        emotion,
        risk="LOW"
    ):

        emotion = emotion.lower()

        # HIGH RISK

        if risk == "HIGH":

            return {

                "title": "Please Reach Out",

                "description":
                (
                    "You deserve support. "
                    "Please tell a trusted family member, "
                    "teacher, counselor, or friend how you're feeling. "
                    "If you believe you are in immediate danger, "
                    "contact your local emergency services or crisis hotline."
                )

            }

        rows = self.data[
            self.data["emotion"] == emotion
        ]

        if len(rows) == 0:

            rows = self.data[
                self.data["emotion"] == "neutral"
            ]

        recommendation = rows.sample(1).iloc[0]

        return {

            "title": recommendation["title"],

            "description": recommendation["description"]

        }


# ----------------------------------

if __name__ == "__main__":

    engine = RecommendationEngine()

    while True:

        emotion = input("Emotion : ")

        if emotion == "exit":
            break

        result = engine.get_recommendations(emotion)

        print()

        print(result["title"])

        print(result["description"])

        print("-" * 50)