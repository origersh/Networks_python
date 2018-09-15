import socket

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 8820))

while True:
    usr_str = raw_input("Enter something: ")

    if usr_str.lower() == "exit":
        break
    else:
        my_socket.send(usr_str)
        data = my_socket.recv(1024)
        print("The server sent: "+data)

print("Bye")
my_socket.close()
