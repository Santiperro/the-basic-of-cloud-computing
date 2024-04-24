import socket


class Client:
    def __init__(self, host = 'localhost', port = 5000):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self):
        while True:
            message = input("Enter message: ")
            
            if message == "quit":
                break
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.send(message.encode('utf-8'))
                response = s.recv(1024).decode('utf-8')
                print(response)


client = Client()
client.send_message()