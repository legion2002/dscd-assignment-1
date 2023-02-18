import sys
sys.path.insert(1, '../proto')

from google.protobuf.timestamp_pb2 import Timestamp

import Message_pb2
import time
import pika
import datetime
import uuid

MAX_CLIENTS = 4
CLIENTELE = {}
ARTICLES = []

returnFlag = 0
corr_id = 0
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

def registry_callback(ch, method, properties, body):
    status = Message_pb2.RegisterResponse()
    global corr_id
    if properties.correlation_id == corr_id:
        status.ParseFromString(body)
        print(status)
        if "SUCCESS" in status.status:
            global returnFlag
            returnFlag = 1

def connectToRegistry(arg):
    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue
    channel.basic_consume(queue=callback_queue, on_message_callback=registry_callback,
            auto_ack=True)

    _IP = arg[1]
    _port= int(arg[2])
    _routing_key = arg[2] + "_server_queue"

    request = Message_pb2.RegisterRequest(typeOfRequest = "register", name=arg[0], address=Message_pb2.Address(IP=_IP, port=_port, routing_key = _routing_key))
    serialized_msg = request.SerializeToString()

    global corr_id
    corr_id = str(uuid.uuid4())
    channel.basic_publish(
        exchange='',
        routing_key='registry_server_queue',
        properties=pika.BasicProperties(
            reply_to=callback_queue,
            correlation_id=corr_id,
        ),
        body=serialized_msg)
    connection.process_data_events(time_limit=None)
    return returnFlag

def client_callback(ch, method, properties, body):
    request = Message_pb2.StandardFormat()
    request.ParseFromString(body)

    if(request.typeOfRequest == "joinServer"):
        result = JoinServer(request.join).SerializeToString()
    elif(request.typeOfRequest == "leaveServer"):
        result = LeaveServer(request.leave).SerializeToString()
    elif(request.typeOfRequest == "getArticle"):
        result = GetArticles(request.getArticles).SerializeToString()
    elif(request.typeOfRequest == "publishArticle"):
        result = PublishArticle(request.publish).SerializeToString()

    channel.basic_publish(exchange='', routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id = \
        properties.correlation_id),
        body=result)
    channel.basic_ack(delivery_tag=method.delivery_tag)

    
def connectToClient(arg):
    channel.queue_declare(arg[2] + "_server_queue")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=arg[2] + "_server_queue", on_message_callback=client_callback)
    channel.start_consuming()



if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    arg = sys.argv[1:]
    status = connectToRegistry(arg)
    if status == 1:
        connectToClient(arg)
        