# Echo client program
import socket

HOST = '169.254.41.147'    # The remote host
PORT = 687              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print ('Received', repr(data))

