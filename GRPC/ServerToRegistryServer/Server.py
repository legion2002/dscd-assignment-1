from __future__ import print_function

import sys
sys.path.insert(1, '../proto')

import ServerToRegistryServer_pb2_grpc
import ServerToRegistryServer_pb2
import Article_pb2


import grpc
from concurrent import futures
import logging

def registerServer(stub, request):
    status = stub.Register(request)
    print(status)


def run():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = ServerToRegistryServer_pb2_grpc.ServerToRegistryServerStub(channel)
        print("-------------- Register Server --------------")
        request = ServerToRegistryServer_pb2.RegisterRequest(name="Server1", address=Article_pb2.Address(IP="localhost", port=123))
        registerServer(stub, request)
        request = ServerToRegistryServer_pb2.RegisterRequest(name="Server2", address=Article_pb2.Address(IP="localhost", port=124))
        registerServer(stub, request)
        request = ServerToRegistryServer_pb2.RegisterRequest(name="Server3", address=Article_pb2.Address(IP="localhost", port=125))
        registerServer(stub, request)
        


if __name__ == '__main__':
    logging.basicConfig()
    run()