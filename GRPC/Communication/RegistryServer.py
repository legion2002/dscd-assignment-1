import sys
sys.path.insert(1, '../proto_files')

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2

import grpc
from concurrent import futures
import logging

MAX_SERVER = 10
Servers = {}

def addServers(name, IP, port):
    if len(Servers) < MAX_SERVER:
        Servers[name] = [IP, port]
        return 0
    else:
        return 1

class CommWithRegistryServerServicer(CommWithRegistryServer_pb2_grpc.CommWithRegistryServerServicer):
    def Register(self, request, context):
        print("JOIN REQUEST FROM " + request.address.IP + ":" + str(request.address.port))
        result = addServers(request.name, request.address.IP, request.address.port)
        if result == 0:
            return CommWithRegistryServer_pb2.RegisterResponse(status="SUCESS")
        else:
            return CommWithRegistryServer_pb2.RegisterResponse(status="FAIL")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CommWithRegistryServer_pb2_grpc.add_CommWithRegistryServerServicer_to_server(CommWithRegistryServerServicer(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
