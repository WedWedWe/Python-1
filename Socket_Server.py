#  === TCP 服务端程序 server.py ===
from socket import *
from threading import Thread

IP = '0.0.0.0'
PORT = 50000
BUFLEN = 512

def clienthandler(dataSocket,addr):
    while True:
        recved = dataSocket.recv(BUFLEN)
        if not recved:
            break
        info = recved.decode()
        print(f'收到对方信息： {info}')
        dataSocket.send(f'服务端接收到了信息 {info}'.encode())
    dataSocket.close()

listenSocket = socket(AF_INET, SOCK_STREAM)#AF_INET=IP SOCK_STREAM=TCP
listenSocket.bind((IP, PORT))
listenSocket.listen(8)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')
while True:
    dataSocket, addr = listenSocket.accept()
    addr=str(addr)
    print('接受一个客户端连接:', addr)
    th=Thread(target=clienthandler,args=(dataSocket,addr))
    th.start

listenSocket.close()

#并发爬虫可用库:asyncio库
