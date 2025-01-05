# HarmonyAI - Mental Health Chatbot with Sentiment Analysis

HarmonyAI is an AI-powered Mental Health Chatbot designed to support and guide individuals seeking emotional and psychological well-being. The bot engages in meaningful conversations, performs sentiment analysis on user inputs, and learns from user interactions to improve its responses over time.

## Features

- **Interactive Chat:** Engage in a conversation with the chatbot using a text-based interface.
- **Sentiment Analysis:** Analyzes user input to detect sentiment (positive, negative, neutral) using TextBlob for more empathetic responses.
- **Knowledge Base Management:** Dynamically loads, updates, and saves responses to user queries using a JSON-based knowledge base.
- **Learning Capability:** The bot can learn new questions and answers based on user feedback.
- **GUI Integration:** Tkinter-based graphical user interface for a more accessible interaction experience.

## Installation

### Clone this repository

```bash
git clone https://github.com/Chaitanya-Kamble19/HarmonyAI.git
cd HarmonyAI
```

### Install the Required Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the chatbot in one of the two modes:

### Console Mode

```bash
python chatbot.py
```

### GUI Mode

```bash
python gui_chatbot.py
```

## How to Use

- Start a conversation by typing a question or sharing how you feel.
- If the bot doesn't know the answer, it will ask for user feedback to learn new responses.
- To exit, type `quit` in console mode or close the GUI window.

## Sentiment Analysis

The chatbot utilizes TextBlob to analyze the sentiment of user inputs. It classifies input into positive, negative, or neutral sentiment, allowing the bot to respond empathetically and adapt based on the user's mood.

## Knowledge Base

The chatbot’s knowledge base is stored in `knowledge_base.json`. Below is an example structure of the knowledge base:

```json
{
  "questions": [
    {
      "question": "What is mental health?",
      "answer": "Mental health refers to emotional, psychological, and social well-being..."
    },
    {
      "question": "How do I manage stress?",
      "answer": "Take deep breaths, exercise, and talk to someone about your feelings..."
    }
  ]
}
```

## Future Improvements

- Integrate advanced NLP models such as OpenAI's GPT for more dynamic and intelligent conversations.
- Add a web-based interface to make the chatbot accessible via the browser.
- Enable multilingual capabilities to serve a global audience.

## Contributing

Feel free to fork this repository, add new features, or submit issues/pull requests. All feedback is welcome!
