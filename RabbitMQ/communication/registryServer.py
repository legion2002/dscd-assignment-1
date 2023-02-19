#!/usr/bin/env python
import sys
sys.path.insert(1, '../proto')

import time
import pika
import Message_pb2

MAX_SERVER = 4
Servers = {}
# RabbitMQ port number is 5672

def addServers(name, IP, port):

    if name in Servers.keys():
        return 1

    for server in Servers.keys():
        addr = Servers[server][0]+str(Servers[server][1])
        check_addr = IP+str(port)
        if addr == check_addr:
            return 1

    if len(Servers) < MAX_SERVER:
        Servers[name] = [IP, port]
        return 0
    else:
        return 1


def Register(request : Message_pb2.RegisterRequest, props, method):
    print("JOIN REQUEST FROM " + request.address.IP + ":" + str(request.address.port))
    result = addServers(request.name, request.address.IP, request.address.port)
    status = 0
    if result == 0:
        status = Message_pb2.RegisterResponse(status="SUCCESS")
    else:
        status = Message_pb2.RegisterResponse(status="FAIL")
    
    serialized_msg = status.SerializeToString()
    channel.basic_publish(exchange='', routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                    props.correlation_id),
                    body=serialized_msg)
    channel.basic_ack(delivery_tag=method.delivery_tag)

def GetServerList(request : Message_pb2.GetServerListRequest, props, method):
    print("SERVER LIST REQUEST FROM " + request.address.IP + ":" + str(request.address.port))
    serverList = []
    for server in Servers.keys():
        IP = Servers[server][0]
        port = Servers[server][1]
        serverList.append(Message_pb2.ServerAddress(name=server, address= Message_pb2.Address(IP=IP, port=port)))
    response = Message_pb2.GetServerListResponse()
    response.serverDetails.extend(serverList)
    serialized_msg = response.SerializeToString()

    channel.basic_publish(exchange='', routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                    props.correlation_id),
                    body=serialized_msg)
    channel.basic_ack(delivery_tag=method.delivery_tag)

#  Wait for next request from client

def callback(ch, method, properties, body):
    standardFormat = Message_pb2.StandardFormat()
    standardFormat.ParseFromString(body)
    
    if(standardFormat.typeOfRequest == "register"):
        Register(standardFormat.register, properties, method)
    elif(standardFormat.typeOfRequest == "getServerList"):
        GetServerList(standardFormat.getServers, properties, method)

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # Connect to exchange
    channel = connection.channel() # Create Channel
    channel.queue_declare(queue='registry_server_queue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='registry_server_queue', on_message_callback=callback)
    channel.start_consuming()
