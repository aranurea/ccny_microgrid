import socket
import sys

try:
    #create an AF_INET, STREAM socket (TCP)
    sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err_msg:
    print ('Unable to instantiate socket. Error code: ' + str(err_msg[0]) + ' , Error message : ' + err_msg[1])
    sys.exit();

print ('Socket Initialized')

sock.bind(localhost, 6676);

sock.listen(1)

conn, addr = mySocket.accept()

print ("Connection from: " + str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print ("from connected  user: " + str(data))

    data = str(data).upper()
    print ("Received from User: " + str(data))

    data = input(" ? ")
    conn.send(data.encode())

    conn.close()
