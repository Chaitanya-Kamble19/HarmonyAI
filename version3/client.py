import asyncio
import subprocess
import websockets

async def start_uvicorn():
    print("Starting Uvicorn server...")
    server_process = subprocess.Popen(
        ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    await asyncio.sleep(20)  # Increase the sleep time to 20 seconds to give the server more time
    print("Uvicorn server started.")
    return server_process

async def chat_with_bot():
    uri = "ws://localhost:8000/ws/1"
    try:
        print("Attempting to connect to the server...")
        async with websockets.connect(uri) as websocket:
            print("Connected to the chatbot server.")
            while True:
                message = input("You: ")
                if message.lower() == "quit":
                    print("Ending chat...")
                    break
                await websocket.send(message)
                response = await websocket.recv()
                print("Bot:", response)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Error: Connection closed unexpectedly - {e}")
    except asyncio.TimeoutError:
        print("Error: Connection attempt timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    server_process = await start_uvicorn()
    await chat_with_bot()
    print("Shutting down the server...")
    server_process.terminate()

if __name__ == "__main__":
    asyncio.run(main())
