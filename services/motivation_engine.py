"""
motivation_engine.py

Returns motivational quotes
based on detected emotion.
"""

import os
import pandas as pd


class MotivationEngine:

    def __init__(self):


      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
      csv_path = os.path.join(BASE_DIR, "datasets", "motivation.csv")

      self.data = pd.read_csv(csv_path)

    # -----------------------------------

    def get_quote(self, emotion):

        emotion = emotion.lower()

        quotes = self.data[
            self.data["emotion"] == emotion
        ]

        if len(quotes) == 0:

            quotes = self.data[
                self.data["emotion"] == "neutral"
            ]

        quote = quotes.sample(1).iloc[0]

        return quote["quote"]


# -----------------------------------

if __name__ == "__main__":

    engine = MotivationEngine()

    while True:

        emotion = input("Emotion : ")

        if emotion.lower() == "exit":
            break

        print()

        print(engine.get_quote(emotion))

        print("-" * 40)