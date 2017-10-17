# coding=utf-8
import socket, sys

# TODO Python3 网络编程
# Python中，使用 socket() 函数来创建套接字，语法格式如下：
'''
socket.socket([family[, type[, proto]]])
其中参数 
family: 套接字家族可以使AF_UNIX或者AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.
'''
# TODO 建立服务端
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
Host = socket.gethostname()
# 端口
port = 9999
# 绑定端口
ServerSocket.bind((Host, port))
# 设置最大连接数，超过后排队
ServerSocket.listen(5)
# 建立客户端连接
while True:
    ClientSocket, Address = ServerSocket.accept()
    print "连接地址： ", str(Address)
    ClientSocket.send("Socket服务端".encode("utf-8"))
    ClientSocket.close()
