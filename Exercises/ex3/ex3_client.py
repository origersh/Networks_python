""" Client, sending data to server and receiving a response from it """
import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8820))

client_socket.send('Ori')

data = client_socket.recv(1024)
print('Server sent: ' + data)

client_socket.close()
