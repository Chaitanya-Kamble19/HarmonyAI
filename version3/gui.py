import tkinter as tk
from tkinter import ttk
from input_processing_original import normalize_input, get_sentiment, is_greeting, tokenize_input
from bot_responses import get_bot_response
from file_handling import load_knowledge_base

# Function to send a message
def send_message():
    user_message = message_entry.get().strip()
    if not user_message:
        return

    # Add user message to chat
    add_message(user_message, sender="user")
    message_entry.delete(0, tk.END)

    # Normalize and tokenize input
    normalized_input, tokens = normalize_input(user_message)
    add_message(f"Tokens: {tokens}", sender="debug")  # Debugging info

    # Sentiment analysis
    polarity, _ = get_sentiment(normalized_input)

    # Load knowledge base and generate bot response
    knowledge_base = load_knowledge_base('knowledge_base.json')
    if is_greeting(user_message):
        bot_response = "Hello! 😊 How can I assist you today?"
    else:
        bot_response = get_bot_response(user_message, knowledge_base)

    # Add bot response to chat
    add_message(bot_response, sender="bot")

# Function to display messages in the chat area
def add_message(message, sender="user"):
    # Colors for different senders
    bubble_color = "#5CC8A6" if sender == "user" else ("#A2C2E8" if sender == "bot" else "#FFD700")
    align = "e" if sender == "user" else "w"
    padx = (10 if sender == "bot" else 0, 10 if sender == "user" else 0)

    # Create a label for the message bubble
    bubble = tk.Label(
        chat_frame_inner,
        text=message,
        wraplength=280,
        bg=bubble_color,
        fg="#333333",
        anchor="w",
        justify="left",
        padx=10,
        pady=5,
        font=("Arial", 12),
        bd=1,
        relief="solid",
    )

    # Align the message bubble: Right for user, Left for bot/debug
    bubble.pack(anchor=align, padx=padx, pady=5)

    # Update chat window and scroll to the latest message
    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1)

# Create the main window
root = tk.Tk()
root.title("Mental Health Chatbot")
root.geometry("400x600")
root.configure(bg="#F0F4F8")

# Top header
header_frame = tk.Frame(root, bg="#5CC8A6", height=50)
header_frame.pack(fill="x")
header_label = tk.Label(
    header_frame,
    text="Mental Health Chatbot",
    bg="#5CC8A6",
    fg="white",
    font=("Arial", 16, "bold"),
)
header_label.pack(pady=10)

# Chat display area
chat_frame = tk.Frame(root, bg="#F0F4F8", bd=0)
chat_frame.pack(fill="both", expand=True)

# Scrollable canvas for chat
chat_canvas = tk.Canvas(chat_frame, bg="#F0F4F8", highlightthickness=0)
chat_scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=chat_canvas.yview)
chat_canvas.configure(yscrollcommand=chat_scrollbar.set)

chat_canvas.pack(side="left", fill="both", expand=True)
chat_scrollbar.pack(side="right", fill="y")

chat_frame_inner = tk.Frame(chat_canvas, bg="#F0F4F8")
chat_canvas.create_window((0, 0), window=chat_frame_inner, anchor="nw")

# Allow scrolling
def on_frame_configure(event):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

chat_frame_inner.bind("<Configure>", on_frame_configure)

# Message input area
input_frame = tk.Frame(root, bg="#A2C2E8", bd=1, relief="sunken")
input_frame.pack(fill="x", side="bottom")

message_entry = tk.Entry(input_frame, font=("Arial", 14), bd=0, bg="#F0F4F8", fg="#333333")
message_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)
message_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#5CC8A6",
    fg="white",
    font=("Arial", 12),
)
send_button.pack(side="right", padx=10, pady=10)

# Initial bot message
add_message("Hello! 😊 I'm your chatbot. Ask me anything or type 'quit' to exit.", sender="bot")

# Run the application
root.mainloop()
