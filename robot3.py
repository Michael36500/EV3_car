#!/usr/bin/env python3
print("socket")
import socket
print("let's go")

# create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)
# connect to the server
client.connect(("192.168.10.29", 8001))
# receive
response = client.recv(4096)
if response.decode() == "ready":
    print("Successful")
else:
    print("Not successful")

    
# send
client.send("hello world".encode())