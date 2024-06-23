import socket
import threading
import json
import os


class Server:
    def __init__(self, host = 'localhost', port = 5000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.filename = 'board.json'
        self.commands = {
            'LIST': self.list_messages,
            '': self.quit,
        }

    def quit(self, client):
        client.close()

    def list_messages(self, client):
        if not os.path.exists(self.filename):
            client.send('No messages yet.'.encode('utf-8'))
            return
        
        with open(self.filename, 'r') as f:
            board = json.load(f)
            
        if not board:
            client.send('No messages yet.'.encode('utf-8'))
            return
        
        client.send(';'.join(board).encode('utf-8'))
            
    def add_message(self, message, client):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                board = json.load(f)
        else:
            board = []
            
        board.append(message)
        
        with open(self.filename, 'w') as f:
            json.dump(board, f)
            
        client.send(f'Message added: "{message}"'.encode('utf-8'))

    def handle_client(self, client):
        message = client.recv(1024).decode('utf-8')
        func = self.commands.get(message, self.add_message)
        if func == self.add_message:
            func(message, client)  # pass 'message' as the first argument
        else:
            func(client)

    def start(self):
        while True:
            client, address = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(client,))  # pass the function reference
            thread.start()

server = Server()
server.start()