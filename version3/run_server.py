import subprocess
import sys

def start_uvicorn():
    try:
        # Run the Uvicorn server as a subprocess
        print("Starting Uvicorn server...")
        command = ['uvicorn', 'server:app', '--reload', '--host', '0.0.0.0', '--port', '8000']
        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Uvicorn server started.")
    except Exception as e:
        print(f"Error starting the server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_uvicorn()
