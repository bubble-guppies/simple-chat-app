import socket
import chatroom
from message import decode_message, Message
import sys
import json
from bcrypt import checkpw
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

    def client_handler(self, client):
        while True:
            data = client.recv(2048)
            if not data:
                break
            message = data.decode("utf-8")
            
            # default processing
            self.broadcast_message(message, client)

        self.exit_connection(client)

    def accept_connections(self):
        client, address = self.server_socket.accept()
        print(f"Connected to: {address[0]}:{str(address[1])}")
        self.client_startup(client)
        start_new_thread(self.client_handler, (client,))

    def client_startup(self, client: socket):
        """This function is called when a client starts a connection with the server.
        See README.txt for information about the startup procedure. 
        """
        username = ""
        startup = client.recv(2048).decode("utf-8")
        if startup == "$STARTUP$":
            client.send("$STARTUP$".encode())
            # Password authentication
            user_data_msg = client.recv(2048).decode("utf-8")
            if user_data_msg == "$SENDING_USERDATA$":
                user_data = client.recv(2048).decode()
                (username, password) = user_data.split(",")
                if self.authenticate(username, password):
                    print(f"Successfully authenticated '{username}.'")
                    reply = "$AUTHENTICATED$"

                else:
                    print(f"Failed to authenticate '{username}.'")
                    reply = "$FAILED$"

                client.send(reply.encode())

                if reply == "$AUTHENTICATED$":
                    # once a user is authenticated, they will request chatroom data
                    if client.recv(2048).decode() == "$REQUEST_CHATROOM_DATA$":
                        print(f"sending chatroom data\n{self.chatroom.getChatroom()[0].encode() = }\n{self.chatroom.getChatroom()[1].bytes =}")
                        client.send(self.chatroom.getChatroom()[0].encode()) # chatroom name
                        client.send(self.chatroom.getChatroom()[1].bytes) # chatroom id
                        msg_data = " "
                        for msg in self.chatroom.getRecentMessages():
                            msg_data += msg.message() + "\n"
                        print(f"{msg_data = }")
                        client.send(msg_data.encode()) # recent 10 messages
            self.clients.append((client,username))

    def broadcast_message(self, message, sender):
        to_send = ""
        try:
            msg = decode_message(message)
            to_send = msg.message().encode()
            self.chatroom.addMessage(msg)
        except Exception as e:
            print(f"Error decoding message: {e}")

        for client in self.clients:
            if client != sender:
                try:
                    client.send(to_send)
                except socket.error as e:
                    print(f"Error while sending message to {client}: {e}")

    def exit_connection(self, conn):
        for (client, username) in self.clients:
            if client == conn:
                self.clients.remove((conn, username))
                disconnect_message = Message("Server", f"<{username} has disconnected from the chatroom>", self.chatroom.getChatroom()[1])
                self.broadcast_message(disconnect_message.encode_message(), None)
        client.close()

    def authenticate(self, username: str, password: str) -> bool:
        with open("pass.json", "r") as file:
            # try to read passwords
            try:
                passwords_dict = json.load(file)
            except Exception as e:
                pass  # <- ADD ERROR HANDLING

            # try to compare passwords
            try:
                return checkpw(
                    password.encode("utf-8"), passwords_dict[username].encode("utf-8")
                )  # could error if username isn't a key
            except Exception as e:
                pass  # <- ADD ERROR HANDLING

            return False  # passwords didn't match or error


if __name__ == "__main__":
    Server("", 8000, "Sample Chatroom")