""" Echo Server - echos all that is sent to him """
import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 1234))

server_socket.listen(1)

(client_socket, client_address) =  server_socket.accept()

while True:
    client_input = client_socket.recv(1024)
    # if the client left the channel - break
    if client_input == 'exit':
        break
    # else - echo back the transmited message
    client_socket.send(client_input)

client_socket.close()
server_socket.close()
