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

        while True:
            run(s, chatroom_id, client)

def run(s, chatroom_id, client):
    try:
        data = s.recv(2048, socket.MSG_DONTWAIT)
        print(f"Received {data.decode()}\n")
    except BlockingIOError as e:
        pass
    message_str = input("Enter a message >")
    send_msg(s, message_str, client, chatroom_id)

def leave():
    ''' 
    Called when client wishes to disconnect from the server.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.disconnect((host, port))

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
