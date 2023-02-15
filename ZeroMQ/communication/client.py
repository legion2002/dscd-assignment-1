import time
import zmq

import sys
sys.path.insert(1, '../proto')
import Message_pb2

from google.protobuf.timestamp_pb2 import Timestamp
import datetime

import uuid

unique_id = str(uuid.uuid1())

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
            pass
            # runServer(arg, inp)
        print("Choose Option: \n1. Get List of Server \n2. Join to Server \n3. Leave Server \n4. Get Articles \n5. Publish Article \n6. Exit")
        inp = int(input())
    