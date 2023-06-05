import socket

HOST = "127.0.0.1"
PORT = 60000

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (HOST, PORT)
data = b'Hello, world'
c.sendto(data, addr)
rdata = c.recvfrom(1024)

print('Received', repr(rdata))
