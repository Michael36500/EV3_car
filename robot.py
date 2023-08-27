#!/usr/bin/env python3

import websocket
from time import sleep
from prikazy import dopredu, zatoc

print("go")

ws = websocket.create_connection("ws://192.168.10.29:8000")
print("connected")


while True:
    # ws.send("update?")
    prikazy = ws.recv()
    print(prikazy)
    prikazy = prikazy.split(";")
    for x in enumerate(prikazy):
        prikazy[x[0]] = float(x[1])

    zatoc(prikazy[0] * 125)
    dopredu(prikazy[1] * 100)