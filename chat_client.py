import socket
import uuid
from client import Client

def get_server() -> tuple[str, int]:
    HOST = input('Provide server IP address >\n')  # The server's hostname or IP address
    PORT = int(input('Provide port number >\n'))  # The port used by the server
    return (HOST, PORT)
    
def get_client(host) -> Client:
    username = input('Provide username >\n')
    password = input('Provide password >\n')

    #Create new client object for interaction w/ remote host
    clientUUID = uuid.uuid4()
    return Client(username, host, password, clientUUID)

def join(host, port, client):
    '''
    Called when client wishes to connect to server.
    '''
    # if type(PORT) is not int:
    #     raise TypeError("Port number must be integer.")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # the first message sent by the server should be the chatroom ID?
        chatroom_id = uuid.UUID(bytes=s.recv(4096))
        # start_new_thread(read_handler, (s, ))
        start_new_thread(write_handler, (s, client, chatroom_id, ))
        while True:
            raw_msg = s.recv(2048)
            print(f"{raw_msg.decode() = }")

def write_handler(s: socket, client: Client, chatroom_id: uuid):
    '''
    Handles the client writing messages to the server.
    '''
    while True:
        print("Enter a message > ")
        message_str = input()
        if message_str == "exit":
            leave(s)
            return
        send_msg(s, message_str, client, chatroom_id)
        # s.send(message_str.encode())

def leave(s: socket):
    ''' 
    Called when client wishes to disconnect from the server.
    '''
    s.close()
    os._exit(1)

def send_msg(s: socket, msg_str: str, client: Client, chatroom_id):
    '''
    Called when client wishes to send a string to the server (msg).
    '''
    encodedMessage = client.create_message(chatroom_id, msg_str)
    s.send(encodedMessage)

def recv_msg(msg: str):
    print(msg)
    
if __name__ == "__main__":
    (host, port) = get_server()
    client = get_client(host)
    join(host, port, client)
