import os
import logging
import google.generativeai as genai
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

# Set up the API key directly in the code
GOOGLE_API_KEY = "Enter_API_Key"  # Replace with your actual API key

# Configure Gemini AI with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# FastAPI application
app = FastAPI()

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        if websocket not in self.active_connections:
            self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, websocket: WebSocket):
        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(message)

manager = ConnectionManager()

# Gemini AI configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 150,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Client #{client_id}: {data}")
            response = process_message_with_gemini(data)
            await manager.send_personal_message(f"Bot: {response}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", websocket)
    except Exception as e:
        logger.exception("Unexpected error in WebSocket communication")

# Process user input with Gemini AI
def process_message_with_gemini(user_input: str) -> str:
    try:
        response = chat_session.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        logger.exception("Error processing message with Gemini AI")
        return "Sorry, I couldn't process that request."

# Run FastAPI with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
