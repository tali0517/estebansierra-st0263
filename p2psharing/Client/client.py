# client/client.py
import requests
from config import load_config

config = load_config()

def search_files():
    response = requests.get(f"{config['seed_peer_url']}/list_files")
    if response.status_code == 200:
        print("Archivos disponibles:", response.json())

def send_echo(message):
    response = requests.post(f"{config['seed_peer_url']}/echo", json={'message': message})
    if response.status_code == 200:
        print("Respuesta ECO:", response.json())

if __name__ == '__main__':
    search_files()
    send_echo("Mensaje de prueba")
