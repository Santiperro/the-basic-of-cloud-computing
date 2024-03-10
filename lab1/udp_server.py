import socket

# Наша "база данных"
books = {
    'Максим Горький': 'На дне',
    'Евгений Замятин' : 'Мы',
    'Лев Толстой' : 'Война и мир'
}

def main():
    # Порт нашего сервера
    port = 13000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', port))
    print("Server started, servicing on port " + str(port))
    while True:
        data, addr = server_socket.recvfrom(1024)
        name = data.decode()
        job = books.get(name, "No such books")
        server_socket.sendto(job.encode(), addr)
        
if __name__ == "__main__":
    main()