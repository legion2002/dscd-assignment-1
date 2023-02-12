from __future__ import print_function

import sys
sys.path.insert(1, '../proto_files')

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2
import Article_pb2

import grpc
from concurrent import futures
import logging

MAX_CLIENTS = 2
CLIENTELE = {}

def addClient(uuid, name, IP, port):

    if name in CLIENTELE.keys():
        return 1

    for server in CLIENTELE.keys():
        addr = CLIENTELE[server][0]+str(CLIENTELE[server][1])
        check_addr = IP+str(port)
        if addr == check_addr:
            return 1

    if len(CLIENTELE) < MAX_CLIENTS:
        CLIENTELE[name] = [IP, port]
        return 0
    else:
        return 1

def registerServer(stub, request):
    status = stub.Register(request)
    print(status)


def run(arg):
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = CommWithRegistryServer_pb2_grpc.CommWithRegistryServerStub(channel)
        request = CommWithRegistryServer_pb2.RegisterRequest(name=arg[0], address=Article_pb2.Address(IP=arg[1], port=int(arg[2])))
        registerServer(stub, request)


if __name__ == '__main__':
    arg = sys.argv[1:]
    logging.basicConfig()
    run(arg)