import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.231.67.23', 1234))
server.listen(5)
while True:
    client, addr = server.accept()
    print addr
    print '.'.join(addr[0].split('.')[:-1])
    client.sendall('welcome to server')
    client.close()
