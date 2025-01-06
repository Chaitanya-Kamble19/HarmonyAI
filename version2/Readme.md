# Chatbot with Modular Design (Version 2)

## Overview
This is the second version of  the chatbot application built using Python. The chatbot now features a modular design, making the codebase more organized and maintainable. The chatbot still includes sentiment analysis, tokenization, and a learning capability and uses a JSON file as its knowledge base.

## Key Changes from Version 1
- **Modular Design**: The code has been split into multiple modules:
  - `main.py`: Entry point for the application.
  - `gui.py`: Handles GUI creation and user interaction.
  - `input_processing.py`: Processes user input, including sentiment analysis and tokenization.
  - `bot_responses.py`: Generates chatbot responses and handles learning logic.
  - `file_handling.py`: Manages loading and saving the knowledge base.
- **Improved Readability**: Each module focuses on a single responsibility, following the single-responsibility principle.
- **Reusability**: Functions are now reusable across different parts of the application.
- **Simpler Main File**: The `main.py` script only initializes and runs the GUI, improving clarity.

## Features
- **Sentiment Analysis**: Understands user sentiment using TextBlob.
- **Tokenization**: Tokenizes user input using spaCy, difflib, and TextBlob to enhance language understanding.
- **Learning Capability**: Learns new responses from the user.
- **Knowledge Base**: Stores questions and answers in a JSON file.
- **Modular Structure**: Code is split into separate files for better maintainability.

## How It Works
1. **GUI**: The graphical user interface is created using the `create_chat_window` function in `gui.py`.
2. **Input Processing**: User input is processed in `input_processing.py`, which normalizes input, analyzes sentiment, and tokenizes the text using spaCy, difflib, and TextBlob.
3. **Response Generation**: Bot responses are generated in `bot_responses.py` based on the knowledge base. Unknown questions trigger a learning prompt.
4. **Knowledge Base Management**: Knowledge base operations (loading and saving) are handled in `file_handling.py`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Chaitanya-Kk/HarmonyAI
   ```
2. Navigate to the project directory:
   ```bash
   cd //path to your file
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure you have Tkinter installed (comes pre-installed with Python on most systems).
5. Ensure you have a `knowledge_base.json` file in the project directory.

## Usage
Run the chatbot:
```bash
python main.py
```
Use the GUI to interact with the chatbot. If the chatbot doesn't know an answer, provide one directly.

## Project Structure
```bash
chatbot-modular/
├── bot_responses.py       # Handles bot response logic
├── file_handling.py       # Manages the knowledge base
├── gui.py                 # Creates and manages the GUI
├── input_processing.py    # Handles user input, sentiment analysis, and tokenization
├── main.py                # Main script for running the chatbot
├── knowledge_base.json    # JSON file for storing questions and answers
├── requirements.txt       # List of required dependencies
└── README.md              # Project documentation
```

## Dependencies
Install dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Example Interaction
```text
Bot: Hello! 😊 I'm your chatbot. Ask me anything or type 'quit' to exit.
You: Hello
Bot: Hello! 😊 How can I assist you today?
You: What is Python?
Bot: I don't know the answer. Can you teach me?
(Type the answer or 'skip' to skip: Python is a programming language.)
Bot: Thank you! I've learned something new. 😊
```

## Future Enhancements
- Implement user authentication for personalized interactions.
- Add a logging system for debugging and tracking chatbot learning.

## Contributing
Feel free to fork the repository, improve the code, and submit pull requests.

## Contact
For any questions or feedback, please reach out to [chaitanya19kamble@gmail.com](mailto:chaitanya19kamble@gmail.com).
