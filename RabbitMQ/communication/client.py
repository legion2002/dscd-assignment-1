import sys
sys.path.insert(1, '../proto')

from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
import uuid
import Message_pb2
import time
import pika

unique_id = str(uuid.uuid1())

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
corr_id = 0

def join_server_callback(ch, method, properties, body):
    global corr_id
    if properties.correlation_id == corr_id:
        status = Message_pb2.JoinServerResponse()
        status.ParseFromString(body)
        print(status)

def leave_server_callback(ch, method, properties, body):
    global corr_id
    if properties.correlation_id == corr_id:
        status = Message_pb2.JoinServerResponse()
        status.ParseFromString(body)
        print(status)

def publish_articles_callback(ch, method, properties, body):
    global corr_id
    if properties.correlation_id == corr_id:
        status = Message_pb2.PublishArticlesResponse()
        status.ParseFromString(body)
        print(status)

def get_articles_callback(ch, method, properties, body):
    global corr_id
    if properties.correlation_id == corr_id:
        response = Message_pb2.GetArticlesResponse()
        response.ParseFromString(body)
        cnt =1
        for article in response.article:
            if article.type == 0:
                type = "FASHION"
            elif article.type == 1:
                type = "SPORTS"
            elif article.type  == 2:
                type = "POLITICS"

            date = datetime.fromtimestamp(article.time_rec.seconds)

            print(str(cnt) + ") " + "\n" + type + "\n" + article.author + "\n" + str(date) + "\n" +  article.content)
            cnt+=1

def joinServer(client, server):
    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue
    channel.basic_consume(queue=callback_queue, on_message_callback=join_server_callback,
            auto_ack=True)

    request = Message_pb2.JoinServerRequest(uuid=unique_id, name=client[0], address=Message_pb2.Address(IP=client[1], port=int(client[2])), typeOfRequest="joinServer")
    serialized_msg = request.SerializeToString()
    global corr_id
    corr_id = str(uuid.uuid4())

    print("Sending to server queue: " + str(server[2]) + "_server_queue" )
    channel.basic_publish(
        exchange='',
        routing_key=str(server[2]) + "_server_queue",
        properties=pika.BasicProperties(
            reply_to=callback_queue,
            correlation_id=corr_id,
        ),
        body=serialized_msg)
    
    connection.process_data_events(time_limit=None)

def leaveServer(client, server):
    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue
    channel.basic_consume(queue=callback_queue, on_message_callback=leave_server_callback,
            auto_ack=True)

    request = Message_pb2.LeaveServerRequest(uuid=unique_id, typeOfRequest="leaveServer")
    serialized_msg = request.SerializeToString()
    global corr_id
    corr_id = str(uuid.uuid4())
    print("Sending to server queue: " + str(server[2]) + "_server_queue" )
    channel.basic_publish(
        exchange='',
        routing_key=str(server[2]) + "_server_queue",
        properties=pika.BasicProperties(
            reply_to=callback_queue,
            correlation_id=corr_id,
        ),
        body=serialized_msg)
    
    connection.process_data_events(time_limit=None)




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
        typeRequest = -1
        if typeForArticle.lower() == "fashion":
            typeRequest = 0
        elif typeForArticle.lower() == "sports":
            typeRequest = 1
        elif typeForArticle.lower() == "politics":
            typeRequest = 2

        if typeRequest != -1:
            result = channel.queue_declare(queue='', exclusive=True)
            callback_queue = result.method.queue
            channel.basic_consume(queue=callback_queue, on_message_callback=publish_articles_callback,
                    auto_ack=True)

            request = Message_pb2.PublishArticlesRequest(uuid=unique_id,  article=Message_pb2.ArticleFormat(type=typeRequest, author=author, content=content), typeOfRequest="publishArticle")
            serialized_msg = request.SerializeToString()
            global corr_id
            corr_id = str(uuid.uuid4())
            print("Sending to server queue: " + str(server[2]) + "_server_queue" )
            channel.basic_publish(
                exchange='',
                routing_key=str(server[2]) + "_server_queue",
                properties=pika.BasicProperties(
                    reply_to=callback_queue,
                    correlation_id=corr_id,
                ),
                body=serialized_msg)
            
            connection.process_data_events(time_limit=None)
        else:
            print("Can not publish. Wrong Type") 

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

        requestedArticle = Message_pb2.ArticleRequest(type=typeRequest, author=info[1], time_rec=time)
        request = Message_pb2.GetArticlesRequest(uuid = unique_id, typeOfRequest = "getArticle", article=requestedArticle)
        
        result = channel.queue_declare(queue='', exclusive=True)
        callback_queue = result.method.queue
        channel.basic_consume(queue=callback_queue, on_message_callback=get_articles_callback,
                auto_ack=True)


        serialized_msg = request.SerializeToString()
        global corr_id
        corr_id = str(uuid.uuid4())
        print("Sending to server queue: " + str(server[2]) + "_server_queue" )
        channel.basic_publish(
            exchange='',
            routing_key=str(server[2]) + "_server_queue",
            properties=pika.BasicProperties(
                reply_to=callback_queue,
                correlation_id=corr_id,
            ),
            body=serialized_msg)
        
        connection.process_data_events(time_limit=None)


        
def registry_callback(ch, method, properties, body):
    global corr_id
    if properties.correlation_id == corr_id:
        status = Message_pb2.GetServerListResponse()
        status.ParseFromString(body)
        for details in status.serverDetails:
            print(details.name + " - " + details.address.IP + ":" + str(details.address.port))

def runRegistryServer(arg):
    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue
    channel.basic_consume(queue=callback_queue, on_message_callback=registry_callback,
            auto_ack=True)
    
    request = Message_pb2.RegisterRequest(typeOfRequest="getServerList", name=arg[0], address=Message_pb2.Address(IP=arg[1], port=int(arg[2])))
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
    