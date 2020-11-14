import json, socket, random, settings
from sys import stderr

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(settings.SERVER_ADDRESS)