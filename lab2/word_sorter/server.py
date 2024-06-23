import socket
import threading


class WordSorter:
    def __init__(self, text_block):
        self.text_block = text_block

    def sort_words(self):
        words = self.text_block.split()
        sorted_words = sorted(set(words), key=str.lower)
        return sorted_words


class Server:
    def __init__(self, host = 'localhost', port = 5001):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def handle_client(self, client):
        text_block = client.recv(1024).decode('utf-8')
        sorter = WordSorter(text_block)
        sorted_words = sorter.sort_words()
        client.send('\n'.join(sorted_words).encode('utf-8'))
        client.close()

    def start(self):
        while True:
            client, address = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

server = Server()
server.start()