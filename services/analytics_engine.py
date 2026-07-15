"""
analytics_engine.py

AI Student Emotional Support System

Emotion Analytics Engine
"""

from collections import Counter
from datetime import datetime


class AnalyticsEngine:

    def __init__(self):
        pass

    # -----------------------------------
    # Emotion Count
    # -----------------------------------

    def emotion_statistics(self, emotions):

        counter = Counter(emotions)

        total = len(emotions)

        report = {}

        for emotion, count in counter.items():

            percentage = round(
                (count / total) * 100,
                2
            )

            report[emotion] = {

                "count": count,

                "percentage": percentage

            }

        return report

    # -----------------------------------
    # Dominant Emotion
    # -----------------------------------

    def dominant_emotion(self, emotions):

        if len(emotions) == 0:

            return "No Data"

        counter = Counter(emotions)

        return counter.most_common(1)[0][0]

    # -----------------------------------
    # Wellness Score
    # -----------------------------------

    def wellness_score(self, emotions):

        score = 100

        for emotion in emotions:

            if emotion == "stress":
                score -= 5

            elif emotion == "sad":
                score -= 5

            elif emotion == "anxiety":
                score -= 6

            elif emotion == "angry":
                score -= 4

            elif emotion == "lonely":
                score -= 5

            elif emotion == "happy":
                score += 2

            elif emotion == "motivated":
                score += 3

        score = max(0, min(score, 100))

        return score

    # -----------------------------------
    # Generate Report
    # -----------------------------------

    def generate_report(self, emotions):

        return {

            "date": datetime.now().strftime("%d-%m-%Y"),

            "dominant_emotion":
                self.dominant_emotion(emotions),

            "wellness_score":
                self.wellness_score(emotions),

            "statistics":
                self.emotion_statistics(emotions)

        }


# -----------------------------------
# Testing
# -----------------------------------

if __name__ == "__main__":

    emotions = [

        "happy",

        "happy",

        "stress",

        "stress",

        "stress",

        "sad",

        "happy",

        "motivated",

        "anxiety",

        "stress"

    ]

    engine = AnalyticsEngine()

    report = engine.generate_report(emotions)

    print(report)