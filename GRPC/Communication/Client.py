from __future__ import print_function

import sys
sys.path.insert(1, '../proto_files')

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2
import CommWithServer_pb2_grpc
import CommWithServer_pb2
import Article_pb2

import grpc
from concurrent import futures
import logging
import uuid

unique_id = str(uuid.uuid1())


def getListOfServers(stub, request):
    status = stub.GetServerList(request)
    for x in status:
        print(x.name + " - " + x.address.IP + ":" + str(x.address.port))


def runRegistryServer(arg):
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = CommWithRegistryServer_pb2_grpc.CommWithRegistryServerStub(channel)
        request = CommWithRegistryServer_pb2.GetServerListRequest(name=arg[0], address=Article_pb2.Address(IP=arg[1], port=int(arg[2])))
        getListOfServers(stub, request)


def joinServer(client, server):
    address = server[1] + ":" + str(server[2])
    with grpc.insecure_channel(address) as channel:
        stub = CommWithServer_pb2_grpc.CommWithServerStub(channel)
        request = CommWithServer_pb2.JoinServerRequest(uuid = unique_id, name=client[0], address=Article_pb2.Address(IP=client[1], port=int(client[2])))
        status = stub.JoinServer(request)
        print(status)



def leaveServer(client, server):
    pass


def getArticles(client, server):
    pass


def publishArticles(client, server):
    pass


def runServer(client, choice):
    print("Enter Server Information")
    info = input()
    list_string = info.split(' ')
    server = ["", "", ""]
    server[0] = list_string[0]
    server[1], server[2] = list_string[1].split(":")
    server[2] = int(server[2])
    if choice == 2:
        joinServer(client, server)
    elif choice == 3:
        leaveServer(client, server)
    elif choice == 4:
        getArticles(client, server)
    elif choice == 5:
        publishArticles(client, server)


if __name__ == '__main__':
    arg = sys.argv[1:]
    logging.basicConfig()
    print("Choose Option: \n1. Get List of Server \n2. Join to Server \n3. Leave Server \n4. Get Articles \n5. Publish Article \n6. Exit")
    inp = int(input())
    while(inp != 6):
        if inp == 1:
            runRegistryServer(arg)
        elif inp == 6:
            break
        else:
            runServer(arg, inp)
        print("Choose Option: \n1. Get List of Server \n2. Join to Server \n3. Leave Server \n4. Get Articles \n5. Publish Article \n6. Exit")
        inp = int(input())