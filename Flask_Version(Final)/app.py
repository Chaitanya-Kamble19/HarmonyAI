from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from textblob import TextBlob
import spacy
import json
import os

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for session management

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load knowledge base
def load_knowledge_base(file_path='knowledge_base.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}

# Normalize input
def normalize_input(user_input):
    normalized = user_input.strip().capitalize()
    tokens = [token.text for token in nlp(normalized)]
    return normalized, tokens

# Sentiment analysis
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Check for greetings
def is_greeting(user_input):
    greetings = ['hello', 'hi', 'hey']
    return any(greeting in user_input.lower() for greeting in greetings)

# Find best match for questions
def find_best_match(user_question, questions):
    user_tokens = set([token.text.lower() for token in nlp(user_question)])
    question_matches = {}

    for question in questions:
        question_tokens = set([token.text.lower() for token in nlp(question)])
        overlap = user_tokens.intersection(question_tokens)
        if overlap:
            question_matches[question] = len(overlap) / len(question_tokens)

    return max(question_matches, key=question_matches.get, default=None)

# Get bot response
def get_bot_response(user_input, knowledge_base):
    normalized_input, _ = normalize_input(user_input)
    best_match = find_best_match(normalized_input, [q['question'] for q in knowledge_base['questions']])

    if best_match:
        return next(q['answer'] for q in knowledge_base['questions'] if q['question'] == best_match)
    else:
        return "I don't know the answer. Can you teach me?"

# Home route
@app.route('/')
def home():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('signin'))

# Sign-in & Sign-up (Integrated)
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action']
        users = load_users()

        if action == "signin":
            for user in users['users']:
                if user['username'] == username and user['password'] == password:
                    session['username'] = username
                    return redirect(url_for('home'))
            return render_template('signin.html', error="Invalid username or password.")

        elif action == "signup":
            for user in users['users']:
                if user['username'] == username:
                    return render_template('signin.html', error="Username already taken.")

            users['users'].append({"username": username, "password": password})
            save_users(users)

            session['username'] = username
            return redirect(url_for('home'))

    return render_template('signin.html')

# Guest access
@app.route('/guest')
def guest():
    session['username'] = 'Guest'
    return redirect(url_for('home'))

# Sign-out route
@app.route('/signout')
def signout():
    session.pop('username', None)
    return redirect(url_for('signin'))

# API for chat interaction
@app.route('/chat', methods=['POST'])
def chat():
    if 'username' not in session:
        return jsonify({"response": "Please sign in first."})

    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({"response": "Please enter a message."})

    knowledge_base = load_knowledge_base()

    if is_greeting(user_input):
        response = "Hello! 😊 How can I assist you today?"
    else:
        sentiment_polarity, _ = get_sentiment(user_input)
        response = get_bot_response(user_input, knowledge_base)

    return jsonify({"response": response})

# Utility functions for user management
def load_users(file_path='users.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

def save_users(users, file_path='users.json'):
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)