import socket
import chatroom
import sys
from _thread import *

class Server:
    ip_address: str
    port: int
    num_clients: int = 3
    server_socket: socket
    clients: list
    chatroom: chatroom.Chatroom

    def __init__(self, ip_address: str, port: int, chatroom_name: str):
        """Initialize a server object.

        Args:
            ip_address (str): the ip address to host the server on.
            port (int): the port to open for the server.
        """
        self.ip_address = ip_address
        self.port = port
        self.clients = []
        self.chatroom = chatroom.Chatroom(chatroom_name)
        self.create_socket()
        while True:
            self.accept_connections()

    def create_socket(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Trying to bind to {self.port}...")
        try:
            server_socket.bind((self.ip_address, self.port))

        except socket.error as msg:
            print(f"Bind failed. Error: {msg}")
            sys.exit()

        print("Socket bind complete")

        server_socket.listen(self.num_clients)

        self.server_socket = server_socket

        return
    
    def client_handler(self, connection):
        self.clients.append(connection)
        connection.send(self.chatroom.getChatroom().encode())
        while True:
            data = connection.recv(4096)
            message = data.decode('utf-8')
            if message == "exit":
                self.exit_connection(connection)
                break
            self.broadcast_message(message)
        connection.close()

    def accept_connections(self):
        client, address = self.server_socket.accept()
        print(f'Connected to: {address[0]}:{str(address[1])}')
        start_new_thread(self.client_handler, (client, )) 
    
    def broadcast_message(self, message):
        for client in self.clients:
            client.send(message.to_str().encode())

    def exit_connection(self, connection):
        connection.close()
        

    
if __name__ == "__main__":
    Server("", 8001, "Sample Chatroom")