import socket, random, settings
from sys import stderr

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(settings.SERVER_ADDRESS)
        self.server.listen()

        self.clients = {}
        self.__client_id = 97 # id client, 97 == 'a'
    def start(self):
        print("Server Started")
        self.accept_clients

    def check_ready(self):  # проверяем, если у нас достаточно клиентов для выполнения операций
        return len(self.clients) >= 2  # проверяем, у нас больше 2 клиентов или нет
    def execute_work(self):
        print('Genereting random matrix')
        new_array = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
        new_array2 = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
        new_array3 = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
        print(f"Code generated 3 random arrays.")
        print(new_array)
        print(new_array2)
        print(new_array3)


    def accept_clients(self):
        while True:
            client_socket, client_address = self.server.accept()
            print(f"Client from address '{client_address}' connected.")

            try:
                self.__client_id += 1
                self.clients[chr(self.__client_id)] = client_socket
            except ValueError:
                print("Maximum client number reached! Cannot connect more!")
                return

            if self.check_ready():
                self.execute_work()
            else:
                print("Not enough clients to execute the processes. Waiting for more to connect.")