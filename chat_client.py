import socket
import uuid
import os
from client import Client
from _thread import start_new_thread
from getpass import getpass
import bcrypt

HOST = input('Provide server IP address: ')  # The server's hostname or IP address
PORT = int(input('Provide port number: '))  # The port used by the server


def join():
    # if type(PORT) is not int:
    #     raise TypeError("Port number must be integer.")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(2048)

        # authenticate the user
        if not client.authenticate(s):
            print("Failed to authenticate. Please run the program again.")
            return

        # after authentication, the server sends three messages:
        # chatroom_name
        # chatroom_id
        # recent 10 messages
        chatroom_name = s.recv(2048).decode()
        chatroom_id = uuid.UUID(bytes=s.recv(2048))
        last_10 = s.recv(2048).decode()
        print(f"--- Connected to {chatroom_name} ---")
        print(last_10)

        # create a separate thread to handle user input
        start_new_thread(write_handler, (s, client, chatroom_id, ))
        while True:
            # loop to listen for new messages
            msg = s.recv(2048)
            print(f"{msg.decode()}")

def write_handler(s: socket, client: Client, chatroom_id: uuid):
    '''
    Handles the client writing messages to the server.
    '''
    while True:
        message_str = input("")
        if message_str == "exit":
            leave(s)
            return
        send_msg(s, message_str, client, chatroom_id)

def leave():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.disconnect((HOST, PORT))

def send_msg(s: socket, msg_str: str, client: Client, chatroom_id):
    '''
    Called when client wishes to send a string to the server (msg).
    '''
    encodedMessage = client.create_message(chatroom_id, msg_str)
    s.send(encodedMessage)
    
if __name__ == "__main__":
    (server, port) = get_server()
    client = get_client()
    join(server, port, client)
