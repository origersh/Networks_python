import socket, time, random

def check(s):
    s = str(s).lower()
    return {
        "time":"Current local Time is: "+str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5]),
        "name":"Ori's server",
        "rand":"Here is a random integer between 1 and 10: "+str(random.randint(1,10)),
    }.get(s, s)

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8820))
server_socket.listen(1)

(usr_socket, usr_address) = server_socket.accept()

# There is an annoying bug here when the client send an 'enter'
# need to solve this...
while True:
    usr_str = usr_socket.recv(1024)
    if usr_str:
        usr_socket.send(check(usr_str))
        print(usr_str)
    else:
        break

print("Bye")
usr_socket.close()
server_socket.close()
