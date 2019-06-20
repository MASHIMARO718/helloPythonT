#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import _thread
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))
# 为线程定义一个函数

def talk():
   while True:
       msg = s.recv(1024).decode('utf-8')
       print(msg)
_thread.start_new_thread(talk,())
# 接收小于 1024 字节的数据
while True:
    msg = input("请输入：\n")
    s.send(msg.encode('utf-8'))




s.close()