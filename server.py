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

    def check_ready(self):
        return len(self.clients) >= 2
    def execute_work(self):
        print("Work!")
        new_array = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
        print(new_array)
        new_array2 = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
        print(new_array2)
        new_array3 = [[random.randint(0, 10) for x in range(3)] for y in range(3)]
        print(new_array3)
        print(f"Code generated 3 random arrays.")

        try:
            print(self.send_message(socket='b', data=new_array, action='data'))

            print(self.send_message(socket='b', data=new_array2, action='data'))
            print(self.send_message(socket='c', data=new_array3, action='data'))

            print(self.send_message(socket='b', data='+', action='operation'))


        except KeyError as exc:
            print(exc, file=stderr)
            self.disconnect()
            return

        response = self.get_full_message(self.clients['b'])
        if response.get('action') == 'error':
            print(f"Error, {response['data']}", file=stderr)
            return

        print(f"B returned '{response}' response")
        print(self.send_message(socket='c', data=response['data'], action='data'))
        print(self.send_message(socket='c', data='+', action='operation'))


        response = self.get_full_message(self.clients['c'])

        if response.get('action') == 'error':
            print(f"Error, {response['data']}", file=stderr)
            return
        print(f"Everything is executed. The result is: {response.get('data', 'No result')}. Stopping the job")
        self.disconnect()



    def accept_clients(self):
        while True:
            client_socket, client_address = self.server.accept()
            print(f"Client from address '{client_address}' connected.")
            self.__client_id += 1
            self.clients[chr(self.__client_id)] = client_socket
