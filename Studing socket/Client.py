import socket

HOST = '169.254.41.147'    # The remote host
PORT = 687              # The same port as used by the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


while True:
    data = client.recv(2048)
    print(data.decode('utf-8'))

    client.send("Okay".encode('utf-8'))

    data = client.recv(2048)
    client.send(data + '+100500')