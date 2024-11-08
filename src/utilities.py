import json

def load_settings(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Settings file {filepath} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filepath}.")
        return {}
