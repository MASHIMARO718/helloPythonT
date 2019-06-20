#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import _thread
import time
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
a = set();
def talkToAll(sclient,massage):
    for client in a:
        if client != sclient:
            clientname = str(sclient.getpeername())+''' said：'''
            newmassage = clientname + massage
            client.send(newmassage.encode('utf-8'))

# 为线程定义一个函数
def talk( clientsocket, delay):
   count = 0
   flag = True
   while flag:
       try:
           msg = clientsocket.recv(1024).decode('utf-8')
           print(msg)
           talkToAll(clientsocket,msg)
       except:
           msg = str(clientsocket.getpeername())+ '下线了'
           print(msg)
           talkToAll(clientsocket,'我下线了,88')
           a.remove(clientsocket)
           _thread.exit()
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    a.add(clientsocket)
    print("连接地址: %s" % str(addr))
    _thread.start_new_thread(talk, (clientsocket, 2,))