# config.py
import json

def load_config(filename='config.json'):
    """Carga la configuración desde un archivo JSON"""
    with open(filename, 'r') as file:
        return json.load(file)
