import socket

HOST = '169.254.41.147' # Symbolic name meaning the local host
PORT = 687              # Arbitrary non-privileged port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
print('Server is listening')

while True:
    user_socket, address = server.accept()
    print('Slave is connected!')

    user_socket.send('You are connected'.encode("utf-8"))
    data = user_socket.recv(2048)

    print(data.decode('utf-8')) #Okay

    user_socket.send('Hello world!')

    data = user_socket.recv(2048)
    print(data)
server.close()