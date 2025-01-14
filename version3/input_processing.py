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
    Finds the best match for a user question using partial word matching.
    """
    user_tokens = set(tokenize_input(user_question.lower()))
    question_matches = {}

    for question in questions:
        question_tokens = set(tokenize_input(question.lower()))
        overlap = user_tokens.intersection(question_tokens)
        if overlap:
            question_matches[question] = len(overlap) / len(question_tokens)

    # Sort matches by their overlap score
    best_match = max(question_matches, key=question_matches.get, default=None)
    return best_match if question_matches else None

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

# Example usage
if __name__ == "__main__":
    predefined_questions = [
        "What is mental health?",
        "How does stress affect the body?",
        "What are the symptoms of anxiety?",
        "How can I improve my mental well-being?"
    ]

    user_input = input("Ask me a question or say something: ")
    
    if is_greeting(user_input):
        print("Hello! How can I help you today?")
    else:
        normalized_input, tokens = normalize_input(user_input)
        sentiment_polarity, sentiment_subjectivity = get_sentiment(normalized_input)

        match = find_best_match(normalized_input, predefined_questions)
        if match:
            print(f"I found a match: {match}")
        else:
            print("I'm not sure I understand your question, but I'm here to help!")

        sentiment_response = get_sentiment_response(sentiment_polarity)
        print(sentiment_response)
