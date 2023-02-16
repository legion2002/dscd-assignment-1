from __future__ import print_function

import sys
sys.path.insert(1, '../proto_files')

from concurrent import futures
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

import CommWithRegistryServer_pb2_grpc
import CommWithRegistryServer_pb2
import CommWithServer_pb2_grpc
import CommWithServer_pb2
import Article_pb2
import grpc
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
    address = server[1] + ":" + str(server[2])
    with grpc.insecure_channel(address) as channel:
        stub = CommWithServer_pb2_grpc.CommWithServerStub(channel)
        request = CommWithServer_pb2.LeaveServerRequest(uuid = unique_id)
        status = stub.LeaveServer(request)
        print(status)


def getArticles(client, server):
    print("Enter Details for Articles to fetch")
    info = ["", "", ""]
    print("Type of Article")
    info[0] = input()
    print("Author of Article")
    info[1] = input()
    print("Timestamp of Article (yy-mm-dd)")
    info[2] = input()
    if info.count("") > 1:
        print("Illegal Format.")
    else:
        typeRequest = 0
        if info[0].lower() == "fashion":
            typeRequest = 0
        elif info[0].lower() == "sports":
            typeRequest = 1
        elif info[0].lower() == "politics":
            typeRequest = 2
        else:
            typeRequest = 3

        info[2] = info[2]+" 00:00:00"
        date_time = datetime.strptime(info[2], '%y-%m-%d %H:%M:%S')
        timestamp = date_time.timestamp()
        time = Timestamp(seconds=int(timestamp))

        address = server[1] + ":" + str(server[2])
        with grpc.insecure_channel(address) as channel:
            stub = CommWithServer_pb2_grpc.CommWithServerStub(channel)
            requestedArticle = Article_pb2.ArticleRequest(type=typeRequest, author=info[1], time_rec=time)
            request = CommWithServer_pb2.GetArticlesRequest(uuid = unique_id, article=requestedArticle)
            status = stub.GetArticles(request)
            
            cnt =1
            for y in status:
                x = y.article
                if x.type == 0:
                    type = "FASHION"
                elif x.type == 1:
                    type = "SPORTS"
                elif x.type  == 2:
                    type = "POLITICS"

                date = datetime.fromtimestamp(x.time_rec.seconds)

                print(str(cnt) + ") " + "\n" + type + "\n" + x.author + "\n" + str(date) + "\n" +  x.content)
                cnt+=1


def publishArticles(client, server):
    print("Enter Details for Publishing Article")
    print("Type of Article")
    typeForArticle = input()
    print("Author of Article")
    author = input()
    print("Content of Article")
    content = input()
    if len(content) > 200:
        print("Can not publish. Content greater than 200 in size")
    else:
        address = server[1] + ":" + str(server[2])
        with grpc.insecure_channel(address) as channel:
            stub = CommWithServer_pb2_grpc.CommWithServerStub(channel)
            typeRequest = -1
            if typeForArticle.lower() == "fashion":
                typeRequest = 0
            elif typeForArticle.lower() == "sports":
                typeRequest = 1
            elif typeForArticle.lower() == "politics":
                typeRequest = 2

            if typeRequest != -1:
                requestedArticle = Article_pb2.ArticleFormat(type=typeRequest, author=author, content=content)
                request = CommWithServer_pb2.PublishArticlesRequest(uuid = unique_id, article=requestedArticle)
                status = stub.PublishArticles(request)
                print(status)
            else:
               print("Can not publish. Wrong Type") 


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
