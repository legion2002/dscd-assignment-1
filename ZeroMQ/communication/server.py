import time
import zmq

import sys
sys.path.insert(1, '../proto')
import Message_pb2

from google.protobuf.timestamp_pb2 import Timestamp
import datetime

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


def connectToRegistry(arg):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
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
    print("tcp://*:" + str(arg[2]))
    socket.bind("tcp://*:" + str(arg[2]))
    while True:
        message = socket.recv()
        joinServerRequest = Message_pb2.JoinServerRequest()
        leaveServerRequest = Message_pb2.LeaveServerRequest()
        joinServerRequest.ParseFromString(message)
        leaveServerRequest.ParseFromString(message)
        if(joinServerRequest.typeOfRequest == "joinServer"):
            result = JoinServer(joinServerRequest)
            time.sleep(1)
            result = result.SerializeToString()
            socket.send(result)
        elif(leaveServerRequest.typeOfRequest == "leaveServer"):
            LeaveServer(leaveServerRequest)
            time.sleep(1)


if __name__ == '__main__':
    arg = sys.argv[1:]
    status = connectToRegistry(arg)
    if status == 0:
        connectToClient(arg)