# Chatbot with Sentiment Analysis

## Overview
This project is a simple chatbot application built using Python. It incorporates sentiment analysis to better understand user input and provides responses accordingly. The chatbot can also learn new responses from the user and save them in a knowledge base.

## Features
- **Graphical User Interface (GUI)**: Created using Tkinter.
- **Sentiment Analysis**: Analyzes user input using TextBlob to determine sentiment polarity and subjectivity.
- **Learning Capability**: If the chatbot doesn't know an answer, it can learn from the user.
- **Knowledge Base**: Stores questions and answers in a JSON file for future interactions.
- **Customizable**: Easily extend the knowledge base by adding new questions and answers.

## How It Works
1. **User Input**: Users interact with the chatbot via a GUI.
2. **Sentiment Analysis**: User input is analyzed for sentiment.
3. **Response Generation**:
   - If the input matches a question in the knowledge base, the chatbot responds with the corresponding answer.
   - If no match is found, the chatbot prompts the user to teach it the correct answer.
4. **Knowledge Base Management**:
   - The knowledge base is stored in a `knowledge_base.json` file.
   - New questions and answers are saved to the file dynamically.

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
   pip install textblob
   ```
4. Ensure you have Tkinter installed (comes pre-installed with Python on most systems).
5. Download or create an empty `knowledge_base.json` file in the project directory:
   ```json
   {
       "questions": []
   }
   ```

## Usage
1. Run the chatbot application:
   ```bash
   python chatbot.py
   ```
2. Interact with the chatbot via the GUI:
   - Ask questions or say hello.
   - Type "quit" or "exit" to close the application.
3. Teach the chatbot:
   - If the chatbot doesn't know an answer, you can provide it directly in the console.

## Project Structure
```
chatbot-sentiment/
├── chatbot.py            # Main application script
├── knowledge_base.json   # JSON file for storing questions and answers
└── README.md             # Project documentation
```

## Dependencies
- **Python 3.7+**
- **Tkinter** (for GUI)
- **TextBlob** (for sentiment analysis)

Install TextBlob using pip:
```bash
pip install textblob
```

## Example Interaction
```
Bot: Hello! 😊 I'm your chatbot. Ask me anything or type 'quit' to exit.
You: Hello
Bot: Hello! 😊 How can I assist you today?
You: What is Python?
Bot: I don't know the answer. Can you teach me?
(Type the answer or 'skip' to skip: Python is a programming language.)
Bot: Thank you! I've learned something new. 😊
```

## Future Enhancements
- Add Tokenization.
- Integrate with external APIs for more dynamic responses.
- Improve GUI with additional features and customizations.

## Contributing
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## Acknowledgments
- [TextBlob](https://textblob.readthedocs.io/) for sentiment analysis.
- Python Tkinter for GUI development.

## Contact
For any questions or feedback, please reach out to chaitanya19kamble@gmail.com.
