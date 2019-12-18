#!/usr/bin/env python
 
import socket
 
 
TCP_IP = '127.0.0.1'    # Standard loopback interface address (localhost)
TCP_PORT = 5005         # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

#start listening for incoming connections
s.listen(1)
 
conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    #reads data from the socket in batches of 1024 bytes using method recv() until it returns an empty string
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data)
    conn.send(data)  # echo
conn.close()