#创建一个tcp socket
import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket Created')

#创建一个udp socket
import socket

s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Created')
