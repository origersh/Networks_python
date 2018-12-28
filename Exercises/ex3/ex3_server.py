""" Server, receiving data from a client and sending back a response """
import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 8820)) # like socket.connect, on the server side we use the 'bind' function to specify connection "line"

server_socket.listen(1) # listening on the given IP and port in bind(), info about the parameter is in 'interesting notes' bellow

(client_socket, client_address) = server_socket.accept() # waiting and accepting the transmiting client_socket and his address

client_name = client_socket.recv(1024) # receiving a name from the client
client_socket.send('Hello ' + client_name)

client_socket.close()
server_socket.close()

# ------------------ // interesting notes // ----------------------- #
#
# accept() is a "blocking" function meaning that it will block code execution until connection with client
