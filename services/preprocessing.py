"""
preprocessing.py

AI Student Emotional Support System

Handles all text preprocessing before sending
messages to the chatbot engine.
"""

import re
import string
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# Download once
try:
    nltk.corpus.stopwords.words("english")
except LookupError:
    nltk.download("punkt")
    nltk.download("stopwords")

STOP_WORDS = set(nltk.corpus.stopwords.words("english"))


class TextPreprocessor:

    def __init__(self):
        pass

    # ------------------------------------
    # Convert to lowercase
    # ------------------------------------

    def lowercase(self, text):

        return text.lower()

    # ------------------------------------
    # Remove URLs
    # ------------------------------------

    def remove_urls(self, text):

        return re.sub(
            r"http\S+|www\S+",
            "",
            text
        )

    # ------------------------------------
    # Remove Email
    # ------------------------------------

    def remove_email(self, text):

        return re.sub(
            r"\S+@\S+",
            "",
            text
        )

    # ------------------------------------
    # Remove Numbers
    # ------------------------------------

    def remove_numbers(self, text):

        return re.sub(
            r"\d+",
            "",
            text
        )

    # ------------------------------------
    # Remove Punctuation
    # ------------------------------------

    def remove_punctuation(self, text):

        return text.translate(
            str.maketrans(
                "",
                "",
                string.punctuation
            )
        )

    # ------------------------------------
    # Remove Extra Spaces
    # ------------------------------------

    def remove_extra_spaces(self, text):

        return " ".join(text.split())

    # ------------------------------------
    # Tokenize
    # ------------------------------------

    def tokenize(self, text):

        return nltk.word_tokenize(text)

    # ------------------------------------
    # Remove Stopwords
    # ------------------------------------

    def remove_stopwords(self, tokens):

        cleaned = []

        for word in tokens:

            if word not in STOP_WORDS:

                cleaned.append(word)

        return cleaned

    # ------------------------------------
    # Join Tokens
    # ------------------------------------

    def join_words(self, tokens):

        return " ".join(tokens)

    # ------------------------------------
    # Complete Pipeline
    # ------------------------------------

    def preprocess(self, text):

        text = self.lowercase(text)

        text = self.remove_urls(text)

        text = self.remove_email(text)

        text = self.remove_numbers(text)

        text = self.remove_punctuation(text)

        text = self.remove_extra_spaces(text)

        tokens = self.tokenize(text)

        tokens = self.remove_stopwords(tokens)

        text = self.join_words(tokens)

        return text


# ------------------------------------
# Example
# ------------------------------------

if __name__ == "__main__":

    processor = TextPreprocessor()

    sentence = "Hello!! I am Feeling Very Sad after my Exam. :( 123"

    print(processor.preprocess(sentence))