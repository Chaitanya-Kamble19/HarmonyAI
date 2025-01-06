from input_processing import normalize_input, find_best_match

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

def get_bot_response(user_input: str, knowledge_base: dict) -> str:
    """
    Generates the bot's response based on knowledge base and input.
    """
    normalized_input, _ = normalize_input(user_input)
    best_match = find_best_match(normalized_input, [q["question"] for q in knowledge_base["questions"]])

    if best_match:
        return next(q["answer"] for q in knowledge_base["questions"] if q["question"] == best_match)
    else:
        return "I don't know the answer. Can you teach me?"
