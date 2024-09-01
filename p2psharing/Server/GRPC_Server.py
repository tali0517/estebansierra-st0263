# servidor/grpc_server.py
from concurrent import futures
import grpc
import os
import shared.grpc_service_pb2 as pb2
import shared.grpc_service_pb2_grpc as pb2_grpc
from config import load_config

class FileService(pb2_grpc.FileServiceServicer):
    def __init__(self, shared_directory):
        self.shared_directory = shared_directory

    def ListFiles(self, request, context):
        files = os.listdir(self.shared_directory)
        return pb2.FileList(files=files)

    def EchoService(self, request, context):
        return pb2.EchoResponse(message=f"ECO: {request.message}")

def serve():
    config = load_config()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_FileServiceServicer_to_server(FileService(config['shared_directory']), server)
    server.add_insecure_port(f"[::]:{config['port']}")
    server.start()
    print(f"Servidor gRPC escuchando en el puerto {config['port']}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
