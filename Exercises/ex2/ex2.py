""" echo server """
import socket

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 1729)) # IP: '127.0.0.1' specifies the local-host network running within the PC

input = raw_input('Enter a message to sent to the echo server: ')
my_socket.send(input)

data = my_socket.recv(1024)
print('The server sent: ' + data)

my_socket.close()
