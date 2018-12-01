import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.43.167"
port = 6676
print (host)
print (port)
serversocket.bind((host, port))

class server(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            cmd = raw_input('Enter command: ')
            self.sock.send(cmd)

serversocket.listen(1)
print ('server started and listening')
while 1:
    try:
        clientsocket, address = serversocket.accept()
        server(clientsocket, address)
    except:
        break
