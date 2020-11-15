import json, socket, random, settings
from sys import stderr

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(settings.SERVER_ADDRESS)

    def start(self):
        print("Client started")
        self.execute_work()

    def send_message(self, **kwargs):
        json_data = json.dumps(kwargs)
        self.client.send(json_data.encode("utf-8"))
        return f"Message to server sent successfully."

    def get_full_message(self):
        response = self.client.recv(settings.BUFFER_SIZE)
        print(response)

        response = json.loads(response.decode("utf-8"))
        return response

    def execute_work(self):
        print("Starting the work!")
        while True:  # бесконечно
            message = self.get_full_message()

            if message.get('action'):
                action = message['action']

                if action == 'data':
                    self.data.append(message['data'])
                elif action == "operation":
                        result = eval(
                        message['data'].join(str(x) for x in self.data))
                        self.send_message(data=result, action='ok')
                        self.data = []
