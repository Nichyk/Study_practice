import socket

HOST = '127.0.0.1'
PORT = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
data, addr = s.recvfrom(1024)
while data:
    s.sendto(data.upper(), addr)

