from __future__ import print_function

import sys
sys.path.insert(1, '../proto_files')

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2
import Article_pb2
import CommWithServer_pb2_grpc
import CommWithServer_pb2
from google.protobuf.timestamp_pb2 import Timestamp
import grpc
from concurrent import futures
import logging

MAX_CLIENTS = 2
CLIENTELE = {}
ARTICLES = []

def addClient(uuid, name, IP, port):
    if name in CLIENTELE.keys():
        return 1

    for server in CLIENTELE.keys():
        addr = CLIENTELE[server][0]+str(CLIENTELE[server][1])
        check_addr = IP+str(port)
        if addr == check_addr:
            return 1
        if CLIENTELE[server][2] == uuid:
            return 1

    if len(CLIENTELE) < MAX_CLIENTS:
        CLIENTELE[name] = [IP, port, uuid]
        return 0
    else:
        return 1


def removeClient(uuid):
    for client in CLIENTELE.keys():
        if CLIENTELE[client][2] == uuid:
            del CLIENTELE[client]
            return 0
    
    return 1


def registerServer(stub, request):
    status = stub.Register(request)
    print(status)
    return status


class CommWithServerServicer(CommWithServer_pb2_grpc.CommWithServerServicer):
    def JoinServer(self, request, context):
        print("JOIN REQUEST FROM " + request.uuid)
        result = addClient(request.uuid, request.name, request.address.IP, request.address.port)
        if result == 0:
            return CommWithServer_pb2.JoinServerResponse(status="SUCCESS")
        else:
            return CommWithServer_pb2.JoinServerResponse(status="FAIL")

    def LeaveServer(self, request, context):
        print("LEAVE REQUEST FROM " + request.uuid)
        result = removeClient(request.uuid)
        if result == 0:
            return CommWithServer_pb2.JoinServerResponse(status="SUCCESS")
        else:
            return CommWithServer_pb2.JoinServerResponse(status="FAIL")

    def PublishArticles(self, request, context):
        for client in CLIENTELE.keys():
            if CLIENTELE[client][2] == request.uuid:
                print("ARTICLE PUBLISH FROM " + request.uuid)
                timestamp = Timestamp().GetCurrentTime()
                ARTICLES.append(Article_pb2.ArticleFormat(type=request.article.type, author=request.article.author, time_rec=timestamp, content=request.article.content))
                return CommWithServer_pb2.JoinServerResponse(status="SUCCESS")

        return CommWithServer_pb2.JoinServerResponse(status="FAIL")

def connectToRegistry(arg):
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = CommWithRegistryServer_pb2_grpc.CommWithRegistryServerStub(channel)
        request = CommWithRegistryServer_pb2.RegisterRequest(name=arg[0], address=Article_pb2.Address(IP=arg[1], port=int(arg[2])))
        status = registerServer(stub, request)


def connectToClient(arg):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CommWithServer_pb2_grpc.add_CommWithServerServicer_to_server(CommWithServerServicer(), server)
    server.add_insecure_port('[::]:' + str(arg[2]))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    arg = sys.argv[1:]
    logging.basicConfig()
    connectToRegistry(arg)
    connectToClient(arg)