import socket

from time import sleep

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ts(response):
    socket.send(response.encode())
    data = ''
    data = socket.recv(1024).decode()
    print (data)

def client_connect():
    while 1:
        try:
            socket.connect(('192.168.43.167', 6676))
            print 'Connected to server.'
            break
        except:
            sleep(60)

def client():
    data = socket.recv(1024).decode()
    return data
