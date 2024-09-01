# server/server.py
from flask import Flask, jsonify, request
import os
from config import load_config

app = Flask(__name__)
config = load_config()

@app.route('/list_files', methods=['GET'])
def list_files():
    files = os.listdir(config['shared_directory'])
    return jsonify(files=files)

@app.route('/echo', methods=['POST'])
def echo_service():
    data = request.get_json()
    return jsonify(message=f"ECO: {data['message']}")

if __name__ == '__main__':
    app.run(host=config['ip'], port=config['port'])
