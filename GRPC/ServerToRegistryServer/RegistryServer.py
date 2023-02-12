import sys
sys.path.insert(1, '../proto')

from GRPC.proto import ServerToRegistryServer_pb2_grpc
from GRPC.proto import ServerToRegistryServer_pb2

import grpc
from concurrent import futures
import logging
import math
import time

MAX_SERVER = 10
Servers = {}

def addServers(name, IP, port):
    if len(Servers) < MAX_SERVER:
        Servers[name] = [IP, port]
        return 0
    else:
        return 1

class ServerToRegistryServerServicer(ServerToRegistryServer_pb2_grpc.ServerToRegistryServerServicer):
    def Register(self, request, context):
        result = addServers(request.name, request.address.IP, request.address.port)
        if result == 0:
            return ServerToRegistryServer_pb2.RegisterResponse(status=0)
        else:
            return ServerToRegistryServer_pb2.RegisterResponse(status=1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ServerToRegistryServer_pb2_grpc.add_ServerToRegistryServerServicer_to_server(ServerToRegistryServerServicer(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
