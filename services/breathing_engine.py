"""
breathing_engine.py

AI Student Emotional Support System

Provides breathing exercises
according to detected emotion.
"""

import pandas as pd
import os


class BreathingEngine:

    def __init__(self):
       
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        csv_path = os.path.join(BASE_DIR, "datasets", "breathing.csv")

        self.data = pd.read_csv(csv_path)

    # -----------------------------------------

    def get_exercise(self, emotion):

        emotion = emotion.lower()

        result = self.data[
            self.data["emotion"] == emotion
        ]

        if len(result) == 0:

            result = self.data[
                self.data["emotion"] == "neutral"
            ]

        exercise = result.sample(1).iloc[0]

        return {

            "exercise": exercise["exercise"],

            "duration": exercise["duration"],

            "instructions": exercise["instructions"]

        }


# -----------------------------------------

if __name__ == "__main__":

    engine = BreathingEngine()

    while True:

        emotion = input("Emotion : ")

        if emotion.lower() == "exit":
            break

        response = engine.get_exercise(emotion)

        print()

        print("Exercise :", response["exercise"])

        print("Duration :", response["duration"])

        print("Instructions :")

        print(response["instructions"])

        print("-" * 50)