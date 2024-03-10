import socket
import threading

LIMIT = 5

books = {
    'Maxim Gorky': 'The Lower Depths',
    'Yevgeny Zamyatin': 'We',
    'Leo Tolstoy': 'War and Peace'
}

def service(client_socket, addr):
    print(f"Connected: {addr}")
    try:
        for author, book in books.items():
            message = f"{author}: {book}\n"
            client_socket.sendall(message.encode())
        client_socket.close()
    except Exception as e:
        print(e)
    print(f"Disconnected: {addr}")

def main():
    port = 13000
    local_addr = "127.0.0.1"
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((local_addr, port))
    server_socket.listen(LIMIT)
    print("Server mounted, listening to port 13000")
    while True:
        # блокировка выполнения пока не установлено входящее соединение
        client_socket, addr = server_socket.accept()
        # Создание потока для обработки соединения
        threading.Thread(target=service, args=(client_socket, addr)).start()  

if __name__ == "__main__":
    main()