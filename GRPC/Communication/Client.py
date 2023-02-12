from __future__ import print_function

import sys
sys.path.insert(1, '../proto_files')

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2
import Article_pb2

import grpc
from concurrent import futures
import logging

def getListOfServers(stub, request):
    status = stub.GetServerList(request)
    for x in status:
        print(x.name + " - " + x.address.IP + ":" + str(x.address.port))

def run(arg):
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = CommWithRegistryServer_pb2_grpc.CommWithRegistryServerStub(channel)
        request = CommWithRegistryServer_pb2.GetServerListRequest(name=arg[0], address=Article_pb2.Address(IP=arg[1], port=int(arg[2])))
        getListOfServers(stub, request)


if __name__ == '__main__':
    arg = sys.argv[1:]
    logging.basicConfig()
    run(arg)