"""
Request-Reply模式只能是一问一答的方式，即客户端不能连续发送两条消息
服务器也不能连续接收两条消息（来自不同的两个客户端同时发消息）
"""
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
count = 0
while True:
    message = socket.recv_string()
    print(message)
    socket.send_string("OK, 200")
