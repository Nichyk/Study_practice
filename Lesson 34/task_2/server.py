import socket
import threading

HOST = '127.0.0.1'
PORT = 8080


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        print(f'Connected by {addr}')
        client = threading.Thread(target=connection_from_client, args=(conn,))
        client.start()


def connection_from_client(conn):
    while True:
        data = conn.recv(1024)
        if data:
            conn.sendall(data.upper())
        else:
            break


if __name__ == '__main__':
    start_server()
