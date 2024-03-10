import socket

def main():
    # IP-адрес и порт нашего сервера
    ip_address = "127.0.0.1"
    port = 13000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        name = input("Name: ")
        if name == "":
            break
        client_socket.sendto(name.encode(), (ip_address, port))
        data, addr = client_socket.recvfrom(1024)
        print(data.decode())

if __name__ == "__main__":
    main()