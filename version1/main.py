import json
import tkinter as tk
from tkinter import scrolledtext
from difflib import get_close_matches
from textblob import TextBlob

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}
    except json.JSONDecodeError:
        return {"questions": []}

# Save the knowledge base to the JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Normalize the user input by capitalizing the first letter
def normalize_input(user_input: str) -> str:
    return user_input.strip().capitalize()

# Sentiment analysis using TextBlob
def get_sentiment(text: str) -> tuple:
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Find the closest matching question
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Check if user input is a greeting
def is_greeting(user_input: str) -> bool:
    return any(greeting in user_input.lower() for greeting in ['hello', 'hi', 'hey'])

# Function to process user input and update the chat
def process_input():
    user_input = entry.get()  # Get user input from the entry widget
    if not user_input:
        return

    # Check for quit or exit command
    if user_input.lower() in ['quit', 'exit']:
        conversation.insert(tk.END, "Bot: Goodbye! Take care. 😊\n")
        entry.delete(0, tk.END)  # Clear the entry widget
        return

    conversation.insert(tk.END, "You: " + user_input + "\n")
    
    # Normalize the input and run sentiment analysis
    normalized_input = normalize_input(user_input)
    polarity, subjectivity = get_sentiment(normalized_input)

    # Sentiment-based response
    if polarity > 0.2:
        sentiment_response = "I'm glad you're feeling positive! 😊 How can I assist you further?"
    elif polarity < -0.2:
        sentiment_response = "I'm sorry you're feeling down. 😔 It's important to talk about how you feel. Can I help you with anything specific?"
    else:
        sentiment_response = "It sounds like you're feeling neutral. If you want to talk more, I'm here to listen."
    
    # Check for greeting
    if is_greeting(user_input):
        bot_response = "Hello! 😊 How can I assist you today?"
    else:
        # Load knowledge base and find a match
        knowledge_base = load_knowledge_base('knowledge_base.json')
        best_match = find_best_match(normalized_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = next(q["answer"] for q in knowledge_base["questions"] if q["question"] == best_match)
            bot_response = answer
        else:
            bot_response = "I don't know the answer. Can you teach me?"
            new_answer = input("Type the answer or 'skip' to skip: ")
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": normalized_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                bot_response = "Thank you! I've learned something new. 😊"
    
    # Display bot's response
    conversation.insert(tk.END, "Bot: " + bot_response + "\n")
    entry.delete(0, tk.END)  # Clear the entry widget

# Create main window for the GUI
root = tk.Tk()
root.title("Chatbot")

# Create a scrolled text widget for the conversation
conversation = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
conversation.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
conversation.insert(tk.END, "Bot: Hello! 😊 I'm your chatbot. Ask me anything or type 'quit' to exit.\n")

# Create an entry widget for user input
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send the user's input
send_button = tk.Button(root, text="Send", width=20, font=("Arial", 12), command=process_input)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
