# cliente/grpc_client.py
import grpc
import shared.grpc_service_pb2 as pb2
import shared.grpc_service_pb2_grpc as pb2_grpc
from config import load_config

def list_files():
    config = load_config()
    channel = grpc.insecure_channel(config['seed_peer_url'])
    stub = pb2_grpc.FileServiceStub(channel)
    response = stub.ListFiles(pb2.Empty())
    print(f"Archivos disponibles: {response.files}")

def send_echo(message):
    config = load_config()
    channel = grpc.insecure_channel(config['seed_peer_url'])
    stub = pb2_grpc.FileServiceStub(channel)
    response = stub.EchoService(pb2.EchoRequest(message=message))
    print(f"Respuesta ECO: {response.message}")

if __name__ == '__main__':
    list_files()
    send_echo("Prueba de mensaje ECO")
