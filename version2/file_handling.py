import json

def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}
    except json.JSONDecodeError:
        return {"questions": []}

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
