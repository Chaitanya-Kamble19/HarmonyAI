import tkinter as tk
from tkinter import scrolledtext
from input_processing import normalize_input, get_sentiment, is_greeting, tokenize_input
from bot_responses import get_sentiment_response, get_bot_response
from file_handling import load_knowledge_base

def create_chat_window():
    """
    Sets up the chatbot GUI with improved appearance.
    """
    root = tk.Tk()
    root.title("Mental Health Chatbot")

    # Chat display area
    conversation = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD,
        width=60,
        height=25,
        font=("Arial", 12),
        bg="#f5f5f5",  # Light background for better readability
        fg="#000000",  # Black text for contrast
        state=tk.DISABLED,
        padx=10,
        pady=10,
        borderwidth=3,
        relief="groove",
    )
    conversation.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    conversation.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
    conversation.tag_configure("bot", foreground="green", font=("Arial", 12))
    conversation.tag_configure("tokens", foreground="#800080", font=("Arial", 10, "italic"))

    # Entry field
    entry = tk.Entry(root, width=50, font=("Arial", 14), borderwidth=2, relief="solid")
    entry.grid(row=1, column=0, padx=10, pady=10)

    # Send button
    send_button = tk.Button(
        root,
        text="Send",
        width=15,
        font=("Arial", 12),
        bg="#0078d7",  # Blue background for the button
        fg="white",  # White text
        relief="raised",
        command=lambda: process_input(entry, conversation),
    )
    send_button.grid(row=1, column=1, padx=10, pady=10)

    # Initial bot message
    add_message(conversation, "Bot", "Hello! 😊 I'm your chatbot. Ask me anything or type 'quit' to exit.")

    return root, conversation, entry


def add_message(conversation, sender, message, tag=None):
    """
    Adds a styled message to the conversation area.
    """
    conversation.config(state=tk.NORMAL)
    conversation.insert(tk.END, f"{sender}: {message}\n", tag if tag else sender.lower())
    conversation.config(state=tk.DISABLED)
    conversation.see(tk.END)


def process_input(entry, conversation):
    """
    Processes user input, updates the chat, and generates a bot response.
    """
    user_input = entry.get().strip()
    if not user_input:
        return

    # Display user message
    add_message(conversation, "You", user_input, "user")

    # Clear the input field
    entry.delete(0, tk.END)

    # Normalize and tokenize input
    normalized_input, tokens = normalize_input(user_input)
    add_message(conversation, "Bot", f"Tokens: {tokens}", "tokens")  # Optional debugging info

    # Sentiment analysis
    polarity, _ = get_sentiment(normalized_input)

    # Load knowledge base and generate bot response
    knowledge_base = load_knowledge_base('knowledge_base.json')
    if is_greeting(user_input):
        bot_response = "Hello! 😊 How can I assist you today?"
    else:
        bot_response = get_bot_response(user_input, knowledge_base)

    # Display bot response
    add_message(conversation, "Bot", bot_response, "bot")


# Main application
if __name__ == "__main__":
    root, conversation, entry = create_chat_window()
    root.mainloop()
