""" sending a meesege to a remote server """
import socket

my_socket = socket.socket() # calling socket_lib's socket obj
my_socket.connect(('54.213.229.251', 8820)) # connecting to the server on IP 54.213.229.251 that is listening on port 8820

my_socket.send('Ori') # sending a message                                  | py-3.6: send(b'Omer')

data = my_socket.recv(1024) # receive 1024 bits of data from the server
print('The server sent: ' + data) #                                        | py -3.6: data.decode('utf-8')

my_socket.close() # closing the connection

# --------------------- // interesting notes // ------------------ #
# When running with python 3: `my_socket.send('String')` fails with an error saying that we must send a byte-obj
    # that means that everthing we send needs to be converted to bytes (using b'String' for exm.),
    # and everything we receive needs to be decoded (using .decode('utf-8') for exm.)
# However when compiling with python 2 - my_socket.send('String') does NOT raise an error
