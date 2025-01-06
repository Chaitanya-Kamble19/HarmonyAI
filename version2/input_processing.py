from textblob import TextBlob
from difflib import get_close_matches
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def tokenize_input(user_input: str) -> list[str]:
    """
    Tokenizes the user input using spaCy.
    """
    doc = nlp(user_input)
    return [token.text for token in doc]

def normalize_input(user_input: str) -> tuple[str, list[str]]:
    """
    Normalizes the input and tokenizes it.
    """
    normalized = user_input.strip().capitalize()
    tokens = tokenize_input(normalized)
    return normalized, tokens

def get_sentiment(text: str) -> tuple:
    """
    Analyzes sentiment using TextBlob.
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    """
    Finds the best match for a user question.
    """
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def is_greeting(user_input: str) -> bool:
    """
    Checks if the user input is a greeting.
    """
    return any(greeting in user_input.lower() for greeting in ['hello', 'hi', 'hey'])

def get_sentiment_response(polarity: float) -> str:
    """
    Generates a sentiment-based response.
    """
    if polarity > 0.2:
        return "I'm glad you're feeling positive! 😊 How can I assist you further?"
    elif polarity < -0.2:
        return "I'm sorry you're feeling down. 😔 It's important to talk about how you feel. Can I help you with anything specific?"
    else:
        return "It sounds like you're feeling neutral. If you want to talk more, I'm here to listen."
