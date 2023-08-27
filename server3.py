import socket
from time import sleep
import threading

# create and bind a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.10.29", 8001))
server.listen(5)
print("Server is listening on port 8001")

def clientHandler(client_socket):
    # receive and display a message from the client
    while True:
        request = client_socket.recv(1024)
        print("Received \"" + request.decode() + "\" from client")
        sleep(0.1)
    # close the connection again
    # client_socket.close()
    # print("Connection closed")

while True:
    # wait for client to connect
    client, addr = server.accept()
    print("Client connected " + str(addr))
    # create and start a thread to handle the client
    client_handler = threading.Thread(target = clientHandler, args=(client,))
    client_handler.start()