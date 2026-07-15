"""
journal_engine.py

AI Student Emotional Support System

Journal Analysis Engine
"""

import pandas as pd

from datetime import datetime


class JournalEngine:

    def __init__(self):

        self.data = pd.read_csv(
            "datasets/journal_prompts.csv"
        )

    # ------------------------------------
    # Journal Prompt
    # ------------------------------------

    def get_prompt(self, emotion):

        emotion = emotion.lower()

        result = self.data[
            self.data["emotion"] == emotion
        ]

        if len(result) == 0:

            result = self.data[
                self.data["emotion"] == "neutral"
            ]

        row = result.sample(1).iloc[0]

        return {

            "prompt": row["prompt"],

            "suggestion": row["suggestion"]

        }

    # ------------------------------------
    # Journal Analysis
    # ------------------------------------

    def analyze(self, journal_text, emotion):

        words = len(journal_text.split())

        characters = len(journal_text)

        return {

            "date": datetime.now().strftime("%d-%m-%Y"),

            "emotion": emotion,

            "word_count": words,

            "character_count": characters,

            "summary":
            (
                "Thank you for writing today's journal. "
                "Writing your thoughts regularly can help you better understand "
                "your emotions and notice patterns over time."
            )

        }


# ------------------------------------
# Testing
# ------------------------------------

if __name__ == "__main__":

    engine = JournalEngine()

    emotion = input("Emotion : ")

    response = engine.get_prompt(emotion)

    print("\nJournal Prompt")
    print("---------------------------")

    print(response["prompt"])

    print()

    text = input("Write Journal : ")

    result = engine.analyze(
        text,
        emotion
    )

    print("\nAnalysis")
    print("---------------------------")

    print(result)