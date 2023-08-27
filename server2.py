from simple_websocket_server import WebSocketServer, WebSocket
from time import sleep


clients = []


class SimpleEcho(WebSocket):
    def handle(self):
        for client in clients:
            client.send_message(self.data)
        print(self.data)

    def connected(self):
        print(self.address, 'connected')
        clients.append(self)

    def handle_close(self):
        clients.remove(self)
        print(self.address, 'closed')



server = WebSocketServer('192.168.10.29', 8000, SimpleEcho)
server.serve_forever()