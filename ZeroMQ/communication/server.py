import sys
sys.path.insert(1, '../proto')

from google.protobuf.timestamp_pb2 import Timestamp

import Message_pb2
import time
import zmq
import datetime

MAX_CLIENTS = 4
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

def GetArticles(request):
    articlesRequested = []
    for client in CLIENTELE.keys():
        if CLIENTELE[client][2] == request.uuid:
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
        joinServerRequest = Message_pb2.JoinServerRequest()
        leaveServerRequest = Message_pb2.LeaveServerRequest()
        getArticlesRequest = Message_pb2.GetArticlesRequest()
        publishArticlesRequest = Message_pb2.PublishArticlesRequest()

        joinServerRequest.ParseFromString(message)
        leaveServerRequest.ParseFromString(message)
        getArticlesRequest.ParseFromString(message)
        publishArticlesRequest.ParseFromString(message)

        if(joinServerRequest.typeOfRequest == "joinServer"):
            result = JoinServer(joinServerRequest)
            time.sleep(1)
            result = result.SerializeToString()
            socket.send(result)
        elif(leaveServerRequest.typeOfRequest == "leaveServer"):
            result = LeaveServer(leaveServerRequest)
            time.sleep(1)
            result = result.SerializeToString()
            socket.send(result)
        elif(getArticlesRequest.typeOfRequest == "getArticle"):
            result = GetArticles(getArticlesRequest)
            time.sleep(1)
            result = result.SerializeToString()
            socket.send(result)
        elif(publishArticlesRequest.typeOfRequest == "publishArticle"):
            result = PublishArticle(publishArticlesRequest)
            time.sleep(1)
            result = result.SerializeToString()
            socket.send(result)


if __name__ == '__main__':
    arg = sys.argv[1:]
    status = connectToRegistry(arg)
    if status == 0:
        connectToClient(arg)
        