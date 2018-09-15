"""
Run this server from powershell and than run the call-response file from
another powershell to make an echo response from the server
"""
import socket

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8820))
server_socket.listen(1) # 1 means how many connections the server can manage
(client_socket, client_address) = server_socket.accept()

# naking a loop to echo input whilel it is not NULL
while True:
    client_str = client_socket.recv(1024)
    if client_str:
        client_socket.send(client_str)
        print(client_str)
    else:
        break
    
print("Bye")
client_socket.close()
server_socket.close()
