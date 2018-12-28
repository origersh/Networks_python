""" echo server from scratch """
import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 1234))

while True:
    input = raw_input('Enter message to send to echo server: ')
    # if requested to exit - inform the server, then close the connection
    if input.lower() == 'exit':
        client_socket.send('exit')
        break
    # else - send message to the server
    client_socket.send(input)

    data = client_socket.recv(1024)
    print('The server sent: ' + data)

client_socket.close()

# TODO: Find a way to avoid '\n' crash - when sending an Enter as input
