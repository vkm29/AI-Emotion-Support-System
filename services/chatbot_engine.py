"""
chatbot_engine.py

AI Student Emotional Support System

Main chatbot engine.

Responsibilities:
- Greeting detection
- Gratitude detection
- Emotional support
- Safety detection
- FAQ search
"""

import random

from services.faq_engine import FAQEngine


class ChatbotEngine:

    def __init__(self):

        self.faq = FAQEngine()

        self.greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening"
        ]

        self.thanks = [
            "thanks",
            "thank you",
            "thankyou"
        ]

        # High-risk phrases
        self.high_risk_keywords = [

            "suicide",
            "kill myself",
            "end my life",
            "die",
            "i don't want to live",
            "life is meaningless",
            "nobody cares",
            "hopeless",
            "worthless",
            "everyone hates me"

        ]

    # ----------------------------------------
    # Greeting
    # ----------------------------------------

    def greeting_response(self):

        responses = [

            "Hello 👋 How are you feeling today?",

            "Hi 😊 I'm here to listen. How can I support you today?",

            "Welcome 🌸 Tell me what's on your mind."

        ]

        return random.choice(responses)

    # ----------------------------------------
    # Thanks
    # ----------------------------------------

    def thanks_response(self):

        responses = [

            "You're always welcome ❤️",

            "I'm happy to help.",

            "Take care of yourself 🌸"

        ]

        return random.choice(responses)

    # ----------------------------------------
    # Safety Detection
    # ----------------------------------------

    def safety_response(self):

        return (
            "I'm really sorry you're going through such a difficult time. "
            "You don't have to face this alone.\n\n"
            "Please consider talking to someone you trust—a family member, "
            "friend, teacher, or counselor—as soon as possible.\n\n"
            "If you feel you might act on these thoughts or you're in immediate "
            "danger, contact your local emergency services or a crisis hotline "
            "right away.\n\n"
            "I'm here to listen, but I also want to help you connect with "
            "people who can support you in person."
        )

    # ----------------------------------------
    # Main Response
    # ----------------------------------------

    def get_response(self, message):

        text = message.lower().strip()

        # Greeting

        if text in self.greetings:

            return self.greeting_response()

        # Thanks

        if text in self.thanks:

            return self.thanks_response()

        # High Risk

        for keyword in self.high_risk_keywords:

            if keyword in text:

                return self.safety_response()

        # FAQ

        result = self.faq.get_answer(message)

        return result["answer"]


# ----------------------------------------
# Testing
# ----------------------------------------

if __name__ == "__main__":

    bot = ChatbotEngine()

    print("\nAI Student Emotional Support System")
    print("-----------------------------------")

    while True:

        message = input("\nYou : ")

        if message.lower() == "exit":
            break

        print()

        print("Bot :", bot.get_response(message))