"""
safety_engine.py

AI Student Emotional Support System

Detects emotional risk level and
returns an appropriate supportive response.
"""

import re


class SafetyEngine:

    def __init__(self):

        self.high_risk = [

            "i want to die",
            "i want to kill myself",
            "end my life",
            "suicide",
            "no reason to live",
            "better off dead",
            "i cannot go on",
            "everyone would be better without me",
            "i don't want to live",
            "i'm done"

        ]

        self.medium_risk = [

            "hopeless",
            "worthless",
            "i hate myself",
            "i am alone",
            "i am lonely",
            "crying",
            "depressed",
            "anxiety",
            "panic",
            "stress",
            "failure",
            "nobody cares",
            "i feel empty",
            "overwhelmed"

        ]

    # -------------------------------------
    # Clean Text
    # -------------------------------------

    def clean(self, text):

        text = text.lower()

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # -------------------------------------
    # Detect Risk
    # -------------------------------------

    def detect(self, message):

        message = self.clean(message)

        # HIGH RISK

        for word in self.high_risk:

            if word in message:

                return {

                    "risk": "HIGH",

                    "color": "danger",

                    "action": "escalate"

                }

        # MEDIUM RISK

        for word in self.medium_risk:

            if word in message:

                return {

                    "risk": "MEDIUM",

                    "color": "warning",

                    "action": "support"

                }

        return {

            "risk": "LOW",

            "color": "success",

            "action": "normal"

        }

    # -------------------------------------
    # Response
    # -------------------------------------

    def response(self, level):

        if level == "HIGH":

            return (
                "I'm really sorry you're going through this. "
                "You deserve support, and you don't have to face it alone.\n\n"
                "Please tell a trusted family member, friend, teacher, or counselor how you're feeling as soon as you can.\n\n"
                "If you feel you might act on these thoughts or you're in immediate danger, contact your local emergency services or a crisis hotline right away."
            )

        if level == "MEDIUM":

            return (
                "It sounds like you're having a difficult time. "
                "Thank you for sharing that with me.\n\n"
                "Would you like to tell me what has been making you feel this way? "
                "Talking to someone you trust or a counselor can also be a really helpful next step."
            )

        return (
            "I'm here to support you. "
            "Feel free to share what's on your mind."
        )


# -------------------------------------
# Testing
# -------------------------------------

if __name__ == "__main__":

    engine = SafetyEngine()

    while True:

        message = input("You : ")

        if message.lower() == "exit":
            break

        result = engine.detect(message)

        print("\nRisk :", result["risk"])

        print("Action :", result["action"])

        print()

        print(engine.response(result["risk"]))

        print("-" * 50)