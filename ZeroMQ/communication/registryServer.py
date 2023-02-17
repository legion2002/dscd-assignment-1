import sys
sys.path.insert(1, '../proto')

import time
import zmq
import Message_pb2

MAX_SERVER = 2
Servers = {}

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


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


def Register(request : Message_pb2.RegisterRequest):
    print("JOIN REQUEST FROM " + request.address.IP + ":" + str(request.address.port))
    result = addServers(request.name, request.address.IP, request.address.port)
    if result == 0:
        status = Message_pb2.RegisterResponse(status="SUCCESS")
        serialized_msg = status.SerializeToString()
        socket.send(serialized_msg)
        time.sleep(1)
        
    else:
        status = Message_pb2.RegisterResponse(status="FAIL")
        serialized_msg = status.SerializeToString()
        socket.send(serialized_msg)
        time.sleep(1)


def GetServerList(request : Message_pb2.GetServerListRequest):
    print("SERVER LIST REQUEST FROM " + request.address.IP + ":" + str(request.address.port))
    serverList = []
    for server in Servers.keys():
        IP = Servers[server][0]
        port = Servers[server][1]
        serverList.append(Message_pb2.ServerAddress(name=server, address= Message_pb2.Address(IP=IP, port=port)))
    response = Message_pb2.GetServerListResponse()
    response.serverDetails.extend(serverList)
    socket.send(response.SerializeToString())


def serve():
    while True:
    #  Wait for next request from client
        message = socket.recv()
        registerRequest = Message_pb2.RegisterRequest()
        serverListRequest = Message_pb2.GetServerListRequest()
        registerRequest.ParseFromString(message)
        serverListRequest.ParseFromString(message)
        if(registerRequest.typeOfRequest == "register"):
            Register(registerRequest)
            time.sleep(1)
        elif(serverListRequest.typeOfRequest == "getServerList"):
            GetServerList(serverListRequest)
            time.sleep(1)


if __name__ == '__main__':
    serve()