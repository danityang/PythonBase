# coding=utf-8
import socket, sys

# TODO Python3 网络编程
# TODO 建立客户
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname
port = 9999
s.connect((host, port))
msg = s.recv(1024)
s.close()
print msg.decode("utf-8")