import sys
sys.path.insert(1, '../proto_files')

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2
import Article_pb2

import grpc
from concurrent import futures
import logging

MAX_SERVER = 2
Servers = {}

def addServers(name, IP, port):

    if name in Servers.keys():
        return 1

    for server in Servers.keys():
        addr = Servers[server][0]+str(Servers[server][1])
        check_addr = IP+str(port)
        if addr == check_addr:
            return 1

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

    def GetServerList(self, request, context):
        print("SERVER LIST REQUEST FROM " + request.address.IP + ":" + str(request.address.port))
        for server in Servers.keys():
            IP = Servers[server][0]
            port = Servers[server][1]
            yield CommWithRegistryServer_pb2.GetServerListResponse(name=server, address= Article_pb2.Address(IP=IP, port=port))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CommWithRegistryServer_pb2_grpc.add_CommWithRegistryServerServicer_to_server(CommWithRegistryServerServicer(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
