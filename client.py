import json, socket, random, settings
from sys import stderr

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(settings.SERVER_ADDRESS)
        self.data = []

    def start(self):
        print("Client started")
        self.execute_work()

    def send_message(self, **kwargs):
        json_data = json.dumps(kwargs)
        self.client.send(json_data.encode("utf-8"))
        return f"Message to server sent successfully."

    def get_full_message(self):
        try:
            response = self.client.recv(settings.BUFFER_SIZE)
        except ConnectionError:
            print("Connection aborted")
            self.client.close()
            return

        print(response)
        if not response:
            return

        try:
            response = json.loads(response.decode("utf-8"))
            return response
        except UnicodeDecodeError and json.JSONDecodeError:
            print("Cannot encode the response. Stopping the job")
            self.send_message(data='Cannot decode the response', action='error')

    def execute_work(self):
        print("Starting the work!")
        while True:
            message = self.get_full_message()
            if not message:
                return

            if message.get('action'):
                action = message['action']

                if action == 'data':
                    self.data.append(message['data'])
                elif action == "operation":
                    try:
                        result = eval(message['data'].join(str(x) for x in self.data))
                        self.send_message(data=result, action='ok')
                        self.data = []
                    except Exception as exc:
                        print(exc, file=stderr)
                        self.send_message(data=str(exc), action='error')

            else:
                print("No action provided!", file=stderr)


if __name__ == '__main__':
    server = Client()
    server.execute_work()