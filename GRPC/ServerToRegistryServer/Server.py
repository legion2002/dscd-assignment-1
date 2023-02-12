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
        register = False
        while not register:
            print("Register Server!")
            print("Enter Server name : ")
            name = input()
            print("Enter Server addres : ")
            print("Enter IP : ")
            IP = input()
            print("Enter port number : ")
            port = int(input())
            request = ServerToRegistryServer_pb2.RegisterRequest(name=name, address=Article_pb2.Address(IP=IP, port=port))
            registerServer(stub, request)
            print("Do you want to register a server? (y/n)")
            choice = input()
            if choice == 'n':
                register = True
        
        


if __name__ == '__main__':
    logging.basicConfig()
    run()