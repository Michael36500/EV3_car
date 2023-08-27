#!/usr/bin/env python3

import websocket
from time import sleep

print("go")

ws = websocket.create_connection("ws://192.168.10.29:8000")
print("connected")
for x in range(100):
    print(x)
    ws.send(str(x))
    sleep(0.1)