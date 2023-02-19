import sys
sys.path.insert(1, '../proto')

from google.protobuf.timestamp_pb2 import Timestamp

import Message_pb2
import time
import zmq
import datetime
import threading

MAX_CLIENTS = 4
SERVERS = {}
CLIENTELE = {}
ARTICLES = []

context_client = zmq.Context()
socket_client = context_client.socket(zmq.REQ)



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


def JoinServer(request):
        print("JOIN REQUEST FROM " + request.uuid)
        result = addClient(request.uuid, request.name, request.address.IP, request.address.port)
        if result == 0:
            return Message_pb2.JoinServerResponse(status="SUCCESS")
        else:
            return Message_pb2.JoinServerResponse(status="FAIL")


def LeaveServer(request):
    print("LEAVE REQUEST FROM " + request.uuid)
    result = removeClient(request.uuid)
    if result == 0:
        return Message_pb2.JoinServerResponse(status="SUCCESS")
    else:
        return Message_pb2.JoinServerResponse(status="FAIL")


def PublishArticle(request):
    for client in CLIENTELE.keys():
        if CLIENTELE[client][2] == request.uuid:
            print("ARTICLE PUBLISH FROM " + request.uuid)
            ct = datetime.datetime.now()
            timestamp = ct.timestamp()
            time = Timestamp(seconds=int(timestamp))
            ARTICLES.append(Message_pb2.ArticleFormat(type=request.article.type, author=request.article.author, time_rec=time, content=request.article.content))
            return Message_pb2.PublishArticlesResponse(status="SUCCESS")

    return Message_pb2.PublishArticlesResponse(status="FAIL")

def askServerForArticles(server):
    socket_client.connect("tcp://localhost:" + SERVERS[server][1])
    socket_client.send(Message_pb2.StandardFormat(typeOfRequest="getAllArticles").SerializeToString())
    message = socket_client.recv()
    response = Message_pb2.GetArticlesResponse()
    response.ParseFromString(message)
    return response.article

def GetAllArticles():
    articlesRequested = []
    for articles in ARTICLES:
        articlesRequested.append(articles)
    response = Message_pb2.GetArticlesResponse()
    response.article.extend(articlesRequested)
    return response


def GetArticles(request, arg):
    articlesRequested = []
    for server in SERVERS.keys():
        socket_client.connect("tcp://localhost:" + SERVERS[server][1])
        requestedArticle = Message_pb2.ArticleRequest(type=request.article.type, author=request.article.author, time_rec=request.article.time_rec)
        req = Message_pb2.GetArticlesRequest(uuid = arg[0], article=requestedArticle)
        socket_client.send(Message_pb2.StandardFormat(typeOfRequest="getArticle", getArticles=req).SerializeToString())
        message = socket_client.recv()
        response = Message_pb2.GetArticlesResponse()
        response.ParseFromString(message)
        for article in response.article:
            if article not in ARTICLES:
                ARTICLES.append(article)

    for client in CLIENTELE.keys():
        if CLIENTELE[client][2] == request.uuid or client == request.uuid:
            print("ARTICLE REQUEST FROM " + request.uuid)
            for articles in ARTICLES:
                timestamp = articles.time_rec
                if(request.article.time_rec.seconds <= timestamp.seconds):
                    # Comparing author
                    if(request.article.author != "" and request.article.author == articles.author):
                        if(request.article.type == articles.type):
                            articlesRequested.append(articles)
                        elif(request.article.type == 3):
                            articlesRequested.append(articles)
                    # Comparing type becaiuse author was empty
                    else:
                        if(request.article.author == "" and request.article.type == articles.type):
                            articlesRequested.append(articles)

    
    response = Message_pb2.GetArticlesResponse()
    response.article.extend(articlesRequested)
    return response

def JoinServerToServer(request):
    print("JOIN REQUEST FROM SERVER: " + request.serverDetails.name + " " + request.serverDetails.address.IP+":"+str(request.serverDetails.address.port))
    CLIENTELE[request.serverDetails.name] = [request.serverDetails.address.IP, request.serverDetails.address.port, "UUID"]
    return Message_pb2.JoinServerResponse(status="SUCCESS")


def connectToRegistry(arg):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    request = Message_pb2.RegisterRequest(typeOfRequest = "register", name=arg[0], address=Message_pb2.Address(IP=arg[1], port=int(arg[2])))
    serialized_msg = request.SerializeToString()
    socket.send(serialized_msg)
    message = socket.recv()
    status = Message_pb2.RegisterResponse()
    status.ParseFromString(message)
    print(status)
    if "SUCCESS" in status.status:
        return 0


def connectToClient(arg):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:" + str(arg[2]))
    while True:
        message = socket.recv()
        request = Message_pb2.StandardFormat()
        request.ParseFromString(message)

        if(request.typeOfRequest == "joinServer"):
            result = JoinServer(request.join).SerializeToString()
        elif(request.typeOfRequest == "leaveServer"):
            result = LeaveServer(request.leave).SerializeToString()
        elif(request.typeOfRequest == "getArticle"):
            result = GetArticles(request.getArticles, arg).SerializeToString()
        elif(request.typeOfRequest == "publishArticle"):
            result = PublishArticle(request.publish).SerializeToString()
        elif(request.typeOfRequest == "articlesForServer"):
            result = JoinServerToServer(request.articlesServer).SerializeToString()
        elif(request.typeOfRequest == "getAllArticles"):
            result = GetAllArticles().SerializeToString()
        socket.send(result)

def createIntermediate(arg):
        
    print("Do you wish to join a server? (y/n)")
    inp = input()
    while(True):
        if inp.lower() == "y":
            print("Enter Server Information")
            info = input()
            list_string = info.split(' ')
            server = ["", "", ""]
            server[0] = list_string[0]
            server[1], server[2] = list_string[1].split(":")
            server[2] = int(server[2])
            if server[0] == arg[0]:
                print("Can not join same server")
                print("Do you wish to join a server? (y/n)")
                inp = input()
                continue

            socket_client.connect("tcp://localhost:" + str(server[2]))
            request = Message_pb2.GetArticlesForServer(serverDetails=Message_pb2.ServerAddress(name=arg[0], address=Message_pb2.Address(IP=arg[1], port=int(arg[2]))))
            data = Message_pb2.StandardFormat(typeOfRequest="articlesForServer", articlesServer=request)
            serialized_msg = data.SerializeToString()
            socket_client.send(serialized_msg)
            message = socket_client.recv()
            response = Message_pb2.JoinServerResponse()
            response.ParseFromString(message)
            print(response)
            if "SUCCESS" in response.status:
                SERVERS[server[0]] = [server[1], str(server[2])]
            
        
        print("Do you wish to join a server? (y/n)")
        inp = input()


if __name__ == '__main__':
    arg = sys.argv[1:]
    status = connectToRegistry(arg)
    if status == 0:
        thread1 = threading.Thread(target=connectToClient, args=(arg, ))
        thread2 = threading.Thread(target=createIntermediate, args=(arg, ))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        
        