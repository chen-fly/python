from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.sendto(("haha").encode('utf-8'), ('192.168.1.99', 8080))

#绑定端口，发送方不必要，接收方必要
#udpSocket.bind('',8080)

#一次接受1024字节消息
#udpSocket.recvfrom(1024)
