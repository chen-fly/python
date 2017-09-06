from threading import Thread
from socket import *

# 1.收数据，然后打印
def recvData():
    while True:
        recvData = udpSocket.recvfrom(1024)
        print('%s:%s'%(str(recvData[1]), recvData[0]))

# 2.检测键盘，发数据
def sendData():
    while True:
        sendInfo = input()
        udpSocket.sendto(sendInfo.encode('gb2312'),(decIp,decPort))

udpSocket = None
decIp = ''
decPort = 0

def main():

    global udpSocket
    global decIp
    global decPort

    decPort = int(input('请输入端口号：'))
    decIp = input('请输入IP地址：')

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind("",4567)

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == '__main__':
    main()
