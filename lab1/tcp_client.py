import socket
import json


def main():
    # IP-адрес и порт нашего сервера
    ip_address = "127.0.0.1"
    port = 13000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port))
    try:
        data = client_socket.recv(1024)
        while data:
            print(data.decode(), end='')
            data = client_socket.recv(1024)
    finally:
        client_socket.close()
        
if __name__ == "__main__":
    main()