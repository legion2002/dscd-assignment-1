import time
import zmq

import sys
sys.path.insert(1, '../proto')
import Message_pb2

from google.protobuf.timestamp_pb2 import Timestamp
import datetime

import uuid

unique_id = str(uuid.uuid1())

def joinServer(client, server):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    address = server[1] + ":" + str(server[2])
    print(address)
    socket.connect("tcp://" + address)
    socket.send(Message_pb2.JoinServerRequest(uuid = unique_id, name=client[0], address=Message_pb2.Address(IP=client[1], port=int(client[2]))).SerializeToString())
    message = socket.recv()
    status = Message_pb2.JoinServerResponse()
    status.ParseFromString(message)
    print(status)

def leaveServer(client, server):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    address = server[1] + ":" + str(server[2])
    socket.connect("tcp://" + address)
    socket.send(Message_pb2.LeaveServerRequest(uuid = unique_id).SerializeToString())
    message = socket.recv()
    status = Message_pb2.JoinServerResponse()
    status.ParseFromString(message)
    print(status)


def runRegistryServer(arg):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    request = Message_pb2.RegisterRequest(typeOfRequest="getServerList", name=arg[0], address=Message_pb2.Address(IP=arg[1], port=int(arg[2])))
    serialized_msg = request.SerializeToString()
    socket.send(serialized_msg)
    message = socket.recv()
    status = Message_pb2.GetServerListResponse()
    status.ParseFromString(message)
    for details in status.serverDetails:
        print(details.name + " - " + details.address.IP + ":" + str(details.address.port))

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
        pass
        # getArticles(client, server)
    elif choice == 5:
        pass
        # publishArticles(client, server)

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
    