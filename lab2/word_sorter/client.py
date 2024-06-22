import socket


class Client:
    def __init__(self, host = 'localhost', port = 5001):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_text(self):
        while True:
            text_block = input("Enter message: ")
            
            if text_block == "quit":
                break
            
            self.client.connect((self.host, self.port))
            self.client.send(text_block.encode('utf-8'))
            sorted_words = self.client.recv(1024).decode('utf-8')
            print(sorted_words)
        
        self.client.close()


client = Client()
client.send_text()