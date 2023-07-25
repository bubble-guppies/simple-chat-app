import socket
import uuid
import os
import os
from client import Client
from _thread import start_new_thread
from getpass import getpass

def get_server() -> tuple[str, int]:
    HOST = input('Provide server IP address >\n')  # The server's hostname or IP address
    PORT = int(input('Provide port number >\n'))  # The port used by the server
    return (HOST, PORT)
    
def get_client() -> Client:
    """
    Create a Client object for interaction w/ remote host.
    """
    username = input('Provide username >\n')
    password = getpass('Provide password >\n')
    host = socket.gethostbyname(socket.gethostname()) # ip address of client

    return Client(username, host, password)

def join(host, port, client):
    '''
    Called when client wishes to connect to server.
    See README.txt for information about the startup procedure. 
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send("$STARTUP$".encode())
        
        if s.recv(4096).decode() == "$STARTUP$":
            # authenticate the user
            if not client.authenticate(s):
                print("Failed to authenticate. Please run the program again.")
                return
            
            # after authentication, request chatroom information
            s.send("$REQUEST_CHATROOM_DATA$".encode())
            raw_msg = s.recv(4096)
            print(raw_msg)
            (chatroom_name, chatroom_bytes, last_10) = raw_msg.decode().split(",")
            print(f"{chatroom_name = }, {chatroom_bytes = }, {last_10 = }")
            chatroom_id = uuid.UUID(bytes=chatroom_bytes.encode())
            last_10 = last_10
            print(f"--- Connected to {chatroom_name} ---")
            print(last_10)
            s.send("$END_STARTUP$".encode())

        # create a separate thread to handle user input
        start_new_thread(write_handler, (s, client, chatroom_id, ))
        while True:
            # loop to listen for new messages
            msg = s.recv(4096)
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

def leave(s: socket):
    ''' 
    Called when client wishes to disconnect from the server.
    '''
    s.close()

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
