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

if __name__ == '__main__':
    arg = sys.argv[1:]
    status = connectToRegistry(arg)
    if status == 0:
        pass