import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))
client.sendall('hello world')
data = client.recv(1024)
print data

time.sleep(1)

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(('127.0.0.1', 12345))
client2.sendall('hello world2')
data = client2.recv(1024)
print data

time.sleep(1)

client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client3.connect(('127.0.0.1', 12345))
client3.sendall('hello world3')
data = client3.recv(1024)
print data